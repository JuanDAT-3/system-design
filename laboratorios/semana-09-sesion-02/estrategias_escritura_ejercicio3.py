"""Ejercicio 3: dos estrategias de escritura, write-through para las
reservas y write-back para el contador de visitas.

Corre las pruebas con:

    pytest test_estrategias_escritura_ejercicio3.py

No cambies los nombres de las clases ni de los metodos: los tests
dependen de que existan exactamente asi.
"""


class DisponibilidadWriteThrough:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.cache = {}

    def disponibilidad(self, cancha, fecha):
        # TODO: igual que cache-aside: si (cancha, fecha) no esta en
        # self.cache, consulta el repositorio y guarda la respuesta.
        # Devuelve lo que quede guardado.
        raise NotImplementedError

    def reservar(self, cancha, fecha, hora):
        # TODO: write-through. Verifica la hora en el repositorio y, si no
        # esta libre, devuelve False. Si esta libre, escribe la reserva en
        # el repositorio y, en la misma operacion, actualiza la entrada
        # del cache (si existe) para que ya no muestre esa hora como
        # libre, en vez de borrarla. Devuelve True.
        raise NotImplementedError


class VisitasWriteBack:
    def __init__(self, repositorio):
        self.repositorio = repositorio
        self.pendientes = {}

    def registrar_visita(self, cancha):
        # TODO: write-back. Suma 1 a la cuenta de esa cancha en
        # self.pendientes, sin escribir nada en el repositorio.
        raise NotImplementedError

    def visitas(self, cancha):
        # TODO: devuelve el total de visitas de la cancha: lo que ya esta
        # en el repositorio mas lo que todavia esta pendiente en el cache.
        raise NotImplementedError

    def vaciar(self):
        # TODO: escribe en el repositorio, con una sola llamada a
        # sumar_visitas(...) por cancha, todas las visitas pendientes, y
        # deja self.pendientes vacio.
        raise NotImplementedError

    def caer(self):
        # Simula que el proceso del cache se reinicia: lo que no se vacio
        # al repositorio se pierde. Ya esta completo.
        self.pendientes = {}