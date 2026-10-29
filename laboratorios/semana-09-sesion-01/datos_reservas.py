"""Datos de prueba de ReservaU para la sesion de sharding. Ya esta
completo: no lo modifiques.

generar_reservas() devuelve siempre las mismas 1000 reservas, repartidas
entre 4 campus y 300 estudiantes, con la misma proporcion que tiene hoy
ReservaU: la mayoria de las reservas son del Campus Norte, donde estan
casi todas las canchas. Ninguna cancha tiene dos reservas en la misma
fecha y hora.
"""

import zlib

CAMPUS = ["Campus Norte", "Campus Sur", "Campus Centro", "Campus Este"]
RESERVAS_POR_CAMPUS = [600, 200, 150, 50]
CANCHAS_POR_CAMPUS = [10, 3, 3, 1]
FECHAS = ["2026-10-19", "2026-10-20", "2026-10-21", "2026-10-22", "2026-10-23"]


class ReservaRegistrada:
    def __init__(self, id_reserva, id_estudiante, campus, cancha, fecha, hora):
        self.id_reserva = id_reserva
        self.id_estudiante = id_estudiante
        self.campus = campus
        self.cancha = cancha
        self.fecha = fecha
        self.hora = hora


def hash_estable(texto):
    """Convierte un texto en un entero, siempre el mismo para el mismo
    texto, en cualquier computador y en cualquier ejecucion.

    No uses hash() de Python para repartir datos entre shards: para un
    str, su valor cambia cada vez que se inicia Python, asi que la misma
    clave caeria en un shard distinto en cada ejecucion.
    """
    return zlib.crc32(texto.encode("utf-8"))


def generar_reservas():
    reservas = []
    numero = 0
    for posicion in range(len(CAMPUS)):
        campus = CAMPUS[posicion]
        for i in range(RESERVAS_POR_CAMPUS[posicion]):
            numero = numero + 1
            id_estudiante = "est-" + str(numero * 7 % 300 + 1).zfill(4)
            canchas = CANCHAS_POR_CAMPUS[posicion]
            cancha = "Cancha " + str(i % canchas + 1)
            fecha = FECHAS[(i // canchas) % len(FECHAS)]
            hora = 7 + (i // (canchas * len(FECHAS))) % 14
            reservas.append(ReservaRegistrada(numero, id_estudiante, campus, cancha, fecha, hora))
    return reservas