#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import os
import logging
import json

from google.appengine.api import rdbms

import webapp2
from webapp2_extras import jinja2

from lms.bll.cms_factory import CompanyFactory, PersonFactory , AddressFactory , PhoneFactory , EmailFactory
from lms.bll.cms import Company,Person, Address , Phone, Email
from web.cms import CompanyListHandler , CompanyHandler , CompanyUpdateHandler , CompanyInsertHandler, PersonInsertHandler , PersonUpdateHandler, CompanyTypeHandler ,  AddressInsertHandler, AddressUpdaterHandler
from web.site import TreeTypeHandler

CLOUDSQL_INSTANCE = ''
DATABASE_NAME = 'test'
USER_NAME = 'root'
PASSWORD = ''


def get_connection():
    return rdbms.connect(instance=CLOUDSQL_INSTANCE, database=DATABASE_NAME,
        user=USER_NAME, password=PASSWORD, charset='utf8')


class BaseHandler(webapp2.RequestHandler):

    @webapp2.cached_property
    def jinja2(self):
        # Returns a Jinja2 renderer cached in the app registry.
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **context):
        # Renders a template and writes the result to the response.
        rv = self.jinja2.render_template(_template, **context)
        self.response.write(rv)


class MainHandler(BaseHandler):
    def get(self):
        # Viewing guestbook
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT t.pkTestId, t.name FROM testtable t')
        rows = cursor.fetchall()
        conn.close()

        template_values = {"rows": rows}
        self.render_response('index.html', **template_values)

TYPES = (  Phone, Email , Person , Address , Company)



class MyEncoder1(json.JSONEncoder):
    def default(self, obj):
        """
        default method is used if there is an unexpected object type
        in our example obj argument will be Decimal('120.50') and datetime
        in this encoder we are converting all Decimal to float and datetime to str
        """

        if isinstance(obj, TYPES):
            key = '%s' % obj.__class__.__name__
            return { key: obj.__dict__ }

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

class PhoneListHandler(webapp2.RequestHandler):
    def get(self):
        phones  = CompanyFactory().get_all()



        j = json.dumps(phones,cls=MyEncoder1)
        self.response.write(j)

class PhoneHandler(webapp2.RequestHandler):
    def get(self,phone_id):
        phones  = CompanyFactory().Get([phone_id])



        j = json.dumps(phones,cls=MyEncoder1)
        self.response.write(j)


app = webapp2.WSGIApplication([
    ('/', MainHandler),
    (r'/company',CompanyListHandler),
    (r'/company/(\d+)', CompanyHandler),
    (r'/company/update', CompanyUpdateHandler),
    (r'/company/insert', CompanyInsertHandler),
    (R'/address/insert', AddressInsertHandler),
    (R'/person/insert', PersonInsertHandler),
    (r'/companytypes',CompanyTypeHandler),
    (r'/person/update',PersonUpdateHandler),
    (r'/address/update',AddressUpdaterHandler),
    (r'/treedata',TreeTypeHandler)

], debug=True)
