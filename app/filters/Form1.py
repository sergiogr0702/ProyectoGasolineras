import tkintermapview
from app.filters.Aditional_window import AditionalWindow
from app.filters.ErrorDialog import ErrorDialog
from app.filters.FormLayout import Layout


class Form1(Layout):

    def __init__(self, master, dao):
        super().__init__(master, dao)
        self.clicked_marker = None
        self.marker_list = []
        self.toplevel_window = None

        # Update name for label and placeholders
        self.logo_form_label.configure(text="Búsqueda por localización")
        self.entry1.configure(placeholder_text="Latitud")
        self.entry2.configure(placeholder_text="Longitud")
        self.entry3.configure(placeholder_text="Distancia (km)")

        # create mapview
        self.map_widget = tkintermapview.TkinterMapView(self.master, corner_radius=3)
        self.map_widget.grid(row=1, column=1, rowspan=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

        self.map_widget.set_position(40.3754532, -3.7196977)
        self.map_widget.set_zoom(7)

        self.map_widget.add_left_click_map_command(self.left_click_event)

        self.open_toplevel()

    def get_frame(self):
        return [self.form_frame, self.map_widget, self.toplevel_window]

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AditionalWindow(self.master)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()

    def left_click_event(self, coordinates_tuple):
        if self.clicked_marker is not None:
            self.clicked_marker.delete()

        self.clicked_marker = self.map_widget.set_marker(coordinates_tuple[0], coordinates_tuple[1],
                                                         marker_color_circle="blue", marker_color_outside="blue")
        self.entry1.delete(0, 'end')
        self.entry2.delete(0, 'end')

        self.entry1.insert(0, coordinates_tuple[1])
        self.entry2.insert(0, coordinates_tuple[0])

    def validate_real_input(self, input_str):
        flag = True
        if not input_str.replace('.', '', 1).replace('-', '', 1).isdigit():
            # If the input contains non-numeric characters, return False
            flag = False

        return flag

    def validate_int_input(self, input_str):
        if not input_str.isdigit():
            # If the input contains non-numeric characters, return False
            return False

        # Convert the input to a number
        num = int(input_str)

        # Check if the number is positive and within the range [1, 10000]
        if 0 < num <= 10000:
            return True
        else:
            return False

    def cleanAllMarkers(self):
        for marker in self.marker_list:
            marker.delete()
        self.marker_list = []

    def print_points_on_map(self, gasolineras):
        self.cleanAllMarkers()
        for gasolinera in gasolineras:
            marker = self.map_widget.set_marker(gasolinera.loc['coordinates'][1],
                                                gasolinera.loc['coordinates'][0],
                                                text=gasolinera.rotulo)
            self.marker_list.append(marker)

    def print_points_on_text(self, gasolineras):
        textbox = self.toplevel_window.getTextbox()
        textbox.delete("0.0", "end")  # delete all text
        for gasolinera in gasolineras:
            textbox.insert("0.0", "Precio_g9: " + str(gasolinera.precio_g9) + "\n")
            textbox.insert("0.0", "Precio_g8: " + str(gasolinera.precio_g8) + "\n")
            textbox.insert("0.0", "Precio_g7: " + str(gasolinera.precio_g7) + "\n")
            textbox.insert("0.0", "Precio_g6: " + str(gasolinera.precio_g6) + "\n")
            textbox.insert("0.0", "Precio_g5: " + str(gasolinera.precio_g5) + "\n")
            textbox.insert("0.0", "Precio_g4: " + str(gasolinera.precio_g4) + "\n")
            textbox.insert("0.0", "Precio_g3: " + str(gasolinera.precio_g3) + "\n")
            textbox.insert("0.0", "Precio_g2: " + str(gasolinera.precio_g2) + "\n")
            textbox.insert("0.0", "Precio_g1: " + str(gasolinera.precio_g1) + "\n")
            textbox.insert("0.0", "Horario: " + gasolinera.horario + "\n")
            textbox.insert("0.0", "REM: " + gasolinera.rem + "\n")
            textbox.insert("0.0", "Tipo: " + gasolinera.tipo + "\n")
            textbox.insert("0.0", "Margen: " + gasolinera.margen + "\n")
            textbox.insert("0.0", "Dirección: " + gasolinera.direccion + "\n")
            textbox.insert("0.0", "CP: " + str(gasolinera.cp) + "\n")
            textbox.insert("0.0", "Municipio: " + gasolinera.municipio + "\n")
            textbox.insert("0.0", "Provincia: " + gasolinera.provinvia + "\n")
            textbox.insert("0.0", "Rótulo: " + gasolinera.rotulo + "\n")
            textbox.insert("0.0", "Rid: " + str(gasolinera.rid) + "\n")
            textbox.insert("0.0", "\n")

    def handle_submit(self):
        if not self.validate_real_input(self.entry1.get()):
            error_dialog = ErrorDialog(self.master, "Invalid input", "Please enter a valid number for the latitude")
            error_dialog.grab_set()
            return

        if not self.validate_real_input(self.entry2.get()):
            error_dialog = ErrorDialog(self.master, "Invalid input", "Please enter a valid number for the longitude")
            error_dialog.grab_set()
            return

        if not self.validate_real_input(self.entry3.get()):
            error_dialog = ErrorDialog(self.master, "Invalid input", "Please enter a valid number for the distance")
            error_dialog.grab_set()
            return

        print("Valid entry for location search")
        gasolineras = self.dao.db_consultar_gasolineras_por_ubicacion(float(self.entry1.get()),
                                                                      float(self.entry2.get()),
                                                                      int(self.entry3.get()))

        self.print_points_on_map(gasolineras)
        self.print_points_on_text(gasolineras)
