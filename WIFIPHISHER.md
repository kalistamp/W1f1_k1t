
MORE RECOURCES TO READ - - (Remove or keep this?)

ettercap tutorial - https://charlesreid1.com/wiki/MITM/Evil_Twin_with_Ettercap


### Personal Notes:

* Evil Twin attack against an open network:
ALL clients will automatically connect to the rogue_AP
This is a typical attack against captive portals

Q: Wifiphisher successfully detected 2.4G hz wifi but not 5G hz - Is 5G hz supported?

A: No it does not. However, i would say that the point is moot since you still need a better frequency range than the target's and there's no better candidate than 2.4Ghz for that.

Q: Why is no one clicking on my Rogue AP? - Why some victim users do not automatically connect to the rogue Access Point?

A: I think you haven't understand the internals of the tool.
There are many reasons why victims would not connect to the rogue AP: https://wifiphisher.readthedocs.io/en/latest/faq.html#why-some-victim-users-do-not-automatically-connect-to-the-rogue-access-point
We rely on Evil Twin (cloning the target network) if the target network is of Open type or the PSK is known to us. I wouldn't recommend cloning a password-protected network and waiting for the user to manually connect (even though it may happen in extreme cases). Mount other kind of attacks, such as KARMA and Known Beacons that will make victims automatically associate with the rogue AP. Wifiphisher supports much more than the "Evil Twin".

Victim’s Network Manager. Different Operating Systems support different wireless features. For example, an Android device will, by default, connect automatically to previously connected open networks making it susceptible to the Known Beacons Wi-Fi automatic association attack. At the same time iOS devices are configured to arbitrarily trasmit probe request frames for previously connected networks making them vulnerable to the KARMA attack.

* Wifiphisher Powerpoint: https://census-labs.com/media/bsideslondon15-wifiphisher.pdf

* Known-Beacon Attck: https://census-labs.com/news/2018/02/01/known-beacons-attack-34c3/


* * *

### "Wifiphisher" Tutorial: (https://github.com/wifiphisher/wifiphisher)

* WifiPhisher is a popular tool to execute Evil Twin Attacks on a Targets Wireless AP (The tool is capable of using modern Wi-Fi association methods such as Known Beacons, KARMA, and Evil Twin)

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

	First step, is to INSTALL the script -
	
	apt-get update

	apt install wifiphisher

	On the first time running it will likely tell you that "hostapd" is not found and will prompt you to install it. Install by typing "y" for yes. It will then proceed to install hostapd (Run again after install)

	Next, the script will start the web server on port 8080 and 443, then go about and discover the available Wi-Fi networks

	When it has completed, it will list all the Wi-Fi networks it has discovered

	Go ahead and hit Ctrl + C on your keyboard and you will be prompted for the number of the AP that you would like to attack ( you will enetr the number of the ap on the list - 1, 2, 3, or 4 etc.)

	When you hit Enter, Wifiphisher will display a screen like the one below that indicates the interface being used and the SSID of the AP being attacked and cloned

	The target user has been de-authenticated from their AP. When they re-authenticate, they will directed to the the cloned evil twin access point

	When they do, the proxy on the web server will catch their request and serve up an authentic-looking message that a firmware upgrade has taken place on their router and they must re-authenticate

	If the user is fooled the will enter there credentials and hit submit

	When the user enters their password, it will be passed to you through the Wifiphisher open terminal

	The user will be passed through to the web through your system and out to the Internet, never suspecting anything awry has happened
