from flask import render_template, redirect, session, flash


class generateKeysBoundary:
	# Constructor
	def __init__(self):
		self.RESPONSE_SUCCESS = "Success"

	# Other Methods
	def displayPage(self):
		return render_template('generateKeys.html')