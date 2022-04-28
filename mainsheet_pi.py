# 
# Team Name: Rouge Leader
# Group Members: Ethan Wheeler & Khizer Shareef
# SP 22 - CS362
#  
# Project title: Sailboat performance measurement
 

from socket import timeout
import serial
from influxdb import InfluxDBClient
import time 
import datetime


# establish connection from the arduino
try:
    from_arduino = serial.Serial( '/dev/cu.usbmodem142101', 9600, timeout = 2 )
except:
    print("failed to retrieve data from arduino")
    exit()

print( "connection from arduino successful, reading ... ")

# connect to influxdb to send data
client = InfluxDBClient(host='ec2-34-230-73-208.compute-1.amazonaws.com', port=8086, database='tesing')
measurement_name = "tension"

while True:
    data_frm_ard = from_arduino.readline()
    data_frm_ard = data_frm_ard.decode()
    data_frm_ard = data_frm_ard.strip()


    time = datetime.datetime.utcnow()

    # disregard the white space
    if len(data_frm_ard) != 0 :
        body = [
                    {
                        "measurement": measurement_name,
                        "time": time,
                        "fields": {
                            "mainsheet" : float(data_frm_ard)
                        }
                    }
                ]

        # write the measurement
        client.write_points(body)