import customtkinter as ctk

class MainWindow(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        self.geometry("1000x600")
        self.title("Saludmed")
        self.iconbitmap("assets/pill.ico")
        self.resizable(1,1)

        self.columnconfigure(0, weight =0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)

        self.container = ctk.CTkFrame(self, fg_color="#f8f9fa")
        self.container.grid(row=0, column=1, sticky="nsew")
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)

        self.sidebar = ctk.CTkFrame(self, corner_radius=0, fg_color="#8DD8FF")
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_columnconfigure(0, weight=1)

    def execute_app(self):
        self.mainloop()
    