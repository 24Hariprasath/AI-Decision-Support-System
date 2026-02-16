from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.rag.chunking import chunk_text
from app.vectorstore.chroma_store import add_documents
from docx import Document
from io import BytesIO

router = APIRouter()


@router.post("/documents/upload")
async def upload_document(
    file: UploadFile = File(...),
    document_type: str = Form(...)
):
    try:
        content = await file.read()

        # Handle DOCX files
        if file.filename.endswith(".docx"):
            doc = Document(BytesIO(content))
            text = "\n".join([para.text for para in doc.paragraphs])

        # Handle TXT files
        elif file.filename.endswith(".txt"):
            text = content.decode("utf-8")

        else:
            raise HTTPException(
                status_code=400,
                detail="Only .txt and .docx files are supported."
            )

        # Chunk text
        chunks = chunk_text(text)

        if not chunks:
            raise HTTPException(
                status_code=400,
                detail="Document contains no readable text."
            )

        metadata = [
            {"source": file.filename, "type": document_type}
            for _ in chunks
        ]

        # Store in vector DB
        add_documents(chunks, metadata)

        return {
            "message": f"{file.filename} uploaded successfully as {document_type}.",
            "chunks_created": len(chunks)
        }
    except Exception as e:
        raise e
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))
