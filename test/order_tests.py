import unittest
import logging
import datetime


from lms.bll.order_manager_factory import OrderItemFactory , CspOrderFactory , SupplierOrderFactory
from lms.bll.order_manager import OrderItem , CspOrder , SupplierOrder


#todo write update test
#todo write items appemd
# have better test asserts

class SupplierOrderTest(unittest.TestCase):
    def test_SupplierOrder_insert_with_items(self):
        co1 = SupplierOrder
        co1.supplier_id = 10
        co1.supplier_contact_id = 1
        co1.owner_id = 11
        co1.owner_contact_id = 2
        co1.owner_po_number = "ITEMS123"
        co1.owner_po_date = datetime.date.today()

        #orderItems = OrderItemFactory().insert([oi1,oi2])

        #co1.items = orderItems

        newsos = SupplierOrderFactory().insert([co1])

        oi1 = OrderItem()
        oi1.owner_id=1
        oi1.csp_id=1
        oi1.csp_contact_id=1
        oi1.supplier_id=1
        oi1.airline_id=1
        oi1.csp_po_number="AB123"
        oi1.comments ="comments"
        oi1.start_date = datetime.date.today()
        oi1.end_date =  datetime.date.today()
        oi1.unit_price = 10

        oi2 = OrderItem()
        oi2.owner_id=1
        oi2.csp_id=1
        oi2.csp_contact_id=1
        oi2.supplier_id=1
        oi2.airline_id=1
        oi2.csp_po_number="XY123"
        oi2.comments ="more comments"
        oi2.start_date = datetime.date.today()
        oi2.end_date =  datetime.date.today()
        oi2.unit_price = 2

        orderItems = OrderItemFactory().insert([oi1,oi2])

        SupplierOrderFactory().addOrderItem(newsos[0],orderItems[0])
        SupplierOrderFactory().addOrderItem(newsos[0],orderItems[1])




    def test_SupplierOrder_insert(self):
        co1 = SupplierOrder
        co1.supplier_id = 10
        co1.supplier_contact_id = 1
        co1.owner_id = 11
        co1.owner_contact_id = 2
        co1.owner_po_number = "POABC123"
        co1.owner_po_date = datetime.date.today()


        #orderItems = OrderItemFactory().insert([oi1,oi2])

        #co1.items = orderItems

        SupplierOrderFactory().insert([co1])

    def test_SupplierOrder_update(self):
        co1 = SupplierOrder
        co1.supplier_id = 10
        co1.supplier_contact_id = 1
        co1.owner_id = 11
        co1.owner_contact_id = 2
        co1.owner_po_number = "POABC123"
        co1.owner_po_date = datetime.date.today()


        #orderItems = OrderItemFactory().insert([oi1,oi2])

        #co1.items = orderItems

        newItems = SupplierOrderFactory().insert([co1])

        so = newItems[0]

        so.owner_po_number = "changed"

        SupplierOrderFactory().update([so])


class CspOrderTest(unittest.TestCase):


    def test_CspOrder_insert_with_items(self):
        co1 = CspOrder
        co1.csp_id = 10
        co1.csp_accounts_payable_contact_id = 1
        co1.owner_id = 11
        co1.owner_contact_id = 2
        co1.owner_invoice_number = "ABC123"
        co1.owner_invoice_date = datetime.date.today()

        oi1 = OrderItem()
        oi1.owner_id=1
        oi1.csp_id=1
        oi1.csp_contact_id=1
        oi1.supplier_id=1
        oi1.airline_id=1
        oi1.csp_po_number="AB123"
        oi1.comments ="comments"
        oi1.start_date = datetime.date.today()
        oi1.end_date =  datetime.date.today()
        oi1.unit_price = 10

        oi2 = OrderItem()
        oi2.owner_id=1
        oi2.csp_id=1
        oi2.csp_contact_id=1
        oi2.supplier_id=1
        oi2.airline_id=1
        oi2.csp_po_number="XY123"
        oi2.comments ="more comments"
        oi2.start_date = datetime.date.today()
        oi2.end_date =  datetime.date.today()
        oi2.unit_price = 2

        orderItems = OrderItemFactory().insert([oi1,oi2])
        #orderItems = OrderItemFactory().insert([oi1,oi2])

        #co1.items = orderItems

        newcos = CspOrderFactory().insert([co1])

        CspOrderFactory().addOrderItem(newcos[0],orderItems[0])
        CspOrderFactory().addOrderItem(newcos[0],orderItems[1])


    def test_CspOrder_insert(self):
        co1 = CspOrder
        co1.csp_id = 10
        co1.csp_accounts_payable_contact_id = 1
        co1.owner_id = 11
        co1.owner_contact_id = 2
        co1.owner_invoice_number = "ABC123"
        co1.owner_invoice_date = datetime.date.today()

        oi1 = OrderItem()
        oi1.owner_id=1
        oi1.csp_id=1
        oi1.csp_contact_id=1
        oi1.supplier_id=1
        oi1.airline_id=1
        oi1.csp_po_number="AB123"
        oi1.comments ="comments"
        oi1.start_date = datetime.date.today()
        oi1.end_date =  datetime.date.today()
        oi1.unit_price = 10

        oi2 = OrderItem()
        oi2.owner_id=1
        oi2.csp_id=1
        oi2.csp_contact_id=1
        oi2.supplier_id=1
        oi2.airline_id=1
        oi2.csp_po_number="XY123"
        oi2.comments ="more comments"
        oi2.start_date = datetime.date.today()
        oi2.end_date =  datetime.date.today()
        oi2.unit_price = 2

        #orderItems = OrderItemFactory().insert([oi1,oi2])

        #co1.items = orderItems

        CspOrderFactory().insert([co1])

    def test_CspOrder_update(self):
        co1 = CspOrder
        co1.csp_id = 10
        co1.csp_accounts_payable_contact_id = 1
        co1.owner_id = 11
        co1.owner_contact_id = 2
        co1.owner_invoice_number = "XYZ123"
        co1.owner_invoice_date = datetime.date.today()

        oi1 = OrderItem()
        oi1.owner_id=1
        oi1.csp_id=1
        oi1.csp_contact_id=1
        oi1.supplier_id=1
        oi1.airline_id=1
        oi1.csp_po_number="AB123"
        oi1.comments ="comments"
        oi1.start_date = datetime.date.today()
        oi1.end_date =  datetime.date.today()
        oi1.unit_price = 10

        oi2 = OrderItem()
        oi2.owner_id=1
        oi2.csp_id=1
        oi2.csp_contact_id=1
        oi2.supplier_id=1
        oi2.airline_id=1
        oi2.csp_po_number="XY123"
        oi2.comments ="more comments"
        oi2.start_date = datetime.date.today()
        oi2.end_date =  datetime.date.today()
        oi2.unit_price = 2

        #orderItems = OrderItemFactory().insert([oi1,oi2])

        #co1.items = orderItems

        newcos = CspOrderFactory().insert([co1])

        self.assertEqual("XYZ123",newcos[0].owner_invoice_number);

        newcos[0].owner_invoice_number = "UPDATED NUMBER 123"

        self.assertEqual(1,len(newcos));

        CspOrderFactory().update(newcos)


class OrderItemTest(unittest.TestCase):
    def test_OrderItemTest_inset(self):
        oi1 = OrderItem()
        oi1.owner_id=1
        oi1.csp_id=1
        oi1.csp_contact_id=1
        oi1.supplier_id=1
        oi1.airline_id=1
        oi1.csp_po_number="AB123"
        oi1.comments ="comments"
        oi1.start_date = datetime.date.today()
        oi1.end_date =  datetime.date.today()
        oi1.unit_price = 10

        oi2 = OrderItem()
        oi2.owner_id=1
        oi2.csp_id=1
        oi2.csp_contact_id=1
        oi2.supplier_id=1
        oi2.airline_id=1
        oi2.csp_po_number="XY123"
        oi2.comments ="more comments"
        oi2.start_date = datetime.date.today()
        oi2.end_date =  datetime.date.today()
        oi2.unit_price = 2

        orderItems = OrderItemFactory().insert([oi1,oi2])

        self.assertEqual(2,len(orderItems));

    def test_OrderItemTest_update(self):
        logging.info("@@@START UPDATE@@@")

        oi1 = OrderItem()
        oi1.owner_id=1
        oi1.csp_id=1
        oi1.csp_contact_id=1
        oi1.supplier_id=1
        oi1.airline_id=1
        oi1.csp_po_number="AB123"
        oi1.comments ="comments"
        oi1.start_date = datetime.date.today()
        oi1.end_date =  datetime.date.today()
        oi1.delivery_date = datetime.date.today()
        oi1.unit_price = 10

        oi2 = OrderItem()
        oi2.owner_id=1
        oi2.csp_id=1
        oi2.csp_contact_id=1
        oi2.supplier_id=1
        oi2.airline_id=1
        oi2.csp_po_number="XY123"
        oi2.comments ="more comments"
        oi2.start_date = datetime.date.today()
        oi2.end_date =  datetime.date.today()
        oi2.delivery_date = datetime.date.today()
        oi2.unit_price = 2

        orderItems = OrderItemFactory().insert([oi1, oi2])

        orderItems[0].comments = "changed comments"
        orderItems[1].comments = "changed comments second"

        logging.info("@@@ABOUT TO UPDATE@@@")

        OrderItemFactory().update(orderItems)

        self.assertEqual(2,len(orderItems));


    # def test_OrderItemTest_update(self):
    #     e1 = Phone()
    #     e1.address="a@a.com"
    #     e1.type = EmailType.Office
    #
    #     e2 = Phone()
    #     e2.address="b@b.com"
    #     e2.type = EmailType.Personal
    #
    #     e3 = Phone()
    #     e3.address="c@c.com"
    #     e3.type = EmailType.Office
    #
    #     emails = EmailFactory().insert([e1,e2,e3])
    #     self.assertEqual(3,len(emails));
    #
    #     emails[0].number = "pjc@.com"
    #     emails[0].type = EmailType.Office
    #
    #     phones = EmailFactory().update([emails[0]])