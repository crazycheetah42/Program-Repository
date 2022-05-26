import cv2
import time
import sys
# below variables came from https://www.thepythoncode.com/article/generate-read-qr-code-python
path = input("Enter the path here: ")
img = cv2.imread(path)
read = cv2.QRCodeDetector()
bbox = read.detectAndDecode(img)
if bbox is not None:
    print(f"QRCode data:\n{bbox}")
    time.sleep(12)
    sys.exit()
