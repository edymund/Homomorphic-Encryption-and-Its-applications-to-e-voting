from flask.templating import render_template
from flask import render_template
from ..views.landingPageView import landingPageView

class landingPageController():
	def __init__(self):
		self.view = landingPageView()

	def displayLandingPage(self):
		return self.view.displayPage()
		