from app import app # app está dentro do meu init principal
from flask import render_template


@app.route("/")
def index():
	return render_template('index.html')

	

