import faiss
import numpy as np
from typing import List


class VectorStore:
    def __init__(self, dimension: int):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.text_chunks = []

    def add(self, embeddings: np.ndarray, chunks: List[str]):
        self.index.add(embeddings)
        self.text_chunks.extend(chunks)

    def search(self, query_embedding: np.ndarray, top_k: int = 3):
        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            if idx < len(self.text_chunks):
                results.append(self.text_chunks[idx])

        return results
