import json
import time

from PIL import Image
from uiautomator2 import Device


def findImage(d, flag_image, sleep=1):
    # 加载图片
    result = d.image.match(Image.open(flag_image))
    time.sleep(sleep)
    return result


def findImageSim(d, flag_image, sleep, sim=0.99):
    result = findImage(d, flag_image, sleep)
    print("检测中[]" + flag_image + "," + json.dumps(result))
    if float(result['similarity']) > sim:
        result['bool'] = True
        return result
    else:
        result['bool'] = False
        return result


def findImageSimWait(d:Device, flag_image, sleep=1, sim=0.99):
    while True:
        if findImageSim(d, flag_image, sleep, sim)['bool']:
            print("检测到[]" + flag_image + ".")
            return True


def findImageSimCount(d, flag_image, sim=0.95, count=3):
    for i in range(count):
        result = findImageSim(d, flag_image, sim)
        if result['bool']:
            return result
