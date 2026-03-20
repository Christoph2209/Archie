from ingest import ingest_documents
from retrieve import query_agent

if __name__ == "__main__":
    # Step 1: Ingest all docs
    ingest_documents()

    # Step 2: Query loop
    print("Agent ready. Ask about your documents!")
    while True:
        q = input("You: ")
        answers = query_agent(q)
        for a in answers:
            print(f"- {a}")