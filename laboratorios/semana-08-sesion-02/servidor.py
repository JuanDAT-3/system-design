"""Arnes de simulacion de servidores de ReservaU. Ya esta completo: no
lo modifiques.

Cada Servidor atiende como maximo "capacidad" solicitudes al mismo
tiempo. Una solicitud ocupa una conexion durante "duracion" segundos
simulados; avanzar_un_segundo() descuenta un segundo a cada solicitud
en curso y libera las que terminaron.

Un servidor caido no responde: si alguien le envia una solicitud igual,
esa solicitud se pierde (en un sistema real, quien la hizo espera hasta
que se agota el tiempo de espera y recibe un error). El contador
"perdidas" registra cuantas solicitudes se perdieron asi.
"""


class Servidor:
    def __init__(self, nombre, capacidad):
        self.nombre = nombre
        self.capacidad = capacidad
        self.activas = []
        self.sano = True
        self.atendidas = 0
        self.perdidas = 0

    def conexiones_activas(self):
        return len(self.activas)

    def health_check(self):
        return self.sano

    def puede_atender(self):
        return self.sano and len(self.activas) < self.capacidad

    def atender(self, duracion):
        if not self.sano:
            self.perdidas = self.perdidas + 1
            return False
        if not self.puede_atender():
            return False
        self.activas.append(duracion)
        self.atendidas = self.atendidas + 1
        return True

    def avanzar_un_segundo(self):
        restantes = []
        for duracion in self.activas:
            if duracion > 1:
                restantes.append(duracion - 1)
        self.activas = restantes

    def caer(self):
        self.sano = False
        self.activas = []


def simular_trafico(balanceador, servidores, duraciones):
    """Envia una solicitud por segundo, con la duracion indicada en cada
    posicion de "duraciones", y avanza el reloj de todos los servidores
    despues de cada envio. Devuelve la lista de nombres de servidor que
    recibio cada solicitud (None si nadie la pudo atender).
    """
    destinos = []
    for duracion in duraciones:
        destinos.append(balanceador.enviar(duracion))
        for servidor in servidores:
            servidor.avanzar_un_segundo()
    return destinos