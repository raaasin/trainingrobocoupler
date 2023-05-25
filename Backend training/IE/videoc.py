import cv2

face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def face_extractor(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)

    if len(faces) == 0:
        return None

    for (x, y, w, h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face

cap = cv2.VideoCapture(0)
count = 0
video_duration = 1.5  # in seconds
frame_rate = 20  # number of frames per second

while True:
    ret, frame = cap.read()
    if face_extractor(frame) is not None:
        count += 1
        face = cv2.resize(face_extractor(frame), (200, 200))
        file_name_path = "videos/user" + str(count) + ".avi"
        out = cv2.VideoWriter(file_name_path, cv2.VideoWriter_fourcc(*'XVID'), frame_rate, (200, 200))

        # Capture frames for the specified duration
        frames_captured = 0
        while frames_captured < int(video_duration * frame_rate):
            out.write(face)
            frames_captured += 1

        out.release()

        cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0))
        cv2.imshow("Face Cropper", face)
    else:
        print("No face detected")
        pass

    if cv2.waitKey(1) == 13 or count == 100:  # Press 'Enter' to exit or record 100 videos
        break

cap.release()
cv2.destroyAllWindows()
print("Video capturing completed")
