# IA & Data Science Studies
Projetos práticos e experimentos com Python, APIs de LLMs e análise de dados.

---

# 🎙️ Automação de Geração de Áudio com Python & OpenAI
Este projeto documenta o desenvolvimento de uma ferramenta para conversão de texto em fala (Text-to-Speech) utilizando a API da OpenAI. O objetivo é criar áudios realistas de forma automatizada.

**Status do Projeto**: 🚧 Em desenvolvimento (Documentação progressiva)

## 📑 Diário de Bordo (Work in Progress)
Aqui registro as etapas conforme são concluídas, garantindo transparência no processo de desenvolvimento.

## 1. Configuração do Ambiente e Segurança
- Inicialização do repositório Git.
- Criação do arquivo .env para proteção da OPENAI_API_KEY.
- Configuração do .gitignore para não expor credenciais sensíveis.
- Criação de um ambiente virtual para evitar conflitos de versão.
- Instalação das dependências principais: openai e python-dotenv.

## 2. Conexão com a API
- Criação do cliente OpenAI no Python.
- Teste de carregamento das variáveis de ambiente com load_dotenv().

## 3. Implementação e Customização
- Configuração de Parâmetros:
  - Seleção de vozes (ex: alloy, echo, nova).
  - Definição de formatos de saída (.mp3 ou .wav).
  - Ajuste de cadência com o parâmetro speed.
- Geração via Chat Completion (Multimodal):
  - Uso do modelo gpt-4o-audio-preview.
  - Decodificação de base64 para salvamento do arquivo .wav.

# 4. 4. Implementação de Text-to-Speech Estruturado
- Geração Direta (Text-to-Speech):
  - Uso do modelo tts-1 para conversão de texto fixo.
  - Salvamento direto usando write_to_file.
---
## 📚 Referências & Créditos
Este projeto foi desenvolvido como parte dos meus estudos práticos, seguindo as orientações de:
- **Tutorial Base**: [Automação de Geração de Áudio com Python](https://youtu.be/LAsayFqjvYM) - Canal **Hashtag Programação**.
- **Documentação Oficial**: [OpenAI API Reference](hhttps://developers.openai.com/api/docs).