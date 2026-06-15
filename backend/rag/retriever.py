import chromadb

from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

client = chromadb.PersistentClient(
    path="backend/rag/chroma_db"
)

collection = client.get_collection(
    "academic_docs"
)


def retrieve(question):

    query_embedding = model.encode(
        question
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=3
    )

    return results["documents"][0]

if __name__ == "__main__":

    docs = retrieve(
        "placement talk policy"
    )

    for doc in docs:

        print("\n")
        print(doc[:300])