##############################################################################
#
# Copyright (C) Zenoss, Inc. 2014, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from zope.interface import implements
from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.component import ComponentInfo

from ZenPacks.zenoss.Fortinet.FortiGate.interfaces import *


class FGSSIDInfo(ComponentInfo):
    implements(IFGSSIDInfo)

    ssid = ProxyProperty('ssid')
    statusadmin = ProxyProperty('statusadmin')
    trafficmode = ProxyProperty('trafficmode')
    securitymode = ProxyProperty('securitymode')
    encryption = ProxyProperty('encryption')


class FGAPInfo(ComponentInfo):
    implements(IFGAPInfo)

    state = ProxyProperty('state')
    connectionstate = ProxyProperty('connectionstate')
    ipaddress = ProxyProperty('ipaddress')
    macaddress = ProxyProperty('macaddress')
    osversion = ProxyProperty('osversion')
    modelnumber = ProxyProperty('modelnumber')

