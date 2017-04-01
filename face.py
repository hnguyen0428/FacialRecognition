import cognitive_face as CF

KEY = '189b110e646145459cbdddd4d8f8d161'  # Replace with a valid subscription key (keeping the quotes in place).
CF.Key.set(KEY)

# You can use this example JPG or replace the URL below with your own URL to a JPEG image.
img = 'pic1.jpg'
result = CF.face.detect(img, True, False, "emotion")
print len(result)
print result