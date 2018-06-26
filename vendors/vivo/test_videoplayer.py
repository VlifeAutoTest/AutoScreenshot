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


    def test_videoplayer(self):
        img_count = 0
        app_name = 'videoplayer'

        try:
            cmd = 'am force-stop {0} '.format(
                'com.android.VideoPlayer')
            self.device.shell(cmd)
            time.sleep(2)
            self.device.start_application('com.android.VideoPlayer/.VideoPlayer')
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 录制的视频
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'录制的视频'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1

        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)