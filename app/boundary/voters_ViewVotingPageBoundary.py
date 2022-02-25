from flask import render_template, redirect, session, flash
from flask import render_template, current_app
import os
from ..controllers.voters_ViewVotingPageController import voters_ViewVotingPageController


class voters_ViewVotingPage:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self,projID):
		controller = voters_ViewVotingPageController()
		
		question = controller.getQuestionNCandidate(projID)
		imagePath = os.path.join(current_app.root_path, current_app.config["UPLOAD_FOLDER"])

		return render_template('voters_ViewVotingPage.html', question=question,
															 projID=projID,
															 imagePath=imagePath)
	
	def onSubmit(self, answers, projectID):
		controller = voters_ViewVotingPageController()

		if controller.submitAnswers(answers, projectID, session['voterID']):
			return self.displaySuccess(projectID)
		else:
			return self.displayError()


	def displaySuccess(self,projID):
		print("Success")
		return redirect('/'+ str(projID) + '/ViewSubmittedVotePage')

	def displayError(self):
		print("Failed")
		return redirect('/')

	def checkEmptyArray(self,array):
		isNotEmpty = True
		for item in array:
			#print("array",len(item))
			if len(item) == 0:
				isNotEmpty = False
				break
			else:
				continue

		return isNotEmpty
				


