#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Xuxh'


import dbmysql
from myglobal import PATH
import datetime


db = dbmysql.MysqlDB(PATH('../config/common.ini'), 'DATABASE')


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
        query = 'update runinfo set status = "{0}",log_path= "{1}" where run_id = {2}'.format(status, message, str(runid))
        db.execute_update(query)
    except Exception, ex:
        print ex


def get_all_themes_info(field):


    themes = []
    query = 'select {0} from theme'.format(field)
    result = db.select_many_record(query)

    for re in result:

        themes.append(re[field])

    return themes


def get_theme_info(theme_id, field):

    ret = ''
    try:
        # get theme name
        query = 'select {0} from theme where id = {1}'.format(field, int(theme_id))
        result = db.select_one_record(query)
        ret = result[0][field]
    except Exception, ex:
        print ex

    return ret


def get_all_application(vendor_id):

    applications = []
    query = 'select name from applications where vendor_id={0}'.format(vendor_id)
    result = db.select_many_record(query)

    for re in result:

        applications.append(re['name'])

    return applications


def get_run_info(runid, field):

    ret = ''
    try:
        # get mobile id
        query = 'select {0}  from runinfo where id = {1}'.format(field, runid)
        result = db.select_one_record(query)
        ret = str(result[0][field])
    except Exception, ex:
        print ex

    return ret


def get_uid(runid):

    mid = get_run_info(runid, 'mid')

    ret = ''
    try:
        # get mobile id
        query = 'select uid from mobile where id = {0}'.format(mid)
        result = db.select_one_record(query)
        ret = str(result[0]["uid"])
    except Exception, ex:
        print ex

    return ret


def get_vendor_name(runid):

    vid = get_run_info(runid, 'vid')

    ret = ''
    try:
        # get mobile id
        query = 'select name from vendor where id = {0}'.format(vid)
        result = db.select_one_record(query)
        ret = str(result[0]["name"])
    except Exception, ex:
        print ex

    return ret


def get_app_name(appid):

    ret = ''
    try:
        # get mobile id
        query = 'select name from application where id = {0}'.format(appid)
        result = db.select_one_record(query)
        ret = str(result[0]["name"])
    except Exception, ex:
        print ex

    return ret


def update_mobile_status(runid, status):

    mid = get_run_info(runid, 'mid')
    sid = get_run_info(runid, 'sid')
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M")

    try:
        query = 'update mobile_status set status = "{0}", last_update = "{1}" where mobile_id = {2} and server_id={3}'.format(status, timestamp, mid, sid)
        db.execute_update(query)
    except Exception, ex:
        print ex


def get_vendor_info(vid, field):

    ret = ''
    try:
        # get theme name
        query = 'select {0} from vendor where id = {1}'.format(field, vid)
        result = db.select_one_record(query)
        ret = result[0][field]
    except Exception, ex:
        print ex

    return ret


if __name__ == '__main__':

    pass