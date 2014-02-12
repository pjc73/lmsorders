Ext.define('LMS.view.company.AddressForm', {
        extend: 'Ext.form.Panel',
        alias: 'widget.addressform',
        padding:5,
        border:5,
        layout: 'column',
        items: [{
            xtype:'fieldset',
            columnWidth: 0.5,
            title: 'Personal',

            items:[
                {
                    xtype: 'textfield',
                    name: 'id',
                    fieldLabel: 'Id'
                },{
                    xtype: 'textfield',
                    name: 'name',
                    fieldLabel: 'Name'
                },{
                    xtype: 'textfield',
                    name: 'line1',
                    fieldLabel: 'Line 1'
                },{
                    xtype: 'textfield',
                    name: 'line2',
                    fieldLabel: 'Line 2'
                },{
                    xtype: 'textfield',
                    name: 'line3',
                    fieldLabel: 'Line 3'
                },{
                    xtype: 'textfield',
                    name: 'city',
                    fieldLabel: 'City'
                },{
                    xtype: 'textfield',
                    name: 'region',
                    fieldLabel: 'Region'
                },{
                    xtype: 'textfield',
                    name: 'country',
                    fieldLabel: 'Country'
                },{
                    xtype: 'textfield',
                    name: 'postal_code',
                    fieldLabel: 'Postal Code'
                }]
        },{
            xtype:'fieldset',
            id:'fieldset-address-contacts',
            columnWidth: 0.5,
            title: 'Contact',

            items:[ ]
        }



        ],
        buttons: [
            {
                text: 'Save',
                action: 'save'
            },
            {
                text: 'Cancel',
                action : 'cancel'
            }
        ]}
);