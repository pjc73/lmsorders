Ext.define('LMS.view.company.AddressList' ,{
    extend: 'Ext.grid.Panel',
    alias : 'widget.addresslist',
    tbar: [{ text: 'New Address', action: 'add', iconCls: 'icon-add'}],
    padding:5,
    columns: [
        {header: 'Name',  dataIndex: 'name',  flex: 1},
        {header: 'Line 1',  dataIndex: 'line1',  flex: 1},
        {header: 'City',  dataIndex: 'city',  flex: 1}

    ]
});
