Ext.define('LMS.store.Companies', {
    extend: 'Ext.data.Store',
    model: 'LMS.model.Company',
    autoLoad: true,
    autoSync : true
});