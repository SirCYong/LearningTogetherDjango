#!/usr/bin/env python
# encoding: utf-8

import RPi.GPIO as driver
import time

# 指定GPIO口的选定模式为GPIO引脚编号模式（而非主板编号模式）
# driver.setmode(driver.BCM)

# 指定GPIO14（就是LED长针连接的GPIO针脚）的模式为输出模式
# 如果上面GPIO口的选定模式指定为主板模式的话，这里就应该指定8号而不是14号。
# driver.setup(23, driver.IN)
number = 8
led_num = 23
"""
有人灯就亮 2s 没人 就关灯
"""
while True:
    driver.setmode(driver.BCM)
    driver.setup(led_num, driver.OUT)
    driver.setup(number, driver.IN)

    if driver.input(number):
        driver.output(led_num, True)
        continue
    else:
        print("没人")
        driver.output(led_num, False)
    time.sleep(2)
    driver.cleanup()

# 最后清理GPIO口（不做也可以，建议每次程序结束时清理一下，好习惯）



