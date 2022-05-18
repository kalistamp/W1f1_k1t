
# FINISH REDAING THIS :

#file:///Users/rec/Downloads/WifiPhisher,%20Hacking%20Tools%20(2022)%20(5_12_2022%208_50_51%20AM).html




# MORE RECOURCES TO READ - - 

#  ettercap tutorial - https://charlesreid1.com/wiki/MITM/Evil_Twin_with_Ettercap


# WHERE DO I ADD THIS ?

 #Evil Twin attack can be performed by running Wifiphisher w/ the following command parameters.

#wifiphisher -aI wlan0 -jI wlan1 -p firmware-upgrade --handshake-capture handshake.pcap

author = 'Автор: калистамп '
x = ' '
title = 'Wifi Phishing Tutorial'
tools = ['https://github.com/gophish/gophish', 'https://github.com/s0lst1c3/eaphammer', 'https://www.bettercap.org/' 'https://github.com/Ettercap/ettercap', 'https://github.com/onevcat/Kingfisher']
# bettercap is like ettercap, but better

print(title)
print(x*2)
print(author.title())
print(x*2)

print('''

Aoccdrnig to rscheearch at an Elingsh uinervtisy, it deosn’t mttaer in waht
oredr the ltteers in a wrod are, the olny iprmoetnt tihng is taht the frist
and lsat ltteer are in the rghit pclae. The rset can be a toatl mses  and
you can sitll raed it wouthit a porbelm. Tihs is bcuseae we do not raed
ervey lteter by it slef but the wrod as a wlohe and the biran fguiers it
out aynawy.

... so please excuse us for every typo in the documentation, man pages or 
code.

	''')
print(x*2)
print(f' Other Tools for wifi phishing besides "Wifiphisher" (https://github.com/wifiphisher/wifiphisher) : {tools}')
print(x*2)

# THIS TUTORIAL WILL SOLEY FOCUS ON THE "Wifiphisher" TOOL TO CONDUCT EVIL-TWIN ATTACKS (https://github.com/wifiphisher/wifiphisher)

MEAT = '''
	WifiPhisher is a popular tool to execute Evil Twin Attacks on a Targets Wireless AP (The tool is capable of using modern Wi-Fi association methods such as Known Beacons, KARMA, and Evil Twin)

	Overview :

	The idea here is to create an evil twin AP, then de-authenticate or DoS the user from their real AP. When they re-authenticate to your fake AP with the same SSID, they will see a legitimate-looking webpage that requests their password because of a "firmware upgrade." When they provide their password, you capture it and then allow them to use the evil twin as their AP, so they don't suspect a thing

	Steps:

	1. De-auth user from there AP
	2. Allow user to authenticate to your evil twin 
	3. Offer a webpage to the user on a proxy that notifies them that a "firmware upgrade" has taken place, and that they need to authenticate again.  
	4. User will manually enter there password and it will be passed onto you

	*****************************************************

	Wifiphisher can be run with or without any parameters or options. To run the tool without setting any parameters, simply type wifiphisher or python bin/wifiphisher in the terminal.
	The tool searches for the corresponding Wi-Fi interface and opens in GUI mode.
	Once the GUI is open, the tool searches for available Wi-Fi networks (ESSID) in the vicinity. The target ESSID can be selected using the up / down arrow keys.

	*****************************************************

	First step, is to RUN the script -

	python3 wifiphisher.py

	sudo python setup.py install

	On the first time running it will likely tell you that "hostapd" is not found and will prompt you to install it. Install by typing "y" for yes. It will then proceed to install hostapd (Run again after install)

	Next, the script will start the web server on port 8080 and 443, then go about and discover the available Wi-Fi networks

	When it has completed, it will list all the Wi-Fi networks it has discovered

	Go ahead and hit Ctrl + C on your keyboard and you will be prompted for the number of the AP that you would like to attack ( you will enetr the number of the ap on the list - 1, 2, 3, or 4 etc.)

	When you hit Enter, Wifiphisher will display a screen like the one below that indicates the interface being used and the SSID of the AP being attacked and cloned

	The target user has been de-authenticated from their AP. When they re-authenticate, they will directed to the the cloned evil twin access point

	When they do, the proxy on the web server will catch their request and serve up an authentic-looking message that a firmware upgrade has taken place on their router and they must re-authenticate

	[ Example jpg - https...//static.wixstatic.com/media/6a4a49_693ecdd612854888b7bbe1ca87b74668~mv2.jpg/v1/fill/w_960,h_522,al_c,lg_1,q_90/6a4a49_693ecdd612854888b7bbe1ca87b74668~mv2.webp ]

	If the user is fooled the will enter there credentials and hit submit

	When the user enters their password, it will be passed to you through the Wifiphisher open terminal

	The user will be passed through to the web through your system and out to the Internet, never suspecting anything awry has happened


'''

def phish():
    choice = input(f'Would you like to [print] or [view] the Tutorial?    ')
    print(x*2)
    if choice == 'view':
        print(f'{MEAT}')
    elif choice == 'print':
        file = open(f"Wi_Phish.txt", "w")
        file.write(f'{MEAT}')
        file.close()
        print(' [+] Tutorial printed in current directory ')
phish()
