from servidor import Servidor
from balanceador_ejercicio2 import BalanceadorRoundRobin


def tres_servidores():
    return [Servidor("a", 2), Servidor("b", 2), Servidor("c", 2)]


def test_reparte_en_turnos():
    servidores = tres_servidores()
    balanceador = BalanceadorRoundRobin(servidores)
    destinos = []
    for _ in range(6):
        destinos.append(balanceador.enviar(10))
    assert destinos == ["a", "b", "c", "a", "b", "c"]


def test_salta_un_servidor_caido():
    servidores = tres_servidores()
    servidores[1].caer()
    balanceador = BalanceadorRoundRobin(servidores)
    destinos = []
    for _ in range(4):
        destinos.append(balanceador.enviar(10))
    assert destinos == ["a", "c", "a", "c"]
    assert servidores[1].perdidas == 0


def test_salta_un_servidor_lleno():
    servidores = tres_servidores()
    servidores[0].atender(10)
    servidores[0].atender(10)
    balanceador = BalanceadorRoundRobin(servidores)
    assert balanceador.enviar(10) == "b"
    assert balanceador.enviar(10) == "c"
    assert balanceador.enviar(10) == "b"


def test_devuelve_none_si_nadie_puede_atender():
    servidores = tres_servidores()
    balanceador = BalanceadorRoundRobin(servidores)
    for _ in range(6):
        balanceador.enviar(10)
    assert balanceador.enviar(10) is None


def test_tres_servidores_de_100_atienden_el_pico_de_250():
    servidores = [Servidor("a", 100), Servidor("b", 100), Servidor("c", 100)]
    balanceador = BalanceadorRoundRobin(servidores)
    rechazadas = 0
    for _ in range(250):
        if balanceador.enviar(5) is None:
            rechazadas = rechazadas + 1
    assert rechazadas == 0
    assert servidores[0].atendidas == 84
    assert servidores[1].atendidas == 83
    assert servidores[2].atendidas == 83