# Use a imagem base do Python 3.10
FROM python:3.10

# Defina o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copie o arquivo de requisitos para o contêiner
COPY requirements.txt .

# Instale o pip 22 e os pacotes necessários
RUN pip install --upgrade pip==22.0.4 \
    && pip install -r requirements.txt

# Copie o código da aplicação para o contêiner
COPY . .

# Defina o comando padrão para executar o CLI
CMD ["python", "main.py"]
