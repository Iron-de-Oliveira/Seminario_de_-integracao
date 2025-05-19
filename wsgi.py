import sys
import os
import logging
import site



# Caminho para o ambiente virtual
venv_path = '/home/tech/Seminario_de_integracao/venv'

site.addsitedir(os.path.join(venv_path, 'lib/python3.12/site-packages'))
# Caminho absoluto
sys.path.insert(0,"/home/tech/Seminario_de_integracao")

#logging para erros
logging.basicConfig(stream=sys.stderr)

# Importa a aplicação
from app import app as application



