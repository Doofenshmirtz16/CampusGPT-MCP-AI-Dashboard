from backend.agent.llm_router import model


def generate_response(
    user_query,
    tool_results
):

    prompt = f"""
User Question:
{user_query}

Tool Results:
{tool_results}

Generate a natural answer.
"""

    response = model.generate_content(
        prompt
    )

    return response.text