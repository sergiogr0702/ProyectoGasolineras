from app.filters.FormLayout import Layout


class Form2(Layout):

    def __init__(self, master, dao):
        # create main entry and button
        super().__init__(master, dao)

        #Update name for label and placeholders
        self.logo_form_label.configure(text="Búsqueda por Localidad & Rótulo")
        self.entry1.configure(placeholder_text="Nombre de la localidad")
        self.entry2.configure(placeholder_text="Nombre del rótulo")
        self.entry3.destroy()

    def handle_submit(self):
        localidadUpper = self.entry1.get().upper()
        rotuloUpper = self.entry2.get().upper()
        gasolineras = self.dao.db_consultar_gasolineras_por_localidad_y_rotulo(localidadUpper, rotuloUpper)

        self.print_result_on_text(gasolineras)
