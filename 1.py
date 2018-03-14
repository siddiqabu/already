x = int(input("enter the value: "))
if x<=20:
	factorial = 1
	if x>0:
		for i in range(1,x+1):
			factorial=factorial*i
		print(factorial) 
	else:
		print(invalid)
