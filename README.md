# info7375-chatbot-rag-vector-db

### Report and Video

[Report](./Ruis_Report.pdf)
[Video](https://youtu.be/3rSdGStHiIc)

### Installation

1. Clone the repository.
2. Navigate to your repository directory: ‘cd your-repository’.
3. Create a virtual environment: 'pipenv shell'.
4. Install the required packages: 'pipenv install'.
5. Set up environment variables:
   Create a `.env` file in the root directory of your project and add your Pinecone API key, OpenAI API key
   ```
   PINECONE_API_KEY=
   OPENAI_API_KEY=
   ```
6. Fetch data from the MongoDB website:
   mkdir mongodb-docs
   wget -r -P mongodb-docs -E https://www.mongodb.com/docs/manual
7. Pre-process the data by running the process_data.py script. You should see the following message if successful:
   Going to add xxx to Pinecone
   Loading to vectorstore done
8. Start the app: streamlit run main.py.


### Explanation of pre-processing data

#### Pass data to vector database (Pinecone) using `process_data.py`

The command wget -r -P mongodb-docs -E https://www.mongodb.com/docs/manual retrieves documents from MongoDB's documentation website, processes them, and stores them in a Pinecone Vector Store for efficient retrieval and embedding using OpenAI's embedding model.

#### Features

- Loads documents from MongoDB documentation.
- Splits documents into smaller chunks for efficient processing.
- Updates document metadata with the correct source URLs.
- Adds processed documents to a Pinecone Vector Store.

#### Requirements

- Python 3.x
- python-dotenv
- langchain
- langchain-community
- langchain-openai
- langchain-pinecone
- Pinecone account and API key

### Explanation of RAG (Retrieval-Augmented Generation) Script (rag.py)

This Python script implements a Retrieval-Augmented Generation (RAG) model using LangChain, OpenAI, and Pinecone. The script retrieves relevant documents based on a query, incorporates chat history, and generates responses using OpenAI's language models.

#### Features

- Embeds documents using OpenAI's embedding model.
- Retrieves documents from Pinecone Vector Store.
- Rephrases queries and performs retrieval-based question answering.
- Combines retrieved documents to generate a response.

#### Requirements

- Python 3.x
- python-dotenv
- langchain
- langchain-openai
- langchain-pinecone
- Pinecone account and API key
- OpenAI API key

#### Functionality

##### `run_llm()`

This function:

1. Initializes OpenAI embeddings and Pinecone Vector Store.
2. Sets up a chat model with OpenAI's language model.
3. Pulls prompts for rephrasing queries and retrieval-based question answering.
4. Creates a history-aware retriever and a retrieval chain.
5. Invokes the retrieval chain with the input query and chat history.
6. Returns the generated result.
