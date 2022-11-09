import cv2
import face_recognition
import numpy as np
import os

path = 'Student_Images'
def setup():
    os.mkdir(path)
    print(f"Created directory {path}")
    


def main():
    images = []
    classes = []  # list for storing names
    myList = os.listdir(path)
    if len(myList) == 0:
        print("No images found")
    # print(myList)

    for face in myList:
        current = cv2.imread(f'{path}/{face}')
        images.append(current)
        classes.append(face[:-4])


    # print(classes)


    def findEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList


    Known_encodeList = findEncodings(images)
    print('Encoding is completed')

    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        small_img = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
        small_img = cv2.cvtColor(small_img, cv2.COLOR_BGR2RGB)

        faces_Cur_Frame = face_recognition.face_locations(small_img)
        encodings_Cur_Frame = face_recognition.face_encodings(small_img, faces_Cur_Frame)

        for encode_face, location in zip(encodings_Cur_Frame, faces_Cur_Frame):
            compare = face_recognition.compare_faces(Known_encodeList, encode_face)
            face_dist = face_recognition.face_distance(Known_encodeList, encode_face)
            # print(face_dist)
            index = np.argmin(face_dist)

            if compare[index]:
                name = classes[index]
                # print(name)
                y1, x2, y2, x1 = location
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 255), 2)
                cv2.putText(frame, name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        cv2.imshow('Camera:', frame)
        cv2.waitKey(1)
