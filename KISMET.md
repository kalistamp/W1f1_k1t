
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

``` kkismetdb_to_wiglecsv -i /home/kali/Kismet-20220808-06-41-29-1.kismet -o new.csv ```

Help Page:

```
Kismetdb to WigleCSV

A simple tool for converting the packet data from a KismetDB log file to
the CSV format used by Wigle

usage: kismetdb_to_wiglecsv [OPTION]
 -i, --in [filename]          Input kismetdb file
 -o, --out [filename]         Output Wigle CSV file
 -f, --force                  Force writing to the target file, even if it exists.
 -r, --rate-limit [rate]      Limit updated records to one update per [rate] seconds
                              per device
 -c, --cache-limit [limit]    Maximum number of device to cache, defaults to 1000.
 -v, --verbose                Verbose output
 -s, --skip-clean             Don't clean (sql vacuum) input database
 -e, --exclude lat,lon,dist   Exclude records within 'dist' *meters* of the lat,lon
                              provided.  This can be used to exclude packets close to
                              your home, or other sensitive locations.

```









