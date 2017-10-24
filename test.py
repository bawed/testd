
User = 'shen'
Pass = '123456'
counter = 0

while True:
	Username = input("pls input your name:")
	if len(Username) == 0:
		print ("empty name, try again!")
		continue
	while Username != User:
		if counter < 2:
			print ("user error,try again!")
			Username = input("pls input your name:")
			counter += 1
			continue
		break
	for i in range(3):
		if Username == User:
			passwd = input("pls input your password:")
			if passwd == Pass:
				print ("welcome!")
				break
			else:
				print ("password error,try again!")
				continue
	break
frff