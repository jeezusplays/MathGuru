import openai
from openai.embeddings_utils import get_embedding
from .settings import OPENAI_API_KEY
openai.api_key=OPENAI_API_KEY

def embedding(string):
    return get_embedding("test",engine="text-embedding-ada-002")