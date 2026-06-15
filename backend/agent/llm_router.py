import google.generativeai as genai
import os

from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def decide_tool(user_query):

    prompt = f"""
You are a routing agent for CampusGPT.

Available tools:

1. library
   - books
   - authors
   - library availability
   - shelf information

2. events
   - workshops
   - hackathons
   - seminars
   - club activities
   - campus events

3. cafeteria
   - food
   - lunch
   - breakfast
   - dinner
   - cafeteria menu

4. academics
   - attendance policy
   - placement policy
   - grading policy
   - exam rules
   - academic regulations
   - handbook questions

Question:
{user_query}

Return ONLY one word:

library
events
cafeteria
academics
"""

    response = model.generate_content(prompt)

    return response.text.strip().lower()

def decide_tools(user_query):

    prompt = f"""
You are a routing agent.

Available tools:

library
events
cafeteria
academics

Determine ALL tools required.

Return ONLY comma-separated names.

Examples:

Question:
What AI books are available?

Answer:
library

Question:
What AI books are available and what workshops are happening?

Answer:
library,events

Question:
What is today's lunch menu and attendance policy?

Answer:
cafeteria,academics

Question:
{user_query}
"""

    response = model.generate_content(prompt)

    return [
        tool.strip().lower()
        for tool in response.text.split(",")
    ]