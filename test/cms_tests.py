import unittest
import logging
from lms.bll.cms_factory import CompanyFactory, PersonFactory , AddressFactory , PhoneFactory , EmailFactory
from lms.bll.cms import Company,Person, Address , Phone, Email, PhoneType, EmailType , CompanyType , PersonRole

class CompanyTest(unittest.TestCase):

    def test_companyFactory(self):

        #insert new company and get id
        c = Company()
        c.name = "PJC"
        c.vat_number = "qwe"
        c.code = "PJC"
        cs = CompanyFactory().Insert([c])
        self.assertEqual(1,len(cs))
        self.assertEqual("PJC",cs[0].name)

        #get new compnay object from id just inserted and check name
        id =cs[0].id
        cs_ii = CompanyFactory().Get([id])
        self.assertEqual(1,len(cs_ii))
        self.assertEqual("PJC",cs_ii[0].name)

        self.assertTrue(True)

    def test_companyFactory_update(self):

        #insert new company and get id
        c = Company()
        c.name = "PJC"
        c.vat_number = "qwe"
        c.code = "PJC"
        cs = CompanyFactory().Insert([c])
        self.assertEqual(1,len(cs))
        self.assertEqual("PJC",cs[0].name)

        #update new company and get

        cs[0].name = "PJC UPDATE"
        id =cs[0].id
        CompanyFactory().Update([cs[0]])

        #check for updates name
        ucs = CompanyFactory().Get([id])
        self.assertEqual("PJC UPDATE",ucs[0].name)

    def test_personFactory_getall(self):
        ads = CompanyFactory().get_all()
        count = CompanyFactory().count_addresses()
        self.assertEqual(len(ads) , count)

    def test_addPerson(self):
        c = Company()
        c.name = "Person Test"
        c.vat_number = "pt123"
        c.code = "PT1"

        cs = CompanyFactory().Insert([c])

        p = Person()
        p.first_name = "Brad"
        p.last_name = "Wiggens"
        p.salutation = "Mr"
        p.job_title = "Racer"

        ps = PersonFactory().Insert([p])

        upc = CompanyFactory().AddPerson(cs[0],ps[0])

        self.assertEqual(len(upc[0].persons) , 1)

    def test_addAddress(self):
        c = Company()
        c.name = "Person Test"
        c.vat_number = "pt123"
        c.code = "PT1"

        cs = CompanyFactory().Insert([c])

        a = Address()
        a.name = "London"
        a.line1 = "1 The Road"
        a.city = "London"
        a.postal_code = "AZ1 1AZ"

        ps = AddressFactory().insert([a])

        upc = CompanyFactory().add_address(cs[0],ps[0])

        self.assertEqual(len(upc[0].addresses) , 1)

    def test_addtype(self):
        c = Company()
        c.name = "Company Type Test"
        c.vat_number = "pt123"
        c.code = "PT1"
        c.company_types = [CompanyType.Distributor,CompanyType.CSP]
        cs = CompanyFactory().Insert([c])
        self.assertEqual(len(cs[0].company_types) , 2)


    def test_addtype_update(self):
        c = Company()
        c.name = "Company Update Type Test"
        c.vat_number = "pt123"
        c.code = "PT1"
        c.company_types = [CompanyType.Distributor,CompanyType.CSP]
        cs = CompanyFactory().Insert([c])
        self.assertEqual(len(cs[0].company_types) , 2)
        cs[0].company_types = [CompanyType.Distributor]
        cs_ii = CompanyFactory().Update(cs)
        self.assertEqual(len(cs_ii[0].company_types) , 1)

class PersonTest(unittest.TestCase):
    # def test_personFactory_get(self):
    #     cs = PersonFactory().Get([1,2])
    #     self.assertEqual(2,len(cs))
    #     self.assertEqual("Jamie",cs[0].first_name)
    #     self.assertEqual(2,cs[1].id)
    #
    #     self.assertTrue(True)

    def test_personFactory_insert(self):
        p = Person()
        p.first_name = "Mark"
        p.last_name = "Cavendish"
        p.job_title = "Sprinter"
        p.salutation = "Mr"

        p.roles = [PersonRole.Operations,PersonRole.Licencing]

        ps = PersonFactory().Insert([p])
        self.assertEqual(1,len(ps))
        self.assertEqual("Mark",ps[0].first_name)
        self.assertEqual("Sprinter",ps[0].job_title)
        self.assertEqual("Mr",ps[0].salutation)

        self.assertEqual(2,len(ps[0].emails))
        self.assertEqual(4,len(ps[0].phones))

        self.assertEqual(2,len(ps[0].roles))

        logging.info('***COUNTS PEOPLE AND EMAIL***')
        logging.info((ps[0].emails[0].id))
        logging.info((ps[0].emails[0].address))
        logging.info(ps[0].emails[0].type)
        logging.info(len(ps[0].emails))
        logging.info(len(ps[0].phones))

    def test_personFactory_update(self):
        p = Person()
        p.first_name = "Mark"
        p.last_name = "Cavendish"
        p.roles = [PersonRole.Operations,PersonRole.Licencing]

        ps = PersonFactory().Insert([p])
        self.assertEqual(1,len(ps))
        self.assertEqual("Mark",ps[0].first_name)

        ps[0].first_name = "Brad"
        ps[0].second_name = "Wiggins"
        ps[0].roles = [PersonRole.Accounts]

        PersonFactory().Update(ps)

        ups = PersonFactory().Get([ps[0].id])
        self.assertEqual("Brad",ups[0].first_name)

        self.assertEqual(1,len(ups[0].roles))

    def test_personFactory_getall(self):
        ps = PersonFactory().get_all()
        count = PersonFactory().count_people()
        self.assertEqual(len(ps) , count)

class AddressTest(unittest.TestCase):
    def test_addressFactory_inset(self):
        a1 = Address()
        a1.name = "test123"
        a1.line1="line1"
        a1.line2="line2"
        a1.line3="line3"
        a1.city="CITY"
        a1.region="region"
        a1.country="country"
        a1.postal_code="PC1 1AZ"

        a2 = Address()
        a2.name = "Orange"
        a2.line1="2line1"
        a2.line2="2line2"
        a2.line3="2line3"
        a2.city="2CITY"
        a2.region="2region"
        a2.country="2country"
        a2.postal_code = "AZ1 1AZ"
        addresses = AddressFactory().insert([a1,a2])
        self.assertEqual(2,len(addresses));

    def test_addressFactory_update(self):
        a1 = Address()
        a1.line1="line1"
        a1.line2="line2"
        a1.line3="line3"
        a1.city="CITY"
        a1.region="region"
        a1.country="country"

        a2 = Address()
        a2.line1="2line1"
        a2.line2="2line2"
        a2.line3="2line3"
        a2.city="2CITY"
        a2.region="2region"
        a2.country="2country"
        addresses = AddressFactory().insert([a1,a2])
        self.assertEqual(2,len(addresses));

        addresses[1].line1="3line1"
        addresses[1].line2="3line2"
        addresses[1].line3="3line3"
        addresses[1].city="3CITY"
        addresses[1].region="3region"
        addresses[1].country="3country"


        addresses = AddressFactory().update([addresses[1]])

class PhoneTest(unittest.TestCase):
    def test_phoneFactory_inset(self):
        p1 = Phone()
        p1.number="1234"
        p1.type = PhoneType.Personal

        p2 = Phone()
        p2.number="12345"
        p1.type = PhoneType.Personal

        phones = PhoneFactory().insert([p1,p2])
        self.assertEqual(2,len(phones));

    def test_phoneFactory_update(self):
        p1 = Phone()
        p1.number="1234"
        p1.type = PhoneType.Office

        p2 = Phone()
        p2.number="12345"
        p2.type = PhoneType.Mobile

        p3 = Phone()
        p3.number="9876"
        p3.type = PhoneType.Personal

        phones = PhoneFactory().insert([p1,p2,p3])
        self.assertEqual(3,len(phones));

        phones[0].number = "999"

        phones = PhoneFactory().update([phones[0]])

    def test_phoneFactory_getall(self):
        ps = PhoneFactory().get_all()
        count = PhoneFactory().count_all()
        self.assertEqual(len(ps) , count)

class EmailTest(unittest.TestCase):
    def test_emailFactory_inset(self):
        e1 = Email()
        e1.address="p@p.com"
        e1.type = EmailType.Office

        e2 = Phone()
        e2.address="j@j.com"
        e2.type = EmailType.Personal

        emails = EmailFactory().insert([e1,e2])
        self.assertEqual(2,len(emails));

    def test_emailFactory_update(self):
        e1 = Phone()
        e1.address="a@a.com"
        e1.type = EmailType.Office

        e2 = Phone()
        e2.address="b@b.com"
        e2.type = EmailType.Personal

        e3 = Phone()
        e3.address="c@c.com"
        e3.type = EmailType.Office

        emails = EmailFactory().insert([e1,e2,e3])
        self.assertEqual(3,len(emails));

        emails[0].number = "pjc@.com"
        emails[0].type = EmailType.Office

        phones = EmailFactory().update([emails[0]])