#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Xuxh'

import os
import dbmysql
from myglobal import PATH

db = dbmysql.MysqlDB(PATH('../config/common.ini'), 'DATABASE')


def insert_image_to_db(app_name, uid, vendor, file_path):

    try:

        # get mobile id
        query = 'select id  from mobile where vendor="{0}" and uid="{1}"'.format(vendor, uid)
        result = db.select_one_record(query)
        mobile_id = str(result[0]['id'])

        # get app id
        query = 'select id  from application where name="{0}" and mobile_id={1} '.format(app_name, mobile_id)
        result = db.select_one_record(query)
        app_id = str(result[0]['id'])

        # get theme name
        theme_name = os.path.dirname(file_path).split('/')[-1]
        query = 'select id  from theme where themename="{0}"'.format(theme_name)
        result = db.select_one_record(query)
        theme_id = str(result[0]['id'])

        # get date
        date = os.path.dirname(file_path).split('/')[-2][0:8]

        # insert data
        query = "insert into image(update_date, theme_id, mobile_id, app_id, small_image_path, image_path) values('{0}',{1},{2},{3},'{4}','{5}')".\
            format(date, int(theme_id), int(mobile_id), int(app_id), file_path, file_path)
        result = db.execute_insert(query)
    except Exception, ex:
        print ex


def get_all_themes():


    themes = []
    query = 'select themename from theme'
    result = db.select_many_record(query)

    for re in result:

        themes.append(re['themename'])

    return themes


if __name__ == '__main__':

    result = get_all_themes()
    print
    #insert_image_to_db('home', 'db6964a4', 'vivo', '/diskb/picture/vivo/db6964a4/201805211648/theme2/home_0.png')
