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


    def test_typewriting(self):
        img_count = 0
        app_name = 'typewriting'

        try:
            time.sleep(1)
            self.device.start_application('com.android.notes/.Notes')
            # 字母
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 95), (int(self.height / 25 * 2)))
            self.device.shell(cmd)
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 37), (int(self.height / 5 * 3)))
            self.device.shell(cmd)
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 50 * 17)))
            self.device.shell(cmd)
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 4 * 3)))
            self.device.shell(cmd)
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 4 * 3)))
            self.device.shell(cmd)
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 4 * 3)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '拼音九键-字母')
            # 数字
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 10 * 9), (int(self.height / 50 * 43)))
            self.device.shell(cmd)
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 4 * 3)))
            self.device.shell(cmd)
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 4 * 3)))
            self.device.shell(cmd)
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 4 * 3)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '拼音九键-数字')
            # 符号
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 10), (int(self.height / 20 * 19)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-最近')
            # 符号中文
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 31), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-中文')
            # 符号英文
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 23), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-英文')
            # 符号表情
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 29), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-表情')
            # 符号网络
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 71), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-网络')
            # 符号序号
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 25 * 21), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-序号')
            # 符号数学
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 99), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 19), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-数学')
            # 符号拼音
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 31), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-拼音')
            # 符号注音
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 23), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-注音')
            # 符号部首
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 29), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-部首')
            # 符号平假
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 71), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-平假')
            # 符号片假
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 25 * 21), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-片假')
            # 符号希腊
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 99), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 23), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-希腊')
            # 符号俄文
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 29), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-俄文')
            # 符号拉丁
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 71), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-拉丁')
            # 符号制表
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 25 * 21), (int(self.height / 100 * 99)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '符号-制表')
            #拼音全键
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 93), (int(self.height / 100 * 62)))
            self.device.shell(cmd)
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 37), (int(self.height / 5 * 3)))
            self.device.shell(cmd)
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 50 * 21)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '拼音全键')
            # 手写半屏
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 37), (int(self.height / 5 * 3)))
            self.device.shell(cmd)
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 100 * 49)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '手写半屏')
            # 手写全屏
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 37), (int(self.height / 5 * 3)))
            self.device.shell(cmd)
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 100 * 56)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '手写全屏')
            # 笔画
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 37), (int(self.height / 5 * 4)))
            self.device.shell(cmd)
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 100 * 62)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '笔画')
            # 英文九键
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 37), (int(self.height / 5 * 3)))
            self.device.shell(cmd)
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 100 * 70)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '英文九键')
            # 英文全键
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 37), (int(self.height / 5 * 3)))
            self.device.shell(cmd)
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 100 * 76)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots('vivo', '英文九键')
            # 切回拼音九键
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 37), (int(self.height / 5 * 3)))
            self.device.shell(cmd)
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 100 * 34)))
            self.device.shell(cmd)


        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)

