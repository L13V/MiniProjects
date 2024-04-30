from djitellopy import tello
import cv2


drone = tello.Tello()
drone.connect()

drone.streamon()
while True:
    frame = drone.get_frame_read(with_queue=False, max_queue_len=32).frame
    cv2.imshow("Tello", frame)
    cv2.waitKey(1)
