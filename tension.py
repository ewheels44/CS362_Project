#!/usr/bin/env python3

USB_PORT = "/dev/ttyACM0"  # Arduino Uno WiFi Rev2


import os.path
import serial
import paramiko 

#
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

        router_ip = "ec2-34-230-73-208.compute-1.amazonaws.com"
        router_username = "ubuntu"

        ssh = paramiko.SSHClient()

# Load SSH host keys.
        ssh.load_system_host_keys()
# Add SSH host key automatically if needed.
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# Connect to router using username/password authentication.
        ssh.connect(router_ip, 
                    username=router_username, 
                    key_filename=os.path.join(os.path.expanduser('~'), ".ssh", "CS362_projectt_keypair.pem"))

# Run command.
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("show ip route")
        output = ssh_stdout.readlines()

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
