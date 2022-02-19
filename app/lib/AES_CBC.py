import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


class AES_CBC:
	def __init__(self, key):
		self.key = bytes.fromhex(key)
	
	@staticmethod
	def generateKey(bits):
		"""
		Takes in 128, 192 or 256
		"""
		if bits not in [128, 192, 256]:
			return None
		return get_random_bytes(bits//8).hex()

	def encrypt(self, data):
		"""
		Returns a string
		"""
		data = str.encode(data)
		cipher = AES.new(self.key, AES.MODE_CBC)
		ct_bytes = cipher.encrypt(pad(data, AES.block_size))
		iv = b64encode(cipher.iv).decode('utf-8')
		ct = b64encode(ct_bytes).decode('utf-8')
		result = json.dumps({'iv':iv, 'ciphertext':ct})
		return result

	def decrypt(self, ciphertext):
		try:
			b64 = json.loads(ciphertext)
			iv = b64decode(b64['iv'])
			ct = b64decode(b64['ciphertext'])
			cipher = AES.new(self.key, AES.MODE_CBC, iv)
			pt = unpad(cipher.decrypt(ct), AES.block_size)
			return pt
		except (ValueError, KeyError):
			print("Incorrect decryption")
			return None