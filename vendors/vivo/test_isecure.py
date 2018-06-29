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


    def test_isecure(self):
        app_name = 'isecure'

        try:
            self.device.start_application('com.iqoo.secure/.MainActivity')
            time.sleep(2)
            cmd = 'am force-stop {0} '.format(
                'com.iqoo.secure')
            self.device.shell(cmd)
            time.sleep(1)
            self.device.start_application('com.iqoo.secure/.MainActivity')
            time.sleep(2)
            common.screenshots(app_name, '首页')

            # 首页-设置
            time.sleep(10)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 20 * 19), (int(self.height / 100 * 7)))
            self.device.shell(cmd)
            time.sleep(1)
            common.screenshots(app_name, '首页-设置')
            # 首页-设置-加速白名单
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'加速白名单') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'加速白名单'])
                time.sleep(1)
                common.screenshots(app_name, '首页-设置-加速白名单')
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 首页-点击体检
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'点击体检') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'点击体检'])
                time.sleep(20)
                common.screenshots(app_name, '首页-点击体检')
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 空间管理
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'空间管理') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'空间管理'])
                time.sleep(5)
                common.screenshots(app_name, '空间管理')
                # 空间管理-设置
                time.sleep(2)
                cmd = 'input tap {0} {1}'.format(
                    int(self.width / 20 * 19), (int(self.height / 100 * 7)))
                self.device.shell(cmd)
                time.sleep(1)
                common.screenshots(app_name, '空间管理-设置')
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 流量监控
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'流量监控') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'流量监控'])
                time.sleep(2)
                common.screenshots(app_name, '流量监控')
                # 流量监控-设置
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'设置') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'设置'])
                    time.sleep(2)
                    common.screenshots(app_name, '流量监控-设置')
                    time.sleep(2)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 软件管理
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'软件管理') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'软件管理'])
                time.sleep(5)
                common.screenshots(app_name, '软件管理')
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 省电管理
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'省电管理') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'省电管理'])
                time.sleep(5)
                common.screenshots(app_name, '省电管理')
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 骚扰拦截
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'骚扰拦截') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'骚扰拦截'])
                time.sleep(5)
                common.screenshots(app_name, '骚扰拦截')
                # 骚扰拦截-设置
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'设置') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'设置'])
                    time.sleep(5)
                    common.screenshots(app_name, '骚扰拦截-设置')
                    time.sleep(2)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 病毒查杀
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'病毒查杀') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'病毒查杀'])
                time.sleep(2)
                common.screenshots(app_name, '病毒查杀')
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 隐私空间
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'隐私空间') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'隐私空间'])
                time.sleep(2)
                common.screenshots(app_name, '隐私空间')
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 查找手机
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'手机寻回') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'手机寻回'])
                time.sleep(2)
                common.screenshots(app_name, '手机寻回')
                # 查找手机-帮助
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'帮助') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'帮助'])
                    time.sleep(2)
                    common.screenshots(app_name, '手机寻回帮助')
                    time.sleep(2)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass

        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
