import os
import json
import logging
from dotenv import load_dotenv
from openai import OpenAI
from models import ProposalRequest, ProposalResponse

# 1. Environment-based API key management 
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 2. Prompt + response logging setup 
logging.basicConfig(
    filename="ai_interactions.log", 
    level=logging.INFO, 
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def generate_b2b_proposal(request_data: ProposalRequest) -> ProposalResponse:
    """
    Core function to generate the B2B proposal using AI.
    It takes the Pydantic request model and returns the Pydantic response model.
    """
    # Create the System Prompt (AI ka Role)
    system_prompt = (
        "You are an expert AI B2B Sustainable Commerce Consultant. "
        "Your task is to generate a structured B2B proposal. "
        "You must provide a suggested sustainable product mix[cite: 16], "
        "ensure the budget allocation is strictly within the provided limit[cite: 17], "
        "provide an estimated cost breakdown[cite: 18], "
        "and write an impact positioning summary (e.g., plastic saved, carbon reduced)[cite: 19]."
    )
    
    # Create the User Prompt (Business Logic Data)
    user_prompt = (
        f"Client Name: {request_data.client_name}\n"
        f"Client Industry: {request_data.industry}\n"
        f"Maximum Budget: ₹{request_data.budget}\n"
        f"Specific Requirements: {request_data.requirements_note}"
    )

    # Log the prompt 
    logging.info("=== NEW AI REQUEST ===")
    logging.info(f"System Prompt: {system_prompt}")
    logging.info(f"User Prompt: {user_prompt}")

    # Call OpenAI API
    # Hum `.beta.chat.completions.parse` use kar rahe hain taaki 
    # AI strict Structured JSON output de [cite: 20, 32] based on our models.py
    response = client.beta.chat.completions.parse(
        model="gpt-4o-mini", # Fast aur sasta model
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        response_format=ProposalResponse, # Ye Pydantic model AI ko force karega exact JSON format dene ke liye
    )

    # Get the parsed response
    ai_output = response.choices[0].message.parsed

    # Log the response 
    logging.info(f"AI Response: {ai_output.model_dump_json()}")

    return ai_output