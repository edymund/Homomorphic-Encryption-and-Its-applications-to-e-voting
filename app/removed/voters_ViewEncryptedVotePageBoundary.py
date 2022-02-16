from flask import render_template
from ..controllers.voters_ViewEncryptedVotePageController import voters_ViewEncryptedVotePageController

class voters_ViewEncryptedVotePage:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self,projID):

		controller = voters_ViewEncryptedVotePageController()
		voteResults = controller.getVoteResults(projID)
		return render_template('voters_ViewEncryptedVotePage.html',voteResults=voteResults,projID=projID)