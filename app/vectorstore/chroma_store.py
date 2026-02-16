import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer
import uuid

# Persistent local storage
chroma_client = chromadb.Client(
    Settings(
        persist_directory="./chroma_db",
        anonymized_telemetry=False
    )
)

# Global collection
collection = chroma_client.get_or_create_collection(
    name="global_documents"
)

# Embedding model
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(texts):
    return embedding_model.encode(texts).tolist()


def add_documents(chunks: list[str], metadata: list[dict]):
    ids = [str(uuid.uuid4()) for _ in chunks]

    embeddings = embed_text(chunks)

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        metadatas=metadata,
        ids=ids
    )



def query_documents(query: str, top_k: int = 3):
    query_embedding = embed_text([query])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=top_k
    )

    return results.get("documents", [[]])[0]
