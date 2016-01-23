from flask import Flask
from flask import redirect

app=Flask(__name__)
app.config.from_pyfile('../config.py')

@app.route('/')
def index():
	return redirect('/main')

def register_blueprints(app):
	from main import main_blueprint
	from auth import auth_blueprint
	
	app.register_blueprint(main_blueprint,url_prefix='/main')
	app.register_blueprint(main_blueprint,url_prefix='/auth')
	
register_blueprints(app)

if __name__=='__main__':
	app.run()
