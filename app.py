
from flask import Flask
from flask_login import LoginManager
from routes.html_rotas import html_rotas 
from routes.user import user_rotas
from routes.pdt import pdt_rotas
from routes.auth import auth_bp
from models.user import Usuario
from flask_cors import CORS
app = Flask (__name__)

CORS(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Usuario.buscar_por_id(user_id)

# rotas html via bluePrint
app.register_blueprint(html_rotas)

# rotas APIs via bluePrint
app.register_blueprint(pdt_rotas)

app.register_blueprint(user_rotas)

# rota de logion via bluePrint

app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)