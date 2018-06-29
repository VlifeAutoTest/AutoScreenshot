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

    def test_filemanager(self):

        app_name = 'filemanager'

        try:
            self.device.start_application('com.android.filemanager/.FileManagerActivity')
            time.sleep(2)
            cmd = 'am force-stop {0} '.format(
                'com.android.filemanager')
            self.device.shell(cmd)
            time.sleep(5)
            self.device.start_application('com.android.filemanager/.FileManagerActivity')

            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'分类浏览') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'分类浏览'])
                time.sleep(1)
                common.screenshots(app_name, '分类浏览')
            else:
                pass

            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'音乐') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'音乐'])
                time.sleep(1)
                common.screenshots(app_name, '音乐')
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass

            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'文档') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'文档'])
                time.sleep(1)
                common.screenshots(app_name, '文档')
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'手机存储') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'手机存储'])
                time.sleep(1)
                common.screenshots(app_name, '手机存储')

            self.assertEqual(1, 1)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)



