from app.boundary.user_viewElectionMessageBoundary import user_viewElectionMessageBoundary
from .boundary.user_viewElectionMessage import user_viewElectionMessageBoundary
from .boundary.landingPageBoundary import landingPageBoundary
from .boundary.user_editProfileBoundary import user_editProfileBoundary
from .boundary.voters_ViewVoterCoverPage import voters_ViewVoterCoverPage
from .boundary.voters_ViewVotingPage import voters_ViewVotingPage
from .boundary.voters_ViewSubmittedVotePage import voters_ViewSubmittedVotePage
from .boundary.voters_ViewEncryptedVotePage import voters_ViewEncryptedVotePage
from .boundary.admin_overviewBoundary import admin_overviewBoundary
from .boundary.admin_manageAdministratorsBoundary import admin_manageAdministratorsBoundary
from .boundary.admin_viewQuestionsBoundary import admin_viewQuestionsBoundary
from .boundary.admin_editQuestionsBoundary import admin_editQuestionsBoundary
from .boundary.admin_editAnswersBoundary import admin_editAnswersBoundary
from .boundary.user_viewElectionMessageBoundary import user_viewElectionMessageBoundary
from .boundary.user_viewImportVoterList import user_viewImportVoterListBoundary
from .boundary.user_viewEmailSetting import user_viewEmailSettingsBoundary
from .boundary.loginBoundary import loginBoundary
# from .boundary.registrationBoundary import registrationBoundary
from .boundary.registrationBoundary import registrationBoundary
from .boundary.user_changePasswordBoundary import user_changePasswordBoundary
from .boundary.user_mainBallotBoundary import user_mainBallotBoundary

from app import application as app, boundary, loginRequired, authorisationRequired

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

@app.route('/ViewVoterCoverPage', methods=['GET'])
def viewVoterCoverPage():
	# Create a boundary object
	boundary = voters_ViewVoterCoverPage()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/ViewVotingPage', methods=['GET'])
def viewVotingPage():
	# Create a boundary object
	boundary = voters_ViewVotingPage()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/ViewSubmittedVotePage', methods=['GET'])
def viewSubmittedVotePage():
	# Create a boundary object
	boundary = voters_ViewSubmittedVotePage()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/ViewEncryptedVotePage', methods=['GET'])
def viewEncryptedVotePage():
	# Create a boundary object
	boundary = voters_ViewEncryptedVotePage()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/overview', methods = ['GET'])
def projectOverviewPage():
	# Create a boundary object
	boundary = admin_overviewBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/<projectID>/manage_administrators', methods = ['GET', 'POST'])
@loginRequired
@authorisationRequired
def projectManageAdministrator(projectID):
	# Create boundary object
	boundary = admin_manageAdministratorsBoundary()
	if request.method == 'GET':
		return boundary.displayPage(projectID)

	if request.method == 'POST':
		dataPosted = request.form['action']
		if dataPosted == 'addSubAdmin':
			print("Entering Add Sub-Admin")
			return boundary.addSubAdministrator(projectID, request.form['addEmail'])
		
		elif dataPosted == 'deleteSubAdmin':
			print("Entering Delete Sub-Admin")
			print(request.form['deleteID'])
			return boundary.deleteAdministrator(projectID, request.form['deleteID'])
		
		else:
			return boundary.displayError("Error with Data Entered")
		
@app.route("/<projectID>/view_questions", methods = ['GET'])
@loginRequired
@authorisationRequired
def projectViewQuestions(projectID):
	# Create boundary object
	boundary = admin_viewQuestionsBoundary()
	if request.method == 'GET':
		return boundary.displayPage(projectID)

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

@app.route('/view_electionMessage', methods=['GET','POST'])
# @app.route('/<projectID>/view_electionMessage', methods = ['GET', 'POST'])
# @loginRequired
# @authorisationRequired
def view_electionMessage():
	# Create a boundary object
	boundary = user_viewElectionMessageBoundary(1)
	# get url
	# base_url = request.base_url
	# projID = boundary.retrieve_proj_details_from_url(base_url)
	# boundary.setProjID(projID)
	
	if request.method == 'GET':
		return boundary.displayPage()
	elif request.method == 'POST':
		preMsg = request.form['preMsg']
		postMsg = request.form['postMsg']
		response = boundary.onSubmit(preMsg, postMsg)
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

# @app.route('/registration', methods=['GET','POST'])
# def registrationPage():
# 	# Create a boundary object
# 	boundary = registrationBoundary()
# 	if request.method == 'GET':
# 		return boundary.displayPage()

@app.route('/registration', methods=['GET','POST'])
def registrationPage():
	# Create a boundary object
	# boundary = registrationBoundary()
	if request.method == 'GET':
		return boundary.displayPage()
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['psw']
		cfm_password = request.form['cfm_psw']
		companyName = request.form['companyName']
		firstName = request.form['fname']
		lastName = request.form['lname']
		response = boundary.onSubmit(email,password,cfm_password,companyName,firstName,lastName)
	if response == boundary.RESULT_SUCCESS:
		return boundary.displaySuccess()
	else:
		return boundary.displayError(message=response)

@app.route('/changepassword', methods=['GET','POST'])
def changePasswordPage():
	# Create a boundary object
	boundary = user_changePasswordBoundary()
	if request.method == 'GET':
		return boundary.displayPage()
	if request.method == 'POST':
		old_password = request.form['old_pw']
		new_password = request.form['new_pw']
		cfm_password = request.form['cfm_pw']
		response = boundary.onSubmit(old_password,new_password, cfm_password)
	if response == boundary.RESPONSE_SUCCESS:
		return boundary.displaySuccess()
	else:
		return boundary.displayError(message=response)

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

