# coding: utf-8

'''
将图片中颜色较深部分转换为透明

使用时，直接python rgb2rgba.py -p img_path即可
这里的img_path换成需要转换的图片的路径

@author: LuoJianxun
'''

import cv2
from optparse import OptionParser

def get_alpha_channel(img, threshold):
    '''获取alpha通道数值

    Args:
        img: numpy.array类型；通过opencv读取的图片
        threshold: int类型；阈值，范围在0~255之间，包括0和255
    
    Returns:
        alpha_channel: numpa.array类型；alpha通道的数值
    '''

    # 将彩色图片转为灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 图片二值化，默认阈值为200，大于200的是白色，小于的是黑色
    ret, binary = cv2.threshold(gray, threshold, 255, cv2.THRESH_BINARY)
    # 将二值化后的图片矩阵赋值给alpha通道
    alpha_channel = binary

    return alpha_channel


def convert(img, alpha_channel):
    '''转换图片

    Args:
        img: numpy.array类型；通过opencv读取的图片
        alpha_channel: numpa.array类型；alpha通道的数值

    '''

    # 将RGB图片转为RGBA图片
    new_img = cv2.cvtColor(img, cv2.COLOR_RGB2RGBA)
    # 将RGBA图片与alpha掩码结合
    new_img[:, :, 3] = alpha_channel
    # 保存图片
    cv2.imwrite('result.png', new_img)

    return new_img


def show_img(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def run(img_path, threshold, show):
    '''程序运行主函数

    Args：
        img_path: str类型，图片路径
        threshold: int类型，阈值，范围在0~255之间，包括0和255
        show: bool类型，是否显示转换后的图片

    '''

    img = cv2.imread(img_path)
    alpha_channel = get_alpha_channel(img, threshold)
    result = convert(img, alpha_channel)
    if show:
        show_img(result)
    print('Finished!')


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-p', '--path', dest='img_path', help='Path to image')
    parser.add_option('-t', '--threshold', 
                     dest='threshold', 
                     help='Threshold with image', 
                     default=200)
    parser.add_option('-s', '--show', 
                     dest='show', 
                     help='Augment with showing image (Default=True)', 
                     action='store_true', 
                     default=False)
    options, args = parser.parse_args()
    if not options.img_path:
        parser.error('Path to image must be specified. Pass -p or --path to command line')
    if options.threshold.isdigit():
        options.threshold = int(options.threshold)
    else:
        parser.error('Threshold must be number.')
    run(options.img_path, options.threshold, options.show)
    