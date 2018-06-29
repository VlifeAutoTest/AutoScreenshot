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

    def test_browser(self):

        img_count = 0
        app_name = 'browser'

        try:
            self.device.start_application('com.vivo.browser/.MainActivity')
            time.sleep(2)
            common.screenshots(app_name, '首页')

            # check baidu web
            myuiautomator.click_element_by_name(DEVICE_NAME, u'搜索或输入网址')
            time.sleep(1)
            self.device.shell('input text baidu.com')
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_ENTER)
            time.sleep(1)
            common.screenshots(app_name, '百度')
            self.assertEqual(1, 1)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)



