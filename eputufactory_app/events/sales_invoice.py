import frappe
from erpnext.accounts.utils import get_balance_on


def validate(doc, event):
    """
        Do something on submit sales invoice
    """
    balance = get_balance_on(
        date=frappe.utils.today(),
        party_type='Customer',
        party=doc.customer
    )
    doc.customer_balance = balance
    doc.as_at = frappe.utils.today()
    #doc = frappe.get_doc('Sales Invoice', doc.name)
    #doc.db_set('customer_balance', balance)
    #doc.db_set('as_at', frappe.utils.today())
    #doc.reload()
