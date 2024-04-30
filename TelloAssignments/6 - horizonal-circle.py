from djitellopy import Tello
import time
tello = Tello()

tello.connect()
time.sleep(1)
tello.takeoff()
time.sleep(1)
tello.curve_xyz_speed(10, 10, 0, 21, 0, 0, 10)
