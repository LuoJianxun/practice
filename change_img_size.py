import cv2
from optparse import OptionParser


def change(img, size):
    new_img = cv2.resize(img, size)
    cv2.imwrite('result.jpg', new_img)

    return new_img


def cal_ratio(img):
    shape = img.shape
    ratio = shape[0]/shape[1]
    
    return ratio


def cal_new_size(ratio, height=0, width=0):
    try:
        if height == 0:
            height = int(width * ratio)
        elif width == 0:
            width = int(height / ratio)
    except BaseException as e:
        print("Error! Size can't be (0, 0)!")

    return (width, height)


def show_img(img):
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def run(img_path, show):
    '''程序运行主函数

    Args：
        img_path: str类型，图片路径
        show: bool类型，是否显示修改后的图片

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