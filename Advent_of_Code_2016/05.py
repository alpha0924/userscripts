import hashlib

door = "ffykfhsq"

def partOne(doorid):
	integer = 0
	password = ""
	for x in range(8):
		test = "xxxxx"
		
		while test[0:5] != "00000":
			hashid = doorid + str(integer)
			m = hashlib.md5()
			m.update(hashid.encode("utf-8"))
			test = m.hexdigest()
			integer += 1
			if test[0:5] == "00000":
				password += test[5]
	return password

def partTwo(doorid):
	integer = 0
	password = ["a", "a", "a", "a", "a", "a", "a", "a"]
	valid = ["0", "1", "2", "3", "4", "5", "6", "7"]
	used = [0, 0, 0, 0, 0, 0, 0, 0]
	while used != [1, 1, 1, 1, 1, 1, 1, 1]:
		test = "xxxxx"
		
		while test[0:5] != "00000":
			hashid = doorid + str(integer)
			m = hashlib.md5()
			m.update(hashid.encode("utf-8"))
			test = m.hexdigest()
			integer += 1
			if test[0:5] == "00000":
				if test[5] in valid and used[int(test[5])] == 0:
					password[int(test[5])] = test[6]
					used[int(test[5])] = 1
	return password

print(partOne(door))
print(partTwo(door))