public class VehicleTab : GLib.Object {
    public Gtk.Label title = new Gtk.Label ("Vehicle");

    public Gtk.Notebook content = new Gtk.Notebook ();

    public VehicleTab () {

        content.set_tab_pos(Gtk.PositionType.LEFT);

        Gtk.Label title = new Gtk.Label ("Vehicle 1");
        Gtk.Label stuff = new Gtk.Label ("Vehicle 1 stuff...");
        content.append_page (stuff, title);

        title = new Gtk.Label ("Vehicle 2");
        stuff = new Gtk.Label ("Vehicle 2 stuff...");
        content.append_page (stuff, title);
    }
}
