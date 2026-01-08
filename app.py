import os
import sqlite3
import pickle
import base64
from flask import Flask, request, render_template_string

app = Flask(__name__)

# VULNERABILIDADE: Segredo exposto (Hardcoded Secret)
SECRET_KEY = "SUPER_SECRET_KEY_12345"
API_TOKEN = "7b897821-432d-4951-8b71-9c1234567890"

@app.route('/')
def index():
    return "Bem-vindo ao Lab de Testes SAST!"

# 1. VULNERABILIDADE: SQL Injection (Injeção de SQL)
@app.route('/user')
def get_user():
    username = request.args.get('username')
    db = sqlite3.connect('users.db')
    cursor = db.cursor()
    # Erro: Concatenar strings diretamente na query
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return str(cursor.fetchone())

# 2. VULNERABILIDADE: Command Injection (Injeção de Comando)
@app.route('/ping')
def network_test():
    hostname = request.args.get('host')
    # Erro: Passar entrada do usuário diretamente para o shell
    command = "ping -c 1 " + hostname
    response = os.system(command)
    return f"Resultado: {response}"

# 3. VULNERABILIDADE: Insecure Deserialization (Deserialização Insegura)
@app.route('/load-profile')
def load_profile():
    data = request.args.get('data')
    # Erro: Usar pickle.loads em dados não confiáveis
    decoded_data = base64.b64decode(data)
    user_obj = pickle.loads(decoded_data)
    return f"Perfil carregado para: {user_obj}"

# 4. VULNERABILIDADE: Cross-Site Scripting (XSS)
@app.route('/hello')
def hello_user():
    name = request.args.get('name')
    # Erro: Renderizar entrada do usuário sem sanitização
    template = f"<h1>Olá, {name}!</h1>"
    return render_template_string(template)

if __name__ == "__main__":
    app.run(debug=True) # Erro: Debug mode ativado em "produção"