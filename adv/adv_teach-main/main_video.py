import cv2
from simple_facerec import SimpleFacerec
from line import Line_detection
# import serial
import time

# Encode faces from a folder
sfr = SimpleFacerec()
ld = Line_detection()
sfr.load_encoding_images("training images/")


file_name = input('Please enter the name of the Lecture to be recorded')

# Load Camera
cap = cv2.VideoCapture(0)

if (cap.isOpened() == False): 
    print("Error reading from camera source")

out = cv2.VideoWriter('RecordedVideo' + file_name + '.avi', -1, 20.0, (640,480))

# start a serial port from arduino
# arduino = serial.Serial(port=' /dev/ttyUSB0 ', baudrate=115200, timeout=.1)


while (cap.isOpened()):
    # read from camera
    ret, frame = cap.read()

    if ret==True:
        # frame = cv2.flip(frame,0)

        # write the flipped frame
        out.write(frame)

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            sub = (int(frame.shape[1]/2)) - int((x1 + x2)/2)
            print (sub)
            # arduino.write(bytes(sub, 'utf-8'))
            time.sleep(0.05)

            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
            cv2.circle(frame, (int((x1 + x2) / 2), int((y1 + y2) / 2)), 5, (255, 255, 255), -1)
            ld.draw_grid(frame,(2,2))
            cv2.line(frame,(int((x1 + x2) / 2), 0),(int((x1 + x2) / 2), 480), color=(0, 255, 0), thickness=3)


        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

cap.release()
cv2.destroyAllWindows()