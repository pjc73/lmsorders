Ext.define('LMS.view.company.List' ,{
    extend: 'Ext.grid.Panel',
    alias : 'widget.companylist',

    title : 'All Companies',
    store: 'Companies',
    tbar: [{ text: 'New Company', action: 'add', iconCls: 'icon-add'}],
    columns: [
        {header: 'Name',  dataIndex: 'name',  flex: 1},
        {header: 'Code',  dataIndex: 'code',  flex: 1}
    ]
});
