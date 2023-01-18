def get_frequencies(str):
	freqdict={}
	for letter in str:
		if letter ==" ":
			continue
		if letter in freqdict:
			freqdict[letter]+=1
		else:
			freqdict[letter]=1

	return freqdict
	pass
