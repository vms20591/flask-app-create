from . import auth_blueprint as auth
from flask.views import MethodView
from flask import render_template

#Define your views here

#This is a sample view
class IndexView(MethodView):
	methods=['GET']
	
	def get(self):
		return render_template('auth/index.html')
		
auth.add_url_rule('/',view_func=IndexView.as_view('auth_view'))
