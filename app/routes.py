from app.boundary.user_viewElectionMessage import user_viewElectionMessageBoundary
from .boundary.landingPageBoundary import landingPageBoundary
from .boundary.user_editProfileBoundary import user_editProfileBoundary
from .boundary.user_viewElectionMessage import user_viewElectionMessageBoundary
from .boundary.user_viewImportVoterList import user_viewImportVoterListBoundary
from .boundary.user_viewEmailSetting import user_viewEmailSettingsBoundary

from app import application as app, boundary, loginRequired
from flask import request

@app.route('/', methods=['GET'])
def landingPage():
	# Creates a boundary object
	boundary = landingPageBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/edit_profile', methods=['GET'])
def editProfilePage():
	# Create a boundary object
	boundary = user_editProfileBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/view_electionMessage', methods=['GET'])
def view_electionMessage():
	# Create a boundary object
	boundary = user_viewElectionMessageBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/view_importList', methods=['GET'])
def view_importList():
	# Create a boundary object
	boundary = user_viewImportVoterListBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/view_emailSettings', methods=['GET'])
def view_emailSetting():
	# Create a boundary object
	boundary = user_viewEmailSettingsBoundary()
	if request.method == 'GET':
		return boundary.displayPage()
		
	# # Create PublicUser_ExposureStatusBoundary Object
	# publicUser_exposureStatusBoundary = PublicUser_ExposureStatusUI()

	# # Exposure status is none if user is not a public user
	# exposureStatus = publicUser_exposureStatusBoundary.getExposureStatus()

	# # Displays the webpage
	# return render_template('overview.html', userType = session['userType'],
	# 										healthStatus = exposureStatus)