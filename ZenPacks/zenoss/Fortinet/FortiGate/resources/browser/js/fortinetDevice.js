(function(){

var ZC = Ext.ns('Zenoss.component');


ZC.FGComponentGridPanel = Ext.extend(ZC.ComponentGridPanel, {
    subComponentGridPanel: false,

    jumpToEntity: function(uid, meta_type) {
        var tree = Ext.getCmp('deviceDetailNav').treepanel;
        var tree_selection_model = tree.getSelectionModel();
        var components_node = tree.getRootNode().findChildBy(
            function(n) {
                if (n.data) {
                    return n.data.text == 'Components';
                }
                
                return n.text == 'Components';
            });
        
        var component_card = Ext.getCmp('component_card');
        
        if (components_node.data) {
            component_card.setContext(components_node.data.id, meta_type);
        } else {
            component_card.setContext(components_node.id, meta_type);
        }

        component_card.selectByToken(uid);
        var component_type_node = components_node.findChildBy(
            function(n) {
                if (n.data) {
                    return n.data.id == meta_type;
                }
                
                return n.id == meta_type;
            });
        
        if (component_type_node.select) {
            tree_selection_model.suspendEvents();
            component_type_node.select();
            tree_selection_model.resumeEvents();
        } else {
            tree_selection_model.select([component_type_node], false, true);
        }
    }
});


ZC.registerName('FGAP', _t('Access Point'), _t('Access Points'));


ZC.FGAPPanel = Ext.extend(ZC.FGComponentGridPanel, {
    subComponentGridPanel: false,

    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            autoExpandColumn: 'name',
            componentType: 'FGAP',
            fields: [
                {name: 'uid'},
                {name: 'meta_type'},
                {name: 'name'},
                {name: 'title'},
                {name: 'state'},
                {name: 'connectionstate'},
                {name: 'ipaddress'},
                {name: 'macaddress'},
                {name: 'osversion'},
                {name: 'modelnumber'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name')
            },{
                id: 'state',
                dataIndex: 'state',
                header: _t('SSID Broadcasting'),
                sortable: true,
                width: 110
            },{
                id: 'connectionstate',
                dataIndex: 'connectionstate',
                header: _t('Connection State'),
                sortable: true,
                width: 110
            },{
                id: 'ipaddress',
                dataIndex: 'ipaddress',
                header: _t('IP Address'),
                sortable: true,
                width: 110
            },{
                id: 'macaddress',
                dataIndex: 'macaddress',
                header: _t('MAC Address'),
                sortable: true,
                width: 110
            },{
                id: 'osversion',
                dataIndex: 'osversion',
                header: _t('OS Version'),
                sortable: true,
                width: 160
            },{
                id: 'modelnumber',
                dataIndex: 'modelnumber',
                header: _t('Model'),
                sortable: true,
                width: 110
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.FGAPPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('FGAPPanel', ZC.FGAPPanel);

ZC.registerName('FGSSID', _t('SSID'), _t('SSIDs'));


ZC.FGSSIDPanel = Ext.extend(ZC.FGComponentGridPanel, {
    subComponentGridPanel: false,

    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            autoExpandColumn: 'name',
            componentType: 'FGSSID',
            fields: [
                {name: 'uid'},
                {name: 'meta_type'},
                {name: 'name'},
                {name: 'title'},
                {name: 'statusadmin'},
                {name: 'securitymode'},
                {name: 'encryption'},
                {name: 'monitor'},
                {name: 'monitored'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name')
            },{
                id: 'statusadmin',
                dataIndex: 'statusadmin',
                header: _t('Admin Status'),
                sortable: true,
                width: 110
            },{
                id: 'securitymode',
                dataIndex: 'securitymode',
                header: _t('Security Mode'),
                sortable: true,
                width: 110
            },{
                id: 'encryption',
                dataIndex: 'encryption',
                header: _t('Encryption'),
                sortable: true,
                width: 110
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 65
            }]
        });
        ZC.FGSSIDPanel.superclass.constructor.call(this, config);
    }
});

Ext.reg('FGSSIDPanel', ZC.FGSSIDPanel);

})();
