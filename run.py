#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Xuxh'

import sys
import argparse
import os
import pytest
import time
import json

from lib import adbtools
from lib import configuration
from lib import common
from lib import querydb


def get_test_info(rid):

    run_info = querydb.get_run_info(rid, 'run_info')
    value = json.loads(run_info)
    themes = map(lambda x: querydb.get_theme_name(x), value["themes"])
    files = value["apps"]

    return themes, files


if __name__ == '__main__':

    newParser = argparse.ArgumentParser()
    newParser.add_argument("-s", dest="uid", type=str, help="your device name")
    newParser.add_argument("-v", dest="vendor", type=str, help="mobile vendor")

    args = newParser.parse_args()
    uid = args.uid
    vendor = args.vendor.lower()

    # insert run info to database, get runid, it will be completed in foreground web
    # ********The following line will be delete after web is completed***************
    cur_run_id = querydb.insert_run_info(uid, vendor)
    # **********************


    # verify if device can be used
    device = adbtools.AdbTools()
    devices = device.get_devices()
    mobile_status = querydb.get_mobile_info(vendor, uid, 'status').lower()
    if uid not in devices or mobile_status == 'block':
        print "Device can not be used, please check"
        querydb.update_run_status(cur_run_id, 'Device is not ready', 'Failed')
        sys.exit(0)


    # update mobile table to 'BLOCK'
    mobile_id = querydb.get_run_info(cur_run_id, 'mobile_id')
    querydb.update_mobile_status(mobile_id, 'block')

    # set config file for different mobile
    cfg_file = os.path.join('config/', vendor + '.ini')
    cfg = configuration.configuration()
    cfg.fileConfig(cfg_file)
    if uid not in cfg.getSections():
        cfg.setValue(uid, 'remote_image_path', '')

    try:

        # start testing
        test_file_dir = os.path.abspath(os.path.join('vendors/', vendor))
        remote_img_path = ''
        theme_list, test_files_list = get_test_info(cur_run_id)
        basic_img_path = querydb.get_run_info(cur_run_id, 'image_path')
        for theme in theme_list:

            # 设置theme
            flag = common.set_theme(theme, uid)
            if flag:
                # create image file and set value in cfg file
                remote_img_path = common.get_remote_path(basic_img_path, theme)
                cfg.setValue(uid, 'remote_image_path', remote_img_path)

                if len(test_files_list) > 0:
                    for fi in test_files_list:
                        if isinstance(fi, unicode):
                            fi = fi.encode('gbk')
                        full_path = os.path.join(test_file_dir, fi)
                        if os.path.isfile(full_path):
                            pytest.main('-q ' + full_path)
                        else:
                            print 'test file {0} is not found!!!!!'.format(full_path)
                else:
                    pytest.main(test_file_dir)
            else:
                print 'theme name {0} is not found!!!!!!!!'.format(theme.encode('gbk'))
                device.send_keyevent(adbtools.KeyCode.KEYCODE_HOME)
                time.sleep(2)

            time.sleep(2)
        # zip image files after finishing test.
        common.zip_files(cur_run_id)
        message = 'Test is finished'
        status = 'Success'
    except Exception, ex:
        message = ex
        status = 'Failed'

    # update run info
    querydb.update_run_status(cur_run_id, message, status)

    # update device info
    querydb.update_mobile_status(mobile_id, 'unknown')