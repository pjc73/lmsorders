Ext.define('LMS.view.company.Container' ,{
    extend: 'Ext.tab.Panel',
    alias : 'widget.companyContainer',
    requires:['LMS.view.company.DetailsForm','LMS.view.company.PeopleList','LMS.view.company.PersonContainer','LMS.view.company.AddressContainer'],

    title : 'Company Form',
    store: 'Companies',
    activeTab: 0,

    items: [{
        title: 'Details',
        items: { xtype: 'detailsForm'},
        layout: 'fit'
    },{
        title: 'Address',
        items: { xtype: 'addresscontainer'},
        layout: 'fit'
    },{
        title: 'People',
        items: { xtype: 'personContainer'},
        layout: 'fit'
    }]
});

/*

 items: { xtype: 'detailsForm'}

 {
 xtype: 'form',
 items: [{
 xtype: 'textfield',
 fieldLabel: 'Your Email Address',
 afterLabelTextTpl: required,
 vtype: 'email',
 allowBlank: false
 }, {
 xtype: 'textfield',
 fieldLabel: 'Subject',
 afterLabelTextTpl: required,
 allowBlank: false
 }]
 }

    */