import cv2
import time
import sys
path = input("Enter the path here: ")
img = cv2.imread(path)
read = cv2.QRCodeDetector()
bbox = read.detectAndDecode(img)
# below if statement came from https://www.thepythoncode.com/article/generate-read-qr-code-python
if bbox is not None:
    print(f"QRCode data:\n{bbox}")
    time.sleep(12)
    sys.exit()