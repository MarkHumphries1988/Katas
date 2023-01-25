def fill_square(lists):
	returnArr=[]
	
	biggestLen=max([len(arg) for arg in lists])
	

	returnArr=[[arg[i] if i<len(arg) else None for i in range(biggestLen)] for arg in lists]
	currentlen=len(returnArr)
	for i in range(currentlen,biggestLen):
		returnArr.append([None for j in range(biggestLen)])

	print(returnArr)
	return returnArr
