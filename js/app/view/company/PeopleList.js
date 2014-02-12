Ext.define('LMS.view.company.PeopleList' ,{
    extend: 'Ext.grid.Panel',
    alias : 'widget.peoplelist',
    tbar: [{ text: 'New Employee', action: 'add', iconCls: 'icon-add'}],
    padding:5,
    columns: [

        {header: 'job_title',  dataIndex: 'job_title',  flex: 1},
        {header: 'First',  dataIndex: 'first_name',  flex: 1},
        {header: 'Last',  dataIndex: 'last_name',  flex: 1}
    ]
});
