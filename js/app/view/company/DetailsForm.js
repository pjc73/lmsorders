
Ext.define('LMS.view.company.DetailsForm', {
    extend: 'Ext.form.Panel',
    alias: 'widget.detailsForm',
    border: 5,

    layout: {
        type: 'auto'
    },
    items: [
                {
                    xtype: 'textfield',
                    name: 'id',
                    fieldLabel: 'Id'
                },
                {
                    xtype: 'textfield',
                    name: 'name',
                    fieldLabel: 'Name'
                },
                {
                    xtype: 'textfield',
                    name: 'code',
                    fieldLabel: 'Code'
                },{
                    xtype: 'textfield',
                    name: 'vat_number',
                    fieldLabel: 'VAT Number'
                },{
                    xtype: 'checkboxgroup',
                    fieldLabel: 'Company Type',
                    name:'ctypes',
                    // Arrange radio buttons into two columns, distributed vertically
                    columns: 2,
                    vertical: true,
                    items: [
                        {boxLabel: 'CSP', name: 'company_types', inputValue: 1 },
                        {boxLabel: 'Distributor', name: 'company_types', inputValue: 2}
                    ]
                }],
    buttons: [
            {
                text: 'Save',
                action: 'save'
            },
            {
                text: 'Cancel',
                scope: this,
                handler: this.close
            }
        ]
        ,
        initComponent: function(){
            this.callParent(arguments);
        }
    }
);