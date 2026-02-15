from sentence_transformers import SentenceTransformer

# Load once globally (important)
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_texts(texts):
    return model.encode(texts, convert_to_numpy=True)
