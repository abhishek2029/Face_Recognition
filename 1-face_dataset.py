
import cv2
import os

cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video width
cam.set(4, 480) # set video height

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#face_id = input('\n enter user id end press <return> ==>  ')
face_name=input('\n Enter user name:')

with open('user_names.txt','r+') as file:
	names=file.read().split("\n")
	names=[word for word in names if len(word)!=0]
	names.append(face_name)
	file.seek(0)
	file.truncate()
	print(names)
	print('Device Unlocked')
	file.write("\n".join(names))
	face_id=len(names)-1
	print(face_id)

print("\n [INFO] Will capture your image. Keep looking at the camera ...")
# Initialize individual sampling face count
count = 0

while(True):

    ret, img = cam.read()
    #img = cv2.flip(img, -1) # flip video image vertically
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)     
        count += 1

        # Save the captured image into the datasets folder
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break
    elif count >= 50: # Take 50 face sample and stop video
         break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()


