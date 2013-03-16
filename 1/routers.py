
from flask import Flask, g, request, redirect, render_template, Response, session


from weiboHandle import *


app = Flask(__name__)
app.debug = True

@app.route('/')
def home_page():
    return render_template( 'home_page.html', content = 'hello world' )

@app.route('/login_to_weibo')
def login_to_weibo():
	url = loginWeibo()
	return redirect( url )
	

@app.route('/oauth_weibo', methods = ['POST', 'GET'])
def oauth_weibo():
	if request.method == "GET":
		code = request.args.get("code")
		content = getAccessToken( code )
		return render_template( 'home_page.html', content = content )