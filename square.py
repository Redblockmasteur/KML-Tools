import math
import xml.etree.ElementTree as ET
import tkinter as tk
from tkinter import filedialog
from geopy.distance import great_circle

def generate_kml(lat, lon, size_meters, output_file, line_color, line_width, extended_data_name, extended_data_value):
    # Déterminer les coins du carré en utilisant les directions cardinales avec great_circle
    half_size = size_meters / 2
    
    top = great_circle(meters=half_size).destination((lat, lon), 0)    # Nord (0°)
    bottom = great_circle(meters=half_size).destination((lat, lon), 180) # Sud (180°)
    left = great_circle(meters=half_size).destination((lat, lon), 270)  # Ouest (270°)
    right = great_circle(meters=half_size).destination((lat, lon), 90)  # Est (90°)
    
    coords = [
        (top.latitude, left.longitude),    # Haut gauche
        (top.latitude, right.longitude),   # Haut droit
        (bottom.latitude, right.longitude),# Bas droit
        (bottom.latitude, left.longitude), # Bas gauche
        (top.latitude, left.longitude)     # Boucle fermée
    ]
    
    # Création du fichier KML
    kml = ET.Element("kml", xmlns="http://www.opengis.net/kml/2.2", 
                     attrib={"xmlns:gx": "http://www.google.com/kml/ext/2.2", 
                             "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance", 
                             "xsi:schemaLocation": "http://www.opengis.net/kml/2.2 https://developers.google.com/kml/schema/kml22gx.xsd"})
    document = ET.SubElement(kml, "Document")
    ET.SubElement(document, "ExtendedData")
    placemark = ET.SubElement(document, "Placemark")
    
    # Ajouter le style
    style = ET.SubElement(placemark, "Style")
    linestyle = ET.SubElement(style, "LineStyle")
    ET.SubElement(linestyle, "color").text = line_color
    ET.SubElement(linestyle, "width").text = str(line_width)
    
    polystyle = ET.SubElement(style, "PolyStyle")
    ET.SubElement(polystyle, "fill").text = "0"  # Pas de remplissage
    
    # Ajouter les données étendues
    extended_data = ET.SubElement(placemark, "ExtendedData")
    data = ET.SubElement(extended_data, "Data", name=extended_data_name)
    ET.SubElement(data, "value").text = extended_data_value
    
    # Ajouter le polygone
    polygon = ET.SubElement(placemark, "Polygon")
    outer_boundary = ET.SubElement(polygon, "outerBoundaryIs")
    linear_ring = ET.SubElement(outer_boundary, "LinearRing")
    coordinates = ET.SubElement(linear_ring, "coordinates")
    
    # Ajouter les coordonnées au KML
    coordinates.text = " ".join(f"{lon},{lat},0" for lat, lon in coords)
    
    # Sauvegarder le fichier
    tree = ET.ElementTree(kml)
    tree.write(output_file, encoding="utf-8", xml_declaration=True)
    print(f"Fichier KML généré : {output_file}")

def open_gui():
    def generate():
        lat = float(entry_lat.get())
        lon = float(entry_lon.get())
        size_meters = float(entry_size.get())
        output_file = filedialog.asksaveasfilename(defaultextension=".kml", filetypes=[("KML files", "*.kml")])
        if not output_file:
            return
        line_color = entry_color.get()
        line_width = int(entry_width.get())
        extended_data_name = entry_data_name.get()
        extended_data_value = entry_data_value.get()
        generate_kml(lat, lon, size_meters, output_file, line_color, line_width, extended_data_name, extended_data_value)
        status_label.config(text=f"Fichier enregistré : {output_file}")
    
    root = tk.Tk()
    root.title("Générateur de KML")
    
    tk.Label(root, text="Latitude :").grid(row=0, column=0)
    entry_lat = tk.Entry(root)
    entry_lat.grid(row=0, column=1)
    
    tk.Label(root, text="Longitude :").grid(row=1, column=0)
    entry_lon = tk.Entry(root)
    entry_lon.grid(row=1, column=1)
    
    tk.Label(root, text="Taille (m) :").grid(row=2, column=0)
    entry_size = tk.Entry(root)
    entry_size.grid(row=2, column=1)
    
    tk.Label(root, text="Couleur ligne (AABBGGRR) :").grid(row=3, column=0)
    entry_color = tk.Entry(root)
    entry_color.insert(0, "ff0000ff")
    entry_color.grid(row=3, column=1)
    
    tk.Label(root, text="Largeur ligne :").grid(row=4, column=0)
    entry_width = tk.Entry(root)
    entry_width.insert(0, "5")
    entry_width.grid(row=4, column=1)
    
    tk.Label(root, text="Nom Extended Data :").grid(row=5, column=0)
    entry_data_name = tk.Entry(root)
    entry_data_name.grid(row=5, column=1)
    
    tk.Label(root, text="Valeur Extended Data :").grid(row=6, column=0)
    entry_data_value = tk.Entry(root)
    entry_data_value.grid(row=6, column=1)
    
    generate_button = tk.Button(root, text="Générer KML", command=generate)
    generate_button.grid(row=7, column=0, columnspan=2)
    
    status_label = tk.Label(root, text="")
    status_label.grid(row=8, column=0, columnspan=2)
    
    root.mainloop()

if __name__ == "__main__":
    open_gui()
