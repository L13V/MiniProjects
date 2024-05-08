#Vertical Triange. Gets height at specified intervals
from djitellopy import tello
import time
import threading

tello = tello.Tello()
tello.connect()

def fly(): #"commands"
    global tello
    tello.takeoff() 
    tello.go_xyz_speed(0, -30, 40, 10)
    time.sleep(1)
    tello.go_xyz_speed(0, -30, -40, 10)
    tello.move_left(30)
    time.sleep(1)
    tello.land()

def height(): #"get height"
	global tello
	while True:
		time.sleep(0.5)
		tello.get_height()

if __name__ =="__main__":
	commands = threading.Thread(target=fly, args=())
	height = threading.Thread(target=height, args=())

	commands.start()
	height.start()

	commands.join()
	print("Done!")