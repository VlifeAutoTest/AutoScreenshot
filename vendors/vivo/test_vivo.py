#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Xuxh'


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

    def test_home(self):

        img_count = 0
        app_name = 'home'

        try:
            # screenshot home page
            common.screenshots(app_name, img_count)
            img_count += 1

            # swipe screen for multiple pages of home
            # width, height = self.device.get_screen_normal_size()
            # width = int(width)
            # height = int(height)
            cmd = 'input swipe {0} {1} {2} {3}'.format(
                int(self.width/3*2), (int(self.height/2)), int(self.width/3), (int(self.height/2)))
            self.device.shell(cmd)
            common.screenshots(app_name, img_count)

            self.assertEqual(1, 1)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)

    def test_dial(self):

        img_count = 0
        app_name = 'dial'

        try:
            self.device.start_application('com.android.dialer/.BBKTwelveKeyDialer')
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1

            # swipe screen for all dial
            cmd = 'input swipe {0} {1} {2} {3}'.format(
                int(self.width/2), (int(self.height/2)), int(self.width/2), (int(self.height/2) + 300))
            self.device.shell(cmd)
            common.screenshots(app_name, img_count)
            self.assertEqual(1, 1)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)

    def test_contacts(self):

        img_count = 0
        app_name = 'contacts'

        try:
            self.device.start_application('com.android.contacts/.DialtactsContactsEntryActivity')
            time.sleep(2)
            common.screenshots(app_name, img_count)
            self.assertEqual(1, 1)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)

    def test_notification(self):

        img_count = 0
        app_name = 'notification'

        try:
            cmd = 'input swipe {0} {1} {2} {3}'.format(
                int(self.width/2), 0, int(self.width/2), (int(self.height/2)))
            self.device.shell(cmd)
            common.screenshots(app_name, img_count)
            self.assertEqual(1, 1)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)

    def test_message(self):

        img_count = 0
        app_name = 'message'

        try:
            self.device.start_application('com.android.mms/.ui.ConversationList')
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1

            # check message info
            cmd = 'input tap {0} {1}'.format(int(self.width/2), (int(self.height/5)))
            self.device.shell(cmd)
            common.screenshots(app_name, img_count)
            self.assertEqual(1, 1)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)

    def test_note(self):

        img_count = 0
        app_name = 'note'

        try:
            self.device.start_application('com.android.notes/.Notes')
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1

            # check note list
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            common.screenshots(app_name, img_count)
            self.assertEqual(1, 1)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)

    def test_browser(self):

        img_count = 0
        app_name = 'browser'

        try:
            self.device.start_application('com.vivo.browser/.MainActivity')
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1

            # check baidu web
            myuiautomator.click_element_by_name(DEVICE_NAME, u'搜索或输入网址')
            time.sleep(1)
            self.device.shell('input text baidu.com')
            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_ENTER)
            time.sleep(1)
            common.screenshots(app_name, img_count)
            img_count += 1
            self.assertEqual(1, 1)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)

if __name__ == '__main__':

    pass
