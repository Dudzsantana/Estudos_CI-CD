import os
import sys

token_projeto = os.getenv('TESTE_SECRET_KEY')

# Dica de DevSecOps: É sempre bom verificar se a chave foi encaontrada
if not token_projeto:
    print("⚠️ Aviso: A variável TESTE_SECRET_KEY não foi configuradaaa!")



def minha_funcao():
  x = 10
  return x

# --- CÓDIGO INSEGURO PARA TESTE ---

# 1. Segredo exposto (Hardcoded Password)
DB_PASSWORD = "Admin_Password_123!" 

# 2. Comando de sistema inseguro (Potencial Injeção de Comando)
import os
usuario_input = "ls" # Simula um dado que viria de um utilizador
os.system("echo Executando comando: " + usuario_input)

# 3. Uso de Eval (Execução de código arbitrário)
comando_perigoso = "2 + 2"
resultado = eval(comando_perigoso)