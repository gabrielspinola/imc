from flask import Flask
from flask_cors import CORS
from src.routes.route_receitas import route_receitas
from src.routes.route_user import route_user

app = Flask(__name__)
CORS(app)

app.register_blueprint(route_receitas)
app.register_blueprint(route_user)