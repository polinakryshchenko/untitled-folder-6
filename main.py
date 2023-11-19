import cv2
from PIL import Image

cat_img_path = 'cat.png'
glasses_img_path = 'glasses.png'
cat_w_glasses_img_path = 'cat_w_glasses.png'

image = cv2.imread(cat_img_path)

cv2.imshow("Cat", image)
cv2.waitKey()


cat_face_cascade = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')
cat_face = cat_face_cascade.detectMultiScale(image)

x, y, w, h = cat_face[0]

cv2.rectangle(image, (x, y), (x+w, y+h), (15, 255, 127), 3)

cv2.imshow("Cat", image)
cv2.waitKey()

cat = Image.open(cat_img_path)
glasses = Image.open(glasses_img_path)
cat = cat.convert("RGBA")
glasses = glasses.convert("RGBA")

glasses = glasses.resize((w, int(h *0.9)))
cat.paste(glasses, (x, y), glasses)
cat.save(cat_w_glasses_img_path)
cat_w_glasses = cv2.imread(cat_w_glasses_img_path)

cv2.imshow("cat_w_glasses", cat_w_glasses)
cv2.waitKey()