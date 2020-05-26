import os

import cv2
import numpy as np
np.set_printoptions(threshold=float('inf'), linewidth=100)

def getDominant(im):
    """获取主色调"""
    return np.round(im.mean(axis = (0,1)))


def fitColor(color1, color2):
    """返回两个颜色之间的差异大小"""
    return sum(np.abs(color1-color2))

def getColors(path):
    """获取图片列表的色调表"""

    color = []
    for file in os.listdir(path):
        img = cv2.imread(path+file)
        try:
            color.append(getDominant(img))
        except:
            print(path+file)

    return color


# img = cv2.imread(r'C:\Users\August-us\Desktop\helin1.jpg')



def generate(im_file, imgs_path, colors, box_size, multiple=1):
    """生成图片"""
    im = cv2.imread(im_file)
    im = cv2.resize(im, (im.shape[1] * multiple, im.shape[0] * multiple))

    img_list = [imgs_path+file for file in os.listdir(imgs_path)]
    # 获取图片宽高
    width, height = im.shape[1], im.shape[0]

    for i in range(height // box_size + 1):
        for j in range(width // box_size + 1):

            # 图块起点坐标
            start_x, start_y = j * box_size, i * box_size

            # 初始化图片块的宽高
            box_w, box_h = box_size, box_size

            box_im = im[start_y:, start_x:]
            if i == height // box_size:
                box_h = box_im.shape[0]
            if j == width // box_size:
                box_w = box_im.shape[1]

            if box_h == 0 or box_w == 0:
                continue

            # 获取主色调
            dominant = getDominant(im[start_y:start_y + box_h, start_x:start_x + box_w])

            img_loc = 0
            # 差异，同主色调最大差异为255*3
            dif = 255 * 3

            # 遍历色调表，查找差异最小的图片
            for index in range(colors.__len__()):
                if fitColor(dominant, colors[index]) < dif:
                    dif = fitColor(dominant, colors[index])
                    img_loc = index

            # 读取差异最小的图片
            box_im = cv2.imread(img_list[img_loc],cv2.IMREAD_COLOR)

            # 转换成合适的大小
            box_im = cv2.resize(box_im, (box_w, box_h))

            # 铺垫色块
            im[start_y:start_y + box_h, start_x:start_x + box_w] = box_im

            j += box_w
        i += box_h

    return im

def main(mainPicture, output, theme, box_size=20, multiple=10):
    colors = getColors(theme)
    result_im = generate(mainPicture,  theme,colors, box_size, multiple )
    cv2.imwrite(output,result_im)
    # cv2.imshow('', result_im)
    # cv2.waitKey()

main(mainPicture=r'F:\Learning\1212/au.png',output=r'C:\Users\August-us\Desktop\12.png', theme=r'F:\Learning\1212/')