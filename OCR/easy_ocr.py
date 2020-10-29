import torch
import easyocr
import cv2

# Check if pytorch is using the GPU?
print(torch.cuda.current_device())
print(torch.cuda.device(0))
print(torch.cuda.device_count())
print(torch.cuda.get_device_name(0))
print(torch.cuda.is_available())

path = 'sample/test.jpg'
reader = easyocr.Reader(['en'], gpu = False)

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

if device.type == 'cuda':
    reader = easyocr.Reader(['en'])
    reader = reader.readtext(path)

    # reader = reader.readtext(path, detail = 0)

cord = reader[-1][0]
x_min, y_min = [int(min(idx)) for idx in zip(*cord)]
x_max, y_max = [int(max(idx)) for idx in zip(*cord)]

img = cv2.imread(path)
cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0,0,255), 2)
cv2.imshow('', img)
cv2.waitKey()
cv2.destroyAllWindows()