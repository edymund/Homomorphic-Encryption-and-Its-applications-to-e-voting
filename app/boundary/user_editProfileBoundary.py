from flask import render_template
class user_editProfileBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self):
		return render_template('user_editProfile.html')