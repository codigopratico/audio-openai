from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

cliente = OpenAI()

resposta = cliente.chat.completions.create(
