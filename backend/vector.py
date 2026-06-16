from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

import os
from pypdf import PdfReader

def read_pdf(path: str):
    reader = PdfReader(path)

    pages = []
    for page in reader.pages:
        text = page.extract_text() or ""
        pages.append(text)

    return pages

embeddings = OllamaEmbeddings(model="embeddinggemma")

db_location = "./chroma_langchain_db"

vector_store = Chroma(
    collection_name="text",
    persist_directory=db_location,
    embedding_function=embeddings
)

def add_pdf_to_db(pdf_path: str):
    pages = read_pdf(pdf_path)

    documents = []
    ids = []

    for i, text in enumerate(pages):
        if not text.strip():
            continue

        doc = Document(
            page_content=text,
            metadata={
                "page": i,
                "source": pdf_path
            }
        )

        documents.append(doc)

        ids.append(f"{os.path.basename(pdf_path)}_{i}")

    if documents:
        vector_store.add_documents(
            documents=documents,
            ids=ids
        )

    return len(documents)


retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)
