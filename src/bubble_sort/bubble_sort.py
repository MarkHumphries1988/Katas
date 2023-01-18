def bubble_sort(array):
	sortcount=0
	interimvalue=0

	for index in range(len(array)-1):
		if array[index]>array[index+1]:
			interimvalue=array[index]
			array[index]=array[index+1]
			array[index+1]=interimvalue
			sortcount+=1
	
	if sortcount==0:
		return array
	else:
		return bubble_sort(array)

	pass
