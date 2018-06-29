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


    def test_baidu(self):
        app_name = 'baidu'

        try:
            self.device.start_application('com.baidu.searchbox/.MainActivity')
            time.sleep(10)
            cmd = 'am force-stop {0} '.format(
                'com.baidu.searchbox')
            self.device.shell(cmd)
            time.sleep(1)
            self.device.start_application('com.baidu.searchbox/.MainActivity')
            time.sleep(10)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 100 * 82)))
            self.device.shell(cmd)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'百度'])
            time.sleep(5)
            common.screenshots(app_name, '百度-首页')
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 2)))
            self.device.shell(cmd)
            time.sleep(5)
            common.screenshots(app_name, '新闻')

            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 67), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '评论')
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'未登录'])
            time.sleep(5)
            common.screenshots(app_name, '未登录')

        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
