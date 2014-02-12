Ext.define('LMS.controller.Companies', {
    extend: 'Ext.app.Controller',

    stores: ['Companies','Persons','Address'],

    models: ['Company'],

    views: ['company.Edit', 'company.List' , 'company.Add', 'company.AddPerson','company.AddressAdd'],

    refs: [
        {
            ref: 'detailsForm',
            selector: 'detailsForm'
        },{
            ref: 'companyadd',
            selector: 'form'

        },{
            ref: 'companyAddForm',
            selector: 'companyaddwindow form'
        },{
            ref: 'companyAddWindow',
            selector: 'companyaddwindow',
            autoCreate: true,
            xtype: 'companyaddwindow'
        },
        { ref: 'peopleList',  selector: 'peoplelist'},
        { ref: 'peopleForm',  selector: 'personform'},
        {ref: 'personAddWindow',
            selector: 'personaddwindow',
            autoCreate: true,
            xtype: 'personaddwindow'
        },
        {ref: 'personAddForm',selector: 'personaddwindow form'},
        {ref: 'companyList', selector: 'companylist'},
        {ref: 'addressList', selector: 'addresslist'},
        {ref: 'addressForm',  selector: 'addressform'},
        {ref: 'addressAddWindow' , selector:'addressaddwindow', autoCreate: true, xtype:'addressaddwindow'},
        {ref: 'addressAddForm',selector: 'addressaddwindow form'},
    ],

    init: function() {
            this.control({
                'companylist': {
                    selectionchange: this.gridSelectionChange
                },
                'companylist dataview': {
                    selectionchange: this.gridSelectionChange
                },
                'detailsForm button[action=save]': {
                    click: this.updateCompany
                },
                'companylist > toolbar > button[action=add]': {
                    click: this.onAddCompany
                },
                'companyaddwindow button[action=save]': {
                    click: this.doCreateCompany
                },
                'peoplelist > toolbar > button[action=add]': {
                    click: this.onAddPerson
                },
                'peoplelist ': {
                    selectionchange: this.gridPersonSelectionChange
                },
                'personaddwindow button[action=save]': {
                    click: this.doCreatePerson
                },
                'personform button[action=save] ' : {
                    click: this.updatePerson
                },
                'addresslist ': {
                    selectionchange: this.gridAddressSelectionChange
                },
                'addresslist > toolbar > button[action=add]': {
                    click: this.onAddAddress
                },
                'addressaddwindow button[action=save]': {
                    click: this.doCreateAddress
                },
                'addressform button[action=save] ' : {
                    click: this.updateAddress
                }
            });

    },

    onAddPerson: function (button) {
        this.getPersonAddWindow().show();
    },

    onAddAddress: function (button) {
        this.getAddressAddWindow().show();
    },

    doCreateAddress: function (button) {
        var win = this.getAddressAddWindow(),
            form = this.getAddressAddForm(),
            addressList = this.getAddressList(),
            values = form.getValues(),
            store = this.getAddressStore(),
            listStore = addressList.getStore("Address"),
            companyList =  this.getCompanyList();

        var selection = companyList.getSelectionModel().getSelection()[0];
        var a = new LMS.model.Address(values);
        a.setCompany(selection);

        selection.addressesStore.add(a);
        selection.addressesStore.sync();
        win.close();
    },

    doCreatePerson: function (button) {
        var win = this.getPersonAddWindow(),
            form = this.getPersonAddForm(),
            peopleList = this.getPeopleList(),
            values = form.getValues(),
            store = this.getPersonsStore(),
            listStore = peopleList.getStore("Persons"),
            companyList =  this.getCompanyList();

            var selection = companyList.getSelectionModel().getSelection()[0];
        var p = new LMS.model.Person(values);
        p.setCompany(selection);

        selection.personsStore.add(p);
        selection.personsStore.sync();
        win.close();
    },

    onAddCompany: function () {
        this.getCompanyAddWindow().show();
    },

    doCreateCompany: function (button) {
        var win = this.getCompanyAddWindow(),
            form = this.getCompanyAddForm();
            values = form.getValues(),
            store = this.getCompaniesStore();
            store.add(values);
            win.close();
    },

    gridSelectionChange: function(view, records) {
        var me = this;
        if (records[0]) {
            var rec = records[0];
            var f =  me.getDetailsForm().getForm();
            f.loadRecord(rec);
            var fs =f.findField('ctypes');
            fs.setValue({company_types : rec.get('company_types')});
            var pl = this.getPeopleList();
            pl.reconfigure(rec.personsStore);
            var al = this.getAddressList()
            al.reconfigure(rec.addressesStore);
        }
    },
    gridPersonSelectionChange: function(view, records){
        if (records[0]) {
            var rec = records[0];
            var f  = this.getPeopleForm().getForm();

            f.loadRecord(rec);

            var emails = rec.get('emails');
            var phones = rec.get('phones');

            c = Ext.getCmp('fieldset-contacts');
            c.removeAll();

            for(var i=0;i<emails.length;i++ ){
                var field = new Ext.form.TextField({
                    id: 'email'+emails[i].id,
                    fieldLabel: 'Email  (' + emails[i].type_name +')',
                    name: 'nemail'+emails[i].id,
                    value: emails[i].address
                });
                c.add(field);
            }

/*            debugger;
            Ext.each((phones, function(phone, index) {
                var field = new Ext.form.TextField({
                    id: 'phone'+phones[i].id,
                    fieldLabel: 'Phone  (' + phones[i].type +')',
                    name: 'nphone'+phones[i].id
                });
                c.add(field);
            }));
*/

            for(var i=0;i<phones.length;i++ ){
                var field = new Ext.form.TextField({
                    id: 'phone'+phones[i].id,
                    fieldLabel: 'Phone  (' + phones[i].type_name +')',
                    name: 'nphone'+phones[i].id,
                    value: phones[i].number
                });
                c.add(field);
            }


//            f.doLayout();

            var fs = f.findField('person_roles');
            fs.setValue({roles : rec.get('roles')});

        }
    },
    gridAddressSelectionChange: function(view, records){
    if (records[0]) {
        var rec = records[0];
        var f  = this.getAddressForm().getForm();

        f.loadRecord(rec);
        }
    },


    editCompany: function(grid, record) {
        var edit = Ext.create('LMS.view.company.Edit').show();

        edit.down('form').loadRecord(record);
    },

    updateCompany: function(button) {

        var form = this.getDetailsForm().getForm(),
        record = form.getRecord(),
        values = form.getValues(),
        store = this.getCompaniesStore();
        record.set(values);
    },

    updatePerson: function(button) {

        var form = this.getPeopleForm().getForm(),
            record = form.getRecord(),
            values = form.getValues(),
            store = this.getPersonsStore();

        record.set(values);

        var emails = record.get('emails');
        var phones = record.get('phones');
        var values = form.getValues();

        for(var i=0;i<phones.length;i++ ){
            var val = values['nphone'+phones[i].id];
            phones[i].number = val;
        }

        for(var i=0;i<emails.length;i++ ){
            var val = values['nemail'+emails[i].id];
            emails[i].address = val;
        }

        record.store.sync();
    },
    updateAddress: function(button) {

        var form = this.getAddressForm().getForm(),
            record = form.getRecord(),
            values = form.getValues(),
            store = this.getAddressStore();

        record.set(values);

//        var emails = record.get('emails');
//        var phones = record.get('phones');
        var values = form.getValues();

//        for(var i=0;i<phones.length;i++ ){
//            var val = values['nphone'+phones[i].id];
//            phones[i].number = val;
//        }

//        for(var i=0;i<emails.length;i++ ){
//            var val = values['nemail'+emails[i].id];
//            emails[i].address = val;
//        }

        record.store.sync();
    }



});
