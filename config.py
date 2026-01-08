import os

# Em vez de 'ghp_123...', pedimos ao sistema a variável 'GITHUB_TOKEN'
token_projeto = os.getenv('TESTE_SECRET_KEY')

# Dica de DevSecOps: É sempre bom verificar se a chave foi encontrada
if not token_projeto:
    print("⚠️ Aviso: A variável TESTE_SECRET_KEY não foi configurada!")