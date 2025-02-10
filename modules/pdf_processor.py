import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

vectorstore = None  # Global FAISS index


def process_pdf(pdf_file):
    """
    Loads PDF, chunks text, generates embeddings, and creates FAISS index.
    """
    global vectorstore

    if not pdf_file:
        return "⚠️ No PDF uploaded. Please upload a document first."

    try:
        # Load PDF
        loader = PyPDFLoader(pdf_file.name)
        documents = loader.load()

        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        texts = text_splitter.split_documents(documents)

        # Generate embeddings and create FAISS index
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.from_documents(texts, embeddings)

        return "✅ PDF processed successfully! You can now ask questions."

    except Exception as e:
        return f"⚠️ Error processing PDF: {str(e)}"
