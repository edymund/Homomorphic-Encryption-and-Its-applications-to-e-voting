from datetime import datetime
import os
from flask import Flask, session, redirect, flash
from functools import wraps

import pytz
from .controllers.loginController import loginController
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from .entity.Projectdetails import ProjectDetails

import sqlite3

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
		try:
			# If user is authenticated, proceed as per normal
			if session['user']:
				print("User authenticated")
				print(session['user'])
				session['userType'] = 'organizer'
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
				return redirect('/overview')

		except KeyError as e:
			# if session['isAuthenticated'] is None or not session['isAuthenticated']:
			print(e)
		print("User not authorized, Redirecting")
		flash("Not authorized to access this resource")
		return redirect('/mainballot')
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

