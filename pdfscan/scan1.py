from PIL import Image
import cv2
import pytesseract
import sys

if len(sys.argv) <= 1:
   print("You must pass the file path of the image to process as an parameter")
   sys.exit(1)

print("DATA FROM SCANNING QR CODE\n\n")
img = cv2.imread(sys.argv[1])
detect = cv2.QRCodeDetector()
value, points, straight_qrcode = detect.detectAndDecode(img)
print(value)
print("\n\nDATA FROM SCANNING FORM\n\n")
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open(sys.argv[1]),config="r'digits'"))
