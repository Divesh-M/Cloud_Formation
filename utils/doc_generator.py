from langchain_openai.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage

def generate_docs_with_langchain(parsed_code, api_key):
    """
    Generates documentation for parsed Python functions using LangChain.

    Args:
        parsed_code (list): List of parsed function details.
        api_key (str): OpenAI API key.

    Returns:
        list: A list of generated documentation strings.
    """
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-4",
        openai_api_key=api_key
    )

    prompt_template = PromptTemplate(
        input_variables=["function_name", "arguments", "docstring"],
        template=(
            "Generate detailed documentation for the following Python function:\n\n"
            "Function Name: {function_name}\n"
            "Arguments: {arguments}\n"
            "Docstring: {docstring}\n\n"
            "Provide a clear description of what the function does, its parameters, and the return value."
        )
    )

    docs = []
    for func in parsed_code:
        try:
            prompt_text = prompt_template.format(
                function_name=func["name"],
                arguments=", ".join(func["args"]),
                docstring=func["docstring"]
            )
            response = llm([HumanMessage(content=prompt_text)])
            docs.append(response.content)
        except Exception as e:
            print(f"Error generating docs for function {func['name']}: {e}")
    return docs