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

#Lesson 4.3 Wifi hotspot enabled by Python Programming
import os
os.system('clear')
print('\n\n\n')
print('Hello World Wifi hotspot Enabler')
print('(c) 2016 Hello World. All Right rserved.')
print()
ssid='Hello_World'#SSID can be change anytime from here
password='12345678'#Password can be change anytime from here
cmd = '0'
while cmd != '3':
	
	print  ('1 command received start')
	print  ('2 command received stop')
	print  ('3 command received exits')
	cmd = input('please enter command 1, 2, or 3: ')
	
	if cmd == '1':
		print('starting wifi........................')
		ssid = input('Please enter ssid: ')# take the ssid
		password = input('Please enter password: ')#take the password
		os.system('netsh wlan set hostednetwork mode=allow ssid=" + ssid + " password=" + password"') #For windows only
		os.system('netsh wlan set hostednetwork mode=allow ssid=Hello_World password=12345678')#fix SSID and password
		os.system('netsh wlan start hostednetwork')
	
	elif cmd == '2':
		print('stopping wifi........................')
		os.system('nets wlan stop hostednetwork')
	
	elif cmd == '3':
		print('Exiting wifi........................')
		quit()
	
	else:
		print('unknown command')
		os.system('pause')
#Lesson 5 - Looping
#Lesson 5.1 find IP and Try except
import socket
print (socket.gethostname())
socket.gethostbyname("www.google.com")
hostname = socket.gethost()
try:
	ip_address = socket.gethostbyname_ex(hostname)
	print(ip_address)
	print("Ipv4 address is " + str(ip_address[2] [0])) #to get ip_address only
except:
	print ("error")
#Lesson 5.2 IP Scanner
#Lesson 6 - Number

	









