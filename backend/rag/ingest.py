import fitz
import chromadb

from sentence_transformers import SentenceTransformer

PDF_PATH = "docs/Placement Policy.pdf"

pdf = fitz.open(PDF_PATH)

text = ""

for page in pdf:
    text += page.get_text()

# Chunking
chunks = []

chunk_size = 500

for i in range(0, len(text), chunk_size):

    chunks.append(
        text[i:i + chunk_size]
    )

print(f"Total Chunks: {len(chunks)}")

# Embedding Model

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Chroma DB

client = chromadb.PersistentClient(
    path="backend/rag/chroma_db"
)

collection = client.get_or_create_collection(
    name="academic_docs"
)

for idx, chunk in enumerate(chunks):

    embedding = model.encode(
        chunk
    ).tolist()

    collection.add(
        ids=[str(idx)],
        documents=[chunk],
        embeddings=[embedding]
    )

print("Embeddings Stored Successfully")