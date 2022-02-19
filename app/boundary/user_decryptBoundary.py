from flask import render_template, redirect, session, flash, current_app
import traceback
from ..controllers.user_decryptController import User_DecryptController

class user_decryptBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self, decryptedData=""):
		return render_template('user_decrypt.html', decryptedData=decryptedData)

	def onSubmit(self, file, secretKey_FHE):
		controller = User_DecryptController()

		# If no file is uploaded
		if file.filename == '':
			return self.displayError("No File Uploaded")

		# If file is uploaded
		encryptedData = file.read()
		try:
			decryptedData = controller.decrypt(encryptedData, int(secretKey_FHE), current_app.config.get("AES_KEY"))
			decryptedData = controller.format(decryptedData)
			return self.displayPage(decryptedData)
		except Exception:
			print (traceback.format_exc())
			return self.displayError("Failed To Decrypt File")
		
	
	def displayError(self, error):
		flash(error, 'error')
		return self.displayPage()

