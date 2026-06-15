from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.agent.tool_router import route_query
from backend.agent.response_generator import generate_response

app = FastAPI(
    title="CampusGPT Agent"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():

    return {
        "message": "CampusGPT Agent Running"
    }


@app.get("/chat")
def chat(query: str):

    result = route_query(query)

    answer = generate_response(
        query,
        result
    )

    return {
        "answer": answer,
        "tools_used": result["tools_used"]
    }