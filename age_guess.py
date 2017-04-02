import cognitive_face as CF
import os

KEY = '189b110e646145459cbdddd4d8f8d161'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

original_image = 'martin.jpg'
result = CF.face.detect(original_image, True, False, "age")

age = result[0]['faceAttributes']

print age
