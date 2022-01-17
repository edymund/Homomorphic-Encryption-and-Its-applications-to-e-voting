from sqlite3.dbapi2 import IntegrityError
from flask import render_template, session, redirect, request, flash
from ..controllers.resetPasswordController import resetPasswordController
import random
import smtplib
import string

class resetPasswordBoundary:
	# Constructor
	def __init__(self):
		self.RESPONSE_SUCCESS = "Success"
		self.RESPONSE_INCORRECT_EMAIL = "Email Does not Exist"

	# Other Methods
	def displayPage(self):
		return render_template('resetPassword.html')

	def random_pw(self,no_of_letters,no_of_num):
		letters = ''.join((random.choice(string.ascii_letters) for i in range(no_of_letters)))
		digits = ''.join((random.choice(string.digits) for i in range(no_of_num)))
		# Convert resultant string to list and shuffle it to mix letters and digits
		random_list = list(letters + digits)
		random.shuffle(random_list)
		# convert list to string
		new_random_password = ''.join(random_list)
		return new_random_password	
	
	def send_reset_pw(self,new_password):
		email_address = "fyp21s403@gmail.com"
		server = smtplib.SMTP("smtp.gmail.com",587)
		server.starttls()
		# login(email address, password)
		server.login(email_address, "eccqringtcgtolnf")
		msg = 'From: ' + email_address + '\r\nTo: ' + email_address + '\r\nSubject: Reset Password \r\n\r\nYour Password has been reset to: ' + str(new_password)
		# sendmail(sender,receiver,message)
		server.sendmail(email_address,email_address,msg)

	def onSubmit(self,email):
		controller = resetPasswordController()
		if controller.checkifEmailexists(email) == True:
			# call random password method with num of letters and digits
			new_password = self.random_pw(5,3) 
			controller.resetPw(email,new_password)
			# send random password to user via email
			self.send_reset_pw(new_password)
			return self.RESPONSE_SUCCESS
		else:
			return self.RESPONSE_INCORRECT_EMAIL
			

	def displaySuccess(self):
		flash("Password Reset Successfully", 'message')
		return redirect('/login')

	def displayError(self, message):
		flash(message, 'error')
		return redirect('/resetpassword')
