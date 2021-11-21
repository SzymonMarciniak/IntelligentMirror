import cv2
import time 
import face_recognition
import numpy as np 
import os 

class FaceRecognition:
    def __init__(self) -> None:

        
        prefix = os.getcwd()
        self.prefix = f"{prefix}/IntelligentMirror/faceRecognition/"

        self.video_capture = cv2.VideoCapture(0)
        
        persons = [p for p in os.listdir(f"{self.prefix}/data")]

        self.known_face_encodings = []
        self.known_face_names = []

        for person_img in persons:

            name =  person_img[:-4]
            name = name+"_nazwisko"

            someone = face_recognition.load_image_file(f"{self.prefix}data/{person_img}") 
            someone_face_encoding = face_recognition.face_encodings(someone)[0]

            self.known_face_encodings.append(someone_face_encoding)
            self.known_face_names.append(name)

        self.process_this_frame = True
        self.no_face = 0

    def recognition(self):

        while True:

            _, frame = self.video_capture.read()
            
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            rgb_small_frame = small_frame[:, :, ::-1]

            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)


            if self.process_this_frame:
                
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "unknown"
                    if name == "unknown":
                        self.no_face = self.no_face + 1
                        print(self.no_face)
                        if self.no_face == 20:
                            RFace = name
                            
                    
                    face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        name = self.known_face_names[best_match_index]
                        RFace = name
                        self.no_face = 0

                    face_names.append(name)
            else:
                self.no_face = self.no_face + 1
                print(self.no_face)
                
                if self.no_face == 20:
                    RFace = "unknown"
                


            self.process_this_frame = not self.process_this_frame


            
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                

        
            cv2.imshow('Video', frame)

            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            #time.sleep(0.5)


        self.video_capture.release()
        cv2.destroyAllWindows()
    
if __name__ == "__main__":

    rec = FaceRecognition()
    rec.recognition()

        