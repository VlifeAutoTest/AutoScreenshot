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


    def test_meituan(self):
        app_name = 'meituan'

        try:
            self.device.start_application('com.sankuai.meituan/com.meituan.android.pt.homepage.activity.MainActivity')
            time.sleep(10)
            cmd = 'am force-stop {0} '.format(
                'com.sankuai.meituan')
            self.device.shell(cmd)
            time.sleep(2)
            self.device.start_application('com.sankuai.meituan/com.meituan.android.pt.homepage.activity.MainActivity')
            time.sleep(10)
            common.screenshots(app_name, '首页')

            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 5 * 4 + 30), (int(self.height / 5 * 2 - 80)))
            self.device.shell(cmd)
            time.sleep(5)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 20 * 17)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '外卖')

            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 5 - 30), (int(self.height / 5 * 2 - 80)))
            self.device.shell(cmd)
            time.sleep(5)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 20 * 19)))
            self.device.shell(cmd)
            time.sleep(5)
            common.screenshots(app_name, '商家')

            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 100 * 36)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '评论')
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
