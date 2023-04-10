from app.filters.FormLayout import Layout
import customtkinter as ctk


class Form3(Layout):

    def __init__(self, master, dao):
        # create main entry and button
        super().__init__(master, dao)

        #Update name for label and placeholders
        self.logo_form_label.configure(text="Búsqueda por Municipio&Rem")
        self.entry1.configure(placeholder_text="Municipio")
        self.entry2.destroy()
        self.entry3.destroy()

        self.optionmenu_var = ctk.StringVar(value="OM")  # set initial value
        self.entry2 = ctk.CTkOptionMenu(master=self.inputs_frame,
                                    values=["OM", "dm"],
                                    variable=self.optionmenu_var,
                                    width=220, height=30, hover=True)
        self.entry2.grid(row=0, column=1, padx=(20, 20), sticky="ew")

    def handle_submit(self):
        gasolineras = self.dao.db_consultar_gasolineras_por_municipio_y_rem(self.entry1.get().upper(),
                                                                            self.optionmenu_var.get())

        self.print_result_on_text(gasolineras)
