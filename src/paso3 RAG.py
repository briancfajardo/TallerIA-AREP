from langchain_community.document_loaders import TextLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone, PodSpec
import os

os.environ["OPENAI_API_KEY"] = "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"
os.environ["PINECONE_API_KEY"] = "c23c8676-ddcf-4739-8e86-fe1fb0dea151"
os.environ["PINECONE_ENV"] = "gcp-starter"

def loadText():
    loader = TextLoader("Conocimiento.txt")
    documents = loader.load()
    #text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap  = 200,
        length_function = len,
        is_separator_regex = False,
    )


    docs = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    import pinecone


    index_name = "langchain-demo"
    pc = Pinecone(api_key='c23c8676-ddcf-4739-8e86-fe1fb0dea151')

    print(pc.list_indexes())

    # First, check if our index already exists. If it doesn't, we create it
    if len(pc.list_indexes())==0:
        # we create a new index
        #pc.create_index(name=index_name, metric="cosine", dimension=1536)
        pc.create_index(
            name=index_name,
            dimension=1536,
            metric="cosine",
            spec=PodSpec(
                environment=os.getenv("PINECONE_ENV"),
                pod_type="p1.x1",
                pods=1
            )
        )

    # The OpenAI embedding model `text-embedding-ada-002 uses 1536 dimensions`
    docsearch = PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)

def search():
    embeddings = OpenAIEmbeddings()

    index_name = "langchain-demo"
    # if you already have an index, you can load it like this
    docsearch = PineconeVectorStore.from_existing_index(index_name, embeddings)

    query = "¿Que pasó en Enero de 2011 en AMD?"
    docs = docsearch.similarity_search(query)

    print(docs[0].page_content)

loadText()
search()