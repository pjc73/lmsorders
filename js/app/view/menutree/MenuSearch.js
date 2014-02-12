Ext.define('LMS.view.menutree.MenuSearch', {
    extend: 'Ext.form.Panel',
    alias: 'widget.menuSearch',
    title: 'Search Form',
    border: 5,
    width: 300,
    layout: {
        type: 'auto'
    },
    items: [{
        xtype: 'datefield',
        name: 'startdate',
        fieldLabel: 'Start Date'
    },{
        xtype: 'datefield',
        name: 'enddate',
        fieldLabel: 'End Date'
    },{
            xtype: 'radiogroup',
            fieldLabel: 'Group Tree By',
            //arrange Radio Buttons into 2 columns
            columns: 2,
            width:275,
            itemId: 'grouptree',
            items: [
                {
                    xtype: 'radiofield',
                    boxLabel: 'CSP',
                    name: 'treetype',
                    checked: true,
                    inputValue: 'csp'
                },
                {
                    xtype: 'radiofield',
                    boxLabel: 'Distributor',
                    name: 'treetype',
                    inputValue: 'dist'
                }
            ]
        }

    ],
    buttons: [
        {
            text: 'Search',
            action: 'search'
        }
    ]}
);