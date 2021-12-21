from .boundary.landingPageBoundary import landingPageBoundary
from .boundary.user_editProfileBoundary import user_editProfileBoundary
from .boundary.loginBoundary import loginBoundary
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

@app.route('/login', methods=['GET'])
def loginPage():
	# Create a boundary object
	boundary = loginBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

	# # Create PublicUser_ExposureStatusBoundary Object
	# publicUser_exposureStatusBoundary = PublicUser_ExposureStatusUI()

	# # Exposure status is none if user is not a public user
	# exposureStatus = publicUser_exposureStatusBoundary.getExposureStatus()

	# # Displays the webpage
	# return render_template('overview.html', userType = session['userType'],
	# 										healthStatus = exposureStatus)