Ext.define('LMS.view.Viewport', {
    extend: 'Ext.container.Viewport',

    requires: ['LMS.view.Viewer','LMS.view.MenuViewer'],

    layout: 'border',
    items: [{
        region: 'west',
        width: 500,
        xtype: 'menuviewer'
    }, {
        region: 'center',
        xtype: 'viewer'
    }]
});