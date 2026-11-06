# LLM-Powered Customer Support Backend API

A reliable, production-ready FastAPI backend service designed to handle customer support inquiries via an LLM, featuring input validation, structured logging, cost estimation, and fallback patterns.

---

## **Tech Stack**
* **Python** (v3.10+)
* **FastAPI** (Web framework & automatic documentation)
* **Pydantic** (Data validation & serialization)
* **Uvicorn** (ASGI server)
* **OpenAI SDK / Python-Dotenv** (LLM integration and environment management)

---

## **Project Structure**
```text
llm-support-backend/
│
├── .env                  # Environment variables (OpenAI API Key)
├── .venv/                # Python virtual environment
├── main.py               # FastAPI application, routing, and error handling
├── models.py             # Pydantic request/response validation schemas
├── services.py           # LLM core logic, fallback handling, token & cost calculation
└── test_main.py          # Automated test suite using TestClient