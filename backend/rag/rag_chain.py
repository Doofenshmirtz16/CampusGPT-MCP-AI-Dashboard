from backend.rag.retriever import retrieve

from backend.agent.llm_router import model


def answer_question(question):

    docs = retrieve(question)

    context = "\n\n".join(docs)

    prompt = f"""
Answer using only the context below.

Context:

{context}

Question:

{question}
"""

    response = model.generate_content(
        prompt
    )

    return response.text