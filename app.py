from flask import Flask
from flask_login import LoginManager
from routes.html_rotas import html_rotas 
from routes.user import user_rotas
from routes.pdt import pdt_rotas
from routes.auth import auth_bp
from models.user import Usuario
from flask_cors import CORS
from database.cenexao import conectar



app = Flask (__name__)
app.secret_key = "uma_chave_super_secreta_e_complexa_aqui_123!"

CORS(app)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # Busque no banco o usuário pelo id e retorne o objeto Usuario
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute("SELECT idusuario, nome, email, senha, telefone, localizacao, foto_perfil FROM usuario WHERE idusuario = %s", (user_id,))
    row = cursor.fetchone()
    cursor.close()
    conexao.close()
    if row:
        return Usuario(*row)
    return None

# rotas html via bluePrint
app.register_blueprint(html_rotas)

# rotas APIs via bluePrint
app.register_blueprint(pdt_rotas)

app.register_blueprint(user_rotas)

# rota de logion via bluePrint

app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)