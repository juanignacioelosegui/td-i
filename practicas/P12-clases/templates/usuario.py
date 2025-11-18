from __future__ import annotations


class Usuario:
    def __init__(self, id_usuario: int, edad: int):
        self.id_usuario: int = id_usuario
        self.edad: int = edad

    def __repr__(self):
        return f'Usuario(id={self.id_usuario}, edad={self.edad})'
