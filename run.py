#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Xuxh'


import argparse
import os
import pytest
import time


from lib import adbtools
from lib import configuration
from lib import common
from lib import querydb


def get_test_info(rid):

    resource_list = querydb.get_run_info(rid, "resource").split(",")
    themes = map(lambda x: querydb.get_theme_name(x), resource_list)
    app_list = querydb.get_run_info(rid, "app").split(",")
    files = map(lambda x: querydb.get_app_name(x), app_list)

    return themes, files


if __name__ == '__main__':


    newParser = argparse.ArgumentParser()
    newParser.add_argument("-n", dest="rid", type=str, help="run id")

    args = newParser.parse_args()
    rid = args.rid

    uid = querydb.get_uid(rid)
    vendor = querydb.get_vendor_name(rid).lower().strip()

    # update mobile status from free to busy
    querydb.update_mobile_status(rid, 'busy')

    # create remote path
    basic_img_path = querydb.get_run_info(rid, 'image_path')
    newpath = '/diskb' + basic_img_path
    common.create_remote_path(newpath)


    # set config file for different mobile
    cfg_file = os.path.join('config/', vendor + '.ini')
    cfg = configuration.configuration()
    cfg.fileConfig(cfg_file)
    if uid not in cfg.getSections():
        cfg.setValue(uid, 'remote_image_path', '')

    device = adbtools.AdbTools(uid)

    message = ''
    status = ''

    try:

        # start testing
        test_file_dir = os.path.abspath(os.path.join('vendors/', vendor))
        remote_img_path = ''
        theme_list, test_files_list = get_test_info(rid)
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
                        full_path = os.path.join(test_file_dir, "test_"+fi+".py")
                        if os.path.isfile(full_path):
                            pytest.main('-q ' + full_path)
                        else:
                            print 'test file {0} is not found!!!!!'.format(full_path)
                else:
                    pytest.main(test_file_dir)
            else:
                print 'theme name {0} is not found!!!!!!!!'.format(theme.encode('gbk'))
                device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                time.sleep(2)
                device.send_keyevent(adbtools.KeyCode.KEYCODE_HOME)
                time.sleep(2)

            time.sleep(2)
        # zip image files after finishing test.
        common.zip_files(rid)
        message = 'Test is finished'
        status = 'Success'
    except Exception, ex:
        message = ex
        status = 'Failed'

    # update run info
    querydb.update_run_status(rid, message, status)

    # update device info
    querydb.update_mobile_status(rid, 'free')