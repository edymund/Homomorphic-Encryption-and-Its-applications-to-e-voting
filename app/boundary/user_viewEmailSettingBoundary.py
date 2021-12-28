from flask import render_template
class user_viewEmailSettingsBoundary:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self):
		return render_template('user_emailSetting.html')
	
	def onSubmit(self,invMsg,rmdMsg):
		
