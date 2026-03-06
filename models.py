from pydantic import BaseModel, Field
from typing import List

# --- INPUT MODEL ---
class ProposalRequest(BaseModel):
    client_name: str
    budget: float = Field(..., description="Maximum budget provided by the client")
    industry: str = Field(..., description="Industry of the client to tailor the products")
    requirements_note: str = Field(..., description="Any specific needs (e.g., 'corporate gifting', 'office supplies')")

# --- OUTPUT MODELS ---
class ProductItem(BaseModel):
    product_name: str
    unit_price: float
    quantity: int
    total_cost: float
    sustainability_reason: str

class ProposalResponse(BaseModel):
    suggested_product_mix: List[ProductItem] = Field(..., description="List of suggested sustainable products")
    total_estimated_cost: float = Field(..., description="Total cost of the proposal, must be <= budget")
    budget_allocation_summary: str = Field(..., description="Brief summary of how the budget was allocated")
    impact_positioning_summary: str = Field(..., description="Summary of the environmental impact of this proposal")