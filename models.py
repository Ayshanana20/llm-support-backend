from pydantic import BaseModel, Field

class SupportRequest(BaseModel):
    question: str = Field(..., min_length=3, description="The customer support question.")
    user_id: str = Field(..., description="Unique identifier for the user.")

class SupportResponse(BaseModel):
    answer: str
    model_used: str
    tokens_used: int
    cost_estimate_usd: float