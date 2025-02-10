def display_sources(source_docs):
    """
    Formats and returns the source documents used to answer the query.
    """
    if not source_docs:
        return "⚠️ No relevant sources found."

    source_text = "📖 **Sources:**\n\n"
    for doc in source_docs:
        page = doc.metadata.get("page", "N/A")
        content = doc.page_content[:200]  # Show first 200 characters
        source_text += f"- **Page {page}**: {content}...\n\n"

    return source_text
