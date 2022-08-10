from email import parser
from dronekit import connect, VehicleMode, APIException
import time 
import socket
import exceptions
import math
import argparse

def connectMyCopter():
    baud_rate = 921600

    vehicle = connect('/dev/ttyAMA0', baud=baud_rate, wait_ready=True)
    return vehicle

def arm(vehicle):
    while vehicle.is_armable == False:
        print("Waiting for vehicle to be armable")
        time.sleep(1)
    
    print("Vehicle is now armable")
    print("")

    vehicle.armed = True
    while vehicle.armed == False:
        print("Wating for vehicle to armed.......")
        time.sleep(1)
    print("Vehicle is now armed.......")
    print("motors are now spinning.......")
    return None

vehicle = connectMyCopter()
arm(vehicle)
print("End")
