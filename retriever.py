import faiss
import numpy as np
import requests

def create_faiss_index(embeddings):
    dimension = len(embeddings[0])
    index = faiss.IndexFlatL2(dimension)

    vectors = np.array(embeddings).astype("float32")
    index.add(vectors)

    return index


def search_chunks(query, chunks, index, k=3):
    response = requests.post(
        "http://localhost:11434/api/embeddings",
        json={
            "model": "nomic-embed-text",
            "prompt": query
        }
    )

    query_embedding = response.json()["embedding"]
    query_vector = np.array([query_embedding]).astype("float32")

    _, indices = index.search(query_vector, k)

    return [chunks[i] for i in indices[0]]