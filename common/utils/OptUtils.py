import time

import uiautomator2
from uiautomator2 import Device, Direction

device = uiautomator2.connect_usb()


def delay_click(x: float, y: float, sleep: int = 1):
    print("进入延迟等待中," + str(sleep))
    time.sleep(sleep)
    print("开始点击")
    device.click(x, y)


def start_app():
    app_package = 'com.nexon.maplem.global'
    app_info = device.app_current()
    if app_info['package'] != app_package:
        print("需要启动")
        device.app_start(app_package, 'com.nexon.maplem.module.MapleUnityActivity')


# 从右向左水平滑动
def swipe(direction: Direction):
    device.swipe_ext(direction, 0.3)


# 计算等待时间
def countWait():
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"已经等待:{count}s")


# 等待
def wait(sleep):
    time.sleep(sleep)
