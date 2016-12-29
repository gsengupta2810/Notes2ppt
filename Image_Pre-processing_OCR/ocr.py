import pytesseract
from package.transform import four_point_transform
import imutils
import numpy as np
import cv2
import os

image = cv2.imread('../testing/output_images/IMG_20161226_014645_HDR.jpg')
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height = 500)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)

cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

(_,cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

#if Value error is coming then change syntax to (cnts,_)


for c in cnts:
	
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02 * peri, True)
 
	if len(approx) == 4:
		screenCnt = approx
		break

cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 2)
cv2.imshow("Outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)
warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
warped = warped.astype("uint8") * 255
print "Wait for few minutes tesseract doing it's work "
cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(warped, height = 650))
cv2.imwrite('../testing/output_images/warped.png',warped)
cv2.waitKey(0)
cv2.destroyAllWindows()
target= open("separate_text.py", 'w')
from PIL import Image
target.write( pytesseract.image_to_string(Image.open('../testing/output_images/warped.png')))
os.remove("../testing/output_images/warped.png")
cv2.waitKey(0)
