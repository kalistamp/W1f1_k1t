
KISMET Setup:

### Installing gpsd on Linux:

First you want to install gpsd which will be managing our gps:

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


### Kismet Conversion:

Export contents of various tables in kismet DB to csv file:

``` kismet_log_to_csv --in /home/kali/Kismet-20220808-06-41-29-1.kismet --out something.csv ```

Help Page:

```

usage: kismet_log_to_csv [-h] [--in INFILE] [--out OUTFILE]
                         [--table SRCTABLE]

Kismet to CSV Log Converter

optional arguments:
  -h, --help        show this help message and exit
  --in INFILE       Input (.kismet) file
  --out OUTFILE     Output CSV filename
  --table SRCTABLE  Select the table to output

```









