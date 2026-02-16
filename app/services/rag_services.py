from typing import List
from app.vectorstore.chroma_store import query_documents


def retrieve_evidence(question: str, documents: List[str] | None = None) -> List[str]:
    """
    Phase: Persistent RAG retrieval.
    Documents parameter ignored — we now use global collection.
    """

    results = query_documents(question)

    if not results:
        return ["No relevant documents found."]

    return results
