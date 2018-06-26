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


    def test_imusic(self):
        img_count = 0
        app_name = 'imusic'

        try:
            cmd = 'am force-stop {0} '.format(
                'com.android.bbkmusic')
            self.device.shell(cmd)
            time.sleep(5)
            self.device.start_application('com.android.bbkmusic/.WidgetToTrackActivity')
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 进入更多
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 10), int(self.height / 10))
            self.device.shell(cmd)
            time.sleep(1)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 在线试听音质
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'在线试听音质'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 音效设置
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'音效设置'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 主题皮肤
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'主题皮肤'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 听歌偏好
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'听歌偏好'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 导入外部歌单
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'导入外部歌单'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 意见反馈
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'意见反馈'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 5 * 2), int(self.height / 100 * 7))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 我的-个人中心
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 37), int(self.height / 50 * 9))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 个人中心-头像
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'头像'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 个人中心-昵称
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'昵称'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 个人中心-性别
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'性别'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 个人中心-生日
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'生日'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-本地歌曲
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'本地歌曲'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 本地歌曲-歌手
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'歌手'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 本地歌曲-专辑
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'专辑'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 本地歌曲-文件夹
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'文件夹'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 本地歌曲-搜索
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 78), int(self.height / 100 * 7))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            cmd = 'input text abcd'
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 本地歌曲-更多
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 78), int(self.height / 100 * 92))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-我的下载
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'我的下载'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 我的下载-正在下载
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'正在下载'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-最近播放
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'最近播放'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 最近播放-下载
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'下载'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 最近播放-多选
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'多选'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-我喜欢
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'我喜欢'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 我喜欢-专辑
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'专辑'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 我喜欢-歌单
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'歌单'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 歌单-管理
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'管理'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-已购音乐
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'已购音乐'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 已购音乐-单曲
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'单曲'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-免流随心听
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'免流随心听'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-听歌识曲
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'听歌识曲'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的-新建
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'新建'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 发现
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 20 * 13), int(self.height / 100 * 7))
            self.device.shell(cmd)
            # 发现-歌单
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'歌单'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 歌单-全部歌单
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'全部歌单'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 发现-排行
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'排行'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 排行-人气榜
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), int(self.height / 2))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 发现-电台
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'电台'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 电台-主题
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'主题'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 电台-场景
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'场景'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 电台-语种
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'语种'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 电台-风格
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'风格'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 电台-星座
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'星座'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 发现-歌手
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'歌手'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 歌手-我的
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'我的'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 歌手-搜索
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 50 * 49), int(self.height / 25 * 2))
            self.device.shell(cmd)
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 播放
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), int(self.height / 100 * 97))
            self.device.shell(cmd)
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), int(self.height / 3))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 播放-更多
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 81), int(self.height / 100 * 97))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 播放-歌单
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 200 * 37), int(self.height / 100 * 97))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

            time.sleep(1)
            cmd = 'am force-stop {0} '.format(
                'com.android.bbkmusic')
            self.device.shell(cmd)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
