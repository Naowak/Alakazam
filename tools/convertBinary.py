def stringBinaryToList(string) :
	if not isinstance(string, bytes) :
		raise Exception("string isn't a byte")
	l = string.decode().split()
	for k in range(len(l)):
		l[k] = int(l[k])
	return l

def listToStringBinary(l) :
	if not isinstance(l, list) :
		raise Exception("l isn't a list")
	s = str()
	for elem in l :
		s += str(elem) + ' '
	return s[:-1].encode()