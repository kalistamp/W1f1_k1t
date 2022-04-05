#!/user/bin python3

# Disclaimer: This script is for educational purposes only.  
# Do not use against any network that you don't own or have authorization to test. 


# CREATES INDIVIDUAL CATEGORIZED FOLDERS FOR ANY RECONNAISSANCE

# Note: If ran in sudo Permissions will default to "Locked" 


import os

main = 'AP'
sub_one = 'SharkCaps'
sub_two = 'WordLi'
sub_tree = 'Hashcat'
sub_four = 'Xtras'
# sub_five = 'Xtras_2'

os.mkdir(main, mode=0o777)
# "0o777" is Defauly Mode to unlock all permissions ...
os.mkdir(sub_one, mode=0o777)
os.mkdir(sub_two, mode=0o777)
os.mkdir(sub_tree, mode=0o777)
os.mkdir(sub_four, mode=0o777)
# os.mkdir(sub_five, mode=0o777)

# [ "os.chmod" can change the permissions of anyy Directory or File created by "os", or any other arugment you use such as "open/write" ]


file = open("Txt", "w") 
file.write("Text Input")
file.close()

file = open("Man", "w") 
file.write("""

Tools:

airmon-ng
airodump-ng
aireplay-ng
aircrack-ng
Monitoring, Recon and Dumping

Using the aircrack-ng suite, Turn on the monitor mode

                                sudo airmon-ng start wlan0

Simple passive listening and capture, Used to discover AP in the environment

                                sudo airodump-ng wlan0mon

Targeted listening and capture, Focus on one AP and one channel

                   airodump-ng wlan0mon -c 11 --bssid E8:2C:6D.... -w sonic

Attacking WEP

WEP is an old encryption protocol but still used in some places, It is vulnerable to direct cracking attacks

Here, you want to get the 4-way WPA Handshake, It requires network traffic between the AP and one device

The process can be enhanced by sending deauth packets – – You can Deauth Packets to every device on the Network with “-a” … or you can target a specific device on the Network by adding “-c”

Aireplay Command used to send Deauth Packets “0” (See sources for more reference)
Deauth connected devices while airodump is running in a separate Terminal to initiate authentication process and try to get the handshake

In the airodump-ng Terminal, the WPA handshake will appear once captured

                       aireplay-ng -0 15 -a 1C:9E:CC:... -c 3C:2E:FF:... wlan0mon

- 0 means deauthentitcation - - 15 is number of deauths sent

- a mac address of access point

- c mac address of the client (station #) (This is optional, you can choose to not add this and knock all devices off network)
- wlan0mon is the interface name
# Another possibility is to use fake authentication to generate IV

# -1 = fake authentication

# 0 = delay between association demands

# -e = AP ESSID (name)

# -a = AP MAC

# -h = attacker MAC

                    aireplay-ng -1 0 -e teddy -a 00:14:7K:7E:40:80 -h 00:0F:9K:88:9K:82 wlan0mon

# ARP Sniffing and injection is another method

Aircrack-ng too directly crack the WEP Key

Cracking can be done using aircrack-ng

Note: Use a good Wordlist !

       aircrack-ng -a2 -b 28:33:88:0A:3A:CB -w '/home/lock/28:33:88:0A:6A:CB/why_.txt' '/home/lock/beyond-01.cap'

- a [a.mode]: force attack mode (1/WEP, 2/WPA-PSK)
- b [bssid]: target selection: access point's MAC
- w [words]: path to wordlist(s) filename(s)
- Drag and drop the .cap file

Introduction

Running "sudo airmon-ng check kill" should be used every time you launch Wi-Fi attacks to ensure there is no other applications that will interfere with our attacks. Good habit to do this every time you plan on hacking a Wi-Fi network.

WPA/WPA2 requires a minimum password of 8 chracters so we need to be using a wordlist that contains passwords >8 characters.

When you're using the tools needed to hack Wi-Fi networks you'll notice the Power/PWR level is displayed in dBi or "db" sometimes with a "-" sign before the number displayed. It doesn't matter which tool you plan on using (airodump-ng, wifite, etc.) since they all display the "Power" level a little differently but all represent the "db/dBi. Notice the power levels 

Hardware and Setup:

It's important to understand that a wireless antenna improves the tranmission and reception of the radiofrequency (RF) signals giving you a reliable connection to the Wi-Fi network. The gain provided by an antenna is measured in Decibels Isotropic (dBi) which is what's represented when you're looking for wireless networks to connect in order to determine which one has the best connection.

Yagi" antennas are known for connecting to a Wi-Fi network from a distance and are widely used in the hacker community. These are best suited when targeting a Wi-Fi network from a great distance. 

Imagine someone thinking something was peculiar about their internet connection at a public Wi-Fi and seeing someone with strange antennas, stickers on their laptop, wearing a top hat, and looking up to no good sitting there. It's just not good. Blend in. Keep your laptop clean looking, keep professional, and appear to be a normal plain user , NO STICKERS ALLOWED

If you encounter an issue with your USBs and Kali won't start without an error this is most likely because you don't have a USB 2.0 or 3.0 port. Make sure your Alfa card is plugged in and attached to your Kali VM with the proper USB settings selected for it. If you do not have a USB 3.0 or USB 2.0 port on your computer you won't be able to use the Alfa network cards recommended in this course and will not be able to continue.

START:

Instead of me explaining every technical detail about WEP, WPS, and WPA/WPA2 WiFi networks I'll direct you to an excellent resource

< https[.]//wwwyoutube.com/watch?v=QHo2hCzxMr0 >

Capture the three way handhsake from the Access Point you are looking to target and crack, Usually this is done by Deauthing a device on the network your monitoring or using "hcxdumptool" 

USE THESE TOOLS - -

airmon-ng
airodump-ng
aireplay-ng

Now at some point you're going to realize you're not able to crack every Wi-Fi network you come across and not every Wi-Fi network can be cracked or hacked. It depends on a lot of factors like signal strength, location, password complexity, etc. 

Running Hashcat :

To utilize hashcat we must first turn the .cap file into a workable format for hashcat. Go to the directory that wifite saved the .cap file of the network you're trying to crack and have had no success using default wordlists on.

Using "wpaclean" you can covert your .cap file into the correct format required for hashcat 

[ wpaclean NEW.cap handshake.cap ]

# Confused about this next part... Where did this new hashcat file come from ??? Is it being created by the "-j" switch after aircrack-ng ???

# The next command from the tutorial tells me to enter this command:

[  aircrack-ng -j hashcat.hccapx New.cap ]

You now have a hccapx file which is meant only for hashcat. We'll now use the GPU on your host machine to increase password cracking significantly.

[  hashcat -m 2500 hashcat.hccapx WORDLIST.txt ]

(  -m 2550 specifies the hash file type which in this case relates to WPA/WPA2 )


EvilTwin Cracking:

Passive Bruteforce attacks failed, Moving onto Engaging Target is the next option 

As you've learned from watching the videos in the Wi-Fi megaprimer you're able to setup your own access point and name it whatever you'd like. If you're targeting "HOME-Wi-Fi" then you would set your rogue AP up to broadcast "HOME-Wi-Fi" as well. One network card will be used to bring up your rogue AP and the other network card will be used to launch a Denial of Service (DoS) attack against the real "HOME-Wi-Fi". The goal with the DoS attack is to overwhelm and take down the real "HOME-Wi-Fi" preventing people from connecting to it while at the same time bringing up your rogue AP tricking people into connecting to you instead. The victims will think they're connecting to their "HOME-Wi-Fi" network and not realize they are indeed connected directly to you

They will click and search for their Wi-Fi network or at least troubleshoot a little bit

Tools we will be using:
wifiphisher
airgeddon
wifipumpkin3


Sources:

https://www.aircrack-ng.org/doku.php?id=cracking_wpa

https://www.aircrack-ng.org/doku.php?id=newbie_guide

https://www.aircrack-ng.org/doku.php?id=compatibility_drivers

https://www.aircrack-ng.org/doku.php?id=wpa_capture

https://shehackske.medium.com/capturing-and-cracking-wpa-handshake-using-aircrack-ng-d9496f30c7c3

https://cryptokait.com/2020/09/02/taking-password-cracking-to-the-next-level/
Update:

After running, airmon-ng check kill to activate adapter to find AP’s

run, service NetworkManager restart – To turn back on Network wifi
    """) 
file.close()
