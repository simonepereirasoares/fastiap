from app.main import app
import psycopg2

# Configurando a codificação na inicialização da aplicação
conn = psycopg2.connect(
    dbname="nome_do_banco",
    user="usuario",
    password="senha",
    host="localhost",
    options="-c client_encoding=UTF8"
)

# Aqui a aplicação será executada normalmente
