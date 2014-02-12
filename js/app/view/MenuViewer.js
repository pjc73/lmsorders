/*
Ext.define('LMS.view.MenuViewer', {
    extend: 'Ext.container.Viewport',
    alias: 'widget.menuviewer',

    requires: ['LMS.view.menutree.Menu','LMS.view.menutree.MenuSearch'],

    layout: 'border',
    items: [{
        region: 'north',
        width: 300,
        xtype: 'menuSearch'
    }, {
        region: 'center',
        xtype: 'lmsTree'
    }]
});
*/

Ext.define('LMS.view.MenuViewer', {
    extend: 'Ext.panel.Panel',
    alias: 'widget.menuviewer',

    requires: ['LMS.view.menutree.MenuSearch','LMS.view.menutree.MenuTree'],

    activeItem: 0,
    margins: '5 5 5 5',
    layout: {
        type: 'vbox',       // Arrange child items vertically
        align: 'stretch',    // Each takes up full width
        padding: 5
    },
    items :[{
        xtype: 'menuSearch',
        height:150
    },{
        xtype: 'lmsTreeii',
        flex: 1
    }]
});