import customtkinter as ctk
from app.filters.Form1 import Form1
from app.filters.Form2 import Form2
from app.filters.Form3 import Form3
from data.gasolineraDAO import GasolineraDAO

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.dao = GasolineraDAO()

        self.activeFrame = []

        # configure window
        self.title("Repostando por España")
        self.geometry(f"{1300}x{800}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets
        self.sidebar_frame = ctk.CTkFrame(self, width=140, corner_radius=0, border_width=5)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Repostando\npor España",
                                       font=ctk.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.sidebar_button_1 = ctk.CTkButton(self.sidebar_frame, text="Coordenadas",
                                              command=self.sidebar_button_event1)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = ctk.CTkButton(self.sidebar_frame, text="Rotulo/Direccion",
                                              command=self.sidebar_button_event2)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = ctk.CTkButton(self.sidebar_frame, text="Municipio&Rem",
                                              command=self.sidebar_button_event3)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Apariencia:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light",
                                                                                         "Dark", "System"],
                                                             command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = ctk.CTkLabel(self.sidebar_frame, text="Escalado de IU:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%",
                                                                                 "110%", "120%"],
                                                     command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

        # create the first form of the app
        self.form = Form1(self, self.dao)
        self.activeFrame = self.form.get_frame()

        # set default config values
        self.appearance_mode_optionemenu.set("Light")
        self.scaling_optionemenu.set("100%")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

    def clean_window(self):
        self.activeFrame[0].destroy()
        self.activeFrame[1].destroy()
        if self.activeFrame[2] is not None:
            self.activeFrame[2].destroy()

    def sidebar_button_event1(self):
        self.clean_window()
        self.form = Form1(self, self.dao)
        self.activeFrame = self.form.get_frame()

    def sidebar_button_event2(self):
        self.clean_window()
        self.form = Form2(self, self.dao)
        self.activeFrame = self.form.get_frame()

    def sidebar_button_event3(self):
        self.clean_window()
        self.form = Form3(self, self.dao)
        self.activeFrame = self.form.get_frame()
