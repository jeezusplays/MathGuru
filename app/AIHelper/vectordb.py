from .settings import PINECONE_API_KEY,PINECONE_ENV
import pinecone

pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENV
)

# TODO 
# - Write helpers for pinecone
# - Include pinecone key in env

PINECONE_API_KEY = ""

def saveEmbedding():
    pass

def delEmbedding():
    pass

def searchQuestions(topics:list[str],question_text:str,k:int):
    pass