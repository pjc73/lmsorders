Ext.define('LMS.model.Person', {
    extend: 'Ext.data.Model',
    store : 'LMS.store.Persons',
    fields: ['id','job_title','salutation', 'first_name','last_name','company_id','emails','phones','roles'],
    belongsTo:[
        {
        name:'company',
        instanceName:'company',
        model:'LMS.model.Company',
        getterName:'getCompany',
        setterName:'setCompany',
        associationKey:'companies',
        foreignKey:'company_id'
        }
    ],
    proxy: {
        type: 'ajax',
        api: {
            update: '/person/update',
            create: '/person/insert'
        },
        reader: {
            type: 'json',
                successProperty: 'success'

        },
        writer: {
            type: 'json',
                writeAllFields: true
        }
        }
});