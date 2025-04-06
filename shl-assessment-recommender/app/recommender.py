from sentence_transformers import SentenceTransformer
import numpy as np
import json

# Load model once
model = SentenceTransformer("all-MiniLM-L6-v2")

def recommend(query, top_k=10):
    # Encode user query
    query_vec = model.encode([query])[0]

    # Load embeddings and assessment data
    db_vecs = np.load("data/embeddings.npy")
    with open("data/assessments.json", "r") as f:
        assessments = json.load(f)

    # Compute cosine similarities
    similarities = np.dot(db_vecs, query_vec)
    top_indices = similarities.argsort()[-top_k:][::-1]

    return [assessments[i] for i in top_indices]
if __name__ == "__main__":
    query = "Looking for assessments to hire people skilled in .NET and C#"
    results = recommend(query)

    for res in results:
        print(f"{res['name']} - {res['url']}")
        print(f"Remote: {res['remote_testing']}, Adaptive: {res['adaptive_support']}, Type: {res['test_type']}")
        print("-" * 50)