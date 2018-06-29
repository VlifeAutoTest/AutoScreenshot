#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Xuxh'


import time
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
try:
    import unittest2 as unittest
except(ImportError):
    import unittest
from lib import common, adbtools
from lib import myuiautomator

from lib import querydb

DEVICE_NAME = querydb.get_uid(sys.argv[2])


class TestBrowser(unittest.TestCase):

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

    def test_clock(self):

        app_name = 'clock'

        try:
            self.device.start_application('com.android.BBKClock/.Timer')
            time.sleep(2)
            cmd = 'am force-stop {0} '.format(
                'com.android.BBKClock')
            self.device.shell(cmd)
            self.device.start_application('com.android.BBKClock/.Timer')
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 4  - 30 ), (int(self.height / 20 * 19)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '闹钟')
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2 - 30), (int(self.height / 20 * 19)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '世界时钟')
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2 + 30), (int(self.height / 20 * 19)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '秒表')
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 4 * 3 + 30), (int(self.height / 20 * 19)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '计时器')
            self.assertEqual(1, 1)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)



