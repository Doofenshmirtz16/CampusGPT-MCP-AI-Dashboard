# CampusGPT – MCP + AI Campus Assistant

CampusGPT is an AI-powered campus assistant that combines **Model Context Protocol (MCP)** services, **Retrieval-Augmented Generation (RAG)**, and **Large Language Models (LLMs)** to answer student queries using structured campus data and institutional documents.

The system can intelligently route questions to the correct campus service, combine information from multiple tools, and answer policy-related questions using semantic document retrieval.

---

## Features

### AI Tool Routing

CampusGPT uses Gemini to determine which campus tools should answer a user query.

Examples:

* "What AI books are available?"
* "What workshops are happening this month?"
* "What is today's lunch menu?"
* "What AI books are available and what workshops are happening this week?"

The system automatically selects the required tools.

---

### Multi-Tool Query Support

A single question can use multiple campus services simultaneously.

Example:

> What AI books are available and what workshops are happening this week?

CampusGPT will:

1. Query the Library Service
2. Query the Events Service
3. Merge results
4. Generate a natural language answer

---

### MCP Services

The system includes multiple campus services exposed as independent APIs:

#### Library Service

Provides:

* Book search
* Author information
* Shelf location
* Availability

#### Events Service

Provides:

* Upcoming events
* Workshops
* Seminars
* Club activities

#### Cafeteria Service

Provides:

* Daily menu
* Meal information
* Food availability

---

### Retrieval-Augmented Generation (RAG)

CampusGPT can answer questions about campus documents.

Current implementation includes:

* Placement Policy PDF
* Semantic document search
* ChromaDB vector database
* Gemini-powered answer generation

Example:

> What is the placement policy regarding pre-placement talks?

The system retrieves relevant document chunks and generates a grounded response.

---

## System Architecture

```text
Frontend (Next.js)
        │
        ▼
CampusGPT Agent
        │
        ▼
Gemini Router
        │
        ▼
 ┌──────────────┬──────────────┬──────────────┬──────────────┐
 │ Library MCP  │ Events MCP   │ Cafeteria MCP│ RAG Engine   │
 └──────────────┴──────────────┴──────────────┴──────────────┘
```

## Tech Stack

### Frontend

* Next.js
* React
* TypeScript
* Tailwind CSS

### Backend

* FastAPI
* Python

### AI

* Gemini API
* Retrieval-Augmented Generation

### Vector Database

* ChromaDB

### Embeddings

* Sentence Transformers
* all-MiniLM-L6-v2

---

## Project Structure

```text
CampusGPT/
│
├── backend/
│   ├── agent/
│   ├── database/
│   ├── rag/
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── mcp_servers/
│   ├── library_server/
│   ├── events_server/
│   └── cafeteria_server/
│
├── docs/
│   └── Placement Policy.pdf
│
└── data/
```

## Installation

### Clone Repository

```bash
git clone https://github.com/Doofenshmirtz16/CampusGPT-MCP-AI-Dashboard.git
cd CampusGPT-MCP-AI-Dashboard
```

### Backend Setup

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

### Frontend Setup

```bash
cd frontend

npm install
```

### Environment Variables

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## Running the Project

### Start MCP Services

```bash
python mcp_servers/library_server/app.py

python mcp_servers/events_server/app.py

python mcp_servers/cafeteria_server/app.py
```

### Start Backend

```bash
python -m uvicorn backend.main:app --reload --port 8000
```

### Start Frontend

```bash
cd frontend

npm run dev
```

Open:

```text
http://localhost:3000
```

---

## Example Queries

### Library

```text
What AI books are available?
```

### Events

```text
What workshops are happening this month?
```

### Cafeteria

```text
What is today's lunch menu?
```

### Multi-Tool

```text
What AI books are available and what workshops are happening this week?
```

### RAG

```text
What is the placement policy for pre-placement talks?
```

---

## Future Improvements

* Authentication
* Student profiles
* Course information MCP
* Hostel management MCP
* Attendance MCP
* Fine-tuned campus model
* Deployment on cloud infrastructure

---

## License

MIT License

---

## Author

Sumit Sharma

Engineering Physics

IIT Roorkee

CampusGPT demonstrates the integration of MCP architecture, LLM-based routing, multi-tool reasoning, and Retrieval-Augmented Generation for intelligent campus assistance.
