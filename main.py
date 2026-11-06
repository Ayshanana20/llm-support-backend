import logging
from fastapi import FastAPI, HTTPException, status
from models import SupportRequest, SupportResponse
from services import call_llm_with_fallback

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title="LLM Support Backend API", version="1.0")

@app.post("/support", response_model=SupportResponse, status_code=status.HTTP_200_OK)
def handle_support_question(payload: SupportRequest):
    logger.info(f"Received support request from user: {payload.user_id}")
    
    try:
        answer, model_used, tokens, cost = call_llm_with_payload = call_llm_with_fallback(payload.question)
        logger.info(f"Successfully processed request using {model_used}. Tokens: {tokens}")
        
        return SupportResponse(
            answer=answer,
            model_used=model_used,
            tokens_used=tokens,
            cost_estimate_usd=cost
        )
    except Exception as e:
        logger.error(f"Failed to process support request: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Service temporarily unavailable. Error: {str(e)}"
        )