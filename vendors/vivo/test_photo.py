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

DEVICE_NAME = sys.argv[2]


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

    def test_photo(self):

        img_count = 0
        app_name = 'photo'

        try:
            cmd = 'am force-stop {0} '.format(
                'com.vivo.gallery')
            self.device.shell(cmd)
            time.sleep(2)
            cmd = 'am start com.vivo.gallery'
            self.device.shell(cmd)
            time.sleep(3)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 相机照片
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'相机照片'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 相机
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'全部相册'])
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'相机'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 照片
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 5), int(self.height / 5))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            # 分享
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'分享'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 编辑
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'编辑'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 删除
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'删除'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 更多
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'更多'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 详细信息
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'详细信息'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

            self.assertEqual(1, 1)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
