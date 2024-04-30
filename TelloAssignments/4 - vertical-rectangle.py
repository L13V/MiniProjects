from djitellopy import tello
import time
drone = tello.Tello()
drone.connect()


drone.takeoff() 
drone.move_up(50)
drone.move_left(30)
drone.move_down(50)
drone.move_right(30)
time.sleep(1)
drone.land()