# -*- coding: utf-8 -*-

import logging
import os
from time import sleep

###################  修改以下参数即可  #######################

# 屏幕分辨率
device_x, device_y = 1920, 1080

# 通关模式：1=重新挑战 -> 挑战界面，2=重新挑战-> 更换阵容
game_mode = 1

# 各步骤等待间隔
part_1_wait = 12     # 点1次  共9秒     等游戏开始
part_2_wait = 18    # 点36次 共36秒    开始刷怪
part_3_wait = 5     # 点6次  共1.2秒   随缘法乱点
part_4_wait = 0.5     # 点1次  共3秒     等页面跳转

# 刷金币次数
repeat_times = 60

##############################################################

# 日志输出
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

def tap_screen(x, y):
    """calculate real x, y according to device resolution."""
    base_x, base_y = 1920, 1080
    real_x = int(x / base_x * device_x)
    real_y = int(y / base_y * device_y)
    os.system('adb shell input tap {} {}'.format(real_x, real_y))

def do_money_work():
## part_1   进入游戏状态
#scene_1
    if game_mode == 1:
        logging.debug('#0 开始闯关')
        tap_screen(1600, 970)
        sleep(part_1_wait)
## part_2   游戏中状态
#scene_2
    logging.debug('#1 自动刷怪开启!')
    tap_screen(1780, 40)
    for i in range(part_2_wait):
        tap_screen(1720, 80)
        sleep(1)
## part_3   妲己说废话状态
#scene_3-7
    logging.debug('#2 跳过...\n')
    for i in range(part_3_wait):
        tap_screen(1600, 980)
        sleep(0.2)
## part_4   过关页面展示状态
#scene_8
    logging.debug('#3 确认结果')
    tap_screen(1600, 970)
    sleep(part_4_wait)

if __name__ == '__main__':
    for i in range(repeat_times):
        logging.info('round #{}'.format(i + 1))
        do_money_work()
