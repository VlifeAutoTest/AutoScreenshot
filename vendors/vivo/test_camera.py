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


    def test_camera(self):
        app_name = 'camera'

        try:
            self.device.start_application('com.android.camera/.CameraActivity')
            time.sleep(2)
            cmd = 'am force-stop {0} '.format(
                'com.android.camera')
            self.device.shell(cmd)
            time.sleep(5)
            self.device.start_application('com.android.camera/.CameraActivity')
            time.sleep(2)
            common.screenshots(app_name, '相机')
            # 更多
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 25 * 23), int(self.height / 100 * 3))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '更多')
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 类型
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 25 * 23), int(self.height / 50 * 47))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '类型')

        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)