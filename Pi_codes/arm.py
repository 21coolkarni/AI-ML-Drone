
from email import parser
from dronekit import connect, VehicleMode, APIException
import time 
import socket
import exceptions
import math
import argparse

def connectMyCopter():
    vehicle = connect('/dev/ttyAMA0', wait_ready=False, baud=921600)
    print("Vehicle is connected")
    print("")
    return vehicle

def arm(vehicle):
    print("Vehicle is now armable.......")
    time.sleep(2)
    print("")
    vehicle.armed = True
    while vehicle.armed==False:
        print("Wating for vehicle to armed.......")
        time.sleep(1)
    print("")
    print("Vehicle is now armed.......")
    print("")
    print("Motors are now spinning.......")
    print("")
    time.sleep(5)
    print("Disarming the vehicle.......")
    print("")
    time.sleep(1)
    vehicle.armed == False

    return None

vehicle = connectMyCopter()
arm(vehicle)
print("End")

