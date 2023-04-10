from app.filters.FormLayout import Layout


class Form2(Layout):

    def __init__(self, master, dao):
        # create main entry and button
        super().__init__(master, dao)

        #Update name for label and placeholders
        self.logo_form_label.configure(text="Búsqueda por Rotulo/Direccion")
        self.entry1.configure(placeholder_text="Nombre del Rotulo/Direccion")
        self.entry2.destroy()
        self.entry3.destroy()

    def handle_submit(self):
        gasolineras = self.dao.db_consultar_gasolineras_por_rotulo_o_direccion(self.entry1.get())

        self.print_result_on_text(gasolineras)
