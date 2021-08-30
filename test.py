import os
os.system('clear')
print('\n\n\n')
print('Hello World Wifi hotspot Enabler')
print('(c) 2016 Hello World. All Right rserved.')
print()

print = ('1 command received start')
print = ('2 command received stop')
print = ('3 command received exits')
cmd = '0'
while cmd != '3':
	cmd = input('please enter command 1, 2, or 3: ')
	if cmd == '1':
		print('starting wifi........................')
		os.system('netsh wlan set hostednetwork mode=allow ssid=Hell0_World key=12345678') #For windows only
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
	





	
	
	