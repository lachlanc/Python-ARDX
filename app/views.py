import markdown
from flask import Flask
from flask import render_template
from flask import Markup
from app import app
import os
#app = Flask(__name__)

@app.route('/')

def index():
	print os.getcwd()
	f= open ('app/content/exercises/ex9.md')
	content= f.read()

	content = Markup(markdown.markdown(content))
	return render_template('index.html', **locals())
	
	
#def index():
#	user = {'nickname': 'Lachlan'}  # fake user
#	return render_template('index.html',
#                           title='Home',
#                           user=user)
