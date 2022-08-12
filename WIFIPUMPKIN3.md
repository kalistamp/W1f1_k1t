### Wifipumpkin3 Installation and Setup:

Before we can use this tool, we need to install the dependent packages for this to work use the following command to do that.

``` 
sudo apt-get update 
apt install libssl-dev libffi-dev build-essential
```

Now that we have installed the dependencies, we need to download the tool from GitHub and change the directory to the wifipumpkin3 and install the python dependency.

```
git clone https://github.com/P0cL4bs/wifipumpkin3.git  
cd wifipumpkin3
apt install python3-pyqt5
apt install hostapd                                                    
python3 -c "from PyQt5.QtCore import QSettings; print('done')"
```

As we are done with that we would like to install the setup file which came with wifipumpkin3, this python file will install all the other dependencies that this tool will need to function properly.

```python3 setup.py install```

Now that we have installed all the tools perfectly let’s use wifipumpkin, the first thing we would do today is to create a fake AP with whatever name you want, with this access point we would wait for a victim to connect to the network and also do a MITM attack to sniffing packets. we will try to sniff out the post request that may contain users’ credentials like email and password, this would only work with HTTP. Let’s go in to see how this works.

WP3 Setup:

    Command      Description
    -------      -----------
    ap           show all variable and status from AP
    clients      show all connected clients on AP


```
wifipumpkin3
set interface wlan0
set ssid Free Wifi
set proxy noproxy
ignore pydns_server
start
```

After starting the Fake access point, we can see that some protocols have also been started these will help in the capturing of sensitive information which is passed over the network
From our second device, we will find the SSID for bogus AP, when the victim connects to this he will receive malicious IP from our DHCP server.

From our second device, we could go to an HTTP page that doesn’t have SSL (secured socket layer ) with this whatever information like email, username, or password entered we would be able to view the text entered by the victim.

Wifipumkin captures the traffic and the credentials which were entered by the victim
