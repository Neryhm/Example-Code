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

# # Function
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

# f=open("Minhf.txt",'w+') 	#r:  Read, !Write, !Create, !Truncate, BEGINNING
							# # r+: Read,  Write, !Create, !Truncate, BEGINNING
							# # w: !Read,  Write,  Create,  Truncate, BEGINNING
							# # w+: Read,  Write,  Create,  Truncate, BEGINNING
							# # a: !Read,  Write,  Create, !Truncate, END
							# # a+: Read,  Write,  Create, !Truncate, END
# f.close()
# with open("E:\\Develop\\Notepad++ Folders\\Python Core Leaning\\Minhf1.txt",'w+') as f1:
	# f1.write("""Hello World!
	# Hello Minh!
	# Hello Earth!""")
# with open("E:\\Develop\\Notepad++ Folders\\Python Core Leaning\\Minhf1.txt",'r+') as f1:
	# print(f1.readlines(1))
	# print(len(f1.read())) #this returns empty string if you already read all content in the file
	
# for _ in file:
    # print(_[0]+str(len(_.strip())))  	#.strip() remove all preceding whitespace which include space,\t and \n
										# Also, these 2 lines of code is the solution to the Book Titles problem on Sololearn

# print(bool(None))
# def func():
	# print("Hi")
# var=func()
# print(var)  #this return None
# print()		#this also return None

# Birthdays={"Minh":1811,"Quyen":1301,}		#Only immutable objects can be used as keys
# print(Birthdays)							#Mutable objects are: list and dict
# Dict.get(key,text if not found)

# Tuples: Lists but immutable
# tuple="one","two","three"	#parentheses is optinal

# List Slice: list[begin:end:step]
# List Comprehensions*: list=[i**2 for i in range(10) if i**2 %2 ==0]

# # String Formatting
# list=[1,2,3]
# text="Numbers:{a}{x}{f}".format(f=list[0],a=list[1],x=list[2])
# msg="Numbers:{0}{1}{2}".format(list[0],list[1],list[2])
# combine="Numbers:{0}{m}{1}{q}{2}".format(list[0],list[1],list[2],m="minh",q="quyen")
# print(msg)
# print(text)
# print(combine)
# name = input("Your name: ")
# age = int(input("Your age: "))
# print("{name} is {age} years old".format(name=name,age=age))

# # String Functions
# print(", ".join(["a","b","c"]))
# print("Hello Minh".replace("Minh","world"))
# print("This is a sentence.".startswith("his"))		#This returns "False" since the string starts with "This" not "his"
# print("This is a sentence.".endswith("sentence.")) 	#This returns "True" since the string really ends with "sentence."
# print("This is a sentence.".upper())
# # Numeric Functions
# print(min(sum([11,22]),max(abs(-30),2)))
# # List Functions
# print(all([i>3 for i in range(5)]))
# print(any([i>3 for i in range(5)]))
# for _ in enumerate([10,20,30]):
	# print(_)

# # Text Analyze
# with open("TestingText.txt","r+") as f:
	# text=f.read()
# def count_char(text,char):
	# return text.count(char)
# print(count_char(text,"r"))
# for char in "abcdefghijklmnopqrstuvwxyz":
  # perc = 100 * count_char(text, char) / len(text)
  # print("{0} - {1}%".format(char, round(perc, 2)))
  
# Longest Word Problem (Sololearn)
# non-pythonic:
txt = input()
words=txt.split()
max_char=0
for i in words:
    if len(i)>max_char:
        max_char=len(i)
        longestword=i
print(longestword)
# pythonic:
text = input().split()
length = [len(x) for x in text]
print(text[length.index(max(length))])
# pythonic ver.2:
text = input().split()
print(max(text, key=len))
