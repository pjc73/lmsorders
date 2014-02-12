Ext.define('LMS.view.company.PersonForm', {
        extend: 'Ext.form.Panel',
        alias: 'widget.personform',
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
                        name: 'salutation',
                        fieldLabel: 'Salutation'
                    },{
                        xtype: 'textfield',
                        name: 'first_name',
                        fieldLabel: 'First Name'
                    },{
                        xtype: 'textfield',
                        name: 'last_name',
                        fieldLabel: 'Last Name'
                    },{
                        xtype: 'textfield',
                        name: 'job_title',
                        fieldLabel: 'Job Title'
                    },{
                    xtype: 'checkboxgroup',
                    fieldLabel: 'Roles',
                    name:'person_roles',
                    // Arrange radio buttons into two columns, distributed vertically
                    columns: 2,
                    vertical: true,
                    items: [
                            {boxLabel: 'Accounts', name: 'roles', inputValue: 1 },
                            {boxLabel: 'Acquisitions', name: 'roles', inputValue: 2},
                            {boxLabel: 'Licencing', name: 'roles', inputValue: 3},
                            {boxLabel: 'Operations', name: 'roles', inputValue: 4}
                        ]
                    }]
               },{
                    xtype:'fieldset',
                    id:'fieldset-contacts',
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