#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Xuxh'

import datetime
import os
import sys
import time

import adbtools
from myglobal import common_config, PATH
import configuration
import ssh
import querydb
import myuiautomator


def click_apply_button(dname, text, x_point):

    element = myuiautomator.Element(dname)
    event = myuiautomator.Event(dname)
    ele = element.findElementByName(text)
    if ele is not None:
        event.touch(x_point, ele[1])
        time.sleep(2)
        return True

    return False


def set_theme(theme_name, uid):

    start_activity = common_config.getValue('APPLICATION','start')
    device = adbtools.AdbTools(uid)
    width, height = device.get_screen_normal_size()
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
        print 'no such file:%s'%my_file


def get_image_path(remote_path, prefix, count):

    remote_image_path = remote_path
    local_image_path = os.path.dirname(os.path.abspath(sys.argv[0]))

    fname = prefix + str(count)
    local_file = os.path.join(local_image_path, fname).replace('\\', '/')
    remote_file = os.path.join(remote_image_path, fname).replace('\\', '/')

    return fname, local_file, remote_file


def get_log_path(vendor, dname):

    cur_date = datetime.datetime.now().strftime("%Y%m%d")
    now = datetime.datetime.now().strftime("%H%M")
    parent_path = os.path.join('log', cur_date, vendor, dname)

    # create multi layer directory
    if not os.path.isdir(parent_path):
        os.makedirs(parent_path)

    return parent_path


def screenshots(app_name, img_count):

        local_image_path = os.path.dirname(os.path.abspath(sys.argv[0]))

        #get remote path
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

    zip_files('/diskb/picture/vivo/db6964a4/201805221455/Aa云想衣裳花想容', 'db6964a4', 'vivo')

    pass
