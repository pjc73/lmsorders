Ext.define('LMS.view.company.PersonContainer' ,{
    extend: 'Ext.panel.Panel',
    alias : 'widget.personContainer',

    requires:['LMS.view.company.PeopleList','LMS.view.company.PersonForm'],

    layout: {
        type: 'hbox',       // Arrange child items vertically
        align: 'stretch',    // Each takes up full width
        padding: 5
    },

    height: '100%',

    items: [{
        flex: 1,
        xtype: 'peoplelist'
    },{
        flex: 2,
        xtype: 'personform'
    }]
});