from .boundary.landingPageBoundary import landingPageBoundary
from app import application as app, boundary, loginRequired
from flask import request

@app.route('/', methods=['GET'])
def landingPage():
	# Creates a controller object
	boundary = landingPageBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

	# # Create PublicUser_ExposureStatusBoundary Object
	# publicUser_exposureStatusBoundary = PublicUser_ExposureStatusUI()

	# # Exposure status is none if user is not a public user
	# exposureStatus = publicUser_exposureStatusBoundary.getExposureStatus()

	# # Displays the webpage
	# return render_template('overview.html', userType = session['userType'],
	# 										healthStatus = exposureStatus)