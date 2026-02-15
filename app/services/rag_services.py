from typing import List
from app.rag.chunking import chunk_text
from app.rag.embedding import embed_texts
from app.rag.vector_store import VectorStore

# Initialize global vector store (in-memory for Phase 2)
vector_store = VectorStore(dimension=384)


def retrieve_evidence(question: str, documents: List[str] | None) -> List[str]:
    if not documents:
        return ["No supporting documents provided."]

    # 1. Chunk documents
    all_chunks = []
    for doc in documents:
        chunks = chunk_text(doc)
        all_chunks.extend(chunks)

    # 2. Embed document chunks
    doc_embeddings = embed_texts(all_chunks)

    # 3. Add to vector store
    vector_store.add(doc_embeddings, all_chunks)

    # 4. Embed query
    query_embedding = embed_texts([question])

    # 5. Search similar chunks
    results = vector_store.search(query_embedding, top_k=3)

    return results
