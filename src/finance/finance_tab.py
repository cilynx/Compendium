from gi.repository import GObject, Gtk

class FinanceTab(GObject.Object):

    def __init__(self):
        self.title = Gtk.Label("Finance")

        self.content = Gtk.Notebook()
        self.content.set_tab_pos(Gtk.PositionType.LEFT)

        self.new_account_id = Gtk.Label("+")

        self.listbox = Gtk.ListBox()

        row = Gtk.ListBoxRow()
        self.button = Gtk.Button("Populate from OFX")
        self.button.connect("clicked", self.on_button_clicked)
        row.add(self.button)

        self.listbox.add(row)

        self.content.append_page(self.listbox, self.new_account_id)

    def on_button_clicked(self, widget):
        dialog = Gtk.FileChooserDialog("Please choose a file", None, Gtk.FileChooserAction.OPEN,
                                       (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        ext_filter = Gtk.FileFilter()
        ext_filter.set_name("OFX / QFX")
        ext_filter.add_pattern("*.[OoQq][Ff][Xx]")
        dialog.add_filter(ext_filter)

        response = dialog.run()

        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())

            from .account import AccountTab
            account_tab = AccountTab(dialog.get_filename())

            self.content.append_page(account_tab.content, account_tab.label)
            self.content.show_all()

        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()
