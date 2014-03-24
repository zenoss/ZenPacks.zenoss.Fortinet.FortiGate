##############################################################################
#
# Copyright (C) Zenoss, Inc. 2014, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from Globals import InitializeClass

from Products.ZenModel.OSComponent import OSComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class FGSSID(OSComponent, ManagedEntity):
    '''
    Model class for Fortinet Access Points
    '''
    meta_type = portal_type = 'FGSSID'

    ssid = None
    statusadmin = None
    trafficmode = None
    securitymode = None
    encryption = None

    _properties = ManagedEntity._properties + (
        {'id': 'ssid', 'type': 'string'},
        {'id': 'statusadmin', 'type': 'string'},
        {'id': 'securitymode', 'type': 'string'},
        {'id': 'encryption', 'type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('os', ToOne(ToManyCont,
                'Products.ZenModel.OperatingSystem.OperatingSystem',
                'FGSSID',
                ),
        ),)

    def device(self):
        return self.os().device()

InitializeClass(FGSSID)
