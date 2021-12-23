from flask import render_template
class user_mainBallotBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self):
		return render_template('user_mainBallot.html')