# Local Import
import os
from datetime import datetime
from functools import wraps
import sqlite3

# Environment Imports
import pytz
from flask import Flask, session, redirect, flash
from apscheduler.schedulers.background import BackgroundScheduler

# Project Imports
from .controllers.loginController import loginController
from .controllers.voters_loginController import voters_loginController
from .entity.Projectdetails import ProjectDetails


# Set templates and static directory
template_dir = os.path.abspath('./app/template')
static_dir = os.path.abspath('./app/static')

# Configure app to run from this file
application = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
application.config['UPLOAD_FOLDER'] = "./static/images/projectImages/{}"

# Sessions secret key
application.secret_key="mykey123456"

# Makes a route unable to be visited unless logged in
def loginRequired(function):
	@wraps(function)
	def decorated_function(*args, **kwargs):
		# If user is not authenticated
		print("-------Checking Login")
		try:
			# If user is authenticated, proceed as per normal
			if session['user'] and session['loginType'] == 'organizer':
				print("User authenticated")
				print("User:", session['user'])
				print("LoginType:", session['loginType'])
				return function(*args, **kwargs)
			
		except KeyError as e:
			print(e)
		print("User not authenticated, Redirecting")
		return redirect('/login')
	return decorated_function

def authorisationRequired(function):
	@wraps(function)
	def decorated_function(*args, **kwargs):
		# If user is not authorised
		print("-------Checking Authorisation")
		try:
			controller = loginController()
			# If user is authenticated, proceed as per normal
			session['ownerProjectID'] = controller.getProjectID_Owner(session['organizerID'])
			session['verifierProjectID'] = controller.getProjectID_Verifier(session['organizerID'])

			accessedResource = kwargs.get("projectID")
			if int(accessedResource) in session['ownerProjectID']:
				session['userType'] = "owner"
				print("User is owner of project")
				return function(*args, **kwargs)

			elif int(accessedResource) in session['verifierProjectID']:
				session['userType'] = "verifier"
				print("User is verifier of project")
				return function(*args, **kwargs)

			else: 
				print("User not authorized, Redirecting")
				flash("Not authorized to access this resource")
				return redirect('/mainballot')

		except KeyError as e:
			print(e)
		print("User not authorized, Redirecting")
		flash("Not authorized to access this resource")
		return redirect('/mainballot')
	return decorated_function

# Makes a route unable to be visited unless logged in
def voterLoginRequired(function):
	@wraps(function)
	def decorated_function(*args, **kwargs):
		# If user is not authenticated
		print("-------Checking Voter Login")
		try:
			# If user is authenticated, proceed as per normal
			if session['user'] and session['loginType'] == 'voter':
				print("User authenticated")
				print(session['user'])
				return function(*args, **kwargs)
			
		except KeyError as e:
			# if session['isAuthenticated'] is None or not session['isAuthenticated']:
			print(e)
		print("User not authenticated, Redirecting")
		return redirect('/')
	return decorated_function

def voterAuthorisationRequired(function):
	@wraps(function)
	def decorated_function(*args, **kwargs):
		# If user is not authorised
		print("-------Checking Voter Authorisation")
		try:
			controller = voters_loginController()

			accessedResource = kwargs.get("projectID")
			print(kwargs)
			if controller.checkVoterAuthorised(session['voterID'], accessedResource):
				return function(*args, **kwargs)
			else: 
				flash("You have voted for this event")
				return redirect('/')

		except KeyError as e:
			print(e)
		print("User not authorized, Redirecting")
		flash("Not authorized to access this resource")
		return redirect('/')
	return decorated_function


def updateProjectStatus():
	projectDetails = ProjectDetails()
	tz = pytz.timezone('Asia/Singapore')
	now = datetime.now(tz)

	# Update Ongoing Status
	projectDetails.updateProjectsStatus_Ongoing(now)

	# Update Completed Status
	projectDetails.updateProjectsStatus_Completed(now)

# Schedule to update project status
scheduler = BackgroundScheduler(timezone=pytz.timezone('Asia/Singapore'))
scheduler.start()
job = scheduler.add_job(updateProjectStatus, trigger='cron', minute="*")

from app import routes

