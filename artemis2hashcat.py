#!/usr/bin/python3

### Find artemis hash in "artemis-users.properties"

### Usage Examples (plaintext password is "7KBeh41j"):
###	python3 artemis2hashcat.py 'ENC(1024:8D873D1EDFB8ABACBC1A8229AC6A691B2856427B385167AC5DA636A8B0D0CF7C:50DE2FF97B69C8B8D127356F8F1090730F8F805DAA288E804E199788394EF0C9363671038857CB7F83ACE9022ACE2119792B9FCFB72CA68D026A5458B2D4C7CF)'
###		OR
###	python3 artemis2hashcat.py '1024:8D873D1EDFB8ABACBC1A8229AC6A691B2856427B385167AC5DA636A8B0D0CF7C:50DE2FF97B69C8B8D127356F8F1090730F8F805DAA288E804E199788394EF0C9363671038857CB7F83ACE9022ACE2119792B9FCFB72CA68D026A5458B2D4C7CF'

### Run Hashcat:
###	hashcat -m 12000 -a 0 test.hashcat test.lst

import binascii
import base64
import sys
import re

if len(sys.argv) != 2:
	print(f"Usage: python3 {sys.argv[0]} 'ENC(ITERATIONS:SALT:HASH)'")
	print("\tOR")
	print(f"Usage: python3 {sys.argv[0]} 'ITERATIONS:SALT:HASH'")
	quit()

artemis_hash = sys.argv[1]

if re.search("^ENC\([0-9]+:[0-9a-fA-F]+:[0-9a-fA-F]+\)$",artemis_hash):
	x = artemis_hash.removeprefix("ENC(")[:-1]
	iter, salt, hash = x.split(":")
elif re.search("^[0-9]+:[0-9a-fA-F]+:[0-9a-fA-F]+$",artemis_hash):
	iter, salt, hash = artemis_hash.split(":")
else:
	print("Invalid Format")
	quit()

iter = int(iter)
salt = base64.b64encode(binascii.unhexlify(salt))
hash = base64.b64encode(binascii.unhexlify(hash))

res = b"sha1:%d:%s:%s" % (iter, salt, hash)

print(res.decode("latin-1"))
