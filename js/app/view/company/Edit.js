Ext.define('LMS.view.company.Edit', {
    extend: 'Ext.window.Window',
    alias : 'widget.companyedit',

    requires: ['Ext.form.Panel'],

    title : 'Edit Company',
    layout: 'fit',
    autoShow: true,
    height: 120,
    width: 280,

    initComponent: function() {
        this.items = [
            {
                xtype: 'form',
                padding: '5 5 0 5',
                border: false,
                style: 'background-color: #fff;',

                items: [
                    {
                        xtype: 'textfield',
                        name : 'name',
                        fieldLabel: 'Name'
                    }
                ]
            }
        ];

        this.buttons = [
            {
                text: 'Save',
                action: 'save'
            },
            {
                text: 'Cancel',
                scope: this,
                handler: this.close
            }
        ];

        this.callParent(arguments);
    }
});
