from gi.repository import GObject, Gtk
from datetime import datetime

class AccountTab():

    def __init__(self, filename):
        with open(filename, 'r') as fileobj:
            from ofxparse import OfxParser
            ofx = OfxParser.parse(fileobj)
        self.store = Gtk.ListStore(GObject.TYPE_STRING, GObject.TYPE_STRING, GObject.TYPE_FLOAT)
        self.content = Gtk.TreeView(self.store)
        for column_title, i in enumerate(["Date", "Memo", "Amount"]):
            renderer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(i, renderer, text=column_title)
            self.content.append_column(column)

        account = ofx.account
        self.label = Gtk.Label(account.account_id)

        statement = account.statement

        for transaction in statement.transactions:
            self.store.append([transaction.date.strftime("%m/%d/%Y, %H:%M:%S"), transaction.memo, transaction.amount])
