# Cloud_Formation

# Python Function Documentation Generator

A tool to automatically generate detailed documentation for Python functions using OpenAI's GPT models.

## Features
- Parses Python files to extract function details.
- Generates documentation using OpenAI GPT (via LangChain).
- Outputs documentation in Markdown format.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd project/

## OPEN_API_KEY
- Add YOUR_OPEN_API_KEY  in config file.


## Testing with Postman
- File Input Example
- Method: POST
- URL: http://127.0.0.1:5000/generate-docs
- Body:
- Form-data:
- Key: file, Value: (python file [Ex: test.py])