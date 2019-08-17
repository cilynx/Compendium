# window.py
#
# Copyright 2019 Randy C. Will
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from gi.repository import Gtk


@Gtk.Template(resource_path='/com/wolfteck/Compendium/window.ui')
class CompendiumWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'CompendiumWindow'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        notebook = Gtk.Notebook()
        self.add(notebook)

        from .finance import FinanceTab
        finance_tab = FinanceTab()

        notebook.append_page(finance_tab.content, finance_tab.title)

        self.show_all()
