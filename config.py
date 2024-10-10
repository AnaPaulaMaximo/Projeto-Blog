ambiente = 'teste'

if ambiente == 'teste':
    #CONFIG BANCO DE DADOS
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'blog'


if ambiente == 'producao':
    #CONFIG BANCO DE DADOS
    DB_HOST = 'ana01.mysql.pythonanywhere-services.com'
    DB_USER = 'ana01'
    DB_PASSWORD = 'maximo241207'
    DB_NAME = 'ana01$blog'

#CONFIG CHAVE SECRETA DE SESSÃO
SECRET_KEY = 'blog'

#SENHA DO ADM
MASTER_PASSWORD = "Blog@dm123"
MASTER_EMAIL = 'adm@adm'