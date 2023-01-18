import math

def roman_numeral_encoder(number):

	finalstr=""
	# if number%10==0:
	# 	if number/10 in [1,2,3]:
	# 		return "X"*int(number/10)
	# 	if number/10==4:
	# 		return "XL"
	# 	if number/10 in [5,6,7,8]:
	# 		return "L"+"X"*(number/10-1)
	# 	if number/10==9:
	# 		return "XC"
	# 	else:
	# 		return "C"

	if number>=10:
		newnumber=math.floor(number/10)
		
		if newnumber in [1,2,3]:
			
			finalstr+= "X"*int(newnumber)
			
		elif newnumber==4:
			finalstr+="XL"
		elif newnumber in [5,6,7,8]:
			finalstr+="L"+"X"*(newnumber-5)
		elif newnumber==9:
			finalstr+="XC"
		else:

			finalstr+="C"

	if number%10==0:
		return finalstr

	 
	if number%10 in [1,2,3]:
		finalstr+= "I"*(number%10)
	if number%10==4:
		finalstr+= "IV"
	if number%10 in [5,6,7,8]:
		finalstr+= "V" +"I"*(number%10-5)
	if number%10==9:
		finalstr+= "IX"
	return finalstr
	pass
