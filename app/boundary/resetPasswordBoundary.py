from sqlite3.dbapi2 import IntegrityError
from flask import render_template, session, redirect, request, flash
from ..controllers.resetPasswordController import resetPasswordController
import random
import smtplib

class resetPasswordBoundary:
	# Constructor
	def __init__(self):
		self.RESPONSE_SUCCESS = "Success"
		self.RESPONSE_INCORRECT_EMAIL = "Email Does not Exist"

	# Other Methods
	def displayPage(self):
		return render_template('resetPassword.html')
	
	def onSubmit(self,email):
		controller = resetPasswordController()
		if controller.checkifEmailexists(email) == True:
			new_password = random.randint(100, 999) 
			controller.resetPw(email,new_password)
			email_address = "fyp.21.s4.03fyp@gmail.com"
			server = smtplib.SMTP("smtp.gmail.com",587)
			server.starttls()
			# login(email address, password)
			server.login(email_address, "fyp_21_s4_03")
			msg = 'From: ' + email_address + '\r\nTo: ' + email_address + '\r\nSubject: Reset Password \r\n\r\nYour Password has been reset to: ' + str(new_password)
			# sendmail(sender,receiver,message)
			server.sendmail(email_address,email_address,msg)

			return self.RESPONSE_SUCCESS
		else:
			return self.RESPONSE_INCORRECT_EMAIL
			

	def displaySuccess(self):
		flash("Password Reset Successfully", 'message')
		return redirect('/login')

	def displayError(self, message):
		flash(message, 'error')
		return redirect('/resetpassword')
