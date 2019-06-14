from flask import Flask
app = Flask(__name__,
 	static_folder = './public',
 	template_folder="./static")

from templates.apps.views import app_blueprint
# register the blueprints
app.register_blueprint(app_blueprint)
