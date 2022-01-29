#!/usr/bin/python3


import Crypto
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_PSS
from Crypto.PublicKey import RSA
import hashlib
import codecs
import os
import glob


pkg_location = './package_for_gf'
keyfile_location = './public_key.der'
flag = None


def read_public_key(filename):
	with open(filename, "rb") as f:
		return RSA.importKey(f.read())


def xor(str1, str2):
	assert(len(str1) == len(str2))
	result = bytearray((b1 ^ b2 for b1, b2 in zip(str1, str2)))
	return result


def check_signature(path, public_key):
	hash_value = compute_hash(path + "/signed_data")
	f = open(path + "/signature.bin", "rb")
	signature = f.read()
	verifier = PKCS1_PSS.new(public_key)
	return verifier.verify(SHA256.new(hash_value), signature)


def compute_hash(messages_path): 
	'''compute a hash of all files contained in <directory>.'''
	files = glob.glob(messages_path + "/**", recursive=True)
	files.sort()
	files.remove(messages_path + "/")
	result = bytearray(hashlib.sha256().digest_size)

	for filename in files:
		complete_path = filename
		relative_path = os.path.relpath(filename, messages_path)
		if os.path.isfile(complete_path):
			with open(complete_path, "rb") as f:
				h = hashlib.sha256(relative_path.encode('ASCII'))
				h.update(b"\0")
				h.update(f.read())
		elif os.path.isdir(complete_path):
			relative_path += "/"
			h = hashlib.sha256(relative_path.encode('ASCII') + b"\0")
		else:
			pass

		result = xor(result, h.digest())

	print( result.hex())
	return result


def verify_signature(data_path, public_key):
	valid = check_signature(data_path, public_key)
	if not valid:
		raise RuntimeError("Invalid signature")
	else:
		print('Valid signature:', valid)
		return True


def main():
	pkg_path = pkg_location
	public_key = read_public_key(keyfile_location)
	verified_signature = verify_signature(pkg_path, public_key)


if __name__ == "__main__":
	main()
