#Vertical Triange. Gets accel at specified intervals
from djitellopy import tello
import time
import threading
run = "yes"

tello = tello.Tello()

tello.connect()
def accel(): #"get accel"
	global tello
	while run == "yes":
		time.sleep(1)
		print("Acceleration - " + "X: " + str(tello.get_acceleration_x()) + "Y: " + str(tello.get_acceleration_y()) + "Z: " + str(tello.get_acceleration_z()))


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
	accel = threading.Thread(target=accel, args=())

	commands.start()
	accel.start()
	commands.join()
	run = "no"
	print("Done!")