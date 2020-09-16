import numpy as np
import cv2


def click_event(event, x, y, flags, params):

    img = params[0]
    points = params[1]

    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ',' , y)
        cv2.circle(img, (x,y), radius=0, color=(255, 0, 0), thickness=7)
        point_count = len(points)

        if not point_count%4 == 0:
            if point_count%4 == 3:
                cv2.line(img, points[-3], (x,y), color=(255, 0, 0), thickness=7)
            cv2.line(img, points[-1], (x,y), color=(255, 0, 0), thickness=7)
        cv2.imshow('image', img)

img = cv2.imread('imgs/1.jpg')
cv2.imshow('image', img)

cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()

