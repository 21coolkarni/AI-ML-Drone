from dronekit import connect
vehicle = connect("/dev/ttyAMA0", wait_ready=True, baud=921600)
print("vehicle is connected")
