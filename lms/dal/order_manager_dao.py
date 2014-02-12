import os
import logging

from google.appengine.api import rdbms
from lms.dal.dao import GenericDao,Dao,get_connection

CLOUDSQL_INSTANCE = ''
DATABASE_NAME = 'test'
USER_NAME = 'root'
PASSWORD = ''



class CspOrderDao(GenericDao):
    #table_def = "lms_orders.Email"
    #pk_def = "email_id"
    #field_defs = [  ("email","VARCHAR(255)")]
    def __init__(self):
        self.table_def = "lms_orders.OrderCsp"
        self.pk_def = "csp_order_id"
        self.field_defs = [
            ("fk_csp_company","int" ) ,
            ("fk_csp_contact","int" ) ,
            ("fk_owner_company","int" ) ,
            ("fk_owner_contact","int" ) ,
            ("invoice_number","varchar(45)" ) ,
            ("invoice_date","datetime" )
        ]

    def joinOrderItem(self,co_id,oi_id):
        fk_join_left = 'fk_csp_order'
        fk_join_right = 'fk_order_item'
        join_table = 'lms_orders.OrderCspToOrderItem'
        Dao().insert_join_table(join_table,fk_join_left,fk_join_right,str(co_id),str(oi_id))

    def getOrderItemIdsIds(self,ids):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT fk_csp_order , fk_order_item FROM lms_orders.OrderCspToOrderItem ')
        rows = cursor.fetchall()
        conn.close()
        return rows




class SupplierOrderDao(GenericDao):
    #table_def = "lms_orders.Email"
    #pk_def = "email_id"
    #field_defs = [  ("email","VARCHAR(255)")]
    def __init__(self):
        self.table_def = "lms_orders.OrderSupplier"
        self.pk_def = "order_supplier_id"
        self.field_defs = [
            ("fk_supplier_company","int") ,
            ("fk_supplier_contact","int") ,
            ("fk_owner_company","int") ,
            ("fk_owner_contact","int") ,
            ("po_number","varchar(50)"),
            ("po_date","datetime")
        ]

    def joinOrderItem(self,so_id,oi_id):
        fk_join_left = 'fk_supplier_order'
        fk_join_right = 'fk_order_item'
        join_table = 'lms_orders.OrderSupplierToOrderItem'
        Dao().insert_join_table(join_table,fk_join_left,fk_join_right,str(so_id),str(oi_id))

    def getOrderItemIdsIds(self,ids):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT fk_supplier_order , fk_order_item FROM lms_orders.OrderSupplierToOrderItem ')
        rows = cursor.fetchall()
        conn.close()
        return rows


class OrderItemDao(GenericDao):
    #table_def = "lms_orders.Email"
    #pk_def = "email_id"
    #field_defs = [  ("email","VARCHAR(255)")]
    def __init__(self):
        self.table_def = "lms_orders.OrderItem"
        self.pk_def = "orderitem_id"
        self.field_defs = [
            ("fk_supplier_company","int"),
            ("fk_csp_company","int") ,
            ("fk_csp_contact","int"),
            ("fk_owner_company","int"),
            ("fk_company_airline", "int"),
            ("csp_po_number", "varchar(45)") ,
            ("supplier_invoice_number", "varchar(45)") ,
            ("title", "varchar(255)") ,
            ("comments", "varchar(500)") ,
            ("start_date", "datetime") ,
            ("end_date", "datetime") ,
            ("unit_price", "decimal(10,0)") ,
            ("units", "int"),
            ("delivery_format", "varchar(45)") ,
            ("total_price", "decimal(10,0)") ,
            ("delivery_date", "datetime")
            #,("fk_csp_order","int"),
            #("fk_supplier_order","int"),
            #("fk_contact_airline", "int")
        ]


# l_id
# l_supplier_id
# l_csp_id
# l_csp_contact_id
# l_owner_id,
# l_airline_id
# l_csp_po_number
# l_supplier_invoice_number


# l_owner_po_number


# l_title
# l_comments
# l_start_date
# l_end_date
# l_unit_price
# l_units
# l_delivery_format
# l_total_price
# l_delivery_date


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
