import os
from flask import Flask, session, redirect
from functools import wraps
import sqlite3

# Set templates and static directory
template_dir = os.path.abspath('./app/templates')
static_dir = os.path.abspath('./app/static')

# Configure app to run from this file
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Sessions secret key
app.secret_key="mykey123456"

# Makes a route unable to be visited unless logged in
def loginRequired(function):
	@wraps(function)
	def decorated_function(*args, **kwargs):
		# If user is not authenticated
		try:
			# If user is authenticated, proceed as per normal
			if session['isAuthenticated']:
				print("User authenticated")
				print(session['userType'])
				return function()
			
		except KeyError as e:
			# if session['isAuthenticated'] is None or not session['isAuthenticated']:
			print(e)
		print("User not authenticated, Redirecting")
		return redirect('/login')
	return decorated_function

from .app import routes

# Configure app to run if this file is executed
if __name__ == '__main__':
    app.run(debug=False, use_reloader=True)