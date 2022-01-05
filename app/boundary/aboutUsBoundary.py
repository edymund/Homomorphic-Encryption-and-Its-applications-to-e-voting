from flask import render_template, redirect, session, flash


class aboutUsBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self):
		return render_template('aboutUs.html')
	
