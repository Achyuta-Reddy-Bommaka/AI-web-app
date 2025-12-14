from fastapi import APIRouter
from app.schemas.rag import RAGRequest
from app.services.rag_service import add_document, answer_query

router = APIRouter()

# Add some sample text
add_document("FastAPI is a modern Python web framework for APIs.")
add_document("Streamlit is used for building data apps quickly.")

@router.post("/ask")
def ask(req: RAGRequest):
    answer, context = answer_query(req.query)
    return {"answer": answer, "context": context}