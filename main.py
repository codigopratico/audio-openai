from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()

cliente = OpenAI()

# Criar um aúdio a partir de um prompt
resposta = cliente.chat.completions.create(
  model='gpt-4o-audio-preview',
  modalities=['text', 'audio'],
  audio={'format': 'wav', 'voice': 'alloy'},
  messages=[
    {'role': 'user', 'content': 'Crie um áudio convidadando as pessoas para participarem da Jornada Python, um jornada de aulas gratuitas onde elas aprendem a construir 4 projetos completos em Python, partindo do zero'}
  ]  
)

faixa_audio = resposta.choices[0].message.audio.data
faixa_audio_bytes = base64.b64decode(faixa_audio)

with open('audio.wav', 'wb') as arquivo_audio:
  arquivo_audio.write(faixa_audio_bytes)