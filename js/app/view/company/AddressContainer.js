Ext.define('LMS.view.company.AddressContainer' ,{
    extend: 'Ext.panel.Panel',
    alias : 'widget.addresscontainer',

    requires:['LMS.view.company.AddressList','LMS.view.company.AddressForm'],

    layout: {
        type: 'hbox',       // Arrange child items vertically
        align: 'stretch',    // Each takes up full width
        padding: 5
    },

    height: '100%',

    items: [{
        flex: 1,
        xtype: 'addresslist'
    },{
        flex: 2,
        xtype: 'addressform'
    }]
});