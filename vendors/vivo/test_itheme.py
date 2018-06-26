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


    def test_itheme(self):
        img_count = 0
        app_name = 'itheme'

        try:
            cmd = 'am force-stop {0} '.format(
                'com.bbk.theme')
            self.device.shell(cmd)
            time.sleep(1)
            self.device.start_application('com.bbk.theme/.Theme')
            time.sleep(30)
            common.screenshots(app_name, img_count)
            img_count += 1

            # 搜索
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 25 * 2)))
            self.device.shell(cmd)
            time.sleep(1)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 活动
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 3), (int(self.height / 25 * 11)))
            self.device.shell(cmd)
            time.sleep(1)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 主题
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'主题'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            # # 主题-排行
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'排行'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 主题详情
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'免费'])
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 3), (int(self.height / 3)))
            self.device.shell(cmd)
            time.sleep(1)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            cmd = 'input swipe {0} {1} {2} {3} 200'.format(
                int(self.width / 2), (int(self.height / 4 * 3)), int(self.width / 2), int(self.height / 4))
            self.device.shell(cmd)
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'评论'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 主题-分类
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'分类'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 主题-壁纸
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'壁纸'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 3), (int(self.height / 3)))
            self.device.shell(cmd)
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 3), (int(self.height / 3)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 字体
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'字体'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 字体-分类
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'分类'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 铃声
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'铃声'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 铃声-分类
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'分类'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'我的'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 我的-消息
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 20), (int(self.height / 25 * 2)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 已购
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'已购'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 已购-已购主题
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'已购主题'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 已购-已购字体
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'已购字体'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 已购-已购锁屏
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'已购锁屏'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 收藏
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'收藏'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 收藏-主题收藏
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'主题收藏'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 收藏-壁纸收藏
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'壁纸收藏'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 收藏-字体收藏
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'字体收藏'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 收藏-锁屏收藏
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'锁屏收藏'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-主题
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'主题'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-壁纸
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'壁纸'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-锁屏
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'锁屏'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-铃声
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'铃声'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-字体
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'字体'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-混搭
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'混搭'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-帮助与反馈
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'帮助与反馈'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-设置
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 97), (int(self.height / 25 * 2)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 设置-左快捷应用
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'左快捷应用'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 设置-右快捷应用
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'右快捷应用'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 设置-联系方式
            time.sleep(2)
            cmd = 'input swipe {0} {1} {2} {3} 200'.format(
                int(self.width / 2), (int(self.height / 4 * 3)), int(self.width / 2), int(self.height / 4))
            self.device.shell(cmd)
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'联系方式'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 设置-用户须知
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'用户须知'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
