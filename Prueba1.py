__author__ = 'oquintansocampo'

from gi.repository import Gtk


class FiestraPrincipal:
    def __init__(self):
        ficheiro = "exemploGlade.glade"
        builder = Gtk.Builder()
        builder.add_from_file(ficheiro)

        sinais = {"on_txtCadro_activate": self.on_txtCadro_activate,
                  "on_btnAceptar_clicked": self.on_btnBoton_clicked,
                  "on_fiestraPrincipal_destroy": Gtk.main_quit}

        builder.connect_signals(sinais)
        self.etiqueta = builder.get_object("lblEtiqueta")
        self.cadroTexto = builder.get_object("txtCadro")
        self.fiesra = builder.get_object("FiestraPrincipal")

    def on_btnBoton_clicked(self, control):
        texto = self.cadroTexto.get_text()
        self.etiqueta.set_text("ola %s" % texto)

    def on_txtCadro_activate(self, control):
        self.on_btnBoton_clicked(control)


if __name__ == "__main__":
    FiestraPrincipal()
    Gtk.main()
