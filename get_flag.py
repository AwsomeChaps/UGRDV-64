#!/usr/bin/python

import base64

def ugrdv_challenge_1(pass_file):
	encode_count = 0
	with open(pass_file) as f:
		password = f.read()

	while(password[:5] != b'flag{'):
		password = base64.b64decode(password)
		encode_count += 1
		
	return (password.decode("utf-8")[5:-1], encode_count)

print(ugrdv_challenge_1("1_UGRDV-64\super_secure_password.txt"))