def format_docs(docs):
    """
    Formats the generated documentation in Markdown.

    Args:
        docs (list): A list of documentation strings.

    Returns:
        str: Formatted Markdown string.
    """
    return "\n\n".join([f"### Function Documentation\n\n{doc}" for doc in docs])
    
