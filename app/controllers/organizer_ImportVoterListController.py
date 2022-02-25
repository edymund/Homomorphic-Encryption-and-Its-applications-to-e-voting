from ..entity.Voter import Voter
from ..entity.Projectdetails import ProjectDetails
import random 

class organizer_importVoterListController:
	def __init__(self,voterList = [], projID = None):
		self.voterList = voterList
		self.projID = projID
	
	def getProjectStatus(self, projectID):
		projectDetails = ProjectDetails(projectID)
		return projectDetails.getStatus()
		
	def update_voter(self, projID,vList):
		voter = Voter(projID)
		all_id = voter.get_all_voters_id(projID)
		if len(all_id) >0:
			for id in all_id:
				for value in id:
					voter.delete_child(value, projID)
			voter.delete_allVoters(projID)
		
		for email in vList:
			hash = random.getrandbits(24)
			hash = str(hex(hash))[2:]
			voter.insert_to_table(hash,email, self.projID)

	def get_random(self):
		return random.randint(0, 100000000)

	def get_all_voters_email(self):
		voter = Voter()
		tup_of_voter = voter.get_all_voters(projectID = self.projID)
		list_of_voter = []
		for voter in tup_of_voter:
			list_of_voter.append(voter[0])
		return list_of_voter

		
