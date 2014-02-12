
var menustore = Ext.create('Ext.data.TreeStore', {
    root: {
        expanded: true,
        children: [
            { text: "detention", leaf: true },
            { text: "homework", expanded: true, children: [
                { text: "book report", leaf: true },
                { text: "alegrbra", leaf: true}
            ] },
            { text: "buy lottery tickets", leaf: true }
        ]
    }
});


Ext.define('LMS.view.menutree.Menu', {
    extend: 'Ext.tree.Panel',
    alias: 'widget.lmsTree',
    title: 'Menu',
    width: 200,
    height: 150,
    rootVisible: false
});


/*

{ xtype: 'treepanel',
 title: 'Simple Tree',
 width: 200,
 height: 150,
 store: MenuTree,
 rootVisible: false
 }


 */
