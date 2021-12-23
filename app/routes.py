from app.boundary.user_viewElectionMessage import user_viewElectionMessageBoundary
from .boundary.landingPageBoundary import landingPageBoundary
from .boundary.user_editProfileBoundary import user_editProfileBoundary
from .boundary.admin_overviewBoundary import admin_overviewBoundary
from .boundary.admin_manageAdministratorsBoundary import admin_manageAdministratorsBoundary
from .boundary.admin_viewQuestionsBoundary import admin_viewQuestionsBoundary
from .boundary.user_viewElectionMessage import user_viewElectionMessageBoundary
from .boundary.user_viewImportVoterList import user_viewImportVoterListBoundary
from .boundary.user_viewEmailSetting import user_viewEmailSettingsBoundary
from .boundary.loginBoundary import loginBoundary
from .boundary.registrationBoundary import registrationBoundary
from .boundary.user_mainBallotBoundary import user_mainBallotBoundary

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
		
@app.route('/login', methods=['GET', 'POST'])
def loginPage():
	# Create a boundary object
	boundary = loginBoundary()
	if request.method == 'GET':
		return boundary.displayPage()
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['psw']
		response = boundary.onSubmit(username,password)
		if response == boundary.RESPONSE_SUCCESS:
			return boundary.displaySuccess()
		else:
			return boundary.displayError(message=response)

@app.route('/registration', methods=['GET','POST'])
def registrationPage():
	# Create a boundary object
	boundary = registrationBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/mainballot', methods=['GET','POST'])
def mainBallotPage():
	# Create a boundary object
	boundary = user_mainBallotBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

	# # Create PublicUser_ExposureStatusBoundary Object
	# publicUser_exposureStatusBoundary = PublicUser_ExposureStatusUI()

	# # Exposure status is none if user is not a public user
	# exposureStatus = publicUser_exposureStatusBoundary.getExposureStatus()

	# # Displays the webpage
	# return render_template('overview.html', userType = session['userType'],
	# 										healthStatus = exposureStatus)