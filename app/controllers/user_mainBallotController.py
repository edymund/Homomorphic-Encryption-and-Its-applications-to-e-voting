from ..entity.Administrator import Administrator


class user_mainBallotController:
	def __init__(self):
		pass

	def getProject(self, user_id):
		proj = Administrator(user_id)
		return proj.getProjectDetails(user_id)

        
		



