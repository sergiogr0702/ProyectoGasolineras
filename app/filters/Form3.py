from app.filters.FormLayout import Layout


class Form3(Layout):

    def __init__(self, master, dao):
        # create main entry and button
        super().__init__(master, dao)

        #Update name for label and placeholders
        self.logo_form_label.configure(text="Búsqueda por Municipio&Rem")
        self.entry1.configure(placeholder_text="Municipio")
        self.entry2.configure(placeholder_text="Rem")
        self.entry3.destroy()
