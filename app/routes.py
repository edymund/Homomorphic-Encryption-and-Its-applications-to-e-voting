from .controllers.landingPageController import landingPageController
from app import application as app, loginRequired
from flask import request

@app.route('/', methods=['GET'])
def landingPage():
	# Creates a controller object
	controller = landingPageController()
	if request.method == 'GET':
		return controller.displayLandingPage()

	# # Create PublicUser_ExposureStatusBoundary Object
	# publicUser_exposureStatusBoundary = PublicUser_ExposureStatusUI()

	# # Exposure status is none if user is not a public user
	# exposureStatus = publicUser_exposureStatusBoundary.getExposureStatus()

	# # Displays the webpage
	# return render_template('overview.html', userType = session['userType'],
	# 										healthStatus = exposureStatus)