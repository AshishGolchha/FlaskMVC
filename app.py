from flask import Flask, request
from UserController import UserController
from FrontendController import FrontendController
import Route
from database import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:Sonu%401045@localhost/flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

Route.resource('/users/',UserController,app)

Route.get("/",FrontendController.index,'index',app)

app.run(debug=True)
