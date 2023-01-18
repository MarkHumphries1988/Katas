

def create_counter(value):
	global counter
	counter=value






	return {"up":counter_up,"down":counter_down}
	pass

def counter_down():
	global counter
	counter-=1
	return counter

def counter_up():
	global counter
	counter+=1
	return counter
