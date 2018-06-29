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
#
from lib import querydb

DEVICE_NAME = querydb.get_uid(sys.argv[2])
#
#
class TestQq(unittest.TestCase):

    @classmethod
    def setUpClass(self):

        self.device = adbtools.AdbTools(DEVICE_NAME)
        common.unlock_screen(DEVICE_NAME)
        width, height = self.device.get_screen_normal_size()
        self.width = int(width)
        self.height = int(height)

    def setUp(self):


        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_HOME)

    def tearDown(self):

        time.sleep(2)
        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_HOME)
        time.sleep(2)


    def test_qq(self):
        app_name = 'qq'

        try:
            self.device.start_application('com.tencent.mobileqq/.activity.SplashActivity')
            time.sleep(2)
            cmd = 'am force-stop {0} '.format(
                'com.tencent.mobileqq')
            self.device.shell(cmd)
            time.sleep(2)
            self.device.start_application('com.tencent.mobileqq/.activity.SplashActivity')
            time.sleep(2)
            common.screenshots(app_name, '首页')
            time.sleep(2)
            # 腾讯新闻
            time.sleep(3)
            if myuiautomator.in_or_not(DEVICE_NAME, u'服务号') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'服务号'])
                time.sleep(3)
                if myuiautomator.in_or_not(DEVICE_NAME, u'腾讯新闻') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'腾讯新闻'])
                    time.sleep(2)
                    common.screenshots(app_name, '腾讯新闻')
                    time.sleep(2)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 联系人
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'联系人'])
            time.sleep(2)
            common.screenshots(app_name, '联系人')
            # 动态
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'动态'])
            time.sleep(2)
            common.screenshots(app_name, '动态')
            cmd = 'am force-stop {0} '.format(
                'com.tencent.mobileqq')
            self.device.shell(cmd)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)

