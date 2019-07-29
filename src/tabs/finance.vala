public class FinanceTab : GLib.Object {
    public Gtk.Label title = new Gtk.Label ("Finance");

    public Gtk.Notebook content = new Gtk.Notebook ();

    public FinanceTab () {

        content.set_tab_pos(Gtk.PositionType.LEFT);

        Gtk.Label title = new Gtk.Label ("Account 1");
        Gtk.Label stuff = new Gtk.Label ("Account 1 stuff...");
        content.append_page (stuff, title);

        title = new Gtk.Label ("Account 2");
        stuff = new Gtk.Label ("Account 2 stuff...");
        content.append_page (stuff, title);
    }
}
