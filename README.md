# Rayeva AI - B2B Proposal Generator

## 📌 Project Overview
This project implements **Module 2: AI B2B Proposal Generator** for the Rayeva AI Systems Assignment. It is a production-ready API built with FastAPI that generates structured, sustainable commerce proposals.

## 🏗️ Architecture Overview
The system follows a strict separation of AI logic and business logic:
* **FastAPI Framework:** Handles HTTP requests and routing (`main.py`).
* **Pydantic Models:** Enforces structured JSON outputs and validates incoming business parameters (`models.py`).
* **AI Service Layer:** Isolates OpenAI API calls, prompt construction, and logging (`ai_service.py`).
* **Environment Variables:** Manages secure API keys via `.env`.

## 🧠 AI Prompt Design
The prompt architecture is split into two parts to maintain clarity and context:
1.  **System Prompt:** Defines the persona ("Expert AI B2B Sustainable Commerce Consultant") and strictly outlines the required output components (budget allocation, cost breakdown, impact positioning).
2.  **User Prompt:** Dynamically injects the specific business logic (Client Name, Industry, Budget, Specific Requirements) without hardcoding values into the core AI instructions.
This separation ensures the AI stays grounded in business logic while generating the structured output.

## 🚀 How to Run
1. Clone the repository.
2. Install dependencies: `pip install fastapi uvicorn pydantic python-dotenv openai`
3. Add your `OPENAI_API_KEY` in the `.env` file.
4. Run the server: `uvicorn main:app --reload`
5. Test the API via Swagger UI at `http://localhost:8000/docs`.
