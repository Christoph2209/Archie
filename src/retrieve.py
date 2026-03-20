from sentence_transformers import SentenceTransformer
import chromadb

# Load vector DB
client = chromadb.Client()
collection = client.get_collection("documents")

# Embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

def query_agent(user_query, top_k=3):
    query_emb = model.encode([user_query])
    results = collection.query(
        query_embeddings=query_emb,
        n_results=top_k
    )
    answers = []
    for doc, meta in zip(results['documents'][0], results['metadatas'][0]):
        answers.append(f"{doc} (Source: {meta['source']})")
    return answers

if __name__ == "__main__":
    while True:
        q = input("Ask: ")
        answers = query_agent(q)
        print("\n".join(answers))
        print("-" * 50)