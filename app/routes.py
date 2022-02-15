import os
import shutil
from .boundary.landingPageBoundary import landingPageBoundary
from .boundary.voters_ViewVoterCoverPage import voters_ViewVoterCoverPage
from .boundary.voters_ViewVotingPage import voters_ViewVotingPage
from .boundary.voters_ViewSubmittedVotePage import voters_ViewSubmittedVotePage
from .boundary.voters_ViewEncryptedVotePage import voters_ViewEncryptedVotePage
from .boundary.projectOwner_overviewBoundary import admin_overviewBoundary
from .boundary.projectOwner_manageAdministratorsBoundary import projectOwner_manageAdministratorsBoundary
from .boundary.projectOwner_viewQuestionsBoundary import projectOwner_viewQuestionsBoundary
from .boundary.projectOwner_editQuestionsBoundary import projectOwner_editQuestionsBoundary
from .boundary.projectOwner_editAnswersBoundary import projectOwner_editAnswersBoundary
from .boundary.organizer_importVoterListBoundary import organizer_importVoterListBoundary
from .boundary.organizer_viewElectionMessageBoundary import organizer_viewElectionMessageBoundary
from .boundary.organizer_emailSettingBoundary import organizer_emailSettingBoundary
from .boundary.loginBoundary import loginBoundary
from .boundary.registrationBoundary import registrationBoundary
from .boundary.organizer_changePasswordBoundary import organizer_changePasswordBoundary
from .boundary.organizer_mainBallotBoundary import organizer_mainBallotBoundary
from .boundary.logoutBoundary import logoutBoundary
from .boundary.organizer_settingsBoundary import organizer_settingsBoundary
from .boundary.resetPasswordBoundary import resetPasswordBoundary
from .boundary.contactUsBoundary import contactUsBoundary
from .boundary.aboutUsBoundary import aboutUsBoundary
from .boundary.projectOwner_publishBoundary import publishBoundary

from .boundary.generateKeysBoundary import generateKeysBoundary

from .boundary.user_decryptBoundary import user_decryptBoundary


from app import application as app, boundary, loginRequired, authorisationRequired
from flask import request
from werkzeug.utils import secure_filename

@app.route('/', methods=['GET'])
def landingPage():
	# Creates a boundary object
	boundary = landingPageBoundary()
	if request.method == 'GET':
		return boundary.displayPage()


@app.route('/<projectID>/publish', methods=['GET', 'POST'])
@loginRequired
@authorisationRequired
def publishPage(projectID):
	# Creates a boundary object
	boundary = publishBoundary()
	if request.method == 'GET':
		return boundary.displayPage(projectID)
	if request.method == 'POST':
		if request.form['action'] == "requestVerification":
			return boundary.requestVerification(projectID)
		elif request.form['action'] == "verify":
			return boundary.verifyProject(projectID)
		elif request.form['action'] == "reject":
			feedback_msg =  request.form['feedback']
			return boundary.rejectProject(projectID, feedback_msg)
		
				
@app.route('/<projectID>/overview', methods = ['GET', 'POST'])
@loginRequired
@authorisationRequired
def projectOverviewPage(projectID):
	# Create a boundary object
	boundary = admin_overviewBoundary()
	if request.method == 'GET':
		return boundary.displayPage(projectID)

	if request.method == 'POST':
		if request.form['action'] == "Delete":
			return boundary.deleteProject(projectID)
		elif request.form['action'] == "Save":
			title = request.form['name']
			startDateTime = request.form['startDateTime']
			endDateTime = request.form['endDateTime']
			publicKey = request.form['publicKey']
			return boundary.onSubmit(projectID, title, startDateTime, endDateTime, publicKey)

@app.route('/<projectID>/manage_administrators', methods = ['GET', 'POST'])
@loginRequired
@authorisationRequired
def projectManageAdministrator(projectID):
	# Create boundary object
	boundary = projectOwner_manageAdministratorsBoundary()
	if request.method == 'GET':
		return boundary.displayPage(projectID)

	if request.method == 'POST':
		dataPosted = request.form['action']
		if dataPosted == 'addVerifier':
			print("Entering Add Verifier")
			return boundary.addVerify(projectID, request.form['addEmail'])
		
		elif dataPosted == 'deleteVerifier':
			print("Entering Delete Verifier")
			print(request.form['deleteID'])
			return boundary.deleteVerifier(projectID, request.form['deleteID'])
		
		else:
			return boundary.displayError("Error with Data Entered")
		
@app.route("/<projectID>/view_questions", methods = ['GET'])
@loginRequired
@authorisationRequired
def projectViewQuestions(projectID):
	# Create boundary object
	boundary = projectOwner_viewQuestionsBoundary()
	if request.method == 'GET':
		return boundary.displayPage(projectID)

@app.route("/<projectID>/edit_questions/<questionID>", methods=['GET', 'POST'])
@loginRequired
@authorisationRequired
def projectEditQuestions(projectID, questionID):
	# Create boundary object
	boundary = projectOwner_editQuestionsBoundary()
	
	if request.method == 'GET':
		return boundary.displayPage(projectID, questionID)
	
	if request.method == 'POST':
		question = request.form['question']
		if questionID == "new_question" :
			return boundary.addQuestion(projectID, question)
		else:
			action = request.form['action']
			if action == "Save":
				return boundary.saveQuestion(projectID, questionID, question)
			if action == "Delete":
				return boundary.deleteQuestion(projectID, questionID)

@app.route("/<projectID>/edit_answers/<questionID>/<candidateID>", methods=['GET', 'POST'])
@loginRequired
@authorisationRequired
def projectEditAnswer(projectID, questionID ,candidateID):
	# Crate boundary object
	boundary = projectOwner_editAnswersBoundary()

	if request.method == 'GET':
		return boundary.displayPage(projectID, questionID, candidateID)
	
	if request.method == 'POST':
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
				return boundary.displayError(projectID, boundary.ERROR_UNAUTHROIZED)
			
			file = request.files['candidateImageFile']
			if file.filename != '':
				filename = secure_filename(file.filename)

			if newCandidate:
				candidateID = boundary.addNewCandidate(projectID, questionID, candidateID, candidateName, candidateDescription, filename)
			else:
				boundary.updateCandidate(projectID, questionID, candidateID, candidateName, candidateDescription, filename)
			
			if filename is not None:
				# Create Directory if it does not exists
				print("candidate ID is ", candidateID)
				if not os.path.exists(os.path.join(app.root_path, 'static', 'images', 'uploads', candidateID)):
					os.makedirs(os.path.join(app.root_path, 'static', 'images', 'uploads', candidateID))

				# Save file to directory
				if filename is not None:
					file.save(os.path.join(app.root_path, 'static', 'images', 'uploads', candidateID, filename))
			
			return boundary.displaySuccess(projectID, questionID)
		
		if action == "Delete":
			# Detele candidate
			shutil.rmtree(os.path.join(app.root_path, 'static', 'images', 'uploads', candidateID), ignore_errors=True)
			return boundary.deleteCandidate(projectID, questionID, candidateID)

@app.route('/<projectID>/view_electionMessage', methods = ['GET', 'POST'])
@loginRequired
@authorisationRequired
def view_electionMessage(projectID):
	# Create a boundary object
	boundary = organizer_viewElectionMessageBoundary(projectID)
	if request.method == 'GET':
		return boundary.displayPage()
	elif request.method == 'POST':
		preMsg = request.form['preMsg']
		postMsg = request.form['postMsg']
		response = boundary.onSubmit(preMsg, postMsg)
		return boundary.displayPage()

@app.route('/<projectID>/view_importList',  methods=['GET', 'POST'])
@loginRequired
@authorisationRequired
def view_importList(projectID):	
	# Create a boundary object
	boundary = organizer_importVoterListBoundary(projectID)
	boundary.setProjID(projectID)

	if request.method == 'GET':		
		return boundary.displayPage()
	elif request.method == 'POST':
		file = request.files['filename']
		response = boundary.onSubmit(file)
		return boundary.displayPage()

@app.route('/<projectID>/view_emailSettings',methods=['GET', 'POST'])
@loginRequired
@authorisationRequired
def view_emailSetting(projectID):
	# Create a boundary object
	boundary = organizer_emailSettingBoundary(projectID)
	if request.method == 'GET':
		return boundary.displayPage()
	if request.method == 'POST':
		rmdMsg = request.form['RmdMsg']
		invMsg = request.form['InvMsg']
		if request.form["action"] =="Update":
			status = boundary.onSubmit(invMsg,rmdMsg)
		if request.form["action"] =="SendEmail":
			boundary.send_reminder(rmdMsg)
		
		# if status == 0:
		# boundary.RESPONSE_SUCCESS()
		return boundary.displayPage()
		# else:
		# 	return boundary.displayError(status)
		
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

@app.route('/<projID>/ ', methods=['GET'])
def viewVoterCoverPage(projID):
	# Create a boundary object
	boundary = voters_ViewVoterCoverPage()
	if request.method == 'GET':
		return boundary.displayPage(projID)

@app.route('/<projID>/ViewVotingPage', methods=['GET','POST'])
def viewVotingPage(projID):
	# Create a boundary object
	boundary = voters_ViewVotingPage()
	if request.method == 'GET':
		return boundary.displayPage(projID)
	if request.method == "POST":
		boundary = voters_ViewVotingPage()
		noOfQues = boundary.getNumberofQuestion(projID)

		answerArray = []
		for i in range(1, noOfQues + 1):
			answer = request.form['candidate' + '[' + str(i) + ']']
			answerArray.append(answer)
		#print(answerArray)

		if boundary.onSubmit(answerArray,projID):
			return boundary.displaySuccess(projID)
		else:
			return boundary.displayError(projID)


@app.route('/<projID>/ViewSubmittedVotePage', methods=['GET'])
def viewSubmittedVotePage(projID):
	# Create a boundary object
	boundary = voters_ViewSubmittedVotePage()
	if request.method == 'GET':
		return boundary.displayPage(projID)

@app.route('/<projID>/ViewEncryptedVotePage', methods=['GET'])
def viewEncryptedVotePage(projID):
	# Create a boundary object
	boundary = voters_ViewEncryptedVotePage()
	if request.method == 'GET':
		return boundary.displayPage(projID)

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

@app.route('/decrypt', methods=['GET'])
def user_decrypt():
	# Create a boundary object
	boundary = user_decryptBoundary()
	if request.method == 'GET':
		return boundary.displayPage()

@app.route('/logout', methods=['GET'])
@loginRequired
def logout():
	# Initialise User_LogoutUI Object
	user_logout = logoutBoundary()

	# Log User Out
	user_logout.logout()

	# Redirect to login page
	return user_logout.redirectToLogin()

@app.route('/generatekeys', methods=['GET','POST'])
def generateKeysPage():
	# Creates a boundary object
	boundary = generateKeysBoundary()

	return boundary.displayPage()