from flask import Flask, request
import mysql.connector
from usuario import Usuario

conexion = mysql.connector.connect(user="michelle", password ="1234", database="INVER")

cursor = conexion.cursor()

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"
	#/login/?usuario=michelle&password=1234

@app.route("/login/",methods=['GET'])
def login():

	usuario=request.args.get('usuario')
	password=request.args.get('password')
	userDB = Usuario(conexion,cursor)

	print(userDB.login(usuario, password))
	print(usuario, password)
	return usuario + " " + password

app.run(debug=True)
