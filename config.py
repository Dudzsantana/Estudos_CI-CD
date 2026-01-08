import os
import sys

token_projeto = os.getenv('TESTE_SECRET_KEY')

# Dica de DevSecOps: É sempre bom verificar se a chave foi encaontrada
if not token_projeto:
    print("⚠️ Aviso: A variável TESTE_SECRET_KEY não foi configuradaaa!")



def minha_funcao():
  x = 10
  return x