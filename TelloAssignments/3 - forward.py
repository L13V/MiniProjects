from djitellopy import tello
import time
drone = tello.Tello()
drone.connect()


drone.takeoff() 
drone.move_forward(30) 
time.sleep(1)
drone.land()