
def acceptinteger(a,b):
	p=a*b
	if p>1000:
		return p
	else:
		return a+b


a1=int(input ("please input 1st numner"))
a2=int(input ("please inpur 2nd number"))
s=a1*a2
if s>1000:
	print ('Since a1*a2 >1000 ' +  str(acceptinteger(a1,a2)))
else:
	print ('Since a1*a2 <1000 '  + str(acceptinteger(a1,a2)))


		




