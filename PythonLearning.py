# import math                 		  #you will need to use math.var
# from random import randint  		  #you don't need to use random.randint(). So instead just randint()
# from random import randint as rdi   #rdi() which means randint()

# print(2**4)
# print(20//6)
# print(num:=int(input()))
# print('''She\'s
# mine''')

# x=input("Input: ") #This is how you print a text before getting input on the same line
# print('Output: '+x*3)

# if temp:=int(input())>=100:print('Boiling')

# nums=[1,2,3]
# nums.append(4)
# nums.insert(0,0)
# nums.insert(0,'hello')
# print(nums.index(3))
# print(len(nums))

# string="Minh dep zai"
# for _ in string:
    # print(_)
	
# DRY principle - Don't Repeat Yourself
# A bad code is said to abide by the WET principle - Write Everything Twice/We Enjoy Typing

# def function(var):
	# var+=1
	# print(var)
# var=int(input())
# function(var)
# print(var)

# s="B R U H"
# print("#"+s.replace(" ",""))

# def shout(word):
	# """Print a word with an
# exclamation mark following it.
# """
	# print(word+"!")
# print(shout.__doc__)
# help(shout)
# shout("hello")

# def add(x, y):
    # return x + y
# def do_twice(func, x, y):
    # return func(func(x, y), func(x, y))
# a = 5
# b = 10
# print(do_twice(add, a, b))

# try:
	# print(1//0)
	# print("Yay!")
# except:
	# print("Do you know Math?")    #This try-except is actually very useful when we need user input
# finally:
	# print("Please type again")
# raise #Which is something that I still not fully understand

# temp=-10
# assert(temp>=10),"Colder than absolute zero!"
# Programmers often place assertions at the start of a function to check for valid input, and after a function call to check for valid output.t
