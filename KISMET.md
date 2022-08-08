
KISMET Setup:

### Installing gpsd on Linux:

``` sudo apt-get install gpsd ```

``` sudo apt install gpsd-clients ```

---------- First thing you


After plugging in a GPS / GNSS receiver through the USB port, your GPS should be automatically configured. To verify, type the below command:

``` ls /dev/tty* ```

To further verify if the GPS has been bound to this folder type:

This will display the GPS input stream

``` cat /dev/ttyACM0 ```

### Stop the systemd gpsd services:

``` systemcyl stop gpsd ```
``` systemctl stop gpsd.socket ```

["  Stopping gpsd.service, but it can still be activated by: gpsd.socket  "]




### View XGPS Display:

Type:

``` xgps ```





* * *

