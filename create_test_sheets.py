import cv2
import numpy as np
import qrcode

#read the blank test sheet
sheet_S4 = cv2.imread("S2.png")

#convert to grayscale
sheet_S4 = cv2.cvtColor(sheet_S4, cv2.COLOR_BGR2GRAY)

name_S4 = "T1_S2"

#make QR code
qr_img_S4 = qrcode.make(name_S4)
qr_img_S4 = np.float32(qr_img_S4)

#crop and resize QR code
qr_img_S4 = qr_img_S4[40:260, 40:250]
qr_img_S4 = cv2.resize(qr_img_S4, (0, 0), fx=0.7, fy=0.7)

#calculate coordinates where the QR code should be placed
y1_S4, y2_S4 = 890, 1044
x1_S4, x2_S4 = 50, 197

#place the QR code on the sheet
sheet_S4[y1_S4:y2_S4, x1_S4:x2_S4] = qr_img_S4 * 255

#write the image file
cv2.imwrite(str(name_S4) + ".png", sheet_S4)
