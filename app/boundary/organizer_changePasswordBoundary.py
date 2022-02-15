from flask import render_template, session, flash, redirect
import re
from ..controllers.organizer_changePasswordController import organizer_changePasswordController

class organizer_changePasswordBoundary:
	# Constructor
	def __init__(self):
		self.RESPONSE_SUCCESS = "Success"
		self.RESPONSE_INCORRECT_PASSWORD = "Old password is incorrect"
		self.RESPONSE_SAME_PASSWORD = "Make sure new password is unique from other passwords you use"

	# Other Methods
	def displayPage(self):
		return render_template('organizer_changePassword.html')

	def __checkIsValidPassword(self, new_password, cfm_password):
		# Check if passwords match 
		if new_password != cfm_password:
			self.ERROR = "Password fields do not match"
			return False
		return True

	def __checkNewPassword(self, new_password):
		# Check if passwords match 
		if not re.search('^(?=.*[a-z])(?=.*[A-Z])(?=.*\\d).+$', new_password):
			self.ERROR = "Password needs to contain at least 1 lowercase, 1 uppercase and 1 digit"
			return False
		if not re.search('.{8}$', new_password):
			self.ERROR = "Password must have minimum length of 8 characters"
			return False
		return True

	def onSubmit(self, old_password, new_password,cfm_password):
		if self.__checkIsValidPassword(new_password, cfm_password) and \
			self.__checkNewPassword(new_password):
			# Create controller to update password
			controller = organizer_changePasswordController()
			
			# Calls the controller to update the user's password
			email = session['user']

			result = controller.updatePassword(email ,old_password, new_password)
			if result == False:
				#if old password is different from current password
				return self.RESPONSE_INCORRECT_PASSWORD
			elif result == "Same Password":
				return self.RESPONSE_SAME_PASSWORD
			else : 
				return self.RESPONSE_SUCCESS
		#new password and confirm password dont match
		else:
			return self.ERROR
	
	def displaySuccess(self):
		flash("Changed Password Successfully", 'message')
		return redirect('/changepassword')

	def displayError(self, message):
		flash(message, 'error')
		return redirect('/changepassword')