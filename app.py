from flask import Flask
from flask_cors import CORS
from routes.html_rotas import html_rotas
from routes.pdt import pdt_rotas
from routes.user import user_rotas

app = Flask (__name__)


CORS(app)

app.register_blueprint(html_rotas)

app.register_blueprint(pdt_rotas)

app.register_blueprint(user_rotas)


app.run(debug = True)