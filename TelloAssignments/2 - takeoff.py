from djitellopy import tello
import time
drone = tello.Tello()
drone.connect()
time.sleep(1)
drone.takeoff() 
time.sleep(20)
drone.land()