#!/usr/bin/env python3

"""Control an Arduino over the USB port."""

# usb.py
# Created by John Woolsey on 12/17/2019.
# Copyright (c) 2019 Woolsey Workshop.  All rights reserved.
#
#
# Edits by: Ethan Wheeler
#


# USB_PORT = "/dev/ttyUSB0"  # Arduino Uno R3 Compatible
USB_PORT = "/dev/ttyACM0"  # Arduino Uno WiFi Rev2


# Imports
import serial


# Functions
def print_commands():
   """Prints available commands."""
   print("Sailing Preformance Limited")
   print("Welcome")
   print("Starting up....")
   print()
   print("Available commands:")
   # print("  a - Retrieve Arduino value")
   print("  s - start monitoring tension")
   print("  x - Exit program")


# Main

# Connect to USB serial port at 9600 baud
try:
   usb = serial.Serial(USB_PORT, 9600, timeout=2)
except:
   print("ERROR - Could not open USB serial port.  Please check your port name and permissions.")
   print("Exiting program.")
   exit()

# Send commands to Arduino
print("Enter a command from the keyboard to send to the Arduino.")
print_commands()

while True:
   command = input("Enter command: ")
   if command == "a":  # read Ardino A0 pin value
    print("fail safe")
   elif command == "s":
      usb.write(b' read_tension')
      line = usb.readline()  # read
      line = line.decode()  # convert 
      line = line.strip()  # strip extra whitespace characters

      print(line)

   elif command == "x":  # exit program
      print("Exiting program.")
      exit()
   else:  # unknown command
      print("Unknown command '" + command + "'.")
      print_commands()
