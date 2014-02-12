__author__ = 'paul'

class CompanyType:
    CSP=1
    Distributor=2

    @staticmethod
    def get(i):
        if i==1 :
            return CompanyType.CSP
        elif i==2 :
            return CompanyType.Distributor

    @staticmethod
    def values():
        return [{'CSP':1},{'Distributor':2}]

class Company:
    def __init__(self,l_id=-1,l_name=""):
        self.id=l_id
        self.name = l_name
        self.addresses = []
        self.persons = []
        self.vat_number = ""
        self.code = ""
        self.company_types = []

class PersonRole:
    Accounts=1
    Acquisitions=2
    Licencing=3
    Operations=4

    @staticmethod
    def get(i):
        if i==1 :
            return PersonRole.Accounts
        elif i==2 :
            return  PersonRole.Acquisitions
        elif i==3 :
            return  PersonRole.Licencing
        elif i==4 :
            return  PersonRole.Operations

class Person:
    def __init__(self,l_id=-1,l_first_name="",l_last_name="",l_job_title="",l_salutation=""):
        self.id=l_id
        self.first_name = l_first_name
        self.last_name = l_last_name
        self.job_title = l_job_title
        self.salutation = l_salutation
        self.address_id = None
        self._address = None
        self.phones = []
        self.emails = []
        self.companies = []
        self.roles=[]

        @property
        def address(self):
            return self._address

        @address.setter
        def address(self,value):
            self.address_id = value.id
            self._address = value


#todo does this work and replace dic with this in encoder
    def dict_for_json(self):
        d = self.__dict__
        d['roles']= ','.join(str(r) for r in self.roles)
        return d


class Address:
    def __init__(self,l_id=-1,l_name="",l_line1="",l_line2="",l_line3="",l_city="",l_region="",l_country="",l_postal_code=""):
        self.id = l_id
        self.line1=l_line1
        self.line2=l_line2
        self.line3=l_line3
        self.city=l_city
        self.region=l_region
        self.country=l_country
        self.postal_code=l_postal_code
        self.phones = []
        self.emails = []
        self.persons = []
        self.name = l_name

class EmailType:
    Office=1
    Personal=2

    @staticmethod
    def get(i):
        if i==1 :
            return EmailType.Office
        elif i==2 :
            return  EmailType.Personal

    @staticmethod
    def name(i):
        if i==1 :
            return 'Office'
        elif i==2 :
            return 'Personal'


class Email:
    def __init__(self,l_id=-1,address="",l_type = None):
        self.id = l_id
        self.address = address
        self.type = l_type
        self.type_name = EmailType.name(self.type)



class PhoneType:
    Office=1
    Personal=2
    Mobile=3
    Fax=4


    @staticmethod
    def get(i):
        if i==1 :
            return PhoneType.Office
        elif i==2 :
            return  PhoneType.Personal
        elif i==3 :
            return PhoneType.Mobile
        elif i==4 :
            return PhoneType.Fax

    @staticmethod
    def name(i):
        if i==1 :
            return "Office"
        elif i==2 :
            return  "Personal"
        elif i==3 :
            return "Mobile"
        elif i==4 :
            return "Fax"

class Phone:
    def __init__(self,l_id=-1,number="",l_type=None):
        self.id = l_id
        self.number = number
        self.type = l_type;
        self.type_name = PhoneType.name(self.type)

