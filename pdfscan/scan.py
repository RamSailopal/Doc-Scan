from PIL import Image
import cv2
import pytesseract

print("DATA FROM SCANNING QR CODE\n\n")
img = cv2.imread('doc-out1.png')
detect = cv2.QRCodeDetector()
value, points, straight_qrcode = detect.detectAndDecode(img)
print(value)
print("\n\nDATA FROM SCANNING FORM\n\n")
# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# Simple image to string
print(pytesseract.image_to_string(Image.open('doc-out1.png'),config="r'digits'"))
