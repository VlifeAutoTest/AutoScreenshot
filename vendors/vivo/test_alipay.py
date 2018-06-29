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
from lib import querydb

DEVICE_NAME = querydb.get_uid(sys.argv[2])


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


    def test_alipay(self):
        app_name = 'alipay'

        try:
            self.device.start_application('com.eg.android.AlipayGphone/.AlipayLogin')
            time.sleep(5)
            cmd = 'am force-stop {0} '.format(
                'com.eg.android.AlipayGphone')
            self.device.shell(cmd)
            time.sleep(1)
            self.device.start_application('com.eg.android.AlipayGphone/.AlipayLogin')
            time.sleep(5)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 5 - 20), (int(self.height / 19 * 18)))
            self.device.shell(cmd)
            time.sleep(1)
            common.screenshots(app_name, '首页')

            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 5 + 20), (int(self.height / 19 * 18)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '财富')

            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 5 * 2 + 20), (int(self.height / 19 * 18)))
            self.device.shell(cmd)
            time.sleep(3)
            common.screenshots(app_name, '口碑')

            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 5 * 3 + 20), (int(self.height / 19 * 18)))
            self.device.shell(cmd)
            time.sleep(1)
            common.screenshots(app_name, '朋友')

            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 5 * 4 + 50), (int(self.height / 19 * 18)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '我的')

            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 10 * 7)))
            self.device.shell(cmd)
            time.sleep(5)
            common.screenshots(app_name, '我的-余额')
            self.assertEqual(1, 1)

        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
