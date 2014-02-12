Ext.define('LMS.view.company.AddressAdd', {
        extend: 'Ext.window.Window',
        alias: 'widget.addressaddwindow',
        title: 'Add Address',
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