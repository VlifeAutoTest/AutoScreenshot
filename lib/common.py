#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Xuxh'

import datetime
import os
import sys
import time

import adbtools
from myglobal import common_config, vivo_config
import configuration
import ssh
import querydb
import myuiautomator
import logging
import threading


def get_vendor_config(vname):

    pkg = ''
    spath = ''

    if vname == 'vivo':
        pkg = vivo_config.getValue('COMMON', 'app_package')
        spath = vivo_config.getValue('COMMON', 'mobile_resource_path')

    return pkg, spath


def install_app(uid, local_path):

    device = adbtools.AdbTools(uid)

    find_text = [u"好", u"安装", u"允许"]

    try:
        threads = []
        install_app = threading.Thread(target=device.install, args=(local_path,))
        proc_process = threading.Thread(target=myuiautomator.do_popup_windows, args=(15, find_text, uid))
        threads.append(proc_process)
        threads.append(install_app)
        for t in threads:
            t.setDaemon(True)
            t.start()
            time.sleep(2)
        t.join()
    except Exception, ex:
        print ex
        pass


def init_device_env(rid):

    uid = querydb.get_uid(rid)
    vendor = querydb.get_vendor_name(rid).lower().strip()
    device = adbtools.AdbTools(uid)
    run_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    # install theme tool
    app_path = os.path.join(run_path, "app", "ThemeHelper.apk").replace("\\", "/")
    pkg, mobile_path = get_vendor_config(vendor)
    # device.uninstall(pkg)
    # install_app(uid, app_path)

    # pull resource files from server to local
    ip = common_config.getValue('IMAGEHOST', 'ip')
    username = common_config.getValue('IMAGEHOST', 'username')
    passwd = common_config.getValue('IMAGEHOST', 'passwd')
    host = ssh.SSHAction(ip, username, passwd)

    # get local path
    resource_list = querydb.get_run_info(rid, "resource").split(",")
    remote_files = map(lambda x: querydb.get_theme_info(x, "path"), resource_list)
    local_path = os.path.join(run_path, "resources").replace("\\", "/")
    if not os.path.isdir(local_path):
        os.makedirs(local_path)

    # start pull file from server, then push to device
    for rf in remote_files:
        name = os.path.basename(rf)
        local_full_path = os.path.join(local_path, name).replace("\\", "/")
        host.download_file(rf, local_full_path)
        device.push(local_full_path, mobile_path)

    host.close()


def click_apply_button(dname, text, x_point):


    element = myuiautomator.Element(dname)
    event = myuiautomator.Event(dname)
    ele = element.findElementByName(text)
    if ele is not None:
        event.touch(x_point, ele[1])
        time.sleep(2)
        return True

    return False


def create_logger(filename):

    # create multi layer directory
    dirname = os.path.dirname(filename)
    if not os.path.isdir(dirname):
        os.makedirs(dirname)
    logger = logging.getLogger("VlifeTest")
    formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s', '%a, %d %b %Y %H:%M:%S',)
    file_handler = logging.FileHandler(filename)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler(sys.stderr)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)
    logger.setLevel(logging.DEBUG)

    return logger


def set_theme(theme_name, uid, logger):

    start_activity = common_config.getValue('APPLICATION', 'start')
    logger.debug("start_activity:" + start_activity)
    device = adbtools.AdbTools(uid)
    width, height = device.get_screen_normal_size()
    logger.debug(width)
    device.start_application(start_activity)

    time.sleep(1)
    myuiautomator.click_element_by_name(uid, u'字体相关测试')
    time.sleep(2)

    for i in xrange(10):

        flag = click_apply_button(uid, theme_name, int(width)/2)

        if flag:
            time.sleep(2)
            device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            device.send_keyevent(adbtools.KeyCode.KEYCODE_BACK)
            time.sleep(2)
            device.send_keyevent(adbtools.KeyCode.KEYCODE_HOME)
            time.sleep(4)
            return True
        else:
            cmd = 'input swipe {0} {1} {2} {3} 200'.format(int(width)/2, int(height)-300, int(width)/2, int(height)-800)
            device.shell(cmd)
            time.sleep(1)

    return False


def zip_files(rid):

    orig_path = '/diskb' + querydb.get_run_info(rid, 'image_path')
    fre_path = os.path.dirname(orig_path)
    dest_file = os.path.join(fre_path, querydb.get_run_info(rid, 'zip_file')).replace('\\', '/')

    ip = common_config.getValue('IMAGEHOST', 'ip')
    username = common_config.getValue('IMAGEHOST', 'username')
    passwd = common_config.getValue('IMAGEHOST', 'passwd')
    host = ssh.SSHAction(ip, username, passwd)

    try:
        host.zipfiles(dest_file, orig_path)
        # mv file to orig_path
        cmd = 'mv {0} {1}'.format(dest_file, orig_path)
        host.run_ssh_command(cmd)
        host.close()
    except Exception, ex:
        print ex


def get_remote_path(base_dir, theme):

    parent_path = os.path.join('/diskb' + base_dir, theme).replace("\\", '/')

    info = create_remote_path(parent_path)

    if info != "":
        return ""
    else:
        return parent_path


def create_remote_path(newpath):

    error = ""

    ip = common_config.getValue('IMAGEHOST', 'ip')
    username = common_config.getValue('IMAGEHOST', 'username')
    passwd = common_config.getValue('IMAGEHOST', 'passwd')
    host = ssh.SSHAction(ip, username, passwd)

    try:
        host.mkdirs(newpath)
    except Exception, ex:

        error = ex

    host.close()
    return error


def unlock_screen(dname):

    device = adbtools.AdbTools(dname)

    width, height = device.get_screen_normal_size()
    width = int(width)
    height = int(height)

    # make screen off
    if device.get_display_state():
        device.send_keyevent(26)

    # screen_on
    device.send_keyevent(26)

    # unlock screen
    cmd = 'input swipe {0} {1} {2} {3}'.format(int(width/6), (int(height/7*6)), int(width/6*5), (int(height/7*6)), 500)
    device.shell(cmd)


def delete_file(my_file):

    if os.path.exists(my_file):
        os.remove(my_file)
    else:
        print 'no such file:%s' % my_file


def get_image_path(remote_path, prefix, count):

    remote_image_path = remote_path
    local_image_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    fname = prefix + str(count)
    local_file = os.path.join(local_image_path, fname).replace('\\', '/')
    remote_file = os.path.join(remote_image_path, fname).replace('\\', '/')

    return fname, local_file, remote_file


def get_log_path(vendor, dname):

    cur_date = datetime.datetime.now().strftime("%Y%m%d")
    parent_path = os.path.join('log', cur_date, vendor, dname)

    # create multi layer directory
    if not os.path.isdir(parent_path):
        os.makedirs(parent_path)

    return parent_path


def screenshots(app_name, img_count):

        local_image_path = os.path.dirname(os.path.abspath(sys.argv[0]))

        # get remote path
        vendor = querydb.get_vendor_name(sys.argv[2]).lower().strip()
        cfg_file = vendor + '.ini'
        cfg = configuration.configuration()
        cfg.fileConfig(os.path.join(local_image_path, 'config', cfg_file))
        uid = querydb.get_uid(sys.argv[2])
        remote_image_path = cfg.getValue(uid, 'remote_image_path')

        fname = app_name + str(img_count)+'.png'
        local_file = os.path.join(local_image_path, uid+fname).replace('\\', '/')
        remote_file = os.path.join(remote_image_path, fname).replace('\\', '/')

        # screeshot and upload remote host
        device = adbtools.AdbTools(uid)
        device.screenshot(fname, local_file)

        ip = common_config.getValue('IMAGEHOST', 'ip')
        username = common_config.getValue('IMAGEHOST', 'username')
        passwd = common_config.getValue('IMAGEHOST', 'passwd')
        remote_host = ssh.SSHAction(ip, username, passwd)

        remote_host.upload_file(local_file, remote_file)
        remote_host.close()
        # delete local file
        delete_file(local_file)


if __name__ == '__main__':

    pass
