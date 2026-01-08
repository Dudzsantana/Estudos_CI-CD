import os

# O Python busca a variável no ambiente do GitHub
api_key = os.getenv('MINHA_CHAVE_SECRETA')

if api_key:
    print("Conectado com sucesso!")
else:
    print("Erro: Chave não encontrada no ambiente.")