from flask import render_template, Blueprint
app_blueprint = Blueprint('app',__name__)

@app_blueprint.route('/')
@app_blueprint.route('/app')
def index():
	return render_template("index.html")
