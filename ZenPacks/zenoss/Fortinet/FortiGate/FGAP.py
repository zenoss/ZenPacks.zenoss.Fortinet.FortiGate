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


class FGAP(OSComponent, ManagedEntity):
    '''
    Model class for Fortinet Access Points
    '''
    meta_type = portal_type = 'FGAP'

    state = None
    connectionstate = None
    ipaddress = None
    macaddress = None
    osversion = None
    modelnumber = None

    _properties = ManagedEntity._properties + (
        {'id': 'state', 'type': 'string'},
        {'id': 'connectionstate', 'type': 'string'},
        {'id': 'ipaddress', 'type': 'string'},
        {'id': 'macaddress', 'type': 'string'},
        {'id': 'osversion', 'type': 'string'},
        {'id': 'modelnumber', 'type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('os', ToOne(ToManyCont,
                'Products.ZenModel.OperatingSystem.OperatingSystem',
                'FGAP',
                ),
        ),)

    def device(self):
        return self.os().device()

InitializeClass(FGAP)
