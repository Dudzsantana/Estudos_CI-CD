import os

token_projeto = os.getenv('TESTE_SECRET_KEY')

# Dica de DevSecOps: É sempre bom verificar se a chave foi encaontrada
if not token_projeto:
    print("⚠️ Aviso: A variável TESTE_SECRET_KEY não foi configuradaaa!")