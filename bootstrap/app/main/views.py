from . import main_blueprint as main
from flask.views import MethodView
from flask import render_template

#Define your views here

#This is a sample view
class IndexView(MethodView):
	methods=['GET']
	
	def get(self):
		return render_template('main/index.html')
		
main.add_url_rule('/',view_func=IndexView.as_view('index_view'))
