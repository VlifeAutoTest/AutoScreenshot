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


    def test_appstore(self):
        img_count = 0
        app_name = 'appstore'

        try:
            cmd = 'am force-stop {0} '.format(
                'com.bbk.appstore')
            self.device.shell(cmd)
            time.sleep(1)
            self.device.start_application('com.bbk.appstore/.ui.AppStoreTabActivity')
            time.sleep(10)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 下载列表
            time.sleep(3)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 20 * 19), (int(self.height / 100 * 7)))
            self.device.shell(cmd)
            time.sleep(1)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 热门
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'热门'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 必备
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'必备'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 新品
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'新品'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 分类
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'分类'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 游戏中心
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'游戏中心'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 游戏中心-推荐-礼包
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 4 - 80), (int(self.height / 25 * 9)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 游戏中心-推荐-礼包-我的礼包
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'我的礼包'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 游戏中心-推荐-专题
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2 - 80), (int(self.height / 25 * 9)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 游戏中心-推荐-精选
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2 + 80), (int(self.height / 25 * 9)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 游戏中心-推荐-社区
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 4 * 3 + 80), (int(self.height / 25 * 9)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 游戏中心-推荐-社区-好友广场
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'好友广场'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 好友信息
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 2)))
            self.device.shell(cmd)
            time.sleep(20)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 排行
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2 - 80), (int(self.height / 21 * 20)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 分类
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2 + 80), (int(self.height / 21 * 20)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 我
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 4 * 3 + 80), (int(self.height / 21 * 20)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 我-设置
            time.sleep(3)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 20), (int(self.height / 100 * 7)))
            self.device.shell(cmd)
            time.sleep(1)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(3)
            cmd = 'input swipe {0} {1} {2} {3} 200'.format(
                int(self.width / 2), int(self.height / 2), int(self.height / 4), int(self.height / 4))
            self.device.shell(cmd)
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'意见反馈'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我-我的论坛
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'我的论坛'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我-V钻.礼券
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'V钻.礼券'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我-消息.好友
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'消息.好友'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 应用
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'应用'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 游戏
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'游戏'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 排行
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'排行'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 管理
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'管理'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 积分可用
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 5), (int(self.height / 25 * 7)))
            self.device.shell(cmd)
            time.sleep(10)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 下载领积分
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 25 * 7)))
            self.device.shell(cmd)
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 下载领积分-查看活动说明
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 4 * 3), (int(self.height / 5 * 4)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 会员中心
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 5 * 4), (int(self.height / 25 * 7)))
            self.device.shell(cmd)
            time.sleep(10)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 应用卸载
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'应用卸载'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 空间清理
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'空间清理'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 帮助
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'帮助'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 应用同步
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'应用同步'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 意见反馈
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'意见反馈'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 设置
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'设置'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
