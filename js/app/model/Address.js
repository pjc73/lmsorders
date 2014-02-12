Ext.define('LMS.model.Address', {
    extend: 'Ext.data.Model',
    store : 'LMS.store.Address',
    fields: ['id','name','line1','line2', 'line3','city','region','country','postal_code','company_id'],
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
            update: '/address/update',
            create: '/address/insert'
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