from flask import Flask
from flask import redirect

def create_app(config_object):
	
	app=Flask(__name__)	
	app.config.from_object(config_object)

	@app.route('/')
	def index():
		return redirect('/main')

	from main import main_blueprint
	from auth import auth_blueprint

	app.register_blueprint(main_blueprint,url_prefix='/main')
	app.register_blueprint(main_blueprint,url_prefix='/auth')
	
	return app
