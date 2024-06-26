#Vertical Triange. Gets height at specified intervals
from djitellopy import tello
import time
import threading
run = "yes"

tello = tello.Tello()
tello.connect()
def height(): #"get height"
	global tello
	while run == "yes":
		time.sleep(1)
		print("Height: " + str(tello.get_height()))


def fly(): #"commands"
    global tello
    tello.takeoff() 
    tello.go_xyz_speed(0, -50, 60, 10)
    time.sleep(1)
    tello.go_xyz_speed(0, -50, -60, 10)
    tello.move_left(30)
    time.sleep(1)
    tello.land()



if __name__ =="__main__":
	commands = threading.Thread(target=fly, args=())
	height = threading.Thread(target=height, args=())

	commands.start()
	height.start()
	commands.join()
	run = "no"
	print("Done!")