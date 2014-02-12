Ext.define('LMS.view.company.AddPerson', {
        extend: 'Ext.window.Window',
        alias: 'widget.personaddwindow',
        title: 'Add Employee',
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
                        name: 'first_name',
                        fieldLabel: 'First Name'
                    },
                    {
                        xtype: 'textfield',
                        name: 'last_name',
                        fieldLabel: 'Last Name'
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