import requests
import os
from backend.agent.llm_router import decide_tools

LIBRARY_URL = os.getenv("LIBRARY_URL")
EVENTS_URL = os.getenv("EVENTS_URL")
CAFETERIA_URL = os.getenv("CAFETERIA_URL")
ACADEMIC_URL = os.getenv("ACADEMIC_URL")

def route_query(user_query):

    tools = decide_tools(user_query)

    results = {}

    if "library" in tools:
        results["library"] = call_library(user_query)

    if "events" in tools:
        results["events"] = call_events(user_query)

    if "cafeteria" in tools:
        results["cafeteria"] = call_cafeteria(user_query)

    if "academics" in tools:
        results["academics"] = call_academics(user_query)

    return {
        "tools_used": tools,
        "results": results
    }

def call_library(query):

    search_term = extract_library_term(query)

    response = requests.get(
        f"{LIBRARY_URL}/search",
        params={"query": search_term},
        timeout=10
    )

    return response.json()


def call_events(query):

    response = requests.get(
        f"{EVENTS_URL}/upcoming",
        timeout=10
    )

    return response.json()


def call_cafeteria(query):

    response = requests.get(
        f"{CAFETERIA_URL}/menu",
        timeout=10
    )

    return response.json()


def call_academics(query):

    response = requests.get(
        f"{ACADEMIC_URL}/ask",
        params={"query": query},
        timeout=20
    )

    return response.json()


def extract_library_term(query):

    q = query.lower()

    if "artificial intelligence" in q:
        return "AI"

    if "ai" in q:
        return "AI"

    if "deep learning" in q:
        return "Deep Learning"

    if "operating system" in q:
        return "Operating Systems"

    return query
