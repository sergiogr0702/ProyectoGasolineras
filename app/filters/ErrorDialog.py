import customtkinter as ctk


class ErrorDialog(ctk.CTkToplevel):
    def __init__(self, parent, title, message):
        super().__init__(parent)
        self.title(title)
        self.geometry("300x100")
        self.resizable(False, False)

        # Create a label to show the error message
        message_label = ctk.CTkLabel(self, text=message, font=("Arial", 12))
        message_label.pack(pady=10)

        # Create an "OK" button to close the dialog
        ok_button = ctk.CTkButton(self, text="OK", font=("Arial", 12), command=self.destroy)
        ok_button.pack(pady=10)
