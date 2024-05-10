from langchain_groq import ChatGroq
from .prompts import chat_prompt
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()


def get_chain_chat():

    llm = ChatGroq(temperature=0, model_name="llama3-70b-8192", api_key="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")
    output_parser = StrOutputParser()
    chain = (chat_prompt 
    | llm 
    | output_parser
    )
    return chain

def invoke_answer(input):
    chain = get_chain_chat()
    res = chain.invoke(input)
    return res
