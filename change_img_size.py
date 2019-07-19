# coding: utf-8

'''
改变图片尺寸

使用时，直接python change_img_size.py -p img_path即可
这里的img_path换成需要转换的图片的路径
可选的参数：是否显示图片，对应-s

@author: LuoJianxun
'''

import cv2
from optparse import OptionParser


def change(img, size):
    '''改变图片尺寸

    Args:
        img: numpy.array类型；通过opencv读取的图片
        size: tuple类型；新图片的尺寸

    Returns:
        new_img: numpy.array类型；变换尺寸后的新图片

    '''

    new_img = cv2.resize(img, size)
    cv2.imwrite('result.jpg', new_img)

    return new_img


def cal_ratio(img):
    '''计算原始图片长宽比

    Args:
        img: numpy.array类型；通过opencv读取的图片

    Returns:
        ratio: float类型；原始图片长宽比

    '''

    shape = img.shape
    ratio = shape[0]/shape[1]
    
    return ratio


def cal_new_size(ratio, height=0, width=0):
    '''计算新图片尺寸值

    直观上理解，图片尺寸一般是长*宽
    但是在计算机视觉中，一般以宽*高来计量
    所以这里的参数使用的是height和width

    Args:
        ratio: float类型；原始图片长宽比
        height: int类型；新图片高度，即传统意义上的宽
        width: int类型；新图片宽度，即传统意义上的长

    Returns:
        size: tuple类型；新图片尺寸

    '''

    try:
        if height == 0:
            height = int(width * ratio)
        elif width == 0:
            width = int(height / ratio)
    except BaseException as e:
        print("Error! Size can't be (0, 0)!")
    size = (width, height)

    return size


def show_img(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def run(img_path, show):
    '''程序运行主函数

    Args：
        img_path: str类型；图片路径
        show: bool类型；是否显示修改后的图片

    '''

    img = cv2.imread(img_path)
    ratio = cal_ratio(img)
    size = cal_new_size(ratio, width=640)
    result = change(img, size)
    if show:
        show_img(result)
    print('Finished!')


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option('-p', '--path', dest='img_path', help='Path to image')
    parser.add_option('-s', '--show', 
                     dest='show', 
                     help='Augment with showing image (Default=True)', 
                     action='store_false', 
                     default=True)
    options, args = parser.parse_args()
    if not options.img_path:
        parser.error('path to image must be specified. Pass -p or --path to command line')
    run(options.img_path, options.show)