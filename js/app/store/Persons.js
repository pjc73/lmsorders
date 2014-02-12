Ext.define('LMS.store.Persons', {
    extend: 'Ext.data.Store',
    model: 'LMS.model.Person',
    autoSync : true
/*    proxy: {
        type: 'ajax',
        api: {
            update: '/person/update',
            create: '/peron/insert'
        },
        reader: {
            type: 'json',
            root: 'Person',
            successProperty: 'success'
        },
        writer: {
            type: 'json',
            writeAllFields: false
        }
    }
   */
});