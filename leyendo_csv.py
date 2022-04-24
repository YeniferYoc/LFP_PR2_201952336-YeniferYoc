import csv
nombre_archivo = "original.csv"
with open(nombre_archivo, "r", encoding='utf-8') as archivo:
    # Omitir el encabezado
    next(archivo, None)
    for linea in archivo:
        # Remover salto de línea
        linea = linea.replace("-",",")
        linea = linea.replace("/",",")
        # Ahora convertimos la línea a arreglo con split
        separador = ","
        lista = linea.split(",")
        # Tenemos la lista. En la 0 tenemos el nombre, en la 1 la calificación y en la 2 el precio
        fecha = str(lista[0])
        inicio = int(lista[1])
        fina = int(lista[2])
        jornada = int(lista[3])
        equipo1 = str(lista[4])
        '''equipo1 = equipo1.replace("Ã±","ñ")
        equipo1 = equipo1.replace("Ã¡","á")
        equipo1 = equipo1.replace("Ã©","é")
        equipo1 = equipo1.replace("Ã­ ","í")
        equipo1 = equipo1.replace("Ã³","ó")
        equipo1 = equipo1.replace("Ãº","ú")'''
        equipo2 = str(lista[5])
        '''equipo2 = equipo2.replace("Ã±","ñ")
        equipo2 = equipo2.replace("Ã¡","á")
        equipo2 = equipo2.replace("Ã©","é")
        equipo2 = equipo2.replace("Ã­ ","í")
        equipo2 = equipo2.replace("Ã³","ó")
        equipo2 = equipo2.replace("Ãº","ú")'''
        goles1 = int(lista[6])
        goles2 = int(lista[7])
        print(
            f"fecha: '{fecha}' temporada {inicio} - {fina} jornada {jornada} equipo1 {equipo1} goles1 {goles1} equipo 2 {equipo2} goles2 {goles2}")

