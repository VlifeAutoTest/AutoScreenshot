#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Xuxh'

import sys
import argparse
import os
import pytest
import time

from lib import adbtools
from lib import configuration
from lib import common
from lib import querydb

if __name__ == '__main__':

    newParser = argparse.ArgumentParser()
    newParser.add_argument("-s", dest="uid", type=str, help="your device name")
    newParser.add_argument("-v", dest="vendor", type=str, help="mobile vendor")

    args = newParser.parse_args()
    uid = args.uid
    vendor = args.vendor.lower()

    if uid is None or vendor is None:
        sys.exit(0)

    # verify if device is connected
    device_conn = adbtools.AdbTools()
    devices = device_conn.get_devices()
    if uid not in devices:
        print "Device is not connected, please check"
        sys.exit(0)

    # check configuration file and config parameters

    cfg_file = os.path.join('config/', vendor + '.ini')

    if not os.path.isfile(cfg_file):
        print "Corresponding vendor file is not exist, please check"
        sys.exit(0)
    else:
        cfg = configuration.configuration()
        cfg.fileConfig(cfg_file)
        if uid not in cfg.getSections():
            cfg.setValue(uid, 'remote_image_path', '')

    # get all screensshot according to different theme
    count = 0
    for theme in querydb.get_all_themes():

        # 设置theme
        flag = common.set_theme(theme, uid)
        if flag:
            # create image file and set value in cfg file
            base_dir = '/'.join(cfg.getValue(uid, 'remote_image_path').split('/')[0:-1])
            remote_img_path = common.get_remote_path(vendor, uid, theme, base_dir, count)
            cfg.setValue(uid, 'remote_image_path', remote_img_path)

            # run all test files
            test_dir = os.path.abspath(os.path.join('vendors/', vendor))
            test_files = cfg.getValue('COMMON', 'testfiles')
            if test_files == '':
                pytest.main(test_dir)
            else:
                for tf in test_files.split(';'):
                    test_file = os.path.join(test_dir, tf)
                    pytest.main('-q ' + test_file)
        else:
            print 'theme name is not found!!!!!!!!'

        time.sleep(2)
        count += 1