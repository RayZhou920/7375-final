import os
from dotenv import load_dotenv

load_dotenv()

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import ReadTheDocsLoader
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore

INDEX_NAME = "mongodb-doc-index"
MODEL_NAME = "text-embedding-3-small"
CHUNK_SIZE = 300
CHUNK_OVERLAP = 20

embeddings = OpenAIEmbeddings(model=MODEL_NAME)


def ingest_docs():
    loader = ReadTheDocsLoader("mongodb-docs/www.mongodb.com")
    raw_documents = loader.load()
    print(f"loaded {len(raw_documents)} documents")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP
    )
    documents = text_splitter.split_documents(raw_documents)

    for doc in documents:
        new_url = doc.metadata["source"]
        print(new_url)
        new_url = new_url.replace("mongodb-docs", "https:/")
        doc.metadata.update({"source": new_url})

    print(f"Going to add {len(documents)} to Pinecone")
    PineconeVectorStore.from_documents(
        documents, embeddings, index_name=INDEX_NAME
    )
    print("**** Loading to vectorstore done ****")


if __name__ == "__main__":
    ingest_docs()
