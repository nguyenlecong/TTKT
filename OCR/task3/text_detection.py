import numpy as np
import pytesseract
import cv2
import pdf2image

PDF_PATH = 'sample/pdftest.pdf'
DPI = 200
OUTPUT_FOLDER = None
FIRST_PAGE = None
LAST_PAGE = None
FORMAT = 'jpg'
THREAD_COUNT = 1
USERPWD = None
USE_CROPBOX = False
STRICT = False

# convert pdf to image
# pdf = pdf2image.convert_from_path(PDF_PATH, dpi=DPI, output_folder=OUTPUT_FOLDER,\
#     first_page=FIRST_PAGE, last_page=LAST_PAGE, fmt=FORMAT, thread_count=THREAD_COUNT,\
#         userpw=USERPWD, use_cropbox=USE_CROPBOX, strict=STRICT)

# index = 1
# for image in pdf:
#     image.save("page_" + str(index) + ".jpg")
#     index += 1

img = cv2.imread('task3/test.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

pytesseract.pytesseract.tesseract_cmd = r'D:\Tai Lieu\HUST-Study\20201\TTKT\tesseract\tesseract.exe'

# detecting characters
# hImg, wImg, _ = img.shape
# boxes = pytesseract.image_to_boxes(img, lang = 'jpn')

# # cong = r'--oem 3 --psm 6 outputbase digits' # only detecting the digits
# # boxes = pytesseract.image_to_boxes(img, lang = 'jpn', config = cong)

# for box in boxes.splitlines():
#     box = box.split(' ')
#     print(box)
#     x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
#     cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 255), 1)
#     # cv2.putText(img, box[0], (x, hImg-y+25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255), 1)
#     cv2.imshow('c',img)

# detecting words
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img, lang = 'jpn')

results = []
for index, box in enumerate(boxes.splitlines()):
    if index != 0:
        box = box.split()
        print(box)
        if len(box) == 12:
            x, y, w, h = int(box[6]), int(box[7]), int(box[8]), int(box[9])
            cv2.rectangle(img, (x, y), (w+x, h+y), (0, 0, 255), 1)
            cv2.putText(img, box[11], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (50,50,255), 1)
            results.append((box[11], x, y, w, h))
            cv2.imshow('w', img)

# cv2.imwrite('task3/word_detect.jpg', img)
cv2.waitKey(0)
cv2.destroyAllWindows()