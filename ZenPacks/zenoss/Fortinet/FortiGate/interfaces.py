##############################################################################
#
# Copyright (C) Zenoss, Inc. 2014, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from Products.Zuul.form import schema
from Products.Zuul.interfaces.component import IComponentInfo

from Products.Zuul.utils import ZuulMessageFactory as _t


class IFGSSIDInfo(IComponentInfo):
    ssid = schema.TextLine(title=_t(u'SSID'), readonly=True)
    statusadmin = schema.TextLine(title=_t(u'Admin Status'), readonly=True)
    trafficmode = schema.TextLine(title=_t(u'Traffic Mode'), readonly=True)
    securitymode = schema.TextLine(title=_t(u'Security Mode'), readonly=True)
    encryption = schema.TextLine(title=_t(u'Encryption'), readonly=True)


class IFGAPInfo(IComponentInfo):
    state = schema.TextLine(title=_t(u'State'), readonly=True)
    connectionstate = schema.TextLine(title=_t(u'Connection State'), readonly=True)
    ipaddress = schema.TextLine(title=_t(u'Connected via IP'), readonly=True)
    macaddress = schema.TextLine(title=_t(u'MAC address'), readonly=True)
    osversion = schema.TextLine(title=_t(u'OS Version'), readonly=True)
    modelnumber = schema.TextLine(title=_t(u'Model Number'), readonly=True)
