#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'Xuxh'


import os

from lib import configuration
import ssh


__all__ = ['common_config', 'vivo_config', 'remote_host']

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

# common configuration file
common_config = configuration.configuration()
fname = PATH('../config/common.ini')
common_config.fileConfig(fname)

# vivo configuration file
vivo_config = configuration.configuration()
fname = PATH('../config/vivo.ini')
vivo_config.fileConfig(fname)


