#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Xuxh'

import os
import dbmysql
from myglobal import PATH
import datetime
import json

db = dbmysql.MysqlDB(PATH('../config/common.ini'), 'DATABASE')


def insert_image_to_db(app_name, uid, vendor, file_path):

    try:

        # get mobile id
        mobile_id = get_mobile_info(vendor, uid, 'id')

        # get app id
        query = 'select id  from application where name="{0}" and mobile_id={1} '.format(app_name, mobile_id)
        result = db.select_one_record(query)
        app_id = str(result[0]['id'])

        # get theme name
        theme_name = os.path.dirname(file_path).split('/')[-1]
        query = 'select id from theme where themename="{0}"'.format(theme_name)
        result = db.select_one_record(query)
        theme_id = str(result[0]['id'])

        # get date
        date = os.path.dirname(file_path).split('/')[-2][0:8]

        # handle file path
        file_path = '/' + '/'.join(file_path.split('/')[2:])

        # insert data
        query = "insert into image(update_date, theme_id, mobile_id, app_id, small_image_path, image_path) values('{0}',{1},{2},{3},'{4}','{5}')".\
            format(date, int(theme_id), int(mobile_id), int(app_id), file_path, file_path)
        result = db.execute_insert(query)
    except Exception, ex:
        print ex


def insert_run_info(uid, vendor):

    cur_date = datetime.datetime.now().strftime("%Y%m%d%H%M")
    zip_file = '_'.join([vendor, uid, cur_date]) + '.zip'
    image_path = os.path.join('/picture', vendor, uid, cur_date).replace("\\", '/')
    mobile_id = get_mobile_info(vendor, uid, 'id')

    # set run_info
    run_info = {}
    apps = get_all_application(mobile_id)
    new_apps = map(lambda x: 'test_' + x + '.py', apps)
    run_info["apps"] = new_apps
    run_info["themes"] = get_all_themes_info('id')
    info = json.dumps(run_info)

    try:
        query = "insert into runinfo(run_time, mobile_id, run_info, image_path, log_path, zip_file, status) values('{0}',{1},'{2}','{3}','{4}','{5}','{6}')".\
            format(cur_date, int(mobile_id), info, image_path, image_path, zip_file, 'Active')
        result = db.execute_insert(query)

        # get new id value
        query = 'select MAX(run_id) from runinfo where mobile_id={0} and run_time="{1}"'.format(mobile_id, cur_date)
        result = db.select_one_record(query)
        run_id = result[0]['MAX(run_id)']

    except Exception, ex:
        run_id = 0
        print ex

    return run_id


def get_run_info(runid, field):

    ret = ''
    try:
        # get mobile id
        query = 'select {0}  from runinfo where run_id = {1}'.format(field, runid)
        result = db.select_one_record(query)
        ret = str(result[0][field])
    except Exception, ex:
        print ex

    return ret


def update_run_status(runid, message, status):

    try:
        query = 'update run_info set status = "{0}" , log= "{1}", where run_id = {2}'.format(status, message, str(runid))
        db.execute_update(query)
    except Exception, ex:
        print ex


def update_mobile_status(mid, status):

    try:
        query = 'update mobile set status = "{0}" where id = {1}'.format(status, str(mid))
        db.execute_update(query)
    except Exception, ex:
        print ex


def get_mobile_info(vendor, uid, field):

    ret = ''
    try:
        # get mobile id
        query = 'select {0} from mobile where vendor="{1}" and uid="{2}"'.format(field, vendor, uid)
        result = db.select_one_record(query)
        ret = str(result[0][field])

    except Exception, ex:
        print ex

    return ret


def get_all_themes_info(field):


    themes = []
    query = 'select {0} from theme'.format(field)
    result = db.select_many_record(query)

    for re in result:

        themes.append(re[field])

    return themes


def get_theme_name(theme_id):

    ret = ''
    try:
        # get theme name
        query = 'select themename from theme where id = {0}'.format(int(theme_id))
        result = db.select_one_record(query)
        ret = result[0]['themename']
    except Exception, ex:
        print ex

    return ret


def get_all_application(mobile_id):

    applications = []
    query = 'select name from application where mobile_id={0}'.format(mobile_id)
    result = db.select_many_record(query)

    for re in result:

        applications.append(re['name'])

    return applications



if __name__ == '__main__':

    #result = get_all_themes()
    #insert_image_to_db('home', 'db6964a4', 'vivo', '/diskb/picture/vivo/db6964a4/201805211648/theme2/home_0.png')

    runid = insert_run_info('db6964a4', 'vivo')
    run_info = get_run_info(runid, 'run_info')

    print type(run_info)
    value = json.loads(run_info)
    temp = get_all_themes_info('themename')
    themes = map(lambda x: get_theme_name(x), value["themes"])
    print