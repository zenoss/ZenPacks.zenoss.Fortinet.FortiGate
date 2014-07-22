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


def lookup_ssid_broadcast(value):
    return {
    1: 'Disabled',
    2: 'Enabled'
    }.get(value, 'Other')


def lookup_ssid_security(value):
    return {
    0: 'Other',
    1: 'Open',
    2: 'Captive Portal',
    3: 'WEP 64',
    4: 'WEB 128',
    5: 'WPA Only Personal',
    6: 'WPA Only Enterprise',
    7: 'WPA2 Personal',
    8: 'WPA2 Enterprise',
    9: 'WPA Personal',
    10: 'WPA Enterprise',
    }.get(value, 'Other')


def lookup_ssid_encryption(value):
    return {
    0: 'Other',
    1: 'None',
    2: 'TKIP',
    3: 'AES',
    4: 'TKIP AES',
    }.get(value, 'Other')
