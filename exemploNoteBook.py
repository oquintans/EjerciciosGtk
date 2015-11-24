from gi.repository import Gtk

__author__ = 'oquintansocampo'


class ExemploNotebookGtk(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Exemplo Notebook")
        self.set_border_width(10)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.paxina1 = Gtk.Box()
        self.paxina1.set_border_width(100)
        self.paxina1.add(Gtk.Label("Paxina por defecto"))
        self.notebook.append_page(
            self.paxina1,
            Gtk.Label("Texto plano")
        )

        self.paxina2 = Gtk.Box()
        self.paxina2.set_border_width(100)
        self.paxina2.add(Gtk.Label("Paxina con unha imaxe"))
        self.notebook.append_page(
            self.paxina2,
            Gtk.Image.new_from_icon_name("help-about", Gtk.IconSize.MENU)
        )


# Instanciar
fiestra = ExemploNotebookGtk()
# Posicion Ventana
fiestra.set_position(Gtk.WindowPosition.CENTER)
# Cierre on Click
fiestra.connect("delete-event", Gtk.main_quit)
# Mostrar ventana
fiestra.show_all()
# Activar atencion de eventos
Gtk.main()
