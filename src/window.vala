/* window.vala
 *
 * Copyright 2019 Randy C. Will
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

namespace Compendium {
	[GtkTemplate (ui = "/com/wolfteck/Compendium/window.ui")]
	public class Window : Gtk.ApplicationWindow {
		public Window (Gtk.Application app) {
			Object (application: app);

			Gtk.Notebook notebook = new Gtk.Notebook ();
			this.add (notebook);

			var finance_tab     = new FinanceTab ();
			var vehicle_tab     = new VehicleTab ();
			var house_tab       = new HouseTab ();
			var pool_tab        = new PoolTab ();
			var wishlist_tab    = new WishlistTab ();

			notebook.append_page (finance_tab.content,  finance_tab.title);
			notebook.append_page (vehicle_tab.content,  vehicle_tab.title);
			notebook.append_page (house_tab.content,    house_tab.title);
			notebook.append_page (pool_tab.content,     pool_tab.title);
			notebook.append_page (wishlist_tab.content, wishlist_tab.title);

			show_all ();
		}
	}
}
