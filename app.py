import os
import gradio as gr
from modules.pdf_processor import process_pdf
from modules.rag_retriever import answer_query

# Set OpenAI API Key
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"  # Replace with your API key

# Gradio UI Setup
with gr.Blocks() as rag_ui:
    gr.Markdown("## 📘 AI-Powered PDF Chatbot")
    gr.Markdown("Upload a PDF, process it, and ask any questions!")

    with gr.Row():
        pdf_input = gr.File(label="📂 Upload PDF")
        process_button = gr.Button("🔄 Process PDF")

    status_output = gr.Textbox(label="⚡ Status", interactive=False)

    with gr.Row():
        query_input = gr.Textbox(label="❓ Ask a Question")
        query_button = gr.Button("🤖 Get Answer")

    answer_output = gr.Textbox(label="💡 Answer", interactive=False)
    sources_output = gr.Textbox(label="🔍 Sources", interactive=False)

    # Button Event Handling
    process_button.click(process_pdf, inputs=[pdf_input], outputs=[status_output])
    query_button.click(answer_query, inputs=[query_input], outputs=[answer_output, sources_output])

# Launch Gradio App
rag_ui.launch()
