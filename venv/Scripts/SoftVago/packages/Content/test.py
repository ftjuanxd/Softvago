import os

# Obtén la ruta absoluta del script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Combina la ruta del script con la ruta relativa al archivo favicon.ico
icon_path = os.path.join(script_dir, "../../../assets/favicon.ico")

# Verifica si el archivo existe
if os.path.exists(icon_path):
    print(f"El archivo se encontró en: {icon_path}")
else:
    print(f"El archivo no se encontró en: {icon_path}")
