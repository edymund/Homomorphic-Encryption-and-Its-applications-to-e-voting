from flask import render_template
from ..controllers.voters_ViewSubmittedVotePageController import voters_ViewSubmittedVotePageController
class voters_ViewSubmittedVotePage:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self,projID):
		controller = voters_ViewSubmittedVotePageController()

		message = controller.getElectionMsg(projID)
		title = controller.getElectionTitle(projID).upper()

		return render_template('voters_ViewSubmittedVotePage.html',message=message,title=title,projID=projID)