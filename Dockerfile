FROM python:3.11-slim as builder

# Define o diretório de trabalho
WORKDIR /app

# Atualiza o pip
RUN pip install --upgrade pip

# Instala as dependências de build (se necessário)
RUN apt-get update && apt-get install -y build-essential

# Cria um ambiente virtual
RUN python -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"

# Copia e instala os requisitos
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Usamos a mesma imagem base limpa para a produção
FROM python:3.11-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o ambiente virtual do estágio 'builder'
COPY --from=builder /app/venv /app/venv

# Copia o código da aplicação
COPY ./src /app/src
COPY ./main.py /app/main.py

# Ativa o ambiente virtual para os comandos subsequentes
ENV PATH="/app/venv/bin:$PATH"

# Expõe a porta que a FastAPI (Uvicorn) usará
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]