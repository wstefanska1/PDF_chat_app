<h1>AI Document Assistant - Local RAG System</h1>

<p>
A containerized backend-centric AI application based on a local LLM (Ollama) and Retrieval-Augmented Generation (RAG).
The system enables PDF document ingestion and generates academic-style responses strictly grounded in retrieved content.
The frontend is minimal and serves as a lightweight interface for API interaction.
</p>

<h2>Technologies</h2>

- <b>Python (FastAPI)</b>  
- <b>Ollama (local LLM + embeddings)</b>  
- <b>LangChain</b>  
- <b>ChromaDB (vector database)</b>  
- <b>Docker / Docker Compose</b>
- <b>HTML / CSS / JavaScript</b>  

<h2>Architecture</h2>

<p>
A containerized multi-component system.  
The application follows a backend-centric RAG architecture integrating document processing, vector search, and local LLM inference.
</p>

<p>
Frontend ↔ FastAPI (single entrypoint) ↔ ChromaDB (vector store) + Ollama LLM
</p>

<h2>Backend Overview</h2>

<p>
The FastAPI backend acts as the core orchestration layer of the system, handling all business logic including document ingestion, processing, retrieval, and text generation.
</p>

<p>
PDF files are split into chunks, embedded, and stored in ChromaDB. Incoming user queries trigger semantic search, and retrieved context is passed to the local LLM for generation.
</p>

<h2>System Design Highlights</h2>

<ul>
  <li>Backend-centric architecture with a single exposed API service</li>
  <li>Containerized multi-service environment (API, LLM, vector database)</li>
  <li>Retrieval-Augmented Generation (RAG) pipeline</li>
  <li>Semantic search over PDF documents using vector embeddings</li>
</ul>

<h2>Key Features</h2>

<ul>
  <li>PDF upload and processing pipeline</li>
  <li>Context-aware text generation based on retrieved documents</li>
  <li>REST API built with FastAPI</li>
  <li>Local LLM inference via Ollama</li>
  <li>Vector search using ChromaDB</li>
  <li>Dockerized deployment (Docker Compose)</li>
</ul>

<h2>Workflow</h2>

<p>
PDF upload → chunking → embedding → ChromaDB storage → query → semantic retrieval → LLM generation → response
</p>

<h2>Demo</h2>

<p>
    <img width="2880" height="1530" alt="demo" src="https://github.com/user-attachments/assets/e4438da9-f331-49b5-b316-1417fe68b4ca" />
</p>

