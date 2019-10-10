# coding: utf-8

'''
将图片中颜色较深部分转换为透明

使用时，直接python rgb2rgba.py -p img_path即可
这里的img_path换成需要转换的图片的路径
可选的参数有阈值和是否显示图片，分别对应-t和-s

@author: LuoJianxun
'''

import cv2
from optparse import OptionParser
import numpy as np

np.set_printoptions(threshold=np.inf)

def get_alpha_channel(img, low_hsv, high_hsv):
    '''获取alpha通道数值

    Args:
        img: numpy.array类型; 通过opencv读取的图片
        low_hsv: list类型; 要转变为透明的颜色的最小HSV值
        high_hsv: list类型; 要转变为透明的颜色的最大HSV值
    
    Returns:
        alpha_channel: numpa.array类型；alpha通道的数值
    '''

    # 将RGB色彩空间图片转换为HSV色彩空间图片
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 要转变为透明的颜色的最小HSV值
    low_hsv = np.array([0, 0, 0])
    # 要转变为透明的颜色的最大HSV值
    high_hsv = np.array([180, 255, 46])
    # 获取指定颜色区域, 低于lowerb的值和高于upperb的值都会置为0
    # 在lowerb~upperb区间的值会置为255
    mask = cv2.inRange(hsv, lowerb=low_hsv, upperb=high_hsv)
    # 将指定颜色的mask值置为0, 其余区域的mask值置为255
    alpha_channel = 255 - mask

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


def run(img_path, low_hsv, high_hsv, show):
    '''程序运行主函数

    Args：
        img_path: str类型，图片路径
        low_hsv: list类型; 要转变为透明的颜色的最小HSV值
        high_hsv: list类型; 要转变为透明的颜色的最大HSV值
        show: bool类型，是否显示转换后的图片

    '''
    try:
        if img_path:
            img = cv2.imread(img_path)
        else:
            return 'Please input image path!'
        alpha_channel = get_alpha_channel(img, low_hsv, high_hsv)
        result = convert(img, alpha_channel)
        if show:
            show_img(result)
        print('Finished!')

        return 'done'
    except BaseException as e:

        return repr(e)


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-p', '--path', dest='img_path', help='Path to image')
    parser.add_option('-l', '--low_hsv', 
                     dest='low_hsv', 
                     help='The min hsv values of color', 
                     default=[0, 0, 0])
    parser.add_option('-i', '--high_hsv', 
                     dest='high_hsv', 
                     help='The max hsv values of color', 
                     default=[180, 255, 46])
    parser.add_option('-s', '--show', 
                     dest='show', 
                     help='Augment with showing image (Default=True)', 
                     action='store_true', 
                     default=False)
    options, args = parser.parse_args()
    if not options.img_path:
        parser.error('Path to image must be specified. Pass -p or --path to command line')
    if not (isinstance(options.low_hsv, list) and isinstance(options.high_hsv, list)):
        parser.error('HSV must be a list.')
    run(options.img_path, options.low_hsv,options.high_hsv, options.show)
    # img_path = r'C:\Users\luo\Desktop\add_flag\add_flag_2\code\background.png'
    # threshold = 216
    # show = False
    # run(img_path, threshold, show)