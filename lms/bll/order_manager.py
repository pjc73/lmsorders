
class CspOrder():
    def __init__(self,l_id, l_csp_id , l_csp_contact_id, l_owner_id, l_owner_contact_id, l_invoice_number, l_invoice_date):
        self.id = l_id
        self.items = []
        self.csp = None
        self.csp_id = l_csp_id
        self.csp_accounts_payable_contact = None
        self.csp_accounts_payable_contact_id = l_csp_contact_id
        self.owner = None
        self.owner_id = l_owner_id
        self.owner_invoice_number = l_invoice_number
        self.owner_invoice_date = l_invoice_date
        self.owner_contact_id = l_owner_contact_id

    def build(self):
        return

class SupplierOrder():
    def __init__(self,l_id,l_supplier_id,l_supplier_contact_id,l_owner_id,l_owner_contact_id,l_owner_po_number,l_owner_po_date):
        self.id = l_id
        self.items = []
        self.supplier = None
        self.supplier_id = l_supplier_id
        self.supplier_contact = None
        self.supplier_contact_id = l_supplier_contact_id

        self.owner = None
        self.owner_id = l_owner_id
        self.owner_po_number = l_owner_po_number
        self.owner_po_date = l_owner_po_date
        self.owner_contact = ""
        self.owner_contact_id = l_owner_contact_id

        self.supplier_invoice_number = ""


class OrderItem():
    def __init__(self,l_id=-1,l_supplier_id=-1,l_csp_id=-1,l_csp_contact_id=-1,l_owner_id=-1,
                 l_airline_id=-1 ,  l_csp_po_number="",
                 l_owner_po_number="" , l_title="" , l_comments="" , l_start_date=""  , l_end_date="" , l_unit_price =0,
                 l_units=0 , l_delivery_format=""  , l_total_price=0 , l_delivery_date="",  l_supplier_invoice_number="" ):
        self.id = l_id
        self.supplier_id = l_supplier_id
        self.supplier = None
        self.csp_id = l_csp_id
        self.csp = None
        self.csp_contact_id = l_csp_contact_id
        self.csp_contact = None
        self.csp_po_number = l_csp_po_number
        self.supplier_invoice_number = l_supplier_invoice_number
        self.owner_id = l_owner_id
        self.owner = None
        self.owner_po_number = l_owner_po_number
        self.title = l_title
        self.comments = l_comments
        self.airline_id = l_airline_id
        self.airline = None
        self.start_date =l_start_date
        self.end_date = l_end_date
        self.unit_price = l_unit_price
        self.units = l_units
        self.delivery_format = l_delivery_format
        self.total_price = l_total_price
        self.delivery_date  = l_delivery_date

    def build(self):
        return



