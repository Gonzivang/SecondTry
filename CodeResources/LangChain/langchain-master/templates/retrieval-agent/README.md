# retrieval-agent

This package uses Azure OpenAI to do retrieval using an agent architecture.
By default, this does retrieval over Arxiv.

## Environment Setup

Since we are using Azure OpenAI, we will need to set the following environment variables:

```shell
export AZURE_OPENAI_API_BASE=...
export AZURE_OPENAI_API_VERSION=...
export AZURE_OPENAI_API_KEY=...
export AZURE_OPENAI_DEPLOYMENT_NAME=...
```

## Usage

To use this package, you should first have the LangChain CLI installed:

```shell
pip install -U langchain-cli
```

To create a new LangChain project and install this as the only package, you can do:

```shell
langchain app new my-app --package retrieval-agent
```

If you want to add this to an existing project, you can just run:

```shell
langchain app add retrieval-agent
```

And add the following code to your `server.py` file:
```python
from retrieval_agent import chain as retrieval_agent_chain

add_routes(app, retrieval_agent_chain, path="/retrieval-agent")
```

(Optional) Let's now configure LangSmith. 
LangSmith will help us trace, monitor and debug LangChain applications. 
LangSmith is currently in private beta, you can sign up [here](https://smith.langchain.com/). 
If you don't have access, you can skip this section


```shell
export LANGCHAIN_TRACING_V2=true
export LANGCHAIN_API_KEY=<your-api-key>
export LANGCHAIN_PROJECT=<your-project>  # if not specified, defaults to "default"
```

If you are inside this directory, then you can spin up a LangServe instance directly by:

```shell
langchain serve
```

This will start the FastAPI app with a server is running locally at 
[http://localhost:8000](http://localhost:8000)

We can see all templates at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
We can access the playground at [http://127.0.0.1:8000/retrieval-agent/playground](http://127.0.0.1:8000/retrieval-agent/playground)  

We can access the template from code with:

```python
from langserve.client import RemoteRunnable

runnable = RemoteRunnable("http://localhost:8000/retrieval-agent")
```