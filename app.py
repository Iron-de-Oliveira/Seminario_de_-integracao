from flask import Flask, render_template, request, jsonify

app = Flask (__name__)

# rotas templates
@app.route("/")
def home1():
    return "<h1>Bem-vindo ao Projeto Integrador!</h1><p>Acesse <a href='/cadastro'>/cadastro</a></p>"

@app.route("/home.html")
def home():
    return render_template("home.html")

@app.route ("/cadastro")
def cadastro():
    return render_template('cadastro.html')


# rotas APIs
# NOVO USUÁRIO
@app.route("/usuario", methods=['POST'])
def novo_usuario():
 data = request.get_json()
 print("Recebido do front-end:", data)


if __name__ == '__main__':
   app.run(debug = True)