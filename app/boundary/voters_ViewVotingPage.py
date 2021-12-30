from flask import render_template
from app.controllers.voters_ViewVotingPageController import voters_ViewVotingPageController

question = "hello"
class voters_ViewVotingPage:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self,projID):
		controller = voters_ViewVotingPageController()
		
		details = controller.getCandidateDetails(projID)
		question = controller.getQuestionDesc(projID)

		return render_template('voters_ViewVotingPage.html',details=details,question=question,projID=projID)