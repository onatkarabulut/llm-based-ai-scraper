from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import logging as lg

lg.basicConfig(filename='logs/streamlit_app.log',
               level=lg.INFO,
               format='%(levelname)s:%(asctime)s:%(message)s',
               datefmt="%Y-%m-%d %H:%M:%S")

class Parse:
    def __init__(self):
        self.prompt = (
            "Your task is to retrieve precise information from the text provided here: {dom_content}."
            "Please adhere strictly to the following guidelines: \n\n" 
            "1. Targeted Extraction: Extract only the information that precisely aligns with this description: {parse_description}. " 
            "2. Limit Output: Include no additional commentary, notes, or explanations in your response." 
            "3. Return if Relevant: If nothing matches the description, respond with an empty string ('')." 
            "4. Exact Data Only: Provide only the explicitly requested data, without any extra text."
        )
        self.model = OllamaLLM(model="gemma2")

    def ollama_parse(self, doms, parse_desc):
        chain = ChatPromptTemplate.from_template(self.prompt) | self.model
        parsed_content = []

        for i, dom_content in enumerate(doms, start=1):
            response = chain.invoke({"dom_content": dom_content, "parse_description": parse_desc})
            lg.info(f"Parsed data {i} --> {len(doms)}")
            parsed_content.append(response)

        return "\n".join(parsed_content)
