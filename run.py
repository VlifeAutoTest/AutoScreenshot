#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Xuxh'


import argparse
import os
import pytest
import time
import sys
import subprocess
reload(sys)
sys.setdefaultencoding('utf8')
import locale


from lib import adbtools
from lib import configuration
from lib import common
from lib import ssh
from lib import myglobal
from lib import querydb


def get_test_info(rid):
    resource_list = querydb.get_run_info(rid, "resource").split(",")
    themes = map(lambda x: querydb.get_theme_info(x, "themename"), resource_list)
    app_list = querydb.get_run_info(rid, "app").split(",")
    files = map(lambda x: querydb.get_app_name(x), app_list)
    return themes, files, app_list


def run_crawler(local_path, remote_path, cmd, host):
    ret = subprocess.Popen(cmd, shell=True)
    encoding = locale.getdefaultlocale()[1]
    while 1:
        time.sleep(10)
        value = ret.poll()
        if value == 0 or value is None:
            all_files = common.get_all_files_in_local_dir(local_path)
            try:
                for fi in all_files:
                    fi = unicode(fi, encoding)
                    filename = os.path.split(fi)[-1]
                    remote_file = os.path.join(remote_path, filename).replace("\\", "/")
                    if not host.check_path(remote_file) and os.path.splitext(filename)[-1] == ".png":
                        host.upload_file(fi, remote_file)
            except Exception, ex:

                print ex

        if value is None:
            continue
        else:
            break

    common.kill_child_processes(ret.pid)


if __name__ == '__main__':

    newParser = argparse.ArgumentParser()
    newParser.add_argument("-n", dest="rid", type=str, help="run id")



    args = newParser.parse_args()
    rid = args.rid

    # set up host connection
    ip = myglobal.common_config.getValue('IMAGEHOST', 'ip')
    username = myglobal.common_config.getValue('IMAGEHOST', 'username')
    passwd = myglobal.common_config.getValue('IMAGEHOST', 'passwd')
    remote_host = ssh.SSHAction(ip, username, passwd)

    # GET database info
    server_id = querydb.get_run_info(rid, "sid")
    mobile_id = querydb.get_run_info(rid, "mid")
    uid = querydb.get_uid(rid)
    vendor = querydb.get_vendor_name(rid).lower().strip()
    style = querydb.get_run_info(rid, 'style').lower()
    bport = querydb.get_mobile_status_info(mobile_id, server_id, "bport")
    port = querydb.get_mobile_status_info(mobile_id, server_id, "port")

    # update mobile status from free to busy
    querydb.update_mobile_status(rid, 'busy')

    # create remote path
    basic_img_path = querydb.get_run_info(rid, 'image_path')
    remote_filepath = '/diskb' + basic_img_path
    common.create_remote_path(remote_filepath)

    # create logger file and remote log name
    run_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    log_name = querydb.get_run_info(rid, 'log_file')
    remote_log_name = os.path.join(remote_filepath, log_name).replace("\\", "/")
    local_log_name = os.path.join(run_path, "log", log_name).replace("\\", "/")
    logger = common.create_logger(local_log_name)

    # set config file for different mobile
    tmp = os.path.join(run_path, 'config').replace("\\", "/")
    cfg_file = tmp + "/" + vendor + '.ini'
    cfg = configuration.configuration()
    cfg.fileConfig(cfg_file)
    if uid not in cfg.getSections():
        cfg.setValue(uid, 'remote_image_path', '')

    # start testing
    appium = None
    try:

        # initi mobile env
        common.init_device_env(rid)

        jar_path = os.path.join(run_path, "appcrawler-2.1.3.jar")

        # start appium
        if style == "random":

            cmd = "".join(["appium -p ", str(port), " -U ",  uid, " --command-timeout 600"])
            appium = subprocess.Popen(cmd, shell=True)
            time.sleep(3)

        # start testing
        tmp = os.path.join(run_path, 'vendors/').replace("\\", "/")
        test_file_dir = os.path.join(tmp, vendor)
        logger.debug("test_file_dir" + test_file_dir)
        remote_img_path = ''
        theme_list, test_files_list, app_list = get_test_info(rid)

        for theme in theme_list:

            # 设置theme
            logger.debug("set theme")
            flag = common.set_theme(theme, uid, logger)
            if flag:
                for (app_name, app_id) in zip(test_files_list, app_list):
                    # create image file and set value in cfg file
                    remote_img_path = common.get_remote_path(basic_img_path, theme, app_name)
                    cfg.setValue(uid, 'remote_image_path', remote_img_path)
                    package = querydb.get_app_info(app_id, "packagename")
                    activity = querydb.get_app_info(app_id, "activity")
                    # run crawler jar
                    if style == "random":
                        local_path = common. create_path(vendor, uid, "screenshots")
                        java_cmd = "".join(["java -jar ", jar_path, " --capability appPackage=", package,
                                            ",appActivity=", activity, ",udid=",  uid, " -o ", local_path, " -u http://127.0.0.1:" + str(port) + "/wd/hub"])
                        run_crawler(local_path, remote_img_path, java_cmd, remote_host)
                    # run custom ui scripts
                    else:
                        if isinstance(app_name, unicode):
                            app_name = app_name.encode('gbk')
                        full_path = os.path.join(test_file_dir, "test_"+app_name+".py")
                        if os.path.isfile(full_path):
                            pytest.main('-q ' + full_path)
                        else:
                            print 'test file {0} is not found!!!!!'.format(full_path)

            else:
                print 'theme name {0} is not found!!!!!!!!'.format(theme.encode('gbk'))
                device = adbtools.AdbTools(uid)
                device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
                time.sleep(2)
                device.send_keyevent(adbtools.KeyCode.KEYCODE_HOME)
                time.sleep(2)

            time.sleep(2)
        # zip image files after finishing test.
        common.zip_files(rid)
        querydb.update_run_status(rid, "Success")
    except Exception, ex:
        querydb.update_run_status(rid, "Failed")

    # close appium
    if style == "random":
        common.kill_child_processes(appium.pid)

    # copy log file to server

    remote_host.upload_file(local_log_name, remote_log_name)
    remote_host.close()

    # update device info
    querydb.update_mobile_status(rid, 'free')