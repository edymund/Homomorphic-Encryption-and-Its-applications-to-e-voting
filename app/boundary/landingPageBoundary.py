from flask import render_template
class landingPageBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self):
		return render_template('home.html')