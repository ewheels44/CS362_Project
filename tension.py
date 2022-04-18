#!/usr/bin/env python3

USB_PORT = "/dev/ttyACM0"  # Arduino Uno WiFi Rev2

import serial
from influxdb import InfluxDBClient
import time 
import datetime 


# print_commands
#
# prints available comands to user
#
def help():
   print("Sailing Preformance Limited")
   print("Welcome")
   print("Starting up....")
   print()
   print("Available commands:")
   # print("  a - Retrieve Arduino value")
   print("  s - start monitoring tension")
   print("  x - Exit program")

#
# tension
#
# reads data frmo the Arduino
#
# def read_tension(s):
#     while True:
#         stop = input("press e to stop: ")



###########################################
#               Main

# Try ad connect to USB serial port at 9600
try:
   usb = serial.Serial(USB_PORT, 9600, timeout=2)
except:
   print("ERROR!!!")
   print("Exiting program.")
   exit()

help()

while True:
   command = input("Enter command: ")
   if command == "a":       # fail safe test
    print("fail safe")
   elif command == "s":
        usb.write(b'read_tension')
        print("press e to stop monitoring")

        client = influxdbclient(host='ec2-34-230-73-208.compute-1.amazonaws.com', port=8086, database='tesing')
        measurement_name = "speedtest"
        time = datetime.datetime.utcnow()

            # connect to influx
        ifclient = influxdbclient(ifhost,ifport,ifdb)

        body = [
        {
            "measurement": measurement_name,
            "time": time,
            "fields": {
                "value" : 0.6
            }
        }
    ]

        # write the measurement
        # ifclient.write_points(body)


      # while True:
      #     line = usb.readline()  # read
      #     line = line.decode()  # convert 
      #     line = line.strip()  # strip extra whitespace characters
      #     print(line)



   elif command == "x":  # exit program
      print("Exiting program.")
      exit()
   else:  # unknown command
      print("Unknown command '" + command + "'.")
      help()
