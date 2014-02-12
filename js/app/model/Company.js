Ext.define('LMS.model.Company', {
    extend: 'Ext.data.Model',
    store : 'LMS.store.Companies',
    requires: ['LMS.model.Person', 'Ext.data.association.HasMany', 'Ext.data.association.BelongsTo'],

    fields: [   {name:'id',type:'int'},
                {name:'name',type:'string'},
                {name:'code',type:'string'},
                {name:'vat_number',type:'string'},
                {name:'newField',type:'string'},
                {name:'company_types',type:'auto'}],

    hasMany: [{model: 'LMS.model.Person', name: 'persons'},{model: 'LMS.model.Address', name: 'addresses'}],

    proxy: {
        type: 'ajax',
        api: {
            read: '/company',
            update: '/company/update',
            create: '/company/insert'
        },
        reader: {
            type: 'json',
            root: 'Company',
            successProperty: 'success'
        },
        writer: {
            type: 'json',
            writeAllFields:true
        }
    }
});