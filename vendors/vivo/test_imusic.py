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
            self.device.start_application('com.android.bbkmusic/.WidgetToTrackActivity')
            time.sleep(2)
            cmd = 'am force-stop {0} '.format(
                'com.android.bbkmusic')
            self.device.shell(cmd)
            time.sleep(5)
            self.device.start_application('com.android.bbkmusic/.WidgetToTrackActivity')
            time.sleep(2)
            common.screenshots(app_name, '首页')
            # 进入更多
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 10), int(self.height / 10))
            self.device.shell(cmd)
            time.sleep(1)
            common.screenshots(app_name, '更多')
            # 在线试听音质
            if myuiautomator.in_or_not(DEVICE_NAME, u'在线试听音质') == True:
                time.sleep(2)
                myuiautomator.click_popup_window(DEVICE_NAME, [u'在线试听音质'])
                time.sleep(2)
                common.screenshots(app_name, '更多-在线试听音质')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 音效设置
            if myuiautomator.in_or_not(DEVICE_NAME, u'音效设置') == True:
                time.sleep(2)
                myuiautomator.click_popup_window(DEVICE_NAME, [u'音效设置'])
                time.sleep(2)
                common.screenshots(app_name, '更多-音效设置')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
                # 主题皮肤
            if myuiautomator.in_or_not(DEVICE_NAME, u'主题皮肤') == True:
                time.sleep(2)
                myuiautomator.click_popup_window(DEVICE_NAME, [u'主题皮肤'])
                time.sleep(5)
                common.screenshots(app_name, '更多-主题皮肤')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
                # test
                # time.sleep(2)
                # if myuiautomator.in_or_not(DEVICE_NAME, u'哈哈哈') == True :
                #         time.sleep(2)
                #         myuiautomator.click_popup_window(DEVICE_NAME, [u'活力橙'])
                #         time.sleep(2)
                #         common.screenshots(app_name, img_count)
                #         img_count += 1
                #         time.sleep(1)
                #         self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                # else:
                #         pass
                # time.sleep(1)
                # self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                # 听歌偏好
            if myuiautomator.in_or_not(DEVICE_NAME, u'听歌偏好') == True:
                time.sleep(2)
                myuiautomator.click_popup_window(DEVICE_NAME, [u'听歌偏好'])
                time.sleep(10)
                common.screenshots(app_name, '更多-听歌偏好')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
                # 导入外部歌单
            if myuiautomator.in_or_not(DEVICE_NAME, u'导入外部歌单') == True:
                time.sleep(2)
                myuiautomator.click_popup_window(DEVICE_NAME, [u'导入外部歌单'])
                time.sleep(2)
                common.screenshots(app_name, '更多-导入外部歌单')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
                # 意见反馈
            if myuiautomator.in_or_not(DEVICE_NAME, u'意见反馈') == True:
                time.sleep(2)
                myuiautomator.click_popup_window(DEVICE_NAME, [u'意见反馈'])
                time.sleep(2)
                common.screenshots(app_name, '更多-意见反馈')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 我的
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 5 * 2), int(self.height / 100 * 7))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '我的')
            # 我的-个人中心
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 37), int(self.height / 50 * 9))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '我的-个人中心')
            # 个人中心-头像
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'头像') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'头像'])
                time.sleep(2)
                common.screenshots(app_name, '我的-个人中心-头像')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 个人中心-昵称
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'昵称') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'昵称'])
                time.sleep(2)
                common.screenshots(app_name, '我的-个人中心-昵称')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 个人中心-性别
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'性别') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'性别'])
                time.sleep(2)
                common.screenshots(app_name, '我的-个人中心-性别')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 个人中心-生日
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'生日') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'生日'])
                time.sleep(2)
                common.screenshots(app_name, '我的-个人中心-生日')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

            # 我的-本地歌曲
            if myuiautomator.in_or_not(DEVICE_NAME, u'本地歌曲') == True:
                time.sleep(2)
                myuiautomator.click_popup_window(DEVICE_NAME, [u'本地歌曲'])
                time.sleep(2)
                common.screenshots(app_name, '我的-本地歌曲-歌曲')
                # 本地歌曲-歌手
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'歌手') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'歌手'])
                    time.sleep(2)
                    common.screenshots(app_name, '我的-本地歌曲-歌手')
                else:
                    pass
                # 本地歌曲-专辑
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'专辑') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'专辑'])
                    time.sleep(2)
                    common.screenshots(app_name, '我的-本地歌曲-专辑')
                else:
                    pass
                # 本地歌曲-文件夹
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'文件夹') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'文件夹'])
                    time.sleep(2)
                    common.screenshots(app_name, '我的-本地歌曲-文件夹')
                else:
                    pass
                time.sleep(2)
                cmd = 'input tap {0} {1}'.format(
                    int(self.width / 100 * 78), int(self.height / 100 * 7))
                # 本地歌曲-搜索
                time.sleep(2)
                cmd = 'input tap {0} {1}'.format(
                    int(self.width / 100 * 78), int(self.height / 100 * 7))
                self.device.shell(cmd)
                time.sleep(2)
                cmd = 'input text abcd'
                self.device.shell(cmd)
                time.sleep(2)
                common.screenshots(app_name, '我的-本地歌曲-搜索')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                # 本地歌曲-更多
                time.sleep(2)
                cmd = 'input tap {0} {1}'.format(
                    int(self.width / 100 * 92), int(self.height / 100 * 95))
                self.device.shell(cmd)
                time.sleep(2)
                common.screenshots(app_name, '我的-播放歌曲列表')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 我的-我的下载
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'我的下载') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'我的下载'])
                time.sleep(2)
                common.screenshots(app_name, '我的-我的下载')
                # 我的下载-正在下载
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'正在下载') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'正在下载'])
                    time.sleep(2)
                    common.screenshots(app_name, '我的下载-正在下载')
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 我的-最近播放
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'最近播放') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'最近播放'])
                time.sleep(2)
                common.screenshots(app_name, '我的-最近播放')
                # 最近播放-下载
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'下载') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'下载'])
                    time.sleep(2)
                    common.screenshots(app_name, '我的-最近播放-下载')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 最近播放-多选
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'多选') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'多选'])
                    time.sleep(2)
                    common.screenshots(app_name, '我的-最近播放-多选')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 我的-我喜欢
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'我喜欢') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'我喜欢'])
                time.sleep(2)
                common.screenshots(app_name, '我的-我喜欢')
                # 我喜欢-专辑
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'专辑') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'专辑'])
                    time.sleep(2)
                    common.screenshots(app_name,  '我的-我喜欢-专辑')
                else:
                    pass
                # 我喜欢-歌单
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'歌单') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'歌单'])
                    time.sleep(2)
                    common.screenshots(app_name, '我的-我喜欢-歌单')
                # 歌单-管理
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'管理') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'管理'])
                        time.sleep(2)
                        common.screenshots(app_name,  '我的-我喜欢-歌单-管理')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
            else:
                pass
            # 我的-已购音乐
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'已购音乐') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'已购音乐'])
                time.sleep(2)
                common.screenshots(app_name, '我的-已购音乐')
                # 已购音乐-单曲
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'单曲') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'单曲'])
                    time.sleep(2)
                    common.screenshots(app_name,  '我的-已购音乐-单曲')
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 我的-免流随心听
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'免流随心听') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'免流随心听'])
                time.sleep(2)
                common.screenshots(app_name, '我的-免流随心听')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 我的-听歌识曲
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'听歌识曲') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'听歌识曲'])
                time.sleep(2)
                common.screenshots(app_name, '我的-听歌识曲')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 我的-新建
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'新建') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'新建'])
                time.sleep(2)
                common.screenshots(app_name, '自建歌曲-新建')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 发现
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 20 * 13), int(self.height / 100 * 7))
            self.device.shell(cmd)
            # 发现-歌单
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'歌单') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'歌单'])
                time.sleep(2)
                common.screenshots(app_name, '发现-歌单')
                # 歌单-全部歌单
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'全部歌单') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'全部歌单'])
                    time.sleep(2)
                    common.screenshots(app_name, '发现-歌单-全部歌单')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 发现-排行
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'排行') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'排行'])
                time.sleep(2)
                common.screenshots(app_name, '发现-排行')
                # 排行-人气榜
                time.sleep(2)
                cmd = 'input tap {0} {1}'.format(
                    int(self.width / 2), int(self.height / 2))
                self.device.shell(cmd)
                time.sleep(2)
                common.screenshots(app_name, '发现-排行-人气榜')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 发现-电台
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'电台') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'电台'])
                time.sleep(2)
                common.screenshots(app_name, '发现-电台')
                # 电台-主题
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'主题') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'主题'])
                    time.sleep(2)
                    common.screenshots(app_name, '发现-电台-主题')
                else:
                    pass
                # 电台-场景
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'场景') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'场景'])
                    time.sleep(2)
                    common.screenshots(app_name, '发现-电台-场景')
                else:
                    pass
                # 电台-语种
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'语种') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'语种'])
                    time.sleep(2)
                    common.screenshots(app_name, '发现-电台-语种')
                else:
                    pass
                # 电台-风格
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'风格') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'风格'])
                    time.sleep(2)
                    common.screenshots(app_name, '发现-电台-风格')
                else:
                    pass
                # 电台-星座
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'星座') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'星座'])
                    time.sleep(2)
                    common.screenshots(app_name, '发现-电台-星座')
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 发现-歌手
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'歌手') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'歌手'])
                time.sleep(5)
                common.screenshots(app_name, '发现-歌手')
            else:
                pass
            # 歌手-我的
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'我的') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'我的'])
                time.sleep(2)
                common.screenshots(app_name, '发现-歌手-我的')
                # 歌手-搜索
                time.sleep(2)
                cmd = 'input tap {0} {1}'.format(
                    int(self.width / 50 * 49), int(self.height / 25 * 2))
                self.device.shell(cmd)
                time.sleep(5)
                common.screenshots(app_name,  '发现-歌手-搜索')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
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
            common.screenshots(app_name, '播放')
            # 播放-更多
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 100 * 81), int(self.height / 100 * 97))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '播放-更多')
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 播放-歌单
            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 200 * 37), int(self.height / 100 * 97))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, '播放-歌单')
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

            time.sleep(1)
            cmd = 'am force-stop {0} '.format(
                'com.android.bbkmusic')
            self.device.shell(cmd)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
