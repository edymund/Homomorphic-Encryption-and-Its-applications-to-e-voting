from flask import render_template

# temporary data to test html
# Note that maximum colum is 4, the browser will be extended to the right if its more than 4
imagePath = ["static/images/candidate1.jpg","static/images/candidate1.jpg","static/images/candidate1.jpg","static/images/candidate1.jpg"]
namePath = ["John Doe Me", "Eve Day You", "Haiya one Two Three", "Just ABCDESSFDJSDNDSHDJDHDSDHD"]
descriptions =["glsdadaldgadlahd","iasujdghasiodugasoidgasdgasdgasodasdgoisagdosaogd","lsdgaskudgdasdgasgadsgdailsgdasg","dsadaskj;hajhdaahdjsakdldddddldasiudhakljdahkljdashkljdahskhasdhasdklhadahklhl"]
question = """Question : Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
in reprehenderit in voluptate velit esse cillum dolore eu fugiat
nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut
enim ad minim veniam, quis nostrud exercitation ullamco laboris
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
in reprehenderit in voluptate velit esse cillum dolore eu fugiat
nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum."""

class voters_ViewVotingPage:
	# Constructor
	def __init__(self):
		pass

	# Other Methods
	def displayPage(self):
		return render_template('voters_ViewVotingPage.html',imagePath=imagePath,namePath=namePath,descriptions=descriptions,question=question )