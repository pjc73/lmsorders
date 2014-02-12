Ext.define('LMS.controller.MenuTree', {
    extend: 'Ext.app.Controller',

    stores: ['MenuTrees'],

    refs: [{
            ref: 'lmsTree',
            selector: 'lmstree'
        }],

    init: function() {
        this.control({
            'lmstree': {
                selectionchange: this.gridSelectionChange
            }
        })
    }
});