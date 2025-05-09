from flask import Flask, render_template, request, jsonify

app = Flask (__name__)

@app.route("/")
def home():
    return "<h1>Bem-vindo ao Projeto Integrador!</h1><p>Acesse <a href='/cadastro'>/cadastro</a></p>"


@app.route ("/cadastro")
def cadastro():
    return render_template('cadastro.html')

if __name__ == '__main__':
   app.run(debug = True)