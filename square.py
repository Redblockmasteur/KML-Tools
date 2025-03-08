import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog, ttk
from geopy.distance import great_circle
import tkintermapview
from PIL import Image, ImageTk

# Dictionnaire de langues
LANGUAGES = {
    "fr": {
        "title": "Générateur de KML",
        "latitude": "Latitude :",
        "longitude": "Longitude :",
        "size": "Longueur du côté (m) :",
        "line_color": "Couleur ligne (AABBVVRR) :",
        "line_width": "Largeur ligne :",
        "extended_data_name": "Nom Extended Data :",
        "extended_data_value": "Valeur Extended Data :",
        "generate": "Générer KML",
        "saved": "Fichier enregistré : ",
        "center": "Centre du Carré"
    },
    "en": {
        "title": "KML Generator",
        "latitude": "Latitude:",
        "longitude": "Longitude:",
        "size": "Side length (m):",
        "line_color": "Line color (AABBGGRR):",
        "line_width": "Line width:",
        "extended_data_name": "Extended Data Name:",
        "extended_data_value": "Extended Data Value:",
        "generate": "Generate KML",
        "saved": "File saved: ",
        "center": "Square center"
    }
}

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.selected_language = "fr"
        self.title(LANGUAGES[self.selected_language]["title"])
        self.geometry("800x650")
        
        self.icon_image = ImageTk.PhotoImage(file="img/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon_image)
        
        lang_frame = tk.Frame(self)
        lang_frame.pack(pady=5)
        tk.Label(lang_frame, text="Langue / Language:").pack(side=tk.LEFT)
        self.lang_selector = ttk.Combobox(lang_frame, values=["fr", "en"], state="readonly")
        self.lang_selector.set("fr")
        self.lang_selector.pack(side=tk.LEFT, padx=5)
        self.lang_selector.bind("<<ComboboxSelected>>", self.change_language)
        
        self.map_frame = tk.Frame(self)
        self.map_frame.pack(pady=10)
        
        self.map_widget = tkintermapview.TkinterMapView(self.map_frame, width=800, height=400, corner_radius=0)
        self.map_widget.set_position(36, 14)
        self.map_widget.set_zoom(0)
        self.map_widget.pack()
        self.map_widget.add_left_click_map_command(self.update_coords)
        
        input_frame = tk.Frame(self)
        input_frame.pack(pady=10)
        
        self.lat_var = tk.StringVar()
        self.lon_var = tk.StringVar()
        self.size_var = tk.StringVar(value="1000")
        self.color_var = tk.StringVar(value="ff0000ff")
        self.width_var = tk.StringVar(value="5")
        self.data_name_var = tk.StringVar()
        self.data_value_var = tk.StringVar()
        
        self.labels = {}
        for i, key in enumerate(["latitude", "longitude", "size", "line_color", "line_width", "extended_data_name", "extended_data_value"]):
            self.labels[key] = tk.Label(input_frame, text=LANGUAGES[self.selected_language][key])
            self.labels[key].grid(row=i, column=0, sticky="w")
        
        self.entry_lat = tk.Entry(input_frame, textvariable=self.lat_var)
        self.entry_lat.grid(row=0, column=1)
        
        self.entry_lon = tk.Entry(input_frame, textvariable=self.lon_var)
        self.entry_lon.grid(row=1, column=1)
        
        self.entry_size = tk.Entry(input_frame, textvariable=self.size_var)
        self.entry_size.grid(row=2, column=1)
        
        self.entry_color = tk.Entry(input_frame, textvariable=self.color_var)
        self.entry_color.grid(row=3, column=1)
        
        self.entry_width = tk.Entry(input_frame, textvariable=self.width_var)
        self.entry_width.grid(row=4, column=1)
        
        self.entry_data_name = tk.Entry(input_frame, textvariable=self.data_name_var)
        self.entry_data_name.grid(row=5, column=1)
        
        self.entry_data_value = tk.Entry(input_frame, textvariable=self.data_value_var)
        self.entry_data_value.grid(row=6, column=1)
        
        self.generate_button = tk.Button(input_frame, text=LANGUAGES[self.selected_language]["generate"], command=self.generate_kml)
        self.generate_button.grid(row=7, column=0, columnspan=2)
        
        self.status_label = tk.Label(self, text="")
        self.status_label.pack()
        
        self.selected_marker = None
    
    def change_language(self, event):
        self.selected_language = self.lang_selector.get()
        self.title(LANGUAGES[self.selected_language]["title"])
        for key in self.labels:
            self.labels[key].config(text=LANGUAGES[self.selected_language][key])
        self.generate_button.config(text=LANGUAGES[self.selected_language]["generate"])
    
    def update_coords(self, coords):
        lat, lon = coords
        self.lat_var.set(str(lat))
        self.lon_var.set(str(lon))
        if self.selected_marker:
            self.selected_marker.delete()
        self.selected_marker = self.map_widget.set_marker(lat, lon, text=LANGUAGES[self.selected_language]["center"])
    
    def generate_kml(self):
        output_file = filedialog.asksaveasfilename(defaultextension=".kml", filetypes=[("KML files", "*.kml")])
        if not output_file:
            return
        
        generate_kml(
            float(self.lat_var.get()),
            float(self.lon_var.get()),
            float(self.size_var.get()),
            output_file,
            self.color_var.get(),
            int(self.width_var.get()),
            self.data_name_var.get(),
            self.data_value_var.get()
        )
        self.status_label.config(text=LANGUAGES[self.selected_language]["saved"] + output_file)

if __name__ == "__main__":
    app = App()
    app.mainloop()
