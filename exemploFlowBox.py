__author__ = 'oquintansocampo'
from gi.repository import Gtk, Gdk


class ExemploFlowBox(Gtk.Window):
    def __init__(self):
        """METODO PARA CREAR UNA PALETA CON COLORES CON UN LAYOUT FLOW BOX"""
        Gtk.Window.__init__(self, title="Exemplo FlowBox")
        self.set_border_width(10)
        self.set_default_size(675, 100)

        # Cabecera
        cabeceira = Gtk.HeaderBar(title="Exemplo Flow Box")
        cabeceira.set_show_close_button(True)
        cabeceira.set_subtitle("Exemplo de aplicacion FlowBox")
        cabeceira.props_show_close_button = True
        self.set_titlebar(cabeceira)

        # Scroll
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        # Layout FlowBox
        flowbox = Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.START)
        flowbox.set_max_children_per_line(30)
        flowbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.crea_flowbox(flowbox)
        scrolled.add(flowbox)
        self.add(scrolled)
        self.show_all()

    def crea_flowbox(self, flowbox):
        """ARRAY QUE ASIGNA COLORES"""
        cores = [
            'AliceBlue',
            'AntiqueWhite',
            'AntiqueWhite1',
            'AntiqueWhite2',
            'AntiqueWhite3',
            'AntiqueWhite4',
            'aqua',
            'aquamarine',
            'aquamarine1',
            'aquamarine2',
            'aquamarine3',
            'aquamarine4',
            'azure',
            'beige',
            'bisque',
            'black']
        for cor in cores:
            boton = self.asigna_cor(cor)
            flowbox.add(boton)

    def asigna_cor(self, cadea_cor):
        """CONVIERTE LOS COLORES ASIGNADOS EN BOTONES"""
        cor = Gdk.color_parse(cadea_cor)
        rgba = Gdk.RGBA.from_color(cor)
        boton = Gtk.Button()

        area = Gtk.DrawingArea()
        area.set_size_request(24, 24)
        area.override_background_color(0, rgba)
        boton.add(area)

        return boton


# Instanciar
fiestra = ExemploFlowBox()
# Posicion Ventana
fiestra.set_position(Gtk.WindowPosition.CENTER)
# Cierre on Click
fiestra.connect("delete-event", Gtk.main_quit)
# Mostrar ventana
fiestra.show_all()
# Activar atencion de eventos
Gtk.main()
