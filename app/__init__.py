import os
from flask import Flask, session, redirect, flash
from functools import wraps
import sqlite3

# Set templates and static directory
template_dir = os.path.abspath('./app/template')
static_dir = os.path.abspath('./app/static')

# Configure app to run from this file
application = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

# Sessions secret key
application.secret_key="mykey123456"

# Makes a route unable to be visited unless logged in
def loginRequired(function):
	@wraps(function)
	def decorated_function(*args, **kwargs):
		# If user is not authenticated
		try:
			# If user is authenticated, proceed as per normal
			if session['user']:
				print("User authenticated")
				print(session['user'])
				return function(*args, **kwargs)
			
		except KeyError as e:
			# if session['isAuthenticated'] is None or not session['isAuthenticated']:
			print(e)
		print("User not authenticated, Redirecting")
		return redirect('/login')
	return decorated_function

def authorisationRequired(function):
	@wraps(function)
	def decorated_function(*args, **kwargs):
		# If user is not authorised
		try:
			# If user is authenticated, proceed as per normal
			if session['userID']:
				print("User authenticated")
				print(session['user'])
				print(session['userID'])
				return function(*args, **kwargs)
			
		except KeyError as e:
			# if session['isAuthenticated'] is None or not session['isAuthenticated']:
			print(e)
		print("User not authorized, Redirecting")
		flash("Not authorized to access this resource")
		return redirect('/overview')
	return decorated_function

from app import routes

