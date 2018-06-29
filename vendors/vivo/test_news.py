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


    def test_news(self):
        img_count = 0
        app_name = 'news'

        try:
            self.device.start_application('com.ss.android.article.news/.activity.MainActivity')
            time.sleep(10)
            cmd = 'am force-stop {0} '.format(
                'com.ss.android.article.news')
            self.device.shell(cmd)
            time.sleep(2)
            self.device.start_application('com.ss.android.article.news/.activity.MainActivity')
            time.sleep(10)
            common.screenshots(app_name, img_count)
            img_count += 1

            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 2), (int(self.height / 2)))
            self.device.shell(cmd)
            time.sleep(5)
            common.screenshots(app_name, img_count)
            img_count += 1

            time.sleep(2)
            cmd = 'input tap {0} {1}'.format(
                int(self.width / 5 * 3), (int(self.height / 20 * 19)))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1

            time.sleep(1)
            self.device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            cmd = 'input tap {0} {1} '.format(
                int(self.width / 2 + 50), int(self.height / 20 * 19))
            self.device.shell(cmd)
            time.sleep(2)
            common.screenshots(app_name, img_count)
            img_count += 1

            time.sleep(2)
            cmd = 'input tap {0} {1} '.format(
                int(self.width / 2), int(self.height / 4))
            self.device.shell(cmd)
            time.sleep(2)
            cmd = 'input swipe {0} {1} {2} {3} 100'.format(
                int(self.width / 2), int(self.height / 10 * 9), int(self.width / 2), int(self.height / 10))
            self.device.shell(cmd)
            common.screenshots(app_name, img_count)
            img_count += 1

        except Exception, ex:
            print ex
            self.assertEqual(1, 0, ex)
