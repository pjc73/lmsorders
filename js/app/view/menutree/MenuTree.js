Ext.define('LMS.view.menutree.MenuTree', {
    extend: 'Ext.tree.Panel',
    alias: 'widget.lmsTreeii',
    tbar: [{ text: 'New Order', action: 'add', iconCls: 'icon-add'}],
    title: 'Menu',
    width: 200,
    height: 150,
    store: 'MenuTrees',
    rootVisible: false
});
