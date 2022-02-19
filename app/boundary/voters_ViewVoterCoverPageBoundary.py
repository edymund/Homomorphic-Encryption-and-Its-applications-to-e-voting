from flask import render_template, redirect
from ..controllers.voters_ViewVoterCoverPageController import voters_ViewVoterCoverPageController
class voters_ViewVoterCoverPage:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self,projID):
		controller = voters_ViewVoterCoverPageController()


		message = controller.getElectionMsg(projID)
		title = controller.getElectionTitle(projID).upper()

		return render_template('voters_ViewVoterCoverPage.html', projID=projID, message=message,title=title)
	