#rodar no cmd
#pip install flask
#importar a biblioteca flask
from flask import Flask
#cria uma instância da aplicação Flask
app = Flask (__name__)
#Este é um decorador que associa a URL
#'/' (a URL raiz do site) à função que vem logo abaixo
@app.route('/')
# A função que é executada quando a rota '/' é acessada
#ele retorna a string "Hello, World!".
def hello_world():
  return 'Hello, World!'

#executa o servidor de desenvolvimento
if __name__ == '__main__':
  app.run(debug=True)