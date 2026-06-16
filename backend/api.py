from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
import os
import shutil

from backend.llm_service import generate_summary
from backend.vector import add_pdf_to_db

router = APIRouter()

DOCUMENTS_DIR = os.path.join("data", "documents")
os.makedirs(DOCUMENTS_DIR, exist_ok=True)


class GenerateRequest(BaseModel):
    topic: str
    file: str = "all"


@router.post("/generate")
def generate(req: GenerateRequest):
    response = generate_summary(req.topic, req.file)
    return {"response": response}


@router.get("/documents")
def list_documents():
    files = os.listdir(DOCUMENTS_DIR)

    return {
        "documents": [
            {
                "name": f,
                "path": os.path.join(DOCUMENTS_DIR, f)
            }
            for f in files
            if os.path.isfile(os.path.join(DOCUMENTS_DIR, f))
        ]
    }


@router.post("/add_pdf")
async def add_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")
    
    file_path = os.path.join(DOCUMENTS_DIR, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    pages_added = add_pdf_to_db(file_path)

    return {
        "message": "PDF uploaded and added to vector DB",
        "file": file.filename,
        "pages_added": pages_added,
    }