# Cloud_Formation

# Python Function Documentation Generator

A tool to automatically generate detailed documentation for Python functions using OpenAI's GPT models.

## Features
- Parses Python files to extract function details.
- Generates documentation using OpenAI GPT (via LangChain).
- Outputs documentation in Markdown format.

- For now we are not saving output in markdown format. You can feel free to change the code to save output in markdown format.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd project/

## Creata a config file 
- While executing code, create a config.py file.
- Add YOUR_OPEN_API_KEY  in config file.
- Example:
- OPENAI_API_KEY = "YOUR_OPEN_API_KEY"


## Testing with Postman
- File Input Example
- Method: POST
- URL: http://127.0.0.1:5000/generate-docs
- Body:
- Form-data:
- Key: file, Value: (python file [Ex: test.py])

