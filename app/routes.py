from app.boundary.user_viewElectionMessageBoundary import user_viewElectionMessageBoundary
from .boundary.landingPageBoundary import landingPageBoundary
from .boundary.user_editProfileBoundary import user_editProfileBoundary
from .boundary.admin_overviewBoundary import admin_overviewBoundary
from .boundary.admin_manageAdministratorsBoundary import admin_manageAdministratorsBoundary
from .boundary.admin_viewQuestionsBoundary import admin_viewQuestionsBoundary
from .boundary.admin_editQuestionsBoundary import admin_editQuestionsBoundary
from .boundary.admin_editAnswersBoundary import admin_editAnswersBoundary
from .boundary.user_viewElectionMessageBoundary import user_viewElectionMessageBoundary
from .boundary.user_viewImportVoterListBoundary import user_viewImportVoterListBoundary
from .boundary.user_viewEmailSettingBoundary import user_viewEmailSettingsBoundary
from .boundary.loginBoundary import loginBoundary
# from .boundary.registrationBoundary import registrationBoundary
from .boundary.user_mainBallotBoundary import user_mainBallotBoundary

from app import application as app, boundary, loginRequired
from flask import request, flash, render_template

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

@app.route('/view_electionMessage', methods=['GET'])
def view_electionMessage():
	# Create a boundary object
	boundary = user_viewElectionMessageBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/view_importList',  methods=['GET', 'POST'])
# Un comment when linked from nav bar
# @loginRequired
# @authorisationRequired

def view_importList():	
	# Create a boundary object
	boundary = user_viewImportVoterListBoundary(1)
	# Un comment when linked from nav bar

	# base_url = request.base_url
	# projID = boundary.retrieve_proj_detail(base_url)
	# boundary.setProjID(projID)

	votersList = boundary.populateTextArea()
	if request.method == 'GET':		
		return boundary.displayPage(votersList)
	elif request.method == 'POST':
		file = request.files['filename']
		response = boundary.onSubmit(file)
		votersList = boundary.populateTextArea()
		return boundary.displayPage(votersList)
		
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