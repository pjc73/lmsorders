import os
import logging
import json

from google.appengine.api import rdbms

import webapp2
from webapp2_extras import jinja2

from lms.bll.cms_factory import CompanyFactory, PersonFactory , AddressFactory , PhoneFactory , EmailFactory
from lms.bll.cms import Company,Person, Address , Phone, Email , CompanyType , PersonRole , EmailType , PhoneType


TYPES = (  Phone, Email , Person , Address , Company , CompanyType , PhoneType , EmailType)


class ExtJsReturnObject:
    def build(self,data,objName,success):
        return { "success" : success, objName : data }

class CompanyListHandler(webapp2.RequestHandler):
    def get(self):
        c  = CompanyFactory().get_all()
        ext = ExtJsReturnObject().build(c,"Company","true")
        j = json.dumps(ext,cls=MyEncoder1)
        self.response.write(j)

class PersonUpdateHandler(webapp2.RequestHandler):
    def post(self):
        jsonToProcess  = self.request.body
        dict = json.loads(jsonToProcess)

        p = self.as_person(dict)

        nc = PersonFactory().Update([p])

        logging.info(jsonToProcess)
        ext = ExtJsReturnObject().build(nc,"Person","true")
        j = json.dumps(ext,cls=MyEncoder1)
        self.response.write(j)

    def as_person(self,dct):
        p = Person()
        p.id = int(dct['id'])

        logging.info('**id**')
        logging.info(dct['id'])

        if dct.has_key('first_name'):
            p.first_name = dct['first_name']
        if dct.has_key('last_name'):
            p.last_name = dct['last_name']
        if dct.has_key('job_title'):
            p.job_title = dct['job_title']
        if dct.has_key('salutation'):
            p.salutation = dct['salutation']
        if dct.has_key('roles'):
            p.roles = []
            if(isinstance( (dct['roles']), int )):
                p.roles.append(dct['roles']);
            else:
                for i in dct['roles']:
                    p.roles.append(PersonRole.get(i));

        if dct.has_key('phones'):
            logging.info('**phone start**')

            if(isinstance( (dct['phones']), str )):
                logging.info('ITS A STRING')

            if(isinstance( (dct['phones']), list )):
                logging.info('ITS A LIST')

            logging.info(dct['phones'])

            for ph in dct['phones']:
                nph = Phone(ph['id'],ph['number'],PhoneType.get(ph['type']))
                p.phones.append(nph);

            logging.info(dct['emails'])

            for em in dct['emails']:
                nem = Email(em['id'],em['address'],EmailType.get(em['type']))
                p.emails.append(nem);
                logging.info(em['address'])

        return p

class AddressUpdaterHandler(webapp2.RequestHandler):
    def post(self):
        jsonToProcess  = self.request.body
        dict = json.loads(jsonToProcess)
        logging.info('***ADDRESS POST A***')
        logging.info(jsonToProcess)

        a = self.as_update_address(dict)
        ac = AddressFactory().update([a])
        ext = ExtJsReturnObject().build(ac[0],"Address","true")

        j = json.dumps(ext,cls=MyEncoder1)
        self.response.write(j)


    def as_update_address(self,dct):
        a = Address(dct['id'])
        if dct.has_key('name'):
            a.name = dct['name']

        if dct.has_key('line1'):
            a.line1 = dct['line1']

        if dct.has_key('line2'):
            a.line2 = dct['line2']

        if dct.has_key('line3'):
            a.line3 = dct['line3']

        if dct.has_key('city'):
            a.city = dct['city']

        if dct.has_key('region'):
            a.region = dct['region']

        if dct.has_key('country'):
            a.country = dct['country']

        if dct.has_key('postal_code'):
            a.postal_code = dct['postal_code']

        return a


class AddressInsertHandler(webapp2.RequestHandler):
    def post(self):
        jsonToProcess  = self.request.body
        dict = json.loads(jsonToProcess)
        logging.info('***ADDRESS POST***')
        logging.info(jsonToProcess)

        a = self.as_new_address(dict)

        ac = AddressFactory().insert([a])

        company_id = int(dict['company_id'])
        c = CompanyFactory().Get([company_id])
        CompanyFactory().add_address(c[0],ac[0])

        ext = ExtJsReturnObject().build(ac[0],"Address","true")
        j = json.dumps(ext,cls=MyEncoder1)
        self.response.write(j)


    def as_new_address(self,dct):
        a = Address()
        if dct.has_key('name'):
            a.name = dct['name']
        return a


class PersonInsertHandler(webapp2.RequestHandler):
    def post(self):
        jsonToProcess  = self.request.body
        dict = json.loads(jsonToProcess)
        logging.info('***PERSON POST***')
        logging.info(jsonToProcess)
        p = self.as_new_person(dict)

        pc = PersonFactory().Insert([p])

        company_id = int(dict['company_id'])
        c = CompanyFactory().Get([company_id])
        CompanyFactory().AddPerson(c[0],pc[0])

        ext = ExtJsReturnObject().build(pc[0],"Person","true")
        j = json.dumps(ext,cls=MyEncoder1)
        self.response.write(j)

    def as_new_person(self,dct):
        p = Person()
        if dct.has_key('first_name'):
            p.first_name = dct['first_name']
        if dct.has_key('last_name'):
            p.last_name = dct['last_name']
        if dct.has_key('job_title'):
            p.job_title = dct['job_title']
        return p


class CompanyInsertHandler(webapp2.RequestHandler):
    def post(self):
        jsonToProcess  = self.request.body
        dict = json.loads(jsonToProcess)
        c = self.as_new_company(dict)
        nc = CompanyFactory().Insert([c])
        ext = ExtJsReturnObject().build(nc,"Company","true")
        j = json.dumps(ext,cls=MyEncoder1)
        self.response.write(j)

    def as_new_company(self,dct):
        c = Company()
        if dct.has_key('name'):
            c.name = dct['name']
        if dct.has_key('code'):
            c.code = dct['code']
        if dct.has_key('vat_number'):
            c.vat_number = dct['vat_number']
        return c

class CompanyUpdateHandler(webapp2.RequestHandler):
    def post(self):
        jsonToProcess  = self.request.body
        dict = json.loads(jsonToProcess)

        c = self.as_company(dict)

        nc = CompanyFactory().Update([c])

        logging.info(jsonToProcess)
        ext = ExtJsReturnObject().build(nc,"Company","true")
        j = json.dumps(ext,cls=MyEncoder1)
        self.response.write(j)



    def as_company(self,dct):
        c = Company(dct['id'])
        if dct.has_key('name'):
            c.name = dct['name']
        if dct.has_key('code'):
            c.code = dct['code']
        if dct.has_key('vat_number'):
            c.vat_number = dct['vat_number']
        if dct.has_key('company_types'):
            c.company_types = []
            if(isinstance( (dct['company_types']), int )):
                c.company_types.append(dct['company_types']);
            else:
                for i in dct['company_types']:
                    c.company_types.append(CompanyType.get(i));
        return c


class CompanyHandler(webapp2.RequestHandler):
    def get(self,phone_id):
        c  = CompanyFactory().Get([phone_id])



        j = json.dumps(c,cls=MyEncoder1)
        self.response.write(j)

class CompanyTypeHandler(webapp2.RequestHandler):
    def get(self):
        ct  = CompanyType.values()
        j = json.dumps(ct,cls=MyEncoder1)
        self.response.write(j)


class MyEncoder1(json.JSONEncoder):
    def default(self, obj):
        """
        default method is used if there is an unexpected object type
        in our example obj argument will be Decimal('120.50') and datetime
        in this encoder we are converting all Decimal to float and datetime to str
        """

        if isinstance(obj, TYPES):
            key = '%s' % obj.__class__.__name__
        #    return  { key: obj.__dict__ }
            return   obj.__dict__

        #        else :
        #            return obj = str(obj)

        return json.JSONEncoder.default(self, obj)

#        else:
#            obj = super(MyEncoder1, self).default(obj)
#        print obj
#        return obj


class MyEncoder2(json.JSONEncoder):
    def encode(self, obj):
        """
        encode method gets an original object
        and returns result string. obj argument will be the
        object that is passed to json.dumps function
        """
        obj['amount'] = float(obj['amount'])
        obj['date'] = str(obj['date'])
        obj['user'] = obj['user']._asdict()

        return super(MyEncoder2, self).encode(obj)
