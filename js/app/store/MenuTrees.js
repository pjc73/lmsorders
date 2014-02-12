Ext.define('LMS.store.MenuTrees', {
    extend: 'Ext.data.TreeStore',
     root: {expanded: true,children: [
                { text: "Orders", expanded: true, children: [
                        { text: "Spafax", children:[
                            { text: "May", leaf: true },
                            { text: "April", leaf: true}
                            ] },
                            { text: "IFP", children:[
                                 { text: "May", leaf: true },
                                 { text: "April", leaf: true}
                             ] },
                             { text: "Inflight Dublin", children:[
                                 { text: "May", leaf: true },
                                 { text: "April", leaf: true}
                             ] }
                        ] },{ text: "Companies", expanded: true,
             children: [
                 { text: "CSP", leaf: true },
                 { text: "Distributor", leaf: true}]
         }] }

//    proxy:{
//        type: 'ajax',
//        api: {
//            read : '/treedata'
//        },
//        reader: {
//            type: 'json',
//            root: 'root' // Is this correct?
//        }
//    }

//    root: {
//        expanded: true,
//        children: [
//            { text: "Companies", expanded: true, children: [
//                { text: "CSP", leaf: true },
//                { text: "Distributor", leaf: true}
//            ] },
//            { text: "Orders", leaf: true }
//        ]
//    }
});
