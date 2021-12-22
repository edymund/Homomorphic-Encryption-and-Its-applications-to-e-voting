from .boundary.landingPageBoundary import landingPageBoundary
from .boundary.user_editProfileBoundary import user_editProfileBoundary
from .boundary.admin_overviewBoundary import admin_overviewBoundary
from .boundary.admin_manageAdministratorsBoundary import admin_manageAdministratorsBoundary
from .boundary.admin_viewQuestionsBoundary import admin_viewQuestionsBoundary
from .boundary.admin_editQuestionsBoundary import admin_editQuestionsBoundary
from .boundary.admin_editAnswersBoundary import admin_editAnswersBoundary
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

@app.route('/overview', methods = ['GET'])
def projectOverviewPage():
	# Create a boundary object
	boundary = admin_overviewBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/manage_administrators', methods = ['GET'])
def projectManageAdministrator():
	# Create boundary object
	boundary = admin_manageAdministratorsBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route("/view_questions", methods = ['GET'])
def projectViewQuestions():
	# Create boundary object
	boundary = admin_viewQuestionsBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route("/edit_questions", methods=['GET'])
def projectEditQuestions():
	# Create boundary object
	boundary = admin_editQuestionsBoundary()
	if request.method =='GET':
		return boundary.displayPage()

@app.route("/edit_answers", methods=['GET'])
def projectEditAnswer():
	# Crate boundary object
	boundary = admin_editAnswersBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

	# # Create PublicUser_ExposureStatusBoundary Object
	# publicUser_exposureStatusBoundary = PublicUser_ExposureStatusUI()

	# # Exposure status is none if user is not a public user
	# exposureStatus = publicUser_exposureStatusBoundary.getExposureStatus()

	# # Displays the webpage
	# return render_template('overview.html', userType = session['userType'],
	# 										healthStatus = exposureStatus)