#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time    : 2023/5/11 17:46
@Author  : alexanderwu
@File    : test_debug_error.py
@Modifiled By: mashenquan, 2023-12-6. According to RFC 135
"""
import uuid

import pytest

from metagpt.actions.debug_error import DebugError
from metagpt.config import CONFIG
from metagpt.const import TEST_CODES_FILE_REPO, TEST_OUTPUTS_FILE_REPO
from metagpt.schema import RunCodeContext, RunCodeResult
from metagpt.utils.file_repository import FileRepository

CODE_CONTENT = '''
from typing import List
from deck import Deck
from card import Card

class Player:
    """
    A class representing a player in the Black Jack game.
    """

    def __init__(self, name: str):
        """
        Initialize a Player object.
        
        Args:
            name (str): The name of the player.
        """
        self.name = name
        self.hand: List[Card] = []
        self.score = 0

    def draw(self, deck: Deck):
        """
        Draw a card from the deck and add it to the player's hand.
        
        Args:
            deck (Deck): The deck of cards.
        """
        card = deck.draw_card()
        self.hand.append(card)
        self.calculate_score()

    def calculate_score(self) -> int:
        """
        Calculate the score of the player's hand.
        
        Returns:
            int: The score of the player's hand.
        """
        self.score = sum(card.value for card in self.hand)
        # Handle the case where Ace is counted as 11 and causes the score to exceed 21
        if self.score > 21 and any(card.rank == 'A' for card in self.hand):
            self.score -= 10
        return self.score
'''

TEST_CONTENT = """
import unittest
from blackjack_game.player import Player
from blackjack_game.deck import Deck
from blackjack_game.card import Card

class TestPlayer(unittest.TestCase):
    ## Test the Player's initialization
    def test_player_initialization(self):
        player = Player("Test Player")
        self.assertEqual(player.name, "Test Player")
        self.assertEqual(player.hand, [])
        self.assertEqual(player.score, 0)

    ## Test the Player's draw method
    def test_player_draw(self):
        deck = Deck()
        player = Player("Test Player")
        player.draw(deck)
        self.assertEqual(len(player.hand), 1)
        self.assertEqual(player.score, player.hand[0].value)

    ## Test the Player's calculate_score method
    def test_player_calculate_score(self):
        deck = Deck()
        player = Player("Test Player")
        player.draw(deck)
        player.draw(deck)
        self.assertEqual(player.score, sum(card.value for card in player.hand))

    ## Test the Player's calculate_score method with Ace card
    def test_player_calculate_score_with_ace(self):
        deck = Deck()
        player = Player("Test Player")
        player.hand.append(Card('A', 'Hearts', 11))
        player.hand.append(Card('K', 'Hearts', 10))
        player.calculate_score()
        self.assertEqual(player.score, 21)

    ## Test the Player's calculate_score method with multiple Aces
    def test_player_calculate_score_with_multiple_aces(self):
        deck = Deck()
        player = Player("Test Player")
        player.hand.append(Card('A', 'Hearts', 11))
        player.hand.append(Card('A', 'Diamonds', 11))
        player.calculate_score()
        self.assertEqual(player.score, 12)

if __name__ == '__main__':
    unittest.main()

"""


@pytest.mark.asyncio
async def test_debug_error():
    CONFIG.src_workspace = CONFIG.git_repo.workdir / uuid.uuid4().hex
    ctx = RunCodeContext(
        code_filename="player.py",
        test_filename="test_player.py",
        command=["python", "tests/test_player.py"],
        output_filename="output.log",
    )

    await FileRepository.save_file(filename=ctx.code_filename, content=CODE_CONTENT, relative_path=CONFIG.src_workspace)
    await FileRepository.save_file(filename=ctx.test_filename, content=TEST_CONTENT, relative_path=TEST_CODES_FILE_REPO)
    output_data = RunCodeResult(
        stdout=";",
        stderr="",
        summary="======================================================================\n"
        "FAIL: test_player_calculate_score_with_multiple_aces (__main__.TestPlayer)\n"
        "----------------------------------------------------------------------\n"
        "Traceback (most recent call last):\n"
        '  File "tests/test_player.py", line 46, in test_player_calculate_score_'
        "with_multiple_aces\n"
        "    self.assertEqual(player.score, 12)\nAssertionError: 22 != 12\n\n"
        "----------------------------------------------------------------------\n"
        "Ran 5 tests in 0.007s\n\nFAILED (failures=1)\n;\n",
    )
    await FileRepository.save_file(
        filename=ctx.output_filename, content=output_data.model_dump_json(), relative_path=TEST_OUTPUTS_FILE_REPO
    )
    debug_error = DebugError(context=ctx)

    rsp = await debug_error.run()

    assert "class Player" in rsp  # rewrite the same class
    # Problematic code:
    # ```
    # if self.score > 21 and any(card.rank == 'A' for card in self.hand):
    #     self.score -= 10
    # ```
    # Should rewrite to (used "gpt-3.5-turbo-1106"):
    # ```
    # ace_count = sum(1 for card in self.hand if card.rank == 'A')
    # while self.score > 21 and ace_count > 0:
    #     self.score -= 10
    #     ace_count -= 1
    # ```
    assert "while self.score > 21" in rsp
