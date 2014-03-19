##############################################################################
#
# Copyright (C) Zenoss, Inc. 2014, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################


__doc__ = """Wireless Access Point Map
    Pulls in Access Point information from the FortiNet managment server
"""

import logging
log = logging.getLogger('zen.FortiNet')

from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin,
    GetTableMap,
    )

from Products.DataCollector.plugins.DataMaps import (
    RelationshipMap,
    )

from ZenPacks.zenoss.Fortinet.FortiGate.utils import (
    lookup_state,
    lookup_connectionstate,
    )


class wirelessAP(SnmpPlugin):
    snmpGetTableMaps = (
        GetTableMap('fgWcWtpConfig',
            '.1.3.6.1.4.1.12356.101.14.4.3.1', {
                '.1': 'fgWcWtpConfigID',
                '.2': 'fgWcWtpConfigWtpAdmin',  # (1=Discovered, 2=disabled, 3=enabled, 0=other)
                '.3': 'fgWcWtpConfigWtpName',
                '.4': 'fgWcWtpConfigWtpLocation',
                }
            ),

        GetTableMap('fgWcWtpSession',
            '.1.3.6.1.4.1.12356.101.14.4.4.1', {
                '.1': 'fgWcWtpSessionWtpID',
                '.3': 'fgWcWtpSessionWtpIpAddress',
                '.6': 'fgWcWtpSessionWtpBaseMacAddress',
                '.7': 'fgWcWtpSessionConnectionState',  # (1=Offline, 2=Online, 3=DownloadingImage, 4=ConnectedImage, 0=Other)
                '.12': 'fgWcWtpSessionWtpModelNumber',
                '.14': 'fgWcWtpSessionWtpSwVersion',
                }
            ),

        GetTableMap('fgWcWlan',
            '.1.3.6.1.4.1.12356.101.14.3.1', {
                '.1': 'fgWcWlanSsid',
                '.2': 'fgWcWlanBroadcastSsid',
                '.3': 'fgWcWlanSecurity',
                '.4': 'fgWcWlanEncryption',
                '.10': 'fgWcWlanMeshBackhaul',
                }
            ),
        )

    def process(self, device, results, log):
        log.info('Modeler %s processing data for device %s',
            self.name(), device.id)

        getdata, tabledata = results

        wtpconfig = tabledata.get('fgWcWtpConfig', {})
        wtpsession = tabledata.get('fgWcWtpSession', {})
        wlan = tabledata.get('fgWcWlan', {})

        # Access Point Components
        rm_ap = []
        for snmpindex, config_entry in wtpconfig.items():
            ap_session = wtpsession.get(snmpindex)

            name = config_entry.get('fgWcWtpConfigWtpName')

            om = self.objectMap()
            om.modname = "ZenPacks.zenoss.Fortinet.FortiGate.FGAP"
            om.classname = "FGAP"
            om.id = self.prepId(name)
            om.snmpindex = snmpindex.lstrip('.')
            om.description = name
            om.state = lookup_state(config_entry.get('fgWcWtpConfigWtpAdmin'))
            om.connectionstate = lookup_connectionstate(
                    ap_session.get('fgWcWtpSessionConnectionState'))
            om.ipaddress = ap_session.get('fgWcWtpSessionWtpIpAddress')
            om.macaddress = ap_session.get('fgWcWtpSessionWtpBaseMacAddress')
            om.osversion = ap_session.get('fgWcWtpSessionWtpSwVersion')
            om.modelnumber = ap_session.get('fgWcWtpSessionWtpModelNumber')

            rm_ap.append(om)

        # SSID Components
        rm_ssid = []
        for snmpindex, wlan_entry in wlan.items():
            name = wlan_entry.get('fgWcWlanSsid')

            om_ssid = self.objectMap()
            om_ssid.modname = "ZenPacks.zenoss.Fortinet.FortiGate.FGSSID"
            om_ssid.classname = "FGSSID"
            om_ssid.id = self.prepId(name)
            om_ssid.snmpindex = snmpindex.lstrip('.')
            om_ssid.description = name
            om_ssid.statusadmin = wlan_entry.get('fgWcWlanBroadcastSsid')
            om_ssid.trafficmode = wlan_entry.get('fgWcWlanMeshBackhaul')
            om_ssid.securitymode = wlan_entry.get('fgWcWlanSecurity')
            om_ssid.encryption = wlan_entry.get('fgWcWlanEncryption')

            rm_ssid.append(om_ssid)

        maps = []

        maps.append(RelationshipMap(
            compname="os",
            relname="FGAP",
            modname="ZenPacks.zenoss.Fortinet.FortiGate.FGAP",
            objmaps=rm_ap))

        maps.append(RelationshipMap(
            compname="os",
            relname="FGSSID",
            modname="ZenPacks.zenoss.Fortinet.FortiGate.FGSSID",
            objmaps=rm_ssid))

        return maps
