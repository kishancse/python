import random
# h=int(input())

# if(h>10):
# 	print("the number is greater than 10")
# elif(h<10):
# 	print("the number is less than 10 ")
# else:
# 	print("equal")
# while(h>10):
# 	print("hello")
# 	h=h-1

r = random.randint(1,20)
while(True):
	inp=int(input())
	if(inp<r):
		print("wrong guess,try a greater number")
	elif(inp>r):
		print("wrong guess,try a smaller number")
	else:
		print("congrats, you have guessed the number")
		break;