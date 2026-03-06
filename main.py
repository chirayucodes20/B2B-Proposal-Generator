from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from models import ProposalRequest, ProposalResponse
from ai_service import generate_b2b_proposal

# YEH WALI LINE TERE CODE SE GAYAB HO GAYI THI!
app = FastAPI(
    title="Rayeva AI - B2B Proposal Generator",
    description="API for Applied AI Sustainable Commerce Module",
    version="1.0.0"
)

# 1. Frontend UI serve karne wala route
@app.get("/")
def serve_frontend():
    return FileResponse("index.html")

# 2. Main API endpoint jo frontend se data lega aur AI ko bhejega
@app.post("/api/generate-proposal", response_model=ProposalResponse)
def create_proposal(request: ProposalRequest):
    try:
        ai_generated_proposal = generate_b2b_proposal(request)
        return ai_generated_proposal
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"AI Processing Error: {str(e)}")