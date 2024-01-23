
# cassandra-entomology-rag

This template will perform RAG using Apache Cassandra® or Astra DB through CQL (`Cassandra` vector store class)

## Environment Setup

For the setup, you will require:
- an [Astra](https://astra.datastax.com) Vector Database. You must have a [Database Administrator token](https://awesome-astra.github.io/docs/pages/astra/create-token/#c-procedure), specifically the string starting with `AstraCS:...`.
- [Database ID](https://awesome-astra.github.io/docs/pages/astra/faq/#where-should-i-find-a-database-identifier).
- an **OpenAI API Key**. (More info [here](https://cassio.org/start_here/#llm-access))

You may also use a regular Cassandra cluster. In this case, provide the `USE_CASSANDRA_CLUSTER` entry as shown in `.env.template` and the subsequent environment variables to specify how to connect to it.

The connection parameters and secrets must be provided through environment variables. Refer to `.env.template` for the required variables.

## Usage

To use this package, you should first have the LangChain CLI installed:

```shell
pip install -U langchain-cli
```

To create a new LangChain project and install this as the only package, you can do:

```shell
langchain app new my-app --package cassandra-entomology-rag
```

If you want to add this to an existing project, you can just run:

```shell
langchain app add cassandra-entomology-rag
```

And add the following code to your `server.py` file:
```python
from cassandra_entomology_rag import chain as cassandra_entomology_rag_chain

add_routes(app, cassandra_entomology_rag_chain, path="/cassandra-entomology-rag")
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
We can access the playground at [http://127.0.0.1:8000/cassandra-entomology-rag/playground](http://127.0.0.1:8000/cassandra-entomology-rag/playground)  

We can access the template from code with:

```python
from langserve.client import RemoteRunnable

runnable = RemoteRunnable("http://localhost:8000/cassandra-entomology-rag")
```

## Reference

Stand-alone repo with LangServe chain: [here](https://github.com/hemidactylus/langserve_cassandra_entomology_rag).
