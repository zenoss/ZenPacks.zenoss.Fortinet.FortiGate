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

import Globals
import os

from Products.ZenModel.ZenPack import ZenPackBase
from Products.ZenModel.OperatingSystem import OperatingSystem
from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenUtils.Utils import unused

from Products.Zuul.interfaces import ICatalogTool

unused(Globals)

# Modules containing model classes. Used by zenchkschema to validate
# bidirectional integrity of defined relationships.
productNames = (
    'FGSSID',
    'FGAP',
    )

# Useful to avoid making literal string references to module and class names
# throughout the rest of the ZenPack.
MODULE_NAME = {}
CLASS_NAME = {}
for product_name in productNames:
    ZP_NAME = 'ZenPacks.zenoss.Fortinet.FortiGate'
    MODULE_NAME[product_name] = '.'.join([ZP_NAME, product_name])
    CLASS_NAME[product_name] = '.'.join([ZP_NAME, product_name, product_name])


NEW_OS_RELATIONS = (
    ('FGAP', 'FGAP'),
    ('FGSSID', 'FGSSID'),
    )

NEW_COMPONENT_TYPES = (
    'ZenPacks.zenoss.Fortinet.FortiGate.FGAP.FGAP',
    'ZenPacks.zenoss.Fortinet.FortiGate.FGSSID.FGSSID',
    )

for relname, modname in NEW_OS_RELATIONS:
    if relname not in (x[0] for x in OperatingSystem._relations):
        OperatingSystem._relations += (
            (relname, ToManyCont(ToOne,
                '.'.join((ZP_NAME, modname)), 'os')),
        )


class ZenPack(ZenPackBase):
    '''
    ZenPack loader.
    '''

    def install(self, app):
        self.packHome = os.path.dirname(__file__)
        super(ZenPack, self).install(app)

        log.info('Adding Fortinet  relationships to existing devices')
        self._buildOSRelations()

    def remove(self, app, leaveObjects=False):
        if not leaveObjects:
            log.info('Removing Fortinet components')
            cat = ICatalogTool(app.zport.dmd)
            for brain in cat.search(types=NEW_COMPONENT_TYPES):
                component = brain.getObject()
                component.getPrimaryParent()._delObject(component.id)

            # Remove our Device relations additions.
            OperatingSystem._relations = tuple(
                [x for x in OperatingSystem._relations
                    if x[0] not in NEW_OS_RELATIONS])

            log.info('Removing Fortinet device relationships')
            self._buildOSRelations()

        super(ZenPack, self).remove(app, leaveObjects=leaveObjects)

    def _buildOSRelations(self):
        for d in self.dmd.Devices.getSubDevicesGen():
            d.os.buildRelations()
