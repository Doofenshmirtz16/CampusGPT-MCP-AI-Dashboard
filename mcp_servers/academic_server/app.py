from fastapi import FastAPI

from backend.rag.rag_chain import answer_question

app = FastAPI(
    title="Academic MCP Server"
)


@app.get("/")
def root():

    return {
        "server": "Academic MCP",
        "status": "running"
    }


@app.get("/ask")
def ask(query: str):

    answer = answer_question(query)

    return {
        "question": query,
        "answer": answer
    }