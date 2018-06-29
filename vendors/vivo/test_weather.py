#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import sys
import time
try:
    import unittest2 as unittest
except(ImportError):
    import unittest
from lib import common, adbtools

from lib import myuiautomator

DEVICE_NAME = sys.argv[2]


class TestVivo(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.device = adbtools.AdbTools(DEVICE_NAME)
        common.unlock_screen(DEVICE_NAME)
        width, height = self.device.get_screen_normal_size()
        self.width = int(width)
        self.height = int(height)

    def setUp(self):

        # return back to home
        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_HOME)

    def tearDown(self):

        time.sleep(2)
        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_HOME)
        time.sleep(2)


    def test_weather(self):
        img_count = 0
        app_name = 'weather'

        try:
            self.device.start_application('com.vivo.weather/.WeatherMain')
            time.sleep(2)
            cmd = 'am force-stop {0} '.format(
                'com.vivo.weather')
            self.device.shell(cmd)
            time.sleep(1)
            self.device.start_application('com.vivo.weather/.WeatherMain')
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1

            # 首页-设置
            time.sleep(10)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 20 * 19), (int(self.height / 100 * 7)))
            self.device.shell(cmd)
            time.sleep(1)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 添加城市
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 20 * 19), (int(self.height / 100 * 7)))
            self.device.shell(cmd)
            time.sleep(1)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
