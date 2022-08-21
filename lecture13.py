for x in range(100,200):
	if all(x%i!=0 for i in range(2,x)):
		print(x)