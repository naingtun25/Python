#Note from Google video
#To check variables
type() 
# put in blanket some variables that you want to check
# To check Bindary 
"{0:b}".format(a)
# a is number that you want to change into binary

#Folder 5 (if Statement)
string_variable = "Hello World"
if "Hello" in string_variable:
	print("Hurray, it exits")
	
list_variable = ["Hello", "World"]
if "Hello" in list_variable:
	print('Yes!')
	
dict_variable = {"message":"Hello World"}
if "message" in dict_variable:
	print('Oh Yeah!')
	
#Folder 5 (if elif and else statement)
num = 3
if num > 0:
   print("num is possitive")
elif num==0:
   print("num is zero")
else:
   print("num is neagative")
   
#Folder 5(Break and continue)
for var in "string":
   if var =='i':
	break
	print(var)
   else:
   	print(var)
print("hello")

#Continue
for var in "string":
   if var=="i":
   	continue
   	print(var)
   else:
   	print(var)
print("Hello")

#Folder 06(Loop in Python)
#for loop in string_variable
string_variable = "Hello World"
for character in string_variable:
	print(character)
#for loop in list
list_variable = ["Hello", "World"]
for item in list_variable:
	print(item)
	 
#range
a = range(10)
print(a)
for i in a:
  print (i)

#while loop
count = 0
while (count<2):
	print(count) 
	count += 1 (count = count +1)
print("Hi")

#Folder 07(Home Assignment1)
for num in range(10, 20):
    for i in range(2, num):
    	if num %i == 0:
    		j = num/i
    		print ('%d equals %d * %d ' %(num, i, j))
    		break
    
    else:
    	print (num, 'is a prime number')
    	
#Folder 08(Number)
a = 1 (intenger)
a = 1.2 (float)
a = 2+3j (complex) 
#abs value
a = -7
abs(a)
#ceil value
import math
a = 12.34
math.ceil(a) 
13 (#get the higher intenger)
#floor value
import math
a = 12.34
math.floor(a)
12(get the floor number)
#exp
import math
math.exp(2)
#max value
a = max(12, 45, 3)
a
45
#min value
a = min(12,45,3)
a
3
#power value
import math
pow(2, 3)
8
#square root
import math
math.sqrt(100)
10
#modf value
import math
math.modf(12.3)
0.3000, 12.0 (#spreate the interger and float value) 
#log value
import math
math.log(10, 10)
1.0

#Folder 09(String)
a = "Hello's World"
#capitalize
a="hello world"
a.capitalize()
#count
a='hello world'
a.count('e')
#position of the charater
a='python'
a.find('t')
2(# t character is second place in the whole world, start count fro 0)
#alphanumeric string
a='hello1234hell0'
a.isalnum()
True
a.isalpha
False(# Because contain number)
#Digit string
a='123'
a.isdigit()
#Length character
a='string python'
len(a)
12(# count the character)
#change the Small letter
a='hello World'
a.lower()
#change the capital letter
a='hello world'
a.upper()
#swap from small letter to capital letter and from capital to small
a='HELLO WORLD'
a.swapcase()
hell world
#max method
a='Hello world'
max(a)
w(#alphabetically the highest character in the string.)
#min method
a='abc'
min(a)
a(#alphabetically the lowest character in the string.)
a='python'
a.replace('p', 'j')
jython

#Folder 10(Play with Lists)
a=['[python', 12334, 'python123']
#access vavlue from the list
print(a[0]) 
python (#count from 0)
#update the list
a=['python', 12.33]
a[1]='hello'
print(a)
['python', 'hello']
#remove the list
a=['python', 12.33]
del a[1]
print(a)
['python']
#minum value
a=[23, 45, 3]
print(min(a))
3
#count method
a=[167, 32, 32, 23]
print(a.count(32))
2
#index method (index means place start from zero)
a=[167, 34, 23, 34]
print(a.index(34))
#Adding some items to the list
a=[167, 34, 23, 34]
a.append('hello')
print(a)
#adding some items to the list that you want to put to the index)
a=[167, 34, 23, 34]
a.insert(2, 'hello'))
print(a)
#reverse method
a=[167, 34, 23, 34]
a.reverse()
print(a)
#sort method
a=[167, 34, 23, 34]
a.sort()(#increasing order)
a.reverse()(#decreasing order)
print(a)

#Folder 11(Tuple)
#Length of Tuple
a=('hello', 23, 24, 34.4, 3, "World")
print(len(a)) 
6
#maximun
a=(23, 23, 34, 43)
print(max(a))
43
#minmun value
a=(23, 23, 34, 43)
print(min(a))
23
#convert tuple to list
a=(23, 23, 34, 43)
b=list(a)
print(b)
#list to tuple
a=[1, 2, 3, 4]
b=tuple(a)
print(b)

#Folder 12(Dictionary)
a={2007:'hello', 2008: 'python'}
a[2007]
'hello'
#length of Dictionary
a={2007: 'iphone', 2008: 'iphone3g', 2009: 'iphone3gs', 'iphone4' :2010}
print(len(a))
4
#Clear method
a={2007: 'iphone', 2008: 'iphone3g', 2009: 'iphone3gs', 'iphone4' :2010}
a.clear()
print(a)
{}
#copy method
a={2007: 'iphone', 2008: 'iphone3g', 2009: 'iphone3gs', 'iphone4' :2010}
b=a.copy()
print(b)
b={2007: 'iphone', 2008: 'iphone3g', 2009: 'iphone3gs', 'iphone4' :2010}
#Get value
a={2007: 'iphone', 2008: 'iphone3g', 2009: 'iphone3gs', 'iphone4' :2010}
print(a.get(2008))
iphone3g
#Items methods
a={2007: 'iphone', 2008: 'iphone3g', 2009: 'iphone3gs', 'iphone4' :2010}
print(a.items())
#keys value
a={2007: 'iphone', 2008: 'iphone3g', 2009: 'iphone3gs', 'iphone4' :2010}
print(a.keys())
#update value
a={2007: 'iphone', 2008: 'iphone3g', 2009: 'iphone3gs', 'iphone4' :2010}
b={20: 'phone', 28: '3g', 29: 'phone3gs', 'iphone' :210}
a.update(b)
print(a)
#Values
a={2007: 'iphone', 2008: 'iphone3g', 2009: 'iphone3gs', 'iphone4' :2010}
print(a.values())
#access value
a={2007: 'iphone', 2008: 'iphone3g', 2009: 'iphone3gs', 'iphone4' :2010}
print(a[2007])
iphone
#update the key value
a={2007: 'iphone', 2008: 'iphone3g', 2009: 'iphone3gs', 'iphone4' :2010}
a[2007]='python'
#add new keys and value
a={2007: 'iphone', 2008: 'iphone3g', 2009: 'iphone3gs', 'iphone4' :2010}
a[2011]='Hello World'
print(a)
#Delete key and value
a={2007: 'iphone', 2008: 'iphone3g', 2009: 'iphone3gs', 'iphone4' :2010}
del a[2007]
print(a)

#Folder 13(Function)
def python ():
  print("hello")
  return
python()
#function in argument 
def hello(x):
	print("hello world!")
	return
x=12
hello(x)
#keywords argument
def hello(x):
    print(x)
    return
hello(23) / hello(x=23)
#default argument
def hello(x,y):
   print(x,y)
   return
hello(23,45)
#variabel length argument
def hello(x,*l):
	print(x)
	for b in l:
	    print(b)
	return
hello(12, 34, 56, 45)
#pass by value
def hello(x):
   x=45
   print(x)
   return
x=13
hello(x)
print(x)
#pass by reference
a=[1, 2, 3, 4]
def hello(x):
   x[0]=12
   print(x)
   return
hello(a)
print(a)

#folder 14(module)
#Create a folder
#make a python file eg. tuna.py
def first():
    print("I am from moudle")
    return
first() #create another file same folder eg.python.py
import tuna #nome of the module
tuna.first()

#call module from another directory
import file_name
file_name.function
    
#Folder 15(Exception Handling)
x=input('give some values')
print(x) #when we get the name wrong is called syntax error. Eg. inpout instead input

x=int(input("enter some value"))
print(x) #when the user tpye the string variables, can't be print. Those kind of error called exception error, otherwise programmer can handle those kind of error

#handle the exception
try:
   x=input("write something")
except:
   print("Please write something correcltly") #if there is error in try block (eg. inpout) the program will show except block.
while True:
   try:
      x=int(input("write something"))
      break
   except:
      print("please write correctly") #when program executed we have to type only intenger not string, if you type string, the message from block will be seen.
while True:
   try:
      x=int(input("write something"))
      break
   except:
      print("please write correctly")
   finally:
      print("over") #finally block not included either try or except. whatever error occurs finally block executed

#folder 16(File operation)
#Steps in Python file operation
#1 Opening
#2 Perform operation(readig, writing, appending, etc.)
#3 closing

try:
   f = open("test.txt", encoding = 'utf-8')
   #perform file operations
finally:
   f.close()

with open("test.txt", encoding = 'utf-8') as f:
# perform file operations

#Create the text file
f = open('python.txt', 'w+') #when we put + sign after w, it means if there is same file name the program will open, unless the program will create new file
#Reading from a file
f = open("test.txt", 'r')
f.read(5)
f.read()
f.tell()
f.seek(0)#go to the first line
f.tell()
print(f.read()) #read the file
for line in f: #read the file using for loop
	print(line)
f.seek(0)
f.readline() #read the text line by line
f.readlines()
#Writing File with python
file=open('python.txt', 'w')
str="hello World"
file.write(str)
file.close()
#other way to create file with python
file=open('python.txt', 'w')
str=input("enter the data:  ')
file.write(str)
file.close()
#Appending Data in existing file (New data will added)
file=open('python.txt', 'a')
str=input("enter the data:  ')
file.write(str)
f.close()
#Download file form internet python
import urllib.request 
urllib.request.urlretrieve("Url link", "give some name")

#folder 17(Home Assignmet on file)
#Assignment
with open("atoc.txt", 'w') as f1, open("fruits.txt", 'w') as f2:
	f1.write("a\n")
	f1.write("b\n")
	f1.write("c\n")
	f1.write("for apple\n")
	f1.write("for banna\n")
	f1.write("for cherry\n") #when we execute the code, there will be to files atoc.txt and fruits.txt
#Combine these two files' words as in one file
from itertools import zip_longest as zip
with open("res.txt", 'w') as res, open("atoc.txt") as f1, open("fruits.txt") as f2:
	for line1, line2 in zip(f1, f2):
		res.write("{}{}\n".format(line1.rstrip(), line2.rstrip()))
#explaining zip functon
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
zipped
[(1, 4), (2, 5), (3, 6)]
#explaining izip function
for i in izip([1,2,3], ['a', 'b', 'c']):
	print i
(1, 'a')(2, 'b')(3, 'c')
#explaining izip_longest
izip_longest('ABCD', 'XY', fillvalue= '-')
AX BY C- D-
izip('ABCD', 'xy') #when we used izip the result will be
Ax By
#rstrip
'     spacious     '.rstrip()
'     spacious'
"AABAA".rstrip("A")
'AAB'
"ABBA".rstrip("AB") #both AB and BA are stripped
''
"ABCABBA".rstrip("AB")
'ABC'
# Python3 program to demonstrate the use of strip() method
string = """ geeks for geeks """
# prints the string without stripping
print(string)
 geeks for geeks 
# prints the string by removing leading and trailing whitespaces
print(string.strip())
geeks for geeks
# prints the string by removing geeks
print(string.strip(' geeks'))
for

#folder 18(OOPS Concepts)
class Student:    #the name of the class is start with Capital, inside the method we have to put attribute and methods. 	def __init__(self):     #self is the parameter
	self.name="alex"
s1=Studet() #create the object 
print(s1.name)
#when we use singal object eg.s1, for all we must use (self)	
class Student:
	def __init__(s1): #change the parameter from self to s1
		s1.name="alex"
s1=Student()
print(s1.name) 
#this is the way to create the method inside the class
class Student:
	def __init__(self):
		self.name="alex"
	
	def walk(self):			#every class has action called methods
		print("my name is alex")
s1=student()
s1.walk() #to call the method using object
#self, names, classes
class Student:
	def __init__(self,names,classes):
		self.name="alex"	#class variable
		self.classes=classes	#class variable
		self.names=name	#class variable
		
	def walk(self):
		print("my name is",self.names)
		print("my name is",self.name)
		print("my name is",self.classes)
s1=Student('xyz',12)
s1.walk() #to call the method using object

s2=Student('zyx', 18)
s2.walk()
#Inheritance
class Father():
     def lastname(self):
     	print("Tun")
class Mother():
     def middlename(self):
     	print("Naing")
class Son(Father, Mother):
     def firstname(self):
     	print("Naing")
s1=Son()
s1.firstname()
s1.lastname()
s1.middlename()
#Folder 19(Working with Database)
#Installiation
#1 MySQL Server Community
#2 MySQL Workbench
#3 MySQL-Python-Connector


		
		







   


   






	
    	
    	


	

