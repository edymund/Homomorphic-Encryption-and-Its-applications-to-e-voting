from flask import render_template

class loginBoundary:
	# Constructor
	def __init__(self):
		pass
	# Other Methods
	def displayPage(self):
		return render_template('login.html')
	

