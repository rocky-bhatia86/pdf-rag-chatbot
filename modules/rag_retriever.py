from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from modules.utils import display_sources
from modules.pdf_processor import vectorstore


def answer_query(query):
    """
    Retrieves relevant content from FAISS and generates an answer using OpenAI.
    """
    if vectorstore is None:
        return "⚠️ No PDF has been processed yet. Please upload and process a PDF first.", ""

    if not query.strip():
        return "⚠️ Please enter a valid question.", ""

    try:
        # Create a retrieval-based QA chain
        qa_chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(model="gpt-3.5-turbo"),
            retriever=vectorstore.as_retriever(),
            return_source_documents=True
        )

        # Get response and sources
        result = qa_chain({"query": query})
        answer = result["result"]
        sources = display_sources(result["source_documents"])

        return answer, sources

    except Exception as e:
        return f"⚠️ Error answering query: {str(e)}", ""
