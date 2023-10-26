# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:01:40 2023

@author: HP
"""
from abc import ABC, abstractmethod
from fecha import *


class CancionABC(ABC):

    @abstractmethod
    def __init__(self):
        pass


class Cancion(CancionABC):

    def __init__(self, nombre_cancion: str, duracion: str,
                 artista: str, release_date: str):
        self.nombre = nombre_cancion
        self.duracion = duracion
        self.artista = artista
        self.release_date = Fecha(release_date)
