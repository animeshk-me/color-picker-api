from colorthief import ColorThief
import cv2

def get_dominant_color(image_file):
    color_thief = ColorThief(image_file)
    rgb_code = color_thief.get_color(quality=1)
    return '#' + '%02x%02x%02x' % rgb_code


def get_image_border_color(image_file):
    img_arr = cv2.imread(image_file)
    rgb_code = tuple(img_arr[2][2])
    return '#' + '%02x%02x%02x' % rgb_code