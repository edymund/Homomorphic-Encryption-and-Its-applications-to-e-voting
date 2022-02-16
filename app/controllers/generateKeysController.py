from ..lib.FHE import FHE

class GenerateKeysController():
	# Constructor
	def __init__(self):
		self.FHE = FHE()
		self.FHE.keyGen()

	def getPublicKey(self):
		return self.FHE.getPublicKeyAsString()
	
	def getSecretKey(self):
		return self.FHE.getPrivateKey()