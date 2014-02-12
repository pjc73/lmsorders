__author__ = 'paul'
from lms.dal.dao import CompanyDao , PersonDao , AddressDao , PhoneDao , EmailDao
from cms import Company , Person , Address , Email, Phone , PhoneType, EmailType , CompanyType ,PersonRole

import logging

class CompanyFactory:
    def AddPerson(self,c,p):
        dao = CompanyDao()
        dao.joinPerson(c.id,p.id)
        c.persons.append(p)
        return (self.Get([c.id]))

    def add_address(self,c,a):
        dao = CompanyDao()
        dao.joinAddress(c.id,a.id)
        c.addresses.append(a)
        return (self.Get([c.id]))


    def Get(self,ids = []):
        csvIds = ','.join(map(str,ids))

        rows = CompanyDao().get(csvIds,ids)
        companies = []

        for row in rows:
            c = Company(row[0],row[1])
            c.code = row[2]
            c.vat_number = row[3]
            companies.append(c)

        for c in companies:
            logging.info("before companies")
            logging.info(c.name)
            for p in c.persons:
                logging.info(p.first_name)

        self.Decorate(companies)

        for c in companies:
            logging.info("built companies")
            logging.info(c.name)
            for p in c.persons:
                logging.info(p.first_name)

        return companies



    def Update(self,companies):
        dao = CompanyDao()
        logging.info("UPDATE DAO")
        for c in companies:
            logging.info("UPDATE COMPANY")
            logging.info(str(c.id))
            logging.info(str(c.vat_number))
            logging.info(str(c.code))
            logging.info("******")
            dao.update(c.id,c.name,c.vat_number,c.code)

            if len(c.company_types) > 0:
                r = [t for t in c.company_types]
                dao.updateTypes(c.id,r)

        return self.Get([c.id for c in companies])

    def Insert(self,companies):
        dao = CompanyDao()
        newIds = []
        for c in companies:
            id = dao.insert(c.name,c.vat_number,c.code)
            newIds.append(id)
            if len(c.company_types) > 0:
                r = [t for t in c.company_types]
                dao.updateTypes(id,r)

        return self.Get(newIds)

#    def Delete(self,companies):

    def get_all(self):
        dao = CompanyDao()
        #rows = dao.GetAllIds()
        ids = [r[0] for r in dao.get_all_ids()]
        return self.Get(ids)

    def count_addresses(self):
        dao = CompanyDao()
        return  dao.count_all()

    def Decorate(self,companies):
        logging.info('Starting logging')
        companyIds = [c.id for c in companies]
        rows = CompanyDao().getPersonIds(companyIds)
        companyPersonMap = []
        for row in rows:
            logging.info([row[0],row[1]])
            companyPersonMap.append([row[0],row[1]])

        personIds = [m[1] for m in companyPersonMap]
        persons = PersonFactory().Get(personIds)


        for c in companies:
            for cpm in companyPersonMap:
                if cpm[0] == c.id:
                    logging.info("matched company")
                    for p in persons:
                        if p.id == cpm[1]:
                            logging.info("matched person")
                            logging.info(p.first_name)
                            c.persons.append(p)
#                            p.companies.append(c)

        rows = CompanyDao().getAddressIds(companyIds)
        companyAddressMap =[]
        for row in rows:
                companyAddressMap.append([row[0],row[1]])

        addressIds = [m[1] for m in companyAddressMap]
        addresses = AddressFactory().get(addressIds)

        for c in companies:
            for cpm in companyAddressMap:
                if cpm[0] == c.id:
                    logging.info("matched company")
                    for a in addresses:
                        if a.id == cpm[1]:
                            logging.info("matched address")
                            logging.info(a.line1)
                            c.addresses.append(a)

        rows = CompanyDao().getRoleIds(companyIds)
        company_role_map =[]

        for row in rows:
            company_role_map.append([row[0],row[1]])

        for c in companies:
            for cpm in company_role_map:

                if cpm[0] == c.id:
                    logging.info("matched company role")
                    c.company_types.append(CompanyType.get(cpm[1]))



#TODO covert to dynamic model

class PersonFactory:
    def Get(self,ids = []):
        rows = PersonDao().get(ids)
        persons = []

        for row in rows:
            p = Person(row[0],row[1],row[2],row[3],row[4])
            p.address_id = row[5]
            persons.append(p)

        self.Decorate(persons)


        return persons

    def Decorate(self,people):
        logging.info('Starting logging')
        people_ids = [p.id for p in people]

        rows = PersonDao().get_email_ids(people_ids)
        personEmailMap = []
        for row in rows:
            logging.info([row[0],row[1]])
            personEmailMap.append([row[0],row[1]])

        emailIds = [m[1] for m in personEmailMap]

        emails = EmailFactory().get(emailIds)

        for p in people:
            for pem in personEmailMap:
                if pem[0] == p.id:
                    logging.info("matched person")
                    for e in emails:
                        if e.id == pem[1]:
                            logging.info("matched email")
                            logging.info(e.id)
                            p.emails.append(e)

        rows = PersonDao().get_phone_ids(people_ids)
        personPhoneMap = []
        for row in rows:
            logging.info([row[0],row[1]])
            personPhoneMap.append([row[0],row[1]])

        phoneIds = [m[1] for m in personPhoneMap]

        phones = PhoneFactory().get(phoneIds)

        for p in people:
            for pem in personPhoneMap:
                if pem[0] == p.id:
                    logging.info("matched person")
                    for ph in phones:
                        if ph.id == pem[1]:
                            logging.info("matched phone")
                            logging.info(ph.id)
                            p.phones.append(ph)

        rows = PersonDao().get_role_ids(people_ids)
        person_role_map =[]

        for row in rows:
            person_role_map.append([row[0],row[1]])

        for p in people:
            for prm in person_role_map:

                if prm[0] == p.id:
                    logging.info("matched company role")
                    p.roles.append(PersonRole.get(prm[1]))


    def Insert(self,people):
        dao = PersonDao()
        newIds = []
        newPhones = []
        newEmails = []

        for p in people:
            newId = dao.insert(p.first_name,p.last_name,p.job_title, p.salutation)
            newIds.append(newId)
            newPhones.append((newId,Phone(-1,"",PhoneType.Office)))
            newPhones.append((newId,Phone(-1,"",PhoneType.Fax)))
            newPhones.append((newId,Phone(-1,"",PhoneType.Mobile)))
            newPhones.append((newId,Phone(-1,"",PhoneType.Personal)))
            newEmails.append((newId,Email(-1,"",EmailType.Office)))
            newEmails.append((newId,Email(-1,"",EmailType.Personal)))
            if len(p.roles) > 0:
                r = [t for t in p.roles]
                dao.updateRoles(newId,r)


        self.insertPhones(newPhones)
        self.insertEmails(newEmails)

        newPeople = self.Get(newIds)

        return newPeople

    def Update(self,people):
        dao = PersonDao()
        newIds = []
        logging.info("Updating Person 1")

        for p in people:
            logging.info("Updating Person 2")
            newIds.append(dao.update(p.id,p.first_name,p.last_name,p.job_title, p.salutation))
            if len(p.roles) > 0:
                r = [t for t in p.roles]
                dao.updateRoles(p.id,r)
            PhoneFactory().update(p.phones)
            EmailFactory().update(p.emails)

        return self.Get([p.id for p in people])

    def get_all(self):
        dao = PersonDao()
        #rows = dao.GetAllIds()
        ids = [r[0] for r in dao.get_all_ids()]
        return self.Get(ids)

    def count_people(self):
        dao = PersonDao()
        return  dao.count_all()

    #peopleToPhone = list of 2 tuples (person_id,insert_phone)
    def insertPhones(self,peopleToPhone):
        new_phones_to_person = []
        for pp in peopleToPhone:
            logging.info('***PEOPLE TO PHONE***')
            logging.info(pp)
            new_phone = PhoneFactory().insert([pp[1]])
            new_phones_to_person.append((pp[0],new_phone[0].id))
        dao = PersonDao().insertPhones(new_phones_to_person)


    #peopleToPhone = list of 2 tuples (person_id,email_id)
    def insertEmails(self,people_to_email):
        new_emails_to_person = []
        for pe in people_to_email:
            logging.info('***PEOPLE TO EMAIL***')
            logging.info(pe)
            new_email = EmailFactory().insert([pe[1]])
            new_emails_to_person.append((pe[0],new_email[0].id))
        dao = PersonDao().insertEmails(new_emails_to_person)

class AddressFactory:
    def get(self,ids=[]):
        dao = AddressDao()
        rows = dao.get(ids)
        addresses = []
        for row in rows:
            addresses.append(Address(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))

        return addresses

    def update(self, addresses):
        dao = AddressDao()
        values = [(a.id,a.name, a.line1,a.line2,a.line3,a.city,a.region,a.country,a.postal_code) for a in addresses]
        dao.update(values)
        ids = [(a.id) for a in addresses]
        ads = self.get(ids)
        return ads

    def insert(self , addresses):
        dao = AddressDao()
        values = [(a.name,a.line1,a.line2,a.line3,a.city,a.region,a.country,a.postal_code) for a in addresses]
        ids = dao.insert(values)
        ads = self.get(ids)

        #set the default phone and email types
        return ads

class PhoneFactory:
    def get(self,ids=[]):
        dao = PhoneDao()
        rows = dao.get(ids)
        phones = []
        for row in rows:
            p = Phone(row[0],row[1],PhoneType.get(int(row[2])))
            phones.append(p)

        return phones
    def update(self,phones):
        dao = PhoneDao()
        values = [(p.id, p.number, p.type ) for p in phones]
        logging.info('*****updating phones*****')
        logging.info(values)
        dao.update(values)
        ids = [(p.id) for p in phones]
        ps = self.get(ids)
        return ps

    def insert(self, phones):
        dao = PhoneDao()
        values = [(p.number,p.type) for p in phones]
        ids = dao.insert(values)
        ps = self.get(ids)
        return ps

    def get_all(self):
        dao = PhoneDao()
        #rows = dao.GetAllIds()
        ids = [r[0] for r in dao.get_all_ids()]
        return self.get(ids)

    def count_all(self):
        dao = PhoneDao()
        return  dao.count_all()

class EmailFactory:
    def get(self,ids=[]):
        dao = EmailDao()
        rows = dao.get(ids)
        emails = []
        for row in rows:
            emails.append(Email(row[0],row[1],EmailType.get(int(row[2]))))

        return emails

    def update(self,emails):
        dao = EmailDao()
        values = [ ( e.id, e.address , e.type ) for e in emails]
        dao.update(values)
        ids = [(e.id) for e in emails]
        es = self.get(ids)
        return es

    def insert(self, emails):
        dao = EmailDao()
        values = [ ( e.address, e.type ) for e in emails]
        ids = dao.insert(values)
        es = self.get(ids)
        return es
