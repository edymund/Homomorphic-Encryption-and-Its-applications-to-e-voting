import os
import shutil
from app import application as app, boundary, loginRequired, authorisationRequired, voterLoginRequired, voterAuthorisationRequired
from flask import request, current_app
from werkzeug.utils import secure_filename

# User Imports
from .boundary.landingPageBoundary import landingPageBoundary
from .boundary.loginBoundary import loginBoundary
from .boundary.registrationBoundary import registrationBoundary
from .boundary.contactUsBoundary import contactUsBoundary
from .boundary.aboutUsBoundary import aboutUsBoundary
from .boundary.user_decryptBoundary import user_decryptBoundary

# Organizer Imports
from .boundary.organizer_overviewBoundary import organizer_overviewBoundary
from .boundary.organizer_manageVerifiersBoundary import organizer_manageVerifiersBoundary
from .boundary.organizer_viewQuestionsBoundary import organizer_viewQuestionsBoundary
from .boundary.organizer_editQuestionsBoundary import organizer_editQuestionsBoundary
from .boundary.organizer_editAnswersBoundary import organizer_editAnswersBoundary
from .boundary.organizer_importVoterListBoundary import organizer_importVoterListBoundary
from .boundary.organizer_viewElectionMessageBoundary import organizer_viewElectionMessageBoundary
from .boundary.organizer_emailSettingBoundary import organizer_emailSettingBoundary
from .boundary.organizer_changePasswordBoundary import organizer_changePasswordBoundary
from .boundary.organizer_mainBallotBoundary import organizer_mainBallotBoundary
from .boundary.organizer_settingsBoundary import organizer_settingsBoundary
from .boundary.organizer_publishBoundary import organizer_publishBoundary
from .boundary.organizer_downloadResultsBoundary import organizer_downloadResultsBoundary
from .boundary.resetPasswordBoundary import resetPasswordBoundary
from .boundary.logoutBoundary import logoutBoundary

# Voter Imports
from .boundary.voters_loginBoundary import voters_loginBoundary
from .boundary.voters_ViewVoterCoverPageBoundary import voters_ViewVoterCoverPage
from .boundary.voters_ViewVotingPageBoundary import voters_ViewVotingPage
from .boundary.voters_ViewSubmittedVotePageBoundary import voters_ViewSubmittedVotePage


@app.route('/', methods=['GET'])
def landingPage():
	# Creates a boundary object
	boundary = landingPageBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/<projectID>/downloadResults', methods=['GET'])
@loginRequired
@authorisationRequired
def downloadPage(projectID):
	# Create a boundary object
	boundary = organizer_downloadResultsBoundary()
	if request.method == 'GET':
		return boundary.displayPage(projectID)

@app.route('/<projectID>/downloadResults/EncryptedResult', methods=['GET'])
@loginRequired
@authorisationRequired
def downloadEncryptedFile(projectID):
	# Create a boundary object
	boundary = organizer_downloadResultsBoundary()
	if request.method == 'GET':
		return boundary.downloadFile(projectID)

@app.route('/<projectID>/publish', methods=['GET', 'POST'])
@loginRequired
@authorisationRequired
def publishPage(projectID):
	print("Entered Route")
	# Creates a boundary object
	boundary = organizer_publishBoundary()
	if request.method == 'GET':
		return boundary.displayPage(projectID)
	if request.method == 'POST':
		projectStatus = boundary.getProjectStatus(projectID)
		if projectStatus == "DRAFT":
			if request.form['action'] == "requestVerification":
				return boundary.requestVerification(projectID)
		elif projectStatus == "PENDING APPROVAL":
			if request.form['action'] == "verify":
				return boundary.verifyProject(projectID)
			elif request.form['action'] == "reject":
				feedback_msg =  request.form['feedback']
				return boundary.rejectProject(projectID, feedback_msg)
		
		return boundary.displayError(projectID,"Unable to edit project")
				
@app.route('/<projectID>/overview', methods = ['GET', 'POST'])
@loginRequired
@authorisationRequired
def projectOverviewPage(projectID):
	# Create a boundary object
	boundary = organizer_overviewBoundary()
	if request.method == 'GET':
		return boundary.displayPage(projectID)

	if request.method == 'POST':
		if request.form['action'] == "Delete":
			return boundary.deleteProject(projectID)
		elif request.form['action'] == "Save":
			title = request.form['name']
			startDateTime = request.form['startDateTime']
			endDateTime = request.form['endDateTime']
			return boundary.onSubmit(projectID, title, startDateTime, endDateTime)

@app.route('/<projectID>/manage_verifiers', methods = ['GET', 'POST'])
@loginRequired
@authorisationRequired
def projectManageVerifier(projectID):
	# Create boundary object
	boundary = organizer_manageVerifiersBoundary()
	if request.method == 'GET':
		return boundary.displayPage(projectID)

	if request.method == 'POST':
		dataPosted = request.form['action']
		if boundary.getProjectStatus(projectID) == "DRAFT":
			if dataPosted == 'addVerifier':
				print("Entering Add Verifier")
				return boundary.addVerify(projectID, request.form['addEmail'])
			
			elif dataPosted == 'deleteVerifier':
				print("Entering Delete Verifier")
				print("Delete ID:", request.form['deleteID'])
				return boundary.deleteVerifier(projectID, request.form['deleteID'])
			
			else:
				return boundary.displayError(projectID,"Error with Data Entered")
		else:
			return boundary.displayError(projectID,"Unable to edit verifier, project is not in draft mode")
		
@app.route("/<projectID>/view_questions", methods = ['GET'])
@loginRequired
@authorisationRequired
def projectViewQuestions(projectID):
	# Create boundary object
	boundary = organizer_viewQuestionsBoundary()
	if request.method == 'GET':
		return boundary.displayPage(projectID)

@app.route("/<projectID>/edit_questions/<questionID>", methods=['GET', 'POST'])
@loginRequired
@authorisationRequired
def projectEditQuestions(projectID, questionID):
	# Create boundary object
	boundary = organizer_editQuestionsBoundary()
	
	if request.method == 'GET':
		return boundary.displayPage(projectID, questionID)
	
	if request.method == 'POST':
		
		if boundary.getProjectStatus(projectID) == "DRAFT":
			question = request.form['question']
			if questionID == "new_question" :
				return boundary.addQuestion(projectID, question)
			else:
				action = request.form['action']
				if action == "Save":
					return boundary.saveQuestion(projectID, questionID, question)
				if action == "Delete":
					return boundary.deleteQuestion(projectID, questionID)
		else:
			return boundary.displayError(projectID,"Unable to edit, project is not in draft mode")	

@app.route("/<projectID>/edit_answers/<questionID>/<candidateID>", methods=['GET', 'POST'])
@loginRequired
@authorisationRequired
def projectEditAnswer(projectID, questionID ,candidateID):
		# Crate boundary object
	boundary = organizer_editAnswersBoundary()

	if request.method == 'GET':
		return boundary.displayPage(projectID, questionID, candidateID)
		
	if request.method == 'POST':
		if boundary.getProjectStatus(projectID) == "DRAFT":
			action = request.form['action']
			if action == "Save":
				# Get Form Fields
				candidateName = request.form['candidateName']
				candidateDescription = request.form['candidateDescription']

				newCandidate = False
				if candidateID == "new_candidate":
					newCandidate = True

					# Store image and filename
				filename = None
				if not boundary.hasPermission(projectID, questionID, candidateID):
					return boundary.displayError(projectID,questionID, boundary.ERROR_UNAUTHROIZED)
				
				file = request.files['candidateImageFile']
				if file.filename != '':
					filename = secure_filename(file.filename)

				if newCandidate:
					candidateID = boundary.addNewCandidate(projectID, questionID, candidateName, candidateDescription, filename)
				else:
					boundary.updateCandidate(projectID, questionID, candidateID, candidateName, candidateDescription, filename)
				
				if filename is not None:
					# Create Directory if it does not exists
					print("candidate ID is ", candidateID)
					if not os.path.exists(os.path.join(app.root_path, current_app.config["UPLOAD_FOLDER"], candidateID)):
						os.makedirs(os.path.join(app.root_path, current_app.config["UPLOAD_FOLDER"], candidateID))

					# Save file to directory
					if filename is not None:
						file.save(os.path.join(app.root_path, current_app.config["UPLOAD_FOLDER"], candidateID, filename))
				
				return boundary.displaySuccess(projectID, questionID)
				
			if action == "Delete":
				# Detele candidate
				shutil.rmtree(os.path.join(app.root_path, current_app.config["UPLOAD_FOLDER"], candidateID), ignore_errors=True)
				return boundary.deleteCandidate(projectID, questionID, candidateID)
		else:
			return boundary.displayError(projectID,questionID,"Unable to edit, project is not in draft mode")	

@app.route('/<projectID>/view_electionMessage', methods = ['GET', 'POST'])
@loginRequired
@authorisationRequired
def view_electionMessage(projectID):
	# Create a boundary object
	boundary = organizer_viewElectionMessageBoundary(projectID)
	if request.method == 'GET':
		return boundary.displayPage(projectID)
	elif request.method == 'POST':
		if boundary.getProjectStatus(projectID) == "DRAFT":
			preMsg = request.form['preMsg']
			postMsg = request.form['postMsg']
			boundary.onSubmit(preMsg, postMsg, projectID)
			return boundary.displayPage(projectID)
		else:
			return boundary.displayError(projectID,"Unable to edit, project is not in draft mode")	

@app.route('/<projectID>/view_importList',  methods=['GET', 'POST'])
@loginRequired
@authorisationRequired
def view_importList(projectID):	
	# Create a boundary object
	boundary = organizer_importVoterListBoundary(projectID)
	if request.method == 'GET':		
		return boundary.displayPage(projectID)
	
	elif request.method == 'POST':
		if boundary.getProjectStatus(projectID) == "DRAFT":
			file = request.files['filename']
			response = boundary.onSubmit(file)
			return boundary.displayPage(projectID)
		else:
			return boundary.displayError(projectID,"Unable to edit, project is not in draft mode")	

@app.route('/<projectID>/view_emailSettings',methods=['GET', 'POST'])
@loginRequired
@authorisationRequired
def view_emailSetting(projectID):
	# Create a boundary object
	boundary = organizer_emailSettingBoundary(projectID)
	if request.method == 'GET':
		return boundary.displayPage(projectID)
	if request.method == 'POST':
		
		rmdMsg = request.form['RmdMsg']
		invMsg = request.form['InvMsg']
		
		if request.form["action"] =="Update":
			if boundary.getProjectStatus(projectID) == "DRAFT":
				boundary.onSubmit(invMsg,rmdMsg,projectID)
			else:
				return boundary.displayError(projectID,"Unable to edit, project is not in draft mode")
		if request.form["action"] =="SendEmail":
			if boundary.getProjectStatus(projectID) == "PUBLISHED":
				boundary.send_reminder(rmdMsg,projectID)
			else:
				return boundary.displayError(projectID,"Unable to send reminder, project is not in published mode")
		
		return boundary.displayPage(projectID)

		
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

@app.route('/settings', methods=['GET','POST'])
@loginRequired
def settingsPage():
	# Create a boundary object
	boundary = organizer_settingsBoundary()
	if request.method == 'GET':
		return boundary.displayPage()
	if request.method == 'POST':
		first_name = request.form['fname']
		last_name = request.form['lname']
		email = request.form['email']
		company_name = request.form['companyName']
		response = boundary.onSubmit(first_name,last_name,email,company_name)	
	if response == boundary.RESPONSE_SUCCESS:
		return boundary.displaySuccess()
	else:
		return boundary.displayError(message=response)

@app.route('/changepassword', methods=['GET','POST'])
@loginRequired
def changePasswordPage():
	# Create a boundary object
	boundary = organizer_changePasswordBoundary()
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
@loginRequired
def mainBallotPage():
	# Create a boundary object
	boundary = organizer_mainBallotBoundary()
	if request.method == 'GET':
		return boundary.displayPage()
	if request.method == 'POST':
		return boundary.addNewProject()

###############################################
#				Voting Pages				  #
###############################################

@app.route('/voter_login', methods=['GET'])
def voterLoginPage():
	boundary = voters_loginBoundary()
	if request.method == 'GET':
		username = request.args['name']
		password = request.args['password']
		projectID = request.args['projectID']
		return boundary.onSubmit(username, password, projectID)


@app.route('/<projectID>/VotingMessage', methods=['GET'])
@voterLoginRequired
@voterAuthorisationRequired
def viewVoterCoverPage(projectID):
	# Create a boundary object
	boundary = voters_ViewVoterCoverPage()
	if request.method == 'GET':
		return boundary.displayPage(projectID)


@app.route('/<projectID>/ViewVotingPage', methods=['GET','POST'])
@voterLoginRequired
@voterAuthorisationRequired
def viewVotingPage(projectID):
	# Create a boundary object
	boundary = voters_ViewVotingPage()
	if request.method == 'GET':
		return boundary.displayPage(projectID)
	if request.method == "POST":
		boundary = voters_ViewVotingPage()
		return boundary.onSubmit(request.form, projectID)


@app.route('/<projectID>/ViewSubmittedVotePage', methods=['GET'])
@voterLoginRequired
def viewSubmittedVotePage(projectID):
	# Create a boundary object
	boundary = voters_ViewSubmittedVotePage()
	if request.method == 'GET':
		return boundary.displayPage(projectID)

# Removed
# @app.route('/<projectID>/ViewEncryptedVotePage', methods=['GET'])
# @voterLoginRequired
# @voterAuthorisationRequired
# def viewEncryptedVotePage(projectID):
# 	# Create a boundary object
# 	boundary = voters_ViewEncryptedVotePage()
# 	if request.method == 'GET':
# 		return boundary.displayPage(projectID)

###############################################
@app.route('/resetpassword', methods=['GET','POST'])
def resetPasswordPage():
	# Create a boundary object
	boundary = resetPasswordBoundary()
	if request.method == 'GET':
		return boundary.displayPage()
	if request.method == 'POST':
		email = request.form['email']
		response = boundary.onSubmit(email)	
	if response == boundary.RESPONSE_SUCCESS:
		return boundary.displaySuccess()
	else:
		return boundary.displayError(message=response)

@app.route('/contactUs', methods=['GET','POST'])
def contactUsPage():
	# Create a boundary object
	boundary = contactUsBoundary()
	if request.method == 'GET':
		return boundary.displayPage()
	if request.method == 'POST':
		email = request.form['email']
		name = request.form['name']
		subject = request.form['subject']
		feedback = request.form['feedback']
		response = boundary.onSubmit(email,name,subject,feedback)	
	if response == boundary.RESPONSE_SUCCESS:
		return boundary.displaySuccess()
	else:
		return boundary.displayError(message=response)

@app.route('/aboutUs', methods=['GET'])
def aboutUsPage():
	# Create a boundary object
	boundary = aboutUsBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/decrypt', methods=['GET', 'POST'])
def user_decrypt():
	# Create a boundary object
	boundary = user_decryptBoundary()
	if request.method == 'GET':		
		return boundary.displayPage()
	elif request.method == 'POST':
		file = request.files['data_file']
		secretKey = request.form['secretKey']
		return boundary.onSubmit(file, secretKey)

@app.route('/logout', methods=['GET'])
@loginRequired
def logout():
	# Initialise User_LogoutUI Object
	user_logout = logoutBoundary()

	# Log User Out
	user_logout.logout()

	# Redirect to login page
	return user_logout.redirectToLogin()