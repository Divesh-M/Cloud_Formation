from utils.parser import parse_code
from utils.doc_generator import generate_docs_with_langchain
from utils.formatter import format_docs
from config import OPENAI_API_KEY,file_path,output_file

def main():
    try:
        with open(file_path, 'r') as file:
            code = file.read()
        
        parsed_code = parse_code(code)
        docs = generate_docs_with_langchain(parsed_code, OPENAI_API_KEY)
        formatted_docs = format_docs(docs)
        
        with open(output_file, 'w') as output:
            output.write(formatted_docs)
        
        print(f"Documentation saved to {output_file}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
