Ext.define('LMS.view.company.Add', {
    extend: 'Ext.window.Window',
    alias: 'widget.companyaddwindow',
    title: 'Add Company',
//    layout: 'fit',
    height: 150,
    autoShow: true,
    items: [
        {
            xtype: 'form',
            bodyStyle: 'padding: 10px;',
            items: [
                    {
                        xtype: 'textfield',
                        name: 'name',
                        fieldLabel: 'Name'
                    },
                    {
                        xtype: 'textfield',
                        name: 'code',
                        fieldLabel: 'Code'
                    },
                    {
                        xtype: 'textfield',
                        name: 'vat_number',
                        fieldLabel: 'vat_number'
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
                }]
        }]
    }
);