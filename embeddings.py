import requests

def create_embeddings(chunks):
    embeddings = []

    for chunk in chunks:
        response = requests.post(
            "http://localhost:11434/api/embeddings",
            json={
                "model": "nomic-embed-text",
                "prompt": chunk
            }
        )

        embeddings.append(response.json()["embedding"])

    return embeddings