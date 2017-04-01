import cognitive_face as CF
import os
import time
import face_stats as fs

KEY = '189b110e646145459cbdddd4d8f8d161'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
while True:
    os.system('imagesnap -w 1 pic.jpg > /dev/null 2>&1')
    img = 'pic.jpg'
    result = CF.face.detect(img, True, False, "emotion")
    emotion = fs.determine_emotion(fs.calculate_stats(result))
    print emotion
    time.sleep(1)