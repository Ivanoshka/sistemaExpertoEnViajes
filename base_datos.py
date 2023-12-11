# Base de datos de lugares turísticos en México
lugares_turisticos = {
    "Ciudad de México": {
        "descripcion": "La capital de México, llena de historia y cultura.",
        "imagen": "cdmx.jpg",
    },
    "Cancún": {
        "descripcion": "Famoso por sus hermosas playas y vida nocturna.",
        "imagen": "cancun.jpg",
    },
    "Guadalajara": {
        "descripcion": "Conocida por su arquitectura y gastronomía.",
        "imagen": "guadalajara.jpg",
    },
    # Agrega más lugares turísticos según sea necesario
}

# Acceder a la información de un lugar específico
ciudad = "Ciudad de México"
descripcion_ciudad = lugares_turisticos[ciudad]["descripcion"]
imagen_ciudad = lugares_turisticos[ciudad]["imagen"]

# Imprimir la información
print(f"Descripción de {ciudad}: {descripcion_ciudad}")
print(f"Imagen de {ciudad}: {imagen_ciudad}")
