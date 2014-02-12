__author__ = 'paul'

import logging

from lms.dal.order_manager_dao import OrderItemDao ,  CspOrderDao , SupplierOrderDao
from cms import Company , Person , Address , Email, Phone , PhoneType, EmailType , CompanyType ,PersonRole
from order_manager import CspOrder , SupplierOrder , OrderItem
from lms.bll.cms_factory import CompanyFactory , PersonFactory

   # def __init__(self,l_id=-1,l_supplier_id=-1,l_csp_id=-1,l_csp_contact_id=-1,l_owner_id=-1,
   #               l_airline_id=-1 ,  l_csp_po_number="",  l_supplier_invoice_number="" ,
   #               l_owner_po_number="" , l_title="" , l_comments="" , l_start_date=""  , l_end_date="" , l_unit_price =0,
   #               l_units=0 , l_delivery_format=""  , l_total_price=0 , l_delivery_date=""):
   #      self.id = l_id
   #      self.supplier_id = l_supplier_id
   #      self.supplier = None
   #      self.csp_id = l_csp_id
   #      self.csp = None
   #      self.csp_contact_id = l_csp_contact_id
   #      self.csp_contact = None
   #      self.csp_po_number = l_csp_po_number
   #      self.supplier_invoice_number = l_supplier_invoice_number
   #      self.owner_id = l_owner_id
   #      self.owner = None
   #      self.owner_po_number = l_owner_po_number
   #      self.title = l_title
   #      self.comments = l_comments
   #      self.airline_id = l_airline_id
   #      self.airline = None
   #      self.start_date =l_start_date
   #      self.end_date = l_end_date
   #      self.unit_price = l_unit_price
   #      self.units = l_units
   #      self.delivery_format = l_delivery_format
   #      self.total_price = l_total_price
   #      self.delivery_date  = l_delivery_date

# `OrderItem`.`orderitem_id`,
# `OrderItem`.`fk_owner_company`,
# `OrderItem`.`fk_csp_order`,
# `OrderItem`.`fk_csp_contact`,
# `OrderItem`.`fk_csp_company`,
# `OrderItem`.`fk_supplier_order`,
# `OrderItem`.`fk_supplier_company`,
# `OrderItem`.`fk_contact_airline`,
# `OrderItem`.`fk_company_airline`,
# `OrderItem`.`csp_po_number`,
# `OrderItem`.`title`,
# `OrderItem`.`comments`,
# `OrderItem`.`start_date`,
# `OrderItem`.`end_date`,
# `OrderItem`.`units`,
# `OrderItem`.`unit_price`,
# `OrderItem`.`total_price`,
# `OrderItem`.`delivery_format`,
# `OrderItem`.`delivery_date`,


#todo improve company and contact decorators
#todo check item decorator is as good


class CspOrderFactory:

    def addOrderItem(self,co,oi):
        dao = CspOrderDao()
        dao.joinOrderItem(co.id,oi.id)
        co.items.append(oi)
        return (self.get([co.id]))

    def get(self,ids=[]):
        dao = CspOrderDao()
        rows = dao.get(ids)
        cspOrders = []
        for row in rows:
            cspOrders.append(CspOrder(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

        self.decorate(cspOrders)

        return cspOrders

    def insert(self,cspOrderItems=[]):
        dao = CspOrderDao()

        values = [(co.csp_id,co.csp_accounts_payable_contact_id,co.owner_id,co.owner_contact_id,co.owner_invoice_number,co.owner_invoice_date) for co in cspOrderItems]

        ids = dao.insert(values)

        newCspOrders = self.get(ids)

        #set the default phone and email types
        return newCspOrders

    def update(self,cspOrderItems=[]):
        dao = CspOrderDao()

        values = [(co.id,co.csp_id,co.csp_accounts_payable_contact_id,co.owner_id,co.owner_contact_id,co.owner_invoice_number,co.owner_invoice_date) for co in cspOrderItems]

        dao.update(values)

        ids = [(co.id) for co in cspOrderItems]
        updatedCspOrders = self.get(ids)
        return updatedCspOrders

    def decorate(self,orderCsps=[]):

        orderCspIds=[O.id for O in orderCsps]

        rows = CspOrderDao().getOrderItemIdsIds(orderCspIds)

        orderItemMap = []

        for row in rows:
            logging.info([row[0],row[1]])
            orderItemMap.append([row[0],row[1]])

        itemIds = [m[1] for m in orderItemMap]
        items = OrderItemFactory().get(itemIds)

        for o in orderCsps:
            for oim in orderItemMap:
                if oim[0] == o.id:
                    logging.info("matched order")
                    for i in items:
                        if i.id == oim[1]:
                            logging.info("matched item")
                            logging.info(i.csp_po_number)
                            o.items.append(i)


        #get csp

        cspIds = list(set([O.csp_id for O in orderCsps]))
        csps = CompanyFactory().Get(cspIds)

        for c in csps:
            matching_csps =  [o for o in orderCsps if o.csp_id == c.id]
            for m in matching_csps:
                    m.csp = c

        #get csp contact

        cspContactIds = list(set([O.csp_accounts_payable_contact_id for O in orderCsps]))
        cspContacts = PersonFactory().Get(cspContactIds)

        for c in cspContacts:
            matching_cspContacts =  [o for o in orderCsps if o.csp_accounts_payable_contact_id == c.id]
            for m in matching_cspContacts:
                    m.csp_accounts_payable_contact = c

        #get owner

        ownerIds = list(set([O.owner_id for O in orderCsps]))
        owners = CompanyFactory().Get(ownerIds)

        for o in owners:
            matching_owners =  [oc for oc in orderCsps if oc.owner_id == o.id]
            for m in matching_owners:
                    m.owner = o

        #get owner contact
        ownerContactIds = list(set([O.owner_contact_id for O in orderCsps]))
        ownerContacts = PersonFactory().Get(ownerContactIds)

        for c in ownerContacts:
            matching_ownerContacts =  [o for o in orderCsps if o.owner_contact_id == c.id]
            for m in matching_ownerContacts:
                    m.owner_contact = c


class SupplierOrderFactory:

    def addOrderItem(self,so,oi):
        dao = SupplierOrderDao()
        dao.joinOrderItem(so.id,oi.id)
        so.items.append(oi)
        return (self.get([so.id]))


    def get(self,ids=[]):
        dao = SupplierOrderDao()
        rows = dao.get(ids)
        supplierOrders = []
        for row in rows:
            supplierOrders.append(SupplierOrder(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))

        self.decorate(supplierOrders)

        return supplierOrders

    def insert(self,supplierOrders=[]):
        dao = SupplierOrderDao()

        values = [(so.supplier_id,so.supplier_contact_id,so.owner_id,so.owner_contact_id,so.owner_po_number,so.owner_po_date) for so in supplierOrders]

        ids = dao.insert(values)

        newSupplierOrders = self.get(ids)

        #set the default phone and email types
        return newSupplierOrders

    def update(self,supplierOrderItems=[]):
        dao = SupplierOrderDao()

        values = [(so.id,so.supplier_id,so.supplier_contact_id,so.owner_id,so.owner_contact_id,so.owner_po_number,so.owner_po_date) for so in supplierOrderItems]

        dao.update(values)

        ids = [(so.id) for so in supplierOrderItems]
        updatedSupplierOrders = self.get(ids)
        return updatedSupplierOrders

    def decorate(self,orderSuppliers=[]):
        orderSuppliersIds=[O.id for O in orderSuppliers]

        rows = SupplierOrderDao().getOrderItemIdsIds(orderSuppliersIds)

        orderItemMap = []

        for row in rows:
            logging.info([row[0],row[1]])
            orderItemMap.append([row[0],row[1]])

        itemIds = [m[1] for m in orderItemMap]
        items = OrderItemFactory().get(itemIds)

        for o in orderSuppliers:
            for oim in orderItemMap:
                if oim[0] == o.id:
                    logging.info("matched order")
                    for i in items:
                        if i.id == oim[1]:
                            logging.info("matched item")
                            logging.info(i.csp_po_number)
                            o.items.append(i)


        #get supplier / supplier_id

        supplierIds = list(set([O.supplier_id for O in orderSuppliers]))
        suppliers = CompanyFactory().Get(supplierIds)

        for s in suppliers:
            matching_suppliers =  [o for o in orderSuppliers if o.supplier_id == s.id]
            for m in matching_suppliers:
                    m.supplier = s

        #get supplier_contact / supplier_contact_id

        supplierContactIds = list(set([O.supplier_contact_id for O in orderSuppliers]))
        supplierContacts = PersonFactory().Get(supplierContactIds)

        for c in supplierContacts:
            matching_supplierContacts =  [o for o in orderSuppliers if o.supplier_contact_id == c.id]
            for m in matching_supplierContacts:
                    m.csp_accounts_payable_contact = c

        #get owner

        ownerIds = list(set([O.owner_id for O in orderSuppliers]))
        owners = CompanyFactory().Get(ownerIds)

        for o in owners:
            matching_owners =  [os for os in orderSuppliers if os.owner_id == o.id]
            for m in matching_owners:
                    m.owner = o

        #get owner contact
        ownerContactIds = list(set([O.owner_contact_id for O in orderSuppliers]))
        ownerContacts = PersonFactory().Get(ownerContactIds)

        for c in ownerContacts:
            matching_ownerContacts =  [o for o in orderSuppliers if o.owner_contact_id == c.id]
            for m in matching_ownerContacts:
                    m.owner_contact = c


class OrderItemFactory:
    def get(self,ids=[]):
        dao = OrderItemDao()
        rows = dao.get(ids)
        orderItems = []
        for row in rows:
            orderItems.append(OrderItem(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16]))

        return orderItems

    def update(self, orderItems):
        dao = OrderItemDao()

        values = [(oi.id, oi.supplier_id,oi.csp_id,oi.csp_contact_id,oi.owner_id,oi.airline_id,
                   oi.csp_po_number,oi.supplier_invoice_number, #oi.owner_po_number,
                   oi.title,oi.comments,oi.start_date,oi.end_date,oi.unit_price, oi.units,
                   oi.delivery_format, oi.total_price,oi.delivery_date) for oi in orderItems]

        dao.update(values)

        ids = [(oi.id) for oi in orderItems]
        updatedOrderItems = self.get(ids)
        return updatedOrderItems

    def insert(self , orderItems):
        dao = OrderItemDao()

        values = [(oi.supplier_id,oi.csp_id,oi.csp_contact_id,oi.owner_id,oi.airline_id,
                   oi.csp_po_number,oi.supplier_invoice_number, # oi.owner_po_number,
                   oi.title,oi.comments,oi.start_date,oi.end_date,oi.unit_price, oi.units,
                   oi.delivery_format, oi.total_price,oi.delivery_date) for oi in orderItems]

        ids = dao.insert(values)
        newOrderItems = self.get(ids)

        #set the default phone and email types
        return newOrderItems

    def Decorate(self , orderItems = []):
        #get suppliers supplier_id supplier

        supplierIds = list(set([O.supplier_id for O in orderItems]))
        suppliers = CompanyFactory().Get(supplierIds)

        for s in suppliers:
            matching_suppliers =  [o for o in orderItems if o.supplier_id == s.id]
            for m in matching_suppliers:
                    m.supplier = s

        #get owners owner_id / owner

        ownerIds = list(set([O.owner_id for O in orderItems]))
        owners = CompanyFactory().Get(ownerIds)

        for o in owners:
            matching_owners =  [oi for oi in orderItems if o.owner_id == o.id]
            for m in matching_owners:
                    m.owner = o

        #get airlines airline_id  / airline

        airlineIds = list(set([O.airline_id for O in orderItems]))
        airlines = CompanyFactory().Get(airlineIds)

        for a in airlines:
            matching_airlines =  [o for o in orderItems if o.airline_id == a.id]
            for m in matching_airlines:
                    m.airline = a

        #get csps csp_id csp


        cspIds = list(set([O.csp_id for O in orderItems]))
        csps = CompanyFactory().Get(cspIds)

        for c in csps:
            matching_csps =  [o for o in orderItems if o.csp_id == c.id]
            for m in matching_csps:
                    m.csp = c

        #get csp contacts csp_contact_id  / csp_contact

        cspContactIds = list(set([O.csp_contact_id for O in orderItems]))
        cspContacts = PersonFactory().Get(cspContactIds)

        for c in cspContacts:
            matching_cspContacts =  [o for o in orderItems if o.csp_contact_id == c.id]
            for m in matching_cspContacts:
                    m.csp_accounts_payable_contact = c


        #getowner contact doesnt exist

        return 1