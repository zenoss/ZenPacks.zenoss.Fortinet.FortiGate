##############################################################################
#
# Copyright (C) Zenoss, Inc. 2014, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################


import logging
log = logging.getLogger('zen.Fortinet')


def lookup_state(value):
    return {
    0: 'Other',
    1: 'Discovered',
    2: 'Disabled',
    3: 'Enabled',
    }.get(value, 'Other')


def lookup_connectionstate(value):
    return {
    0: 'Other',
    1: 'Offline',
    2: 'Online',
    3: 'Downloading Image',
    4: 'Connected Image',
    }.get(value, 'Other')
