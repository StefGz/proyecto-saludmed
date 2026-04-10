import ttkbootstrap as tb
from ttkbootstrap.constants import *

class MainWindow(tb.Window):

    def __init__(self):
        super().__init__(themename="litera")
        self.withdraw()
        self.geometry("1000x600")
        self.title("Saludmed")
        self.iconbitmap("assets/pill.ico")
        self.resizable(1,1)

        style = tb.Style()
        style.configure("Container.TFrame", background="#f8f9fa")
        style.configure("Sidebar.TFrame", background="#8DD8FF")
        
        self.columnconfigure(0, weight =0)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        
        self.container = tb.Frame(self, style="Container.TFrame")
        self.container.grid(row=0, column=1, sticky="nsew")
        self.container.grid_columnconfigure(0, weight=1)
        self.container.grid_rowconfigure(0, weight=1)
        
        self.sidebar = tb.Frame(self, style="Sidebar.TFrame", width=200)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_columnconfigure(0, weight=1)
        self.sidebar.grid_propagate(False)

        self.place_window_center()

        self.after(10, self.deiconify)

    def execute_app(self):
        self.mainloop()
