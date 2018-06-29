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

        app_name = 'setting'

        try:
            cmd = 'am force-stop {0} '.format(
                'com.android.settings')
            self.device.shell(cmd)
            time.sleep(2)
            self.device.start_application('com.android.settings/.Settings')
            time.sleep(2)
            common.screenshots(app_name, '设置')
            self.assertEqual(1, 1)

            # WLAN
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'WLAN') == True:
                myuiautomator.click_popup_window(DEVICE_NAME,[u'WLAN'])
                time.sleep(2)
                common.screenshots(app_name, 'WLAN')

                time.sleep(1)
                if myuiautomator.in_or_not(DEVICE_NAME, u'添加网络') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME,[u'添加网络'])
                    time.sleep(2)
                    common.screenshots(app_name, '添加网络')
                    time.sleep(1)
                    myuiautomator.click_popup_window(DEVICE_NAME,[u'取消'])
                else:
                    pass
                time.sleep(2)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass

            # 个人热点
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'个人热点') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'个人热点'])
                time.sleep(2)
                common.screenshots(app_name, '个人热点')
                # 密码配置
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'密码配置') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'密码配置'])
                    time.sleep(2)
                    common.screenshots(app_name, '密码配置')
                    time.sleep(2)
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'取消'])
                else:
                    pass
            #     连接管理
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'连接管理') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'连接管理'])
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'允许连接数量') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'允许连接数量'])
                        time.sleep(2)
                        common.screenshots(app_name, '允许连接数量')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass

            #     其他共享方式
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'其他共享方式') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'其他共享方式'])
                    time.sleep(2)
                    common.screenshots(app_name, '其他共享方式')
                #     帮助
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'帮助') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'帮助'])
                        time.sleep(2)
                        common.screenshots(app_name,  '其他共享方式-帮助')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass


        #     移动网络

        # 声音
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'声音') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'声音'])
                time.sleep(2)
                common.screenshots(app_name, '声音')

            #     勿扰模式
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'勿扰模式') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'勿扰模式'])
                    time.sleep(2)
                    common.screenshots(app_name, '勿扰模式')
                    # 允许打扰
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'允许打扰') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'允许打扰'])
                        time.sleep(2)
                        common.screenshots(app_name, '允许打扰')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass

            # 音量键调整
                time.sleep(1)
                if myuiautomator.in_or_not(DEVICE_NAME, u'音量键调整') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'音量键调整'])
                    time.sleep(2)
                    common.screenshots(app_name, '音量键调整')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass


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
                if myuiautomator.in_or_not(DEVICE_NAME, u'Hi-Fi') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'Hi-Fi'])
                    time.sleep(2)
                    common.screenshots(app_name, 'Hi-Fi')
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'关于Hi-Fi') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'关于Hi-Fi'])
                        time.sleep(2)
                        common.screenshots(app_name, '关于Hi-Fi')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass

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
            if myuiautomator.in_or_not(DEVICE_NAME, u'显示与亮度') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'显示与亮度'])
                time.sleep(2)
                common.screenshots(app_name, '显示与亮度')
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'全局护眼') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'全局护眼'])
                    time.sleep(2)
                    common.screenshots(app_name, '全局护眼')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass

        # 壁纸与字体
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'壁纸与字体') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'壁纸与字体'])
                time.sleep(2)
                common.screenshots(app_name, '壁纸与字体')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass

        # 状态栏与通知
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'状态栏与通知') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'状态栏与通知'])
                time.sleep(2)
                common.screenshots(app_name, '状态栏与通知')
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'顶部预览样式') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'顶部预览样式'])
                    time.sleep(2)
                    common.screenshots(app_name, '顶部预览样式')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass

        #     系统升级
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'系统升级') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'系统升级'])
                time.sleep(20)
                common.screenshots(app_name, '系统升级')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass

        #     账户与同步
            time.sleep(1)
            cmd = 'input swipe {0} {1} {2} {3} 100'.format(
                int(self.width / 2), int(self.height / 2), int(self.width / 2), int(self.height / 10 * 3))
            self.device.shell(cmd)
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'帐户与同步') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'帐户与同步'])
                time.sleep(2)
                common.screenshots(app_name, '帐户与同步')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass

        #     指纹与密码
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'指纹与密码') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'指纹与密码'])
                time.sleep(2)
                common.screenshots(app_name, '指纹与密码')
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'屏幕锁定') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'屏幕锁定'])
                    time.sleep(2)
                    common.screenshots(app_name, '屏幕锁定')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'支付') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'支付'])
                    time.sleep(2)
                    common.screenshots(app_name, '支付')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass

        #     安全
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'安全') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'安全'])
                time.sleep(2)
                common.screenshots(app_name, '安全')
                # 访客模式
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'访客模式') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'访客模式'])
                    time.sleep(2)
                    common.screenshots(app_name, '访客模式')
                    # 保护联系人
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'保护联系人') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'保护联系人'])
                        time.sleep(2)
                        common.screenshots(app_name, '保护联系人')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    # 隐藏图标
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'隐藏图标') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'隐藏图标'])
                        time.sleep(2)
                        common.screenshots(app_name, '隐藏图标')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    # 访客模式使用说明
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'访客模式使用说明') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'访客模式使用说明'])
                        time.sleep(2)
                        common.screenshots(app_name, '访客模式使用说明')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
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
                if myuiautomator.in_or_not(DEVICE_NAME, u'设备管理器') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'设备管理器'])
                    time.sleep(2)
                    common.screenshots(app_name, '设备管理器')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 通知使用权
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'通知使用权') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'通知使用权'])
                    time.sleep(2)
                    common.screenshots(app_name, '通知使用权')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 受信任的凭据
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'受信任的凭据') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'受信任的凭据'])
                    time.sleep(2)
                    common.screenshots(app_name, '受信任的凭据')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 定位服务
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'定位服务') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'定位服务'])
                time.sleep(2)
                common.screenshots(app_name, '定位服务')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 运存与存储空间
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'运存与存储空间') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'运存与存储空间'])
                time.sleep(2)
                common.screenshots(app_name, '运存与存储空间')
                # 正在运行程序
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'正在运行程序') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'正在运行程序'])
                    time.sleep(5)
                    common.screenshots(app_name, '正在运行程序')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 管理已安装程序
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'管理已安装程序') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'管理已安装程序'])
                    time.sleep(2)
                    common.screenshots(app_name, '管理已安装程序')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 管理存储文件
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'管理存储文件') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'管理存储文件'])
                    time.sleep(2)
                    common.screenshots(app_name, '管理存储文件')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 更多设置
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'更多设置') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'更多设置'])
                time.sleep(2)
                common.screenshots(app_name, '更多设置')
                # 关于手机
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'关于手机') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'关于手机'])
                    time.sleep(2)
                    common.screenshots(app_name, '关于手机')
                    # CPU实时数据
                    time.sleep(1)
                    cmd = 'input tap {0} {1}'.format(
                        int(self.width / 2), int(self.height - 100))
                    self.device.shell(cmd)
                    time.sleep(2)
                    common.screenshots(app_name, 'CPU实时数据')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    time.sleep(1)
                    cmd = 'input swipe {0} {1} {2} {3} 100'.format(
                        int(self.width / 2), int(self.height / 5 * 3), int(self.width / 2), int(self.height / 4))
                    self.device.shell(cmd)
                    # SIM卡状态
                    time.sleep(1)
                    cmd = 'input tap {0} {1}'.format(
                        int(self.width / 2), int(self.height / 5 * 3))
                    self.device.shell(cmd)
                    time.sleep(2)
                    common.screenshots(app_name, 'SIM卡状态')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    # 法律信息
                    time.sleep(1)
                    cmd = 'input tap {0} {1}'.format(
                        int(self.width / 2), int(self.height - 100))
                    self.device.shell(cmd)
                    time.sleep(2)
                    common.screenshots(app_name, '法律信息')
                    # vivo法律咨询
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'vivo法律咨询') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'vivo法律咨询'])
                        time.sleep(2)
                        common.screenshots(app_name, 'vivo法律咨询')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    # 开放源代码许可
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'开放源代码许可') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'开放源代码许可'])
                        time.sleep(2)
                        common.screenshots(app_name, '开放源代码许可')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                # 全局搜索
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'全局搜索') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'全局搜索'])
                    time.sleep(2)
                    common.screenshots(app_name, '全局搜索')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 虚拟专用网设置
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'虚拟专用网设置') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'虚拟专用网设置'])
                    time.sleep(2)
                    common.screenshots(app_name, '虚拟专用网设置')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 指示灯
                time.sleep(1)
                cmd = 'input swipe {0} {1} {2} {3} 100'.format(
                    int(self.width / 2), int(self.height / 2), int(self.width / 2), int(self.height / 10 * 3))
                self.device.shell(cmd)
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'指示灯') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'指示灯'])
                    time.sleep(2)
                    common.screenshots(app_name, '指示灯')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 按键
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'按键') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'按键'])
                    time.sleep(2)
                    common.screenshots(app_name, '按键')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 日期和时间
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'日期和时间') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'日期和时间'])
                    time.sleep(2)
                    common.screenshots(app_name, '日期和时间')
                    # 设置时间
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'设置时间') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'设置时间'])
                        time.sleep(2)
                        common.screenshots(app_name, '设置时间')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    # 设置日期
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'设置日期') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'设置日期'])
                        time.sleep(2)
                        common.screenshots(app_name, '设置日期')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    # 选择时区
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'选择时区') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'选择时区'])
                        time.sleep(2)
                        common.screenshots(app_name, '选择时区')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 语言
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'语言') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'语言'])
                    time.sleep(2)
                    common.screenshots(app_name, '语言')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 输入法
                time.sleep(1)
                cmd = 'input swipe {0} {1} {2} {3} 100'.format(
                    int(self.width / 2), int(self.height / 2), int(self.width / 2), int(self.height / 4))
                self.device.shell(cmd)
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'输入法') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'输入法'])
                    time.sleep(2)
                    common.screenshots(app_name, '输入法')
                    # vivo输入法
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'vivo输入法') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'vivo输入法'])
                        time.sleep(2)
                        common.screenshots(app_name, 'vivo输入法')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 定时任务
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'定时任务') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'定时任务'])
                    time.sleep(2)
                    common.screenshots(app_name, '定时任务')
                    # 定时开关机
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'定时开关机') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'定时开关机'])
                        time.sleep(2)
                        common.screenshots(app_name, '定时开关机')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 应用程序
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'应用程序') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'应用程序'])
                    time.sleep(2)
                    common.screenshots(app_name, '应用程序')
                    # 已安装
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'已安装') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'已安装'])
                        time.sleep(2)
                        common.screenshots(app_name, '已安装')
                        cmd = 'input tap {0} {1}'.format(
                            int(self.width / 2), int(self.height / 2))
                        self.device.shell(cmd)
                        time.sleep(2)
                        common.screenshots(app_name, 'APP')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    # 正在运行
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'正在运行') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'正在运行'])
                        time.sleep(2)
                        common.screenshots(app_name, '正在运行')
                        cmd = 'input tap {0} {1}'.format(
                            int(self.width / 2), int(self.height / 2))
                        self.device.shell(cmd)
                        time.sleep(2)
                        common.screenshots(app_name, '正在运行-app')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    # 全部
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'全部') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'全部'])
                        time.sleep(2)
                        common.screenshots(app_name, '全部')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    # 出厂应用程序管理
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'出厂应用程序管理') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'出厂应用程序管理'])
                        time.sleep(2)
                        common.screenshots(app_name, '出厂应用程序管理')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 恢复出厂设置
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'恢复出厂设置') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'恢复出厂设置'])
                    time.sleep(2)
                    common.screenshots(app_name, '恢复出厂设置')
                    # 清除所有数据
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'清除所有数据') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'清除所有数据'])
                        time.sleep(2)
                        common.screenshots(app_name, '清除所有数据')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 说明书
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'说明书') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'说明书'])
                    time.sleep(2)
                    common.screenshots(app_name, '说明书')
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'工具') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'工具'])
                        time.sleep(2)
                        common.screenshots(app_name, '工具')
                        time.sleep(2)
                        if myuiautomator.in_or_not(DEVICE_NAME, u'计算器') == True:
                            myuiautomator.click_popup_window(DEVICE_NAME, [u'计算器'])
                            time.sleep(2)
                            common.screenshots(app_name, '计算器')
                            time.sleep(1)
                            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                        else:
                            pass
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                        time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 售后服务
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'售后服务') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'售后服务'])
                    time.sleep(2)
                    common.screenshots(app_name, '售后服务')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 电子保修卡
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'电子保修卡') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'电子保修卡'])
                    time.sleep(2)
                    common.screenshots(app_name, '电子保修卡')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 用户体验改进计划
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'用户体验改进计划') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'用户体验改进计划'])
                    time.sleep(2)
                    common.screenshots(app_name, '用户体验改进计划')
                    # 有关用户体验改进计划
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'有关用户体验改进计划') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'有关用户体验改进计划'])
                        time.sleep(2)
                        common.screenshots(app_name, '有关用户体验改进计划')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 更新号码归属地
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'更新号码归属地') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'更新号码归属地'])
                    time.sleep(2)
                    common.screenshots(app_name, '更新号码归属地')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 辅助功能
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'辅助功能') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'辅助功能'])
                    time.sleep(2)
                    common.screenshots(app_name, '辅助功能')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 智能体感
            time.sleep(1)
            cmd = 'input swipe {0} {1} {2} {3} 100'.format(
                int(self.width / 2), int(self.height / 2), int(self.width / 2), int(self.height / 4))
            self.device.shell(cmd)
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'智能体感') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'智能体感'])
                time.sleep(2)
                common.screenshots(app_name, '智能体感')
                # Smartwake
                time.sleep(1)
                cmd = 'input tap {0} {1}'.format(
                    int(self.width / 2), int(self.height / 50 * 9))
                self.device.shell(cmd)
                time.sleep(2)
                common.screenshots(app_name, 'Smartwake')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                # 隔空操作
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'隔空操作') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'隔空操作'])
                    time.sleep(2)
                    common.screenshots(app_name, '隔空操作')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 智能亮屏熄屏
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'智能亮屏熄屏') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'智能亮屏熄屏'])
                    time.sleep(2)
                    common.screenshots(app_name, '智能亮屏熄屏')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 智能通话
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'智能通话') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'智能通话'])
                    time.sleep(2)
                    common.screenshots(app_name, '智能通话')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 多屏互动
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'多屏互动') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'多屏互动'])
                time.sleep(2)
                common.screenshots(app_name, '多屏互动')
                # 使用说明
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'使用说明') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'使用说明'])
                    time.sleep(2)
                    common.screenshots(app_name, '使用说明')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 分屏多任务
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'分屏多任务') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'分屏多任务'])
                time.sleep(2)
                common.screenshots(app_name, '分屏多任务')
                # 消息分屏
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'消息分屏') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'消息分屏'])
                    time.sleep(2)
                    common.screenshots(app_name, '消息分屏')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                # 手动分屏
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'手动分屏') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'手动分屏'])
                    time.sleep(2)
                    common.screenshots(app_name, '手动分屏')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 单手操作
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'单手操作') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'单手操作'])
                time.sleep(2)
                common.screenshots(app_name, '单手操作')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 超级截屏
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'超级截屏') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'超级截屏'])
                time.sleep(2)
                common.screenshots(app_name, '超级截屏')
                # 使用说明
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'使用说明') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'使用说明'])
                    time.sleep(2)
                    common.screenshots(app_name, '使用说明')
                    # 图形截屏
                    time.sleep(2)
                    if myuiautomator.in_or_not(DEVICE_NAME, u'图形截屏') == True:
                        myuiautomator.click_popup_window(DEVICE_NAME, [u'图形截屏'])
                        time.sleep(2)
                        common.screenshots(app_name, '图形截屏')
                        time.sleep(1)
                        self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                    else:
                        pass
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 应用分身
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'应用分身') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'应用分身'])
                time.sleep(2)
                common.screenshots(app_name, '应用分身')
                # 应用分身说明
                time.sleep(2)
                if myuiautomator.in_or_not(DEVICE_NAME, u'应用分身说明') == True:
                    myuiautomator.click_popup_window(DEVICE_NAME, [u'应用分身说明'])
                    time.sleep(2)
                    common.screenshots(app_name, '应用分身说明')
                    time.sleep(1)
                    self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                else:
                    pass
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
            # 快捷启动
            time.sleep(2)
            if myuiautomator.in_or_not(DEVICE_NAME, u'快捷启动') == True:
                myuiautomator.click_popup_window(DEVICE_NAME, [u'快捷启动'])
                time.sleep(2)
                common.screenshots(app_name, '快捷启动')
                time.sleep(1)
                self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            else:
                pass
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
