from gi.repository import Gtk, Gio


class ExemploHeaderBarGtk(Gtk.Window):
    def __init__(self):
        """METODO PARA CREAR UNA CABECERA PERSONALIZADA"""
        Gtk.Window.__init__(self, title="Exemplo HeaderBar para formulario")
        self.set_border_width(10)
        self.set_default_size(400, 200)

        # Cabecera
        cabeceira = Gtk.HeaderBar()
        cabeceira.set_show_close_button(True)
        cabeceira.props.title = "Exemplo HeaderBar"
        self.set_titlebar(cabeceira)

        # Icono
        boton = Gtk.Button()
        icono = Gio.ThemedIcon(name="mail-send-receive-symbolic")
        imaxe = Gtk.Image.new_from_gicon(icono, Gtk.IconSize.BUTTON)
        boton.add(imaxe)
        cabeceira.pack_end(boton)

        # Layout Box
        caixa = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
        Gtk.StyleContext.add_class(caixa.get_style_context(), "linked")

        # Flecha IZQ
        boton2 = Gtk.Button()
        boton2.add(Gtk.Arrow(Gtk.ArrowType.LEFT, Gtk.ShadowType.NONE))
        caixa.add(boton2)

        # Flecha DER
        boton3 = Gtk.Button()
        boton3.add(Gtk.Arrow(Gtk.ArrowType.RIGHT, Gtk.ShadowType.NONE))
        caixa.add(boton3)

        cabeceira.pack_start(caixa)
        self.add(Gtk.TextView())


# Instanciar
fiestra = ExemploHeaderBarGtk()
# Posicion Ventana
fiestra.set_position(Gtk.WindowPosition.CENTER)
# Resizable
fiestra.set_resizable(False)
# Cierre on Click
fiestra.connect("delete-event", Gtk.main_quit)
# Mostrar ventana
fiestra.show_all()
# Activar atencion de eventos
Gtk.main()
