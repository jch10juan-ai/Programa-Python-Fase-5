#Nombre del estudiante: Juan Camilo Hincapié Fernández
#Grupo: 481
#Programa: Ingeniería de Telecomunicaciones 

videoteca = [
    ["Batman: El caballero de la noche",     2008, 9.0, "Acción"],
    ["Inception",                            2010, 8.8, "Ciencia Ficción"],
    ["Oppenheimer",                          2023, 8.5, "Drama"],
    ["Son como niños",                       2010, 6.0, "Comedia"],
    ["Batman",                               2022, 7.9, "Acción"],
    ["Avengers: Endgame",                    2019, 8.4, "Acción"],
    ["Interstellar",                         2014, 8.6, "Ciencia Ficción"],
    ["Dune: Parte Dos",                      2024, 8.7, "Ciencia Ficción"],
    ["Parasite",                             2019, 8.5, "Drama"],
    ["The Marvels",                          2023, 5.3, "Acción"],
]

def contar_titulos(peliculas, anio_minimo, calificacion_minima):
    conteo = 0
    for pelicula in peliculas:
        if pelicula[2] >= calificacion_minima and pelicula[1] >= anio_minimo:
            conteo += 1
    return conteo

ANIO_LIMITE         = 2019
UMBRAL_CALIFICACION = 8.2  

# salida

total = contar_titulos(videoteca, ANIO_LIMITE, UMBRAL_CALIFICACION)

print(f"\n VIDEOTECA DIGITAL \n\n Año mínimo: {ANIO_LIMITE}")
print(f" Calificación mín : {UMBRAL_CALIFICACION}\n Títulos encontrados: {total}\n")