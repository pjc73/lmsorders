Ext.define('LMS.store.Address', {
    extend: 'Ext.data.Store',
    model: 'LMS.model.Address',
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