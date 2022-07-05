# # ProjectGurukul Number plate recognition
# # import necessary packages

# import cv2
# import easyocr

# # initialize cascade classifier 
# numberPlate_cascade = (r"C:\Users\bisho\Desktop\test.xml")
# detector = cv2.CascadeClassifier(numberPlate_cascade)

# # initialize the easyocr Reader object 
# reader = easyocr.Reader(['en'])

# # read image
# img = cv2.imread(r"C:\Users\bisho\Desktop\hello.jpg")

# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #-- Detect Number plates
# plates = detector.detectMultiScale(
#         img_gray,scaleFactor=1.05, minNeighbors=7,
#         minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
# print(plates)

# # iterate through each detected number plates
# for (x,y,w,h) in plates:
    
#     # draw bounding box
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

#     # Crop the numberplate
#     plateROI = img_gray[y:y+h,x:x+w]
#     cv2.imshow("Numberplate", plateROI)

#     # detect text
    
#     text = reader.readtext(plateROI)

#     if len(text) == 0:
#         continue
#     print(text)
#     print(text[0][1])

#     # draw text in the frame
#     cv2.putText(img, text[0][1], (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

# # Show the final output
# cv2.imshow('Output', img)

# # wait until  any key is pressed
# cv2.waitKey(0)

#____________________________________________________2______________________________________


# import cv2
# import numpy as np
# import easyocr

# frameWidth = 640    #Frame Widtha
# franeHeight = 480   # Frame Height

# plateCascade = (r"C:\Users\shish\Desktop\numberplate.xml")
# minArea = 500

# # initialize the easyocr Reader object 
# reader = easyocr.Reader(['en'])

# detector = cv2.CascadeClassifier(plateCascade)

# cap =cv2.VideoCapture(0)
# cap.set(3,frameWidth)
# cap.set(4,franeHeight)
# cap.set(10,150)
# count = 0

# while True:
#     success , img  = cap.read()

#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#     # numberPlates = plateCascade.detectMultiScale(imgGray, 1.1, 4)
#     plates = detector.detectMultiScale(
#         imgGray,scaleFactor=1.05, minNeighbors=7,
#         minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)
#     print(plates)

#     for (x, y, w, h) in plates:
#         cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

#         imgRoi = imgGray[y:y+h,x:x+w]
#         cv2.imshow("ROI",imgRoi)

#         cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
        

#         # detect text
#         text = reader.readtext(imgRoi)

#         # if len(text) == 0:
#         #     continue
#         # print(text)
#         # print(text[0][1])

#         # draw text in the frame
#         cv2.putText(img, text[0][1], (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

# # Show the final output
#     cv2.imshow('Output', img)



##########__________________________________3___________________________________
import cv2
import numpy as np
import easyocr


frameWidth = 640    #Frame Width
franeHeight = 480   # Frame Height

plateCascade = cv2.CascadeClassifier(r"C:\Users\shish\Desktop\numberplate.xml")
minArea = 500

reader = easyocr.Reader(['en'])

cap =cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,franeHeight)
cap.set(10,150)
count = 0
number_plate =""

number_plates_list = ["VJ2KRT4","MH2V3T6"]

while True:
    success , img  = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlates = plateCascade .detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in numberPlates:
        area = w*h
        if area > minArea:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            # cv2.putText(img,"NumberPlate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)
            # Read the text from img
            text = reader.readtext(imgRoi)
            if len(text) == 0:
                continue
            print(text)
            # print(text[0][1])
            number_plate = text[0][1]
            print(number_plate)
            for i in number_plates_list:
                if(number_plate==i):
                    servo.angle = 90
                    sleep(15)
                    servo.angle = 0
                    sleep(1)
                else:
                    servo.angle = 0
                    sleep(1)
            

            # draw text in the frame
            cv2.putText(img, text[0][1], (x, y-5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0, 255, 0), 2)

    cv2.imshow("Result",img)
    if cv2.waitKey(1) & 0xFF ==ord('s'):
        cv2.imwrite("D:\SACHIN\cascade\IMAGES"+str(count)+".jpg",imgRoi)
        cv2.rectangle(img,(0,200),(640,300),(0,255,0),cv2.FILLED)
        cv2.putText(img,"Scan Saved",(15,265),cv2.FONT_HERSHEY_COMPLEX,2,(0,0,255),2)
        cv2.imshow("Result",img)
        cv2.waitKey(500)
        count+=1