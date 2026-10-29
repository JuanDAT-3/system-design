"""Un reloj que solo avanza cuando se lo pide la prueba. Ya esta
completo: no lo modifiques.

Un cache con tiempo de vida (TTL) necesita saber que hora es. Si lee
time.time(), probar que una entrada vence a los 30 segundos obliga a
esperar 30 segundos de verdad. Con este reloj, la prueba llama a
avanzar(30) y el cache ve pasar 30 segundos al instante.
"""


class RelojSimulado:
    def __init__(self):
        self.segundos = 0

    def ahora(self):
        return self.segundos

    def avanzar(self, segundos):
        self.segundos = self.segundos + segundos