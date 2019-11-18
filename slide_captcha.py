# coding=utf-8

import cv2 as cv


def get_pos(image):
    blurred = cv.GaussianBlur(image, (5, 5), 0)
    canny = cv.Canny(blurred, 250, 500)
    contours, hierarchy = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    for i, contour in enumerate(contours):
        M = cv.moments(contour)
        if M['m00'] == 0:
            cx = cy = 0
        else:
            cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
        if 6000 < cv.contourArea(contour) < 9000 and 370 < cv.arcLength(contour, True) < 390:
            if cx < 400:
                continue
            x, y, w, h = cv.boundingRect(contour)  # 外接矩形
            #21 22行用于展示轮廓效果，，
            #cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            #cv.imshow('image', image)
            return x
    for i, contour in enumerate(contours):
        M = cv.moments(contour)
        if M['m00'] == 0:
            cx = cy = 0
        else:
            cx, cy = M['m10'] / M['m00'], M['m01'] / M['m00']
        if cx < 400:
            continue
        x, y, w, h = cv.boundingRect(contour)  # 外接矩形
        area = w*h
        length = 2*w+2*h
        print("{} {}".format(area, length))
        if 6000 < area < 9000 and 370 < length < 390:
            #38 39行用于展示轮廓效果
            #cv.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            #cv.imshow('image', image)
            return x
    return 0


def test_captcha():
    base = "D:\\WorkspacePython\\slide_captcha_cracker\\"
    img0 = cv.imread(base+'source2.jpg')
    pos_x = get_pos(img0)
    print("pos_x:"+str(pos_x))
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    test_captcha()
