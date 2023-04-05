import customtkinter as ctk


class Layout:

    def __init__(self, master, dao):
        self.master = master
        self.dao = dao

        # create main entry and button
        self.form_frame = ctk.CTkFrame(self.master, width=140, corner_radius=5, border_width=5)
        self.form_frame.grid(row=0, column=1, padx=(20, 20), pady=(20, 0), rowspan=1, sticky="nsew")
        self.form_frame.grid_rowconfigure(1, weight=1)
        self.form_frame.grid_columnconfigure(2, weight=1)
        self.logo_form_label = ctk.CTkLabel(self.form_frame, text="Búsqueda por localización",
                                            font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_form_label.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="nsew")

        self.inputs_frame = ctk.CTkFrame(self.form_frame, width=140, corner_radius=5)
        self.inputs_frame.grid(row=1, column=1, padx=(20, 20), rowspan=1, sticky="nsew")
        self.inputs_frame.grid_rowconfigure(0, weight=1)
        self.inputs_frame.grid_columnconfigure(4, weight=1)

        self.entry1 = ctk.CTkEntry(self.inputs_frame, width=220, height=30, placeholder_text="Longitud")
        self.entry1.grid(row=0, column=0, padx=(20, 20), sticky="ew")

        self.entry2 = ctk.CTkEntry(self.inputs_frame, width=220, height=30, placeholder_text="Latitud")
        self.entry2.grid(row=0, column=1, padx=(20, 20), sticky="ew")

        self.entry3 = ctk.CTkEntry(self.inputs_frame, width=220, height=30, placeholder_text="Distancia (km)")
        self.entry3.grid(row=0, column=2, padx=(20, 20), sticky="ew")

        self.main_button_1 = ctk.CTkButton(self.form_frame, text="Buscar", fg_color="transparent",
                                           border_width=2, text_color=("gray10", "#DCE4EE"),
                                           command=self.handle_submit)
        self.main_button_1.grid(row=2, column=2, padx=(20, 20), pady=(20, 20), sticky="e")
        self.main_button_1.configure(cursor="hand2")

        # create textbox
        self.textbox = ctk.CTkTextbox(self.master, width=250, border_width=5)
        self.textbox.grid(row=1, column=1, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.textbox.insert("0.0", "")

    def get_frame(self):
        return [self.form_frame, self.textbox, None]

    def handle_submit(self):
        pass
