Ext.define('LMS.model.CompanyType', {
    extend: 'Ext.data.Model',
    fields: ['id','name'],
    proxy: {
        type: 'ajax',
        api: {
            read: '/company'
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