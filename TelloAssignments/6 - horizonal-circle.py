from djitellopy import Tello
import time
tello = Tello()

tello.connect()
time.sleep(1)
tello.takeoff()
time.sleep(1)
tello.curve_xyz_speed(70, 70, 0, 140, 0, 0, 20) 
tello.curve_xyz_speed(-70, -70, 0, -140, 0, 0, 20)
tello.land()