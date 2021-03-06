#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Xuxh'


import sys
import time
from lib import querydb
try:
    import unittest2 as unittest
except(ImportError):
    import unittest
from lib import common, adbtools

DEVICE_NAME = querydb.get_uid(sys.argv[2])


class TestContacts(unittest.TestCase):

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

    def test_contacts(self):

        app_name = 'contacts'

        try:
            self.device.start_application('com.android.contacts/.DialtactsContactsEntryActivity')
            time.sleep(2)
            cmd = 'am force-stop {0} '.format(
                'com.android.contacts')
            self.device.shell(cmd)
            time.sleep(5)
            self.device.start_application('com.android.contacts/.DialtactsContactsEntryActivity')
            time.sleep(2)
            common.screenshots(app_name, '联系人')
            self.assertEqual(1, 1)
        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)





