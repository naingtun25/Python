#hex Desimal calculate
0x260 #0x is hex decimal number
608 #turn into decimal
#floot 
f=23.5e6 #e means ten to the power,ten to the power 6
23500000.0
f=25.5e+6 #put the zero
f=25.5e-6#increase the decimal nunber
#complex number
c=3.2j
#Screen Clear in python 
import os
os.systme("clear")

#operator 3.1
#Circle of Area
r = float(input("Enter radius: ")
A = 3.14 * r * r
print("Circle of Area: ",A)
#Even odd
number = 0 #when you want to quit you have to put negative number
while number >= 0: #to run the program again and again (loop)
	number = int(input('type number: ')
	if number %2 == 0:
		print("Even num")
	else:
		print("odd num")
#Calculator
while 1: #to do the program again and again looping
	first_no = float(input("type the num: ")
	operator = input("operator: ")
	second_no = float(input("type the num: ")
	if operator == '+':
		result = first_no + second_no
	elif operator == '-':
		result = first_no - second_no
	elif operator == '*':
		result = first_no * second_no
	elif operator == '/':
		result = first_no / second_no
	else:
		print("Check Again")
	print("Ans: ",result)

#Lesson 4.1 Dos Command by Python
import os
os.system("clear")
os.system("ls")
os.system('neofetch')
os.system('whoami')
os.system('ping google.com')#ping program using python
#Creating and Deleting Folder using python 
import os
print("ls")
print("*****************************")
os.system("ls")

print("mkdir testdir")
print("**************************")
os.system("mkdir teskdir")

print("ls testdir")
print("**************************")
os.system("ls testdir")
os.system("pause")

print("rmdir testdir")
print("**************************")
os.system("rmdir testdir")

print("ls testdir")
print("*****************************")
os.system("ls testdir")

#Create shell using python
import os
os.system('clear')
print(\n\n\n\n) #go to the next four enter
print("Hello World [Version 0.1]")
print('(c) 2020 Hello World, All Right rserved.')
print()
while 1:
	print('C:\\Users\Naing>', end="") #put end for, not to go next line
	cmd = input('')
	os.system(cmd)

#Lesson 4.2 Github for Python




