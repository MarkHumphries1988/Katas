def get_distinct_letters(word1,word2):
	endstr=""
	
	for letter in word1:
		if len(word2.replace(letter,""))==len(word2):
			endstr+=letter

	for letter in word2:
		if len(word1.replace(letter,""))==len(word1):
			endstr+=letter

	

	endstr="".join(sorted(endstr))

	return endstr
	pass
