from langchain.chains import LLMChain
from langchain.llms import OpenAIChat
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import SequentialChain

from .settings import OPENAI_API_KEY

gpt35 = OpenAIChat(openai_api_key=OPENAI_API_KEY,temperature=0, model="gpt-3.5-turbo-0613")
gpt4 = OpenAIChat(openai_api_key=OPENAI_API_KEY,temperature=0, model="gpt-4-0613")

template1 = """
Role:
You are a primary school math expert that can filter and segment the questions from OCR scanned text
Task:
From the given OCR scanned text: {ocr_text}, extract all the relevant questions and associated text into a list of lists (list[list[string]]).
{{ "questions": <<list here>> }}
"""

prompt1 = PromptTemplate(
    input_variables=["ocr_text"],
    template=template1                     
)

chain1 = LLMChain(
    llm=gpt4, # Using the stronger model for better extraction
    prompt=prompt1,
    output_key="question_list"
)

template2 = """
Role:
You are a primary school math expert that extracts the topics, and difficulty of the question given the primary school level
Task:
For the question: {question_text}, identify and provide the following metadata in the given structure:
{{
   "level": "{primary_level}",
   "topics": "[<<topics here>>]" (list[string]) ,
   "difficulty": "<<One of 'Very Easy', 'Easy', 'Medium', 'Hard', 'Very Hard'>>"
}}
A: <<response in JSON format>>
"""

prompt2 = PromptTemplate(
    input_variables=["question_text","primary_level"],
    template=template2                     
)

chain2 = LLMChain(
    llm=gpt4,
    prompt=prompt2,
    output_key="question_metadata"
)


#WE CANT STITCH IT TGT LIKE THIS, WE HAVE TO SPLIT IT BY A LOOP

get_questions = SequentialChain(
    chains=[chain1],
    input_variables=["ocr_text"],
    output_variables=["question_list"],
    verbose=True
)

get_metadata = SequentialChain(
    chains=[chain2],
    input_variables=["question_text","primary_level"],
    output_variables=["question_metadata"],
    verbose=True
)

