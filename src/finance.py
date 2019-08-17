from gi.repository import GObject, Gtk

class FinanceTab(GObject.Object):

    def __init__(self):
        self.title = Gtk.Label("Finance")

        self.content = Gtk.Notebook()
        self.content.set_tab_pos(Gtk.PositionType.LEFT)

        title = Gtk.Label("Account 1")
        stuff = Gtk.Label("Account 1 stuff...")
        self.content.append_page(stuff, title)

        title = Gtk.Label("Account 2")
        stuff = Gtk.Label("Account 2 stuff...")
        self.content.append_page(stuff, title)
