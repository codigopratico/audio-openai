from openai import OpenAI
from dotenv import load_dotenv
import base64

load_dotenv()

cliente = OpenAI()

# Criar um áudio a partir de um prompt
# resposta = cliente.chat.completions.create(
#   model='gpt-4o-audio-preview',
#   modalities=['text', 'audio'],
#   audio={'format': 'wav', 'voice': 'alloy'},
#   messages=[
#     {'role': 'user', 'content': 'Gere e narre um áudio profissional para meu GitHub: apresente-me como desenvolvedor Python focado em IA e LLMs, mencione que este áudio é fruto de automação via código e destaque meu interesse em Transformação Digital e inovação no setor público, mantendo um tom técnico e motivador.'}
#   ]  
# )

# Gerar aúdio por meio de um texto
resposta = cliente.audio.speech.create(
  model='tts-1',
  voice='alloy',
  response_format='wav',
  input='Oi, tudo bem? Você está ouvindo um arquivo gerado automaticamente através de um script Python que desenvolvi. Este projeto faz parte dos meus estudos em Grandes Modelos de Linguagem e IA generativa, onde exploro a criação de ferramentas que automatizam a comunicação multimodal. Convido você a explorar meu código no GitHub para ver como estou aplicando as tecnologias mais recentes do mercado em soluções reais.'
)

resposta.write_to_file('audio2.wav')

# faixa_audio = resposta.choices[0].message.audio.data
# faixa_audio_bytes = base64.b64decode(faixa_audio)

with open('audio2.wav', 'wb') as arquivo_audio:
  arquivo_audio.write(resposta.content)