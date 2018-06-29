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


class TestSetting(unittest.TestCase):

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

    def test_setting(self):

        img_count = 0
        app_name = 'setting'

        try:
            cmd = 'am force-stop {0} '.format(
                'com.android.settings')
            self.device.shell(cmd)
            time.sleep(2)
            self.device.start_application('com.android.settings/.Settings')
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            self.assertEqual(1, 1)

            # WLAN
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME,[u'WLAN'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1

            time.sleep(1)
            myuiautomator.click_popup_window(DEVICE_NAME,[u'添加网络'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            myuiautomator.click_popup_window(DEVICE_NAME,[u'取消'])
            time.sleep(2)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

            # 个人热点
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'个人热点'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 密码配置
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'密码配置'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'取消'])
        #     连接管理
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'连接管理'])
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'允许连接数量'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        #     其他共享方式
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'其他共享方式'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
        #     帮助
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'帮助'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        #     移动网络

        # 声音
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'声音'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1

        #     勿扰模式
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'勿扰模式'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 允许打扰
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'允许打扰'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        # 音量键调整
            time.sleep(1)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'音量键调整'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)


        #     来电铃声
        #     time.sleep(2)
        #     myuiautomator.click_popup_window(DEVICE_NAME, [u'来电铃声'])
        #     time.sleep(2)
        #     common.screenshots(app_name, img_count)
        #     img_count += 1
        #     time.sleep(1)
        #     self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        #     信息铃声
        #     time.sleep(2)
        #     myuiautomator.click_popup_window(DEVICE_NAME, [u'信息铃声'])
        #     time.sleep(2)
        #     common.screenshots(app_name, img_count)
        #     img_count += 1
        #     time.sleep(1)
        #     self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        #     通知铃声
            time.sleep(1)
            cmd = 'input swipe {0} {1} {2} {3} 100'.format(
                int(self.width / 2), int(self.height / 30 * 29), int(self.width / 2), int(self.height / 11))
            self.device.shell(cmd)
        #     time.sleep(2)
        #     common.screenshots(app_name, img_count)
        #     img_count += 1
        #     time.sleep(2)
        #     myuiautomator.click_popup_window(DEVICE_NAME, [u'通知铃声'])
        #     time.sleep(2)
        #     common.screenshots(app_name, img_count)
        #     img_count += 1
        #     time.sleep(1)
        #     self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        #     Hi-Fi
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'Hi-Fi'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'关于Hi-Fi'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        #     移动KTV
        #     time.sleep(2)
        #     myuiautomator.click_popup_window(DEVICE_NAME, [u'移动KTV'])
        #     time.sleep(2)
        #     common.screenshots(app_name, img_count)
        #     img_count += 1
        #     time.sleep(1)
        #     self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
        #     time.sleep(1)
        #     self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        # 显示与亮度
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'显示与亮度'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'全局护眼'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        # 壁纸与字体
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'壁纸与字体'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        # 状态栏与通知
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'状态栏与通知'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'顶部预览样式'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        #     系统升级
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'系统升级'])
            time.sleep(20)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        #     账户与同步
            time.sleep(1)
            cmd = 'input swipe {0} {1} {2} {3} 100'.format(
                int(self.width / 2), int(self.height / 2), int(self.width / 2), int(self.height / 10 * 3))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'帐户与同步'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        #     指纹与密码
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'指纹与密码'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'屏幕锁定'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'支付'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)

        #     安全
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'安全'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 访客模式
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'访客模式'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 保护联系人
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'保护联系人'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 隐藏图标
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'隐藏图标'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 访客模式使用说明
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'访客模式使用说明'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 设置SIM卡锁
            # time.sleep(2)
            # myuiautomator.click_popup_window(DEVICE_NAME, [u'设置SIM卡锁'])
            # time.sleep(2)
            # common.screenshots(app_name, img_count)
            # img_count += 1
            # time.sleep(1)
            # self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 设备管理器
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'设备管理器'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 通知使用权
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'通知使用权'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 受信任的凭据
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'受信任的凭据'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 定位服务
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'定位服务'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 运存与存储空间
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'运存与存储空间'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 正在运行程序
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'正在运行程序'])
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 管理已安装程序
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'管理已安装程序'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 管理存储文件
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'管理存储文件'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 更多设置
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'更多设置'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 关于手机
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'关于手机'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # CPU实时数据
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), int(self.height - 100))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            cmd = 'input swipe {0} {1} {2} {3} 100'.format(
                int(self.width / 2), int(self.height / 5 * 3), int(self.width / 2), int(self.height / 4))
            self.device.shell(cmd)
            time.sleep(1)
            common.screenshots(app_name, img_count)
            img_count += 1
            # SIM卡状态
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), int(self.height / 5 * 3))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 法律信息
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), int(self.height - 100))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # vivo法律咨询
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'vivo法律咨询'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 开放源代码许可
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'开放源代码许可'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 全局搜索
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'全局搜索'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 虚拟专用网设置
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'虚拟专用网设置'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 指示灯
            time.sleep(1)
            cmd = 'input swipe {0} {1} {2} {3} 100'.format(
                int(self.width / 2), int(self.height / 2), int(self.width / 2), int(self.height / 10 * 3))
            self.device.shell(cmd)
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'指示灯'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 按键
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'按键'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 日期和时间
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'日期和时间'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 设置时间
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'设置时间'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 设置日期
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'设置日期'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 选择时区
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'选择时区'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 语言
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'语言'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 输入法
            time.sleep(1)
            cmd = 'input swipe {0} {1} {2} {3} 100'.format(
                int(self.width / 2), int(self.height / 2), int(self.width / 2), int(self.height / 4))
            self.device.shell(cmd)
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'输入法'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # vivo输入法
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'vivo输入法'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 定时任务
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'定时任务'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 定时开关机
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'定时开关机'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 应用程序
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'应用程序'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 已安装
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'已安装'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
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
            # 正在运行
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'正在运行'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
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
            # 全部
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'全部'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 出厂应用程序管理
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'出厂应用程序管理'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 恢复出厂设置
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'恢复出厂设置'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 清除所有数据
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'清除所有数据'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 说明书
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'说明书'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'工具'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'计算器'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 售后服务
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'售后服务'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 电子保修卡
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'电子保修卡'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 用户体验改进计划
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'用户体验改进计划'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 有关用户体验改进计划
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'有关用户体验改进计划'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 更新号码归属地
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'更新号码归属地'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 辅助功能
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'辅助功能'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 智能体感
            time.sleep(1)
            cmd = 'input swipe {0} {1} {2} {3} 100'.format(
                int(self.width / 2), int(self.height / 2), int(self.width / 2), int(self.height / 4))
            self.device.shell(cmd)
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'智能体感'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # Smartwake
            time.sleep(1)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), int(self.height / 50 * 9))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 隔空操作
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'隔空操作'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 智能亮屏熄屏
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'智能亮屏熄屏'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 智能通话
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'智能通话'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 多屏互动
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'多屏互动'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 使用说明
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'使用说明'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 分屏多任务
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'分屏多任务'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 消息分屏
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'消息分屏'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 手动分屏
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'手动分屏'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 单手操作
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'单手操作'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 超级截屏
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'超级截屏'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 使用说明
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'使用说明'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 图形截屏
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'图形截屏'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 应用分身
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'应用分身'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            # 应用分身说明
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'应用分身说明'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            # 快捷启动
            time.sleep(2)
            myuiautomator.click_popup_window(DEVICE_NAME, [u'快捷启动'])
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
