import cv2
import numpy as np

def do_remove(img, h_start, h_end, w_start, w_end):
    # 开始操作
    copy_img = img[h_start:h_end, w_start:w_end]

    num = 0
    for i in copy_img:
        if [255, 255, 255] in i:
            num = num+1

    if num < 0:
        return img

    thresh = cv2.inRange(copy_img, np.array([150, 150, 150]), np.array([255, 255, 255]))
    scan = np.ones((3, 3), np.uint8)
    cor = cv2.dilate(thresh, scan, iterations=1)
    specular = cv2.inpaint(copy_img, cor, 5, flags=cv2.INPAINT_TELEA)

    img[h_start:h_end, w_start:w_end] = specular

    return img


def remove_water_mark(filename,save_name):
    img = cv2.imread(filename)
    height, width = img.shape[0:2]
    # 计算操作区域
    # 右下角
    h_start = int(height - height*0.4)
    h_end = height
    w_start = int(width - width*0.30)
    w_end = width
    img = do_remove(img, h_start, h_end, w_start, w_end)

    #左下角
    h_start = int(height - height*0.14)
    h_end = height
    w_start = 0
    w_end = int(width * 0.3)
    img = do_remove(img, h_start, h_end, w_start, w_end)

    
    # 正下方
    h_start = int(height - height * 0.07)
    h_end = height
    w_start = int(width - width * 0.8)
    w_end = int(width - width * 0.45)
    img = do_remove(img, h_start, h_end, w_start, w_end)

    # 正中间
    h_start = int(height - height/2 - (height * 0.03))
    h_end = int(height - height/2 + (height * 0.03))
    w_start = int(width * 0.30)
    w_end = int(width * 0.80)
    img = do_remove(img, h_start, h_end, w_start, w_end)

    # 保存图片
    cv2.imwrite(save_name,img)