# Chatbot de Atendimento ao Cliente com RAG (Retrieval-Augmented Generation)

![Badge de Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Badge de Licença](https://img.shields.io/badge/license-MIT-blue)

## 📖 Visão Geral do Projeto

Este projeto consiste na criação de um chatbot inteligente de atendimento ao cliente. A solução utiliza a arquitetura RAG (Retrieval-Augmented Generation) para consumir uma base de conhecimento, especificamente o FAQ (Perguntas Frequentes) de uma empresa, e responder às dúvidas dos clientes de forma precisa e contextualizada.

## 🎯 O Problema

Empresas de todos os tamanhos enfrentam um grande volume de dúvidas repetitivas de clientes. Isso sobrecarrega as equipes de suporte, aumenta o tempo de espera e pode gerar inconsistência nas respostas. Embora os FAQs existam para mitigar isso, os clientes muitas vezes não os encontram ou preferem uma interação mais direta.

## 💡 A Solução

Este projeto implementa um chatbot que atua como um assistente virtual de primeira linha. Em vez de depender de respostas pré-programadas e rígidas, ele usa um modelo de linguagem (LLM) potencializado pela arquitetura RAG.

**O que é RAG?**
O RAG permite que o modelo de linguagem "consulte" uma base de dados externa antes de gerar uma resposta. Neste caso:
1.  O usuário envia uma pergunta (ex: "Como faço para rastrear meu pedido?").
2.  O sistema busca as informações mais relevantes dentro do FAQ da empresa.
3.  O modelo de linguagem (LLM) recebe a pergunta original *juntamente* com o contexto encontrado no FAQ.
4.  O LLM gera uma resposta em linguagem natural, precisa e baseada nos dados oficiais da empresa.

Isso garante que o chatbot forneça respostas atualizadas e corretas, diretamente da fonte de verdade (o FAQ), ao mesmo tempo em que mantém uma conversação fluida.

## ✨ Funcionalidades Principais

* **Processamento de Linguagem Natural (PLN):** O chatbot entende perguntas feitas em linguagem natural, sem a necessidade de comandos exatos.
* **Respostas Baseadas em Conhecimento:** As respostas são estritamente fundamentadas no conteúdo do FAQ, reduzindo alucinações ou informações incorretas.
* **Interação em Tempo Real:** Fornece respostas instantâneas, melhorando a experiência do cliente e reduzindo o tempo de espera.
* **Escalabilidade:** A base de conhecimento pode ser facilmente atualizada apenas modificando o arquivo de FAQ, sem necessidade de retreinar o modelo.

## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Orquestração de LLMs:** LangChain (ou LlamaIndex)
* **Modelo de Linguagem (LLM):** [Ex: GPT-3.5-Turbo da OpenAI, Llama 3, ou um modelo do Hugging Face]
* **Embeddings:** [Ex: OpenAI Embeddings, Sentence Transformers (Hugging Face)]
* **Banco de Dados Vetorial:** [Ex: ChromaDB, FAISS, Pinecone]
* **Interface do Chat (Frontend):** [Ex: Streamlit, FastAPI + React]
* **Processamento de Dados:** Pandas

## 📈 Como Funciona (Arquitetura)

O fluxo de dados do projeto segue o pipeline clássico de RAG:

1.  **Ingestão de Dados (Offline):**
    * O documento de FAQ (ex: `.csv`, `.md`, `.txt`) é carregado.
    * O texto é dividido em blocos menores (chunks).
    * Esses blocos são transformados em *embeddings* (vetores numéricos) e armazenados em um Banco de Dados Vetorial.

2.  **Geração de Resposta (Online):**
    * O usuário insere uma pergunta no chat.
    * A pergunta é convertida em um *embedding*.
    * O sistema realiza uma busca de similaridade no banco de dados vetorial para encontrar os blocos de texto do FAQ mais relevantes.
    * Esses blocos (o "contexto") são enviados, junto com a pergunta original, para o LLM.
    * O LLM gera a resposta final e a exibe para o usuário.

## 🚀 Como Executar o Projeto (Exemplo)

```bash
# 1. Clone o repositório
git clone [URL-DO-SEU-REPOSITÓRIO]
cd [NOME-DO-SEU-REPOSITÓRIO]

# 2. Crie e ative um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure suas variáveis de ambiente
# (Crie um arquivo .env e adicione suas chaves de API, ex: OPENAI_API_KEY)
export OPENAI_API_KEY='sua-chave-aqui'

# 5. Execute o script de ingestão de dados (se necessário)
python ingest.py

# 6. Inicie a aplicação de chat
streamlit run app.py
```

## 👨‍💻 Autor: Pedro Vinícius Meerholz

[LinkedIn](https://www.linkedin.com/in/pmeerholz/)

[GitHub](https://github.com/PedroMeerholz)

[Portfólio](https://pedromeerholz.netlify.app/)