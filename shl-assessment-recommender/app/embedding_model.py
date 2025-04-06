from sentence_transformers import SentenceTransformer
import json
import numpy as np
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

def generate_embeddings(json_path="data/assessments.json", output_path="data/embeddings.npy"):
    with open(json_path, "r") as f:
        data = json.load(f)

    texts = [item["name"] + " " + item["test_type"] for item in data]
    embeddings = model.encode(texts)

    np.save(output_path, embeddings)
    print(f"Embeddings saved to {output_path}")

if __name__ == "__main__":
    generate_embeddings()