Ext.define('LMS.view.Viewer', {
    extend: 'Ext.panel.Panel',
    alias: 'widget.viewer',

    requires: ['LMS.view.company.Container','LMS.view.company.List','LMS.view.company.DetailsForm'],

    activeItem: 0,
    margins: '5 5 5 5',
    layout: {
        type: 'vbox',       // Arrange child items vertically
        align: 'stretch',    // Each takes up full width
        padding: 5
    },
    items :[{
            xtype: 'companylist',
            flex: 1
        },{
            xtype: 'companyContainer',
            flex: 1
        }]
});