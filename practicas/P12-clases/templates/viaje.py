from __future__ import annotations


class Viaje:
    """
    Representa un viaje en bicicleta de un usuario. La unidad de la duración
    de un viaje es en segundos.
    """
    def __init__(self, duracion: int, estacion_origen: str, estacion_destino: str):
        self.duracion: int = duracion
        self.estacion_origen: str = estacion_origen
        self.estacion_destino: str = estacion_destino

    def __repr__(self):
        return f'Viaje(duracion={self.duracion} segs)'

print(Viaje(20,'Retiro','Tigre'))