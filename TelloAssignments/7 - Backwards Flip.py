from djitellopy import Tello
import time
tello = Tello()

tello.connect()
time.sleep(1)
tello.takeoff()
time.sleep(1)
tello.flip_back()
time.sleep(1)
tello.land()