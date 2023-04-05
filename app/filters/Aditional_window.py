import customtkinter as ctk


class AditionalWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # configure window
        self.title("Gasolineras ordenadas por precio")
        self.geometry(f"{600}x{600}")

        self.label = ctk.CTkLabel(self, text="Respuesta",
                                  font=ctk.CTkFont(size=20, weight="bold"))
        self.label.pack(side="top", padx=20, pady=(20, 0))

        # create textbox
        self.textbox = ctk.CTkTextbox(self, border_width=5)
        self.textbox.pack(side="top", padx=20, pady=20, fill="both", expand=True)

        self.textbox.insert("0.0", "")

    def getTextbox(self):
        return self.textbox