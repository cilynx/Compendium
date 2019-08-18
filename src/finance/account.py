from gi.repository import GObject, Gtk
from datetime import datetime

class AccountTab():

    def __init__(self, filename):
        with open(filename, 'r') as fileobj:
            from ofxparse import OfxParser
            ofx = OfxParser.parse(fileobj)
        self.store = Gtk.ListStore(GObject.TYPE_STRING, GObject.TYPE_STRING, GObject.TYPE_STRING, GObject.TYPE_STRING)
        treeview = Gtk.TreeView(self.store)
        for i, column_title in enumerate(["Date", "Memo", "Withdrawal", "Deposit"]):
            cell = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(column_title, cell, text=i)
            if column_title in ("Withdrawal", "Deposit"):
                cell.set_alignment(1, 0.5)
            treeview.append_column(column)

        account = ofx.account
        statement = account.statement

        for transaction in statement.transactions:
            if transaction.amount < 0:
                self.store.append([transaction.date.strftime("%m/%d/%Y"), transaction.memo, '{:2f}'.format(transaction.amount), None])
            else:
                self.store.append([transaction.date.strftime("%m/%d/%Y"), transaction.memo, None, '{:2f}'.format(transaction.amount)])

        self.label = Gtk.Label(account.account_id)
        self.content = Gtk.ScrolledWindow()
        self.content.add(treeview)
