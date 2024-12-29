from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os
from utils.parser import parse_code
from utils.doc_generator import generate_docs_with_langchain
from utils.formatter import format_docs
from config import OPENAI_API_KEY

app = Flask(__name__)

@app.route("/generate-docs", methods=["POST"])
def generate_docs():
    """
    API endpoint to generate documentation for an uploaded Python file.
    """
    # Check for API key
    if not OPENAI_API_KEY:
        return jsonify({"error": "OpenAI API key is missing or not configured"}), 500

    # Check for uploaded file
    if "file" not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    # Ensure the uploaded file is a Python file
    if file.filename.rsplit(".", 1)[1].lower() != "py":
        return jsonify({"error": "Invalid file type. Only .py files are allowed."}), 400

    try:
        # Read the file content in memory
        code = file.read().decode("utf-8")

        # Parse the code
        parsed_code = parse_code(code)

        if not parsed_code:
            return jsonify({"error": "No valid functions found in the uploaded Python file"}), 400

        # Generate documentation
        docs = generate_docs_with_langchain(parsed_code, OPENAI_API_KEY)

        # Format the documentation
        formatted_docs = format_docs(docs)

        # Return the generated documentation
        return jsonify({"documentation": formatted_docs})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
