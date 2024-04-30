from djitellopy import tello
import time
drone = tello.Tello()
drone.connect()


drone.takeoff() 
drone.go_xyz_speed(0, -30, 40, 10)
time.sleep(1)
drone.go_xyz_speed(0, -30, -40, 10)
drone.move_left(30)
time.sleep(1)
drone.land()