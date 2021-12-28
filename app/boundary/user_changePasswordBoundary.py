from flask import render_template, session, flash, redirect
from ..controllers.user_changePasswordController import user_changePasswordController

class user_changePasswordBoundary:
	# Constructor
	def __init__(self):
		self.RESPONSE_SUCCESS = "Success"
		self.RESPONSE_INVALID_PASSWORD = "Passwords does not match"
		self.RESPONSE_INCORRECT_PASSWORD = "Old password is incorrect"

	# Other Methods
	def displayPage(self):
		return render_template('user_changePassword.html')

	def onSubmit(self, old_password, new_password,cfm_password):
		"""
	 	Calls relevant function for the controller handle the 
		request to update password. Returns True if password 
		is updated successfully
		"""

		if new_password == cfm_password:
			# Create controller to update password
			controller = user_changePasswordController()

			# Calls the controller to update the user's password
			email = session['user']

			result = controller.updatePassword(email ,old_password, new_password)
			if result == False:
				#if old password is different from current password
				return self.RESPONSE_INCORRECT_PASSWORD
			else : 
				return self.RESPONSE_SUCCESS
		#new password and confirm password dont match
		else:
			return self.RESPONSE_INVALID_PASSWORD
	
	def displaySuccess(self):
		flash("Changed Password Successfully", 'message')
		return redirect('/changepassword')

	def displayError(self, message):
		flash(message, 'error')
		return redirect('/changepassword')