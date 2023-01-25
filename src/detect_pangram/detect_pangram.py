def detect_pangram(string):
	
	previousstring=string

	for i in range(97,123):
		if len(previousstring)==len(previousstring.replace(chr(i),"")):
			return False
		else:
			previousstring=previousstring.replace(chr(i),"")

	return True

	pass
