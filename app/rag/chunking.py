from typing import List


def chunk_text(text: str, chunk_size: int = 300, overlap: int = 50) -> List[str]:
    """
    Simple sliding window chunking.
    """
    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap

    return chunks
