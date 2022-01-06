from ..entity.Administrator import Administrator


class organizer_mainBallotController:
	def __init__(self):
		pass

	def getProject(self, organizers_id):
		proj = Administrator(organizers_id)
		return proj.getProjectDetails(organizers_id)

        
		



