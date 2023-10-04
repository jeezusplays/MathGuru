from .settings import PINECONE_API_KEY,PINECONE_ENV
import pinecone

OPENAI_EMBEDDING_DIMENSION = 1536

pinecone.init(
    api_key=PINECONE_API_KEY,
    environment=PINECONE_ENV
)


# TODO 
# - Write helpers for pinecone
# - Include pinecone key in env | DONE

def _getindex(topic):
    current_indexes = pinecone.list_indexes()
    topic_index = f'ebs-{topic}-questions'
    if topic_index not in current_indexes:
        pinecone.create_index(topic_index, dimension=OPENAI_EMBEDDING_DIMENSION)

    return pinecone.Index(topic_index)

def saveEmbedding():
    pass

def delEmbedding():
    pass

# May not be needed - For future improvements
def searchQuestions(topics:list[str],question_text:str,k:int):
    pass