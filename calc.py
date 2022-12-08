def add1 (a,b):
	return a+b
def sub1(a,b):
	return a-b
def mul1(a,b):
	return a*b
def div1(a,b):
	return a/b

print ('Input 1 for add \n Input 2 for sub \n Input 3 for mul \n Input 4 for div ')

num1=float (input ('Enter First Number '))
num2=float (input ('Enter 2nd Number '))

c= int(input("Enter your choice "))

if c==1:
	r1 = add1(num1,num1)
	print (f'The add of number is {r1} ')

	#print ('The add of numbers are {add1(num1,num2)} ')
elif c==2:
	print (f'The sub of numbers are {sub1(num1,num2)} ')
elif c==3:
	print (f'The mul of numbers are {mul1(num1,num2)} ')
elif c==4:
	print (f'The div of numbers are {div1(num1,num2)} ')
else:
	print ('You have entered a wrong choice ')






