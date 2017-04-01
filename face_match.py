import cognitive_face as CF
import os

KEY = '189b110e646145459cbdddd4d8f8d161'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

original_image = 'hoang.jpg'
original_detect = CF.face.detect(original_image)
original_face_id = original_detect[0]['faceId']

os.system('imagesnap -w 1 pic.jpg > /dev/null 2>&1')
verify_image = 'pic.jpg'
image_detect = CF.face.detect(verify_image)

if len(image_detect) != 0:
    image_face_id = image_detect[0]['faceId']

matched = CF.face.verify(original_face_id, image_face_id)
print matched
