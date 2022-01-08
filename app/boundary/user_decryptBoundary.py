from flask import render_template, redirect, session, flash
class user_decryptBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self):
		return render_template('user_decrypt.html')