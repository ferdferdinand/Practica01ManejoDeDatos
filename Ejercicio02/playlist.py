# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:09:55 2023

@author: HP
"""

from abc import ABC, abstractmethod
from cancion import *
from insercion_seleccion_class import *


class PlayListABC(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def agregar_cancion(self):
        pass

    @abstractmethod
    def ordenar_nombre(self):
        pass

    @abstractmethod
    def nombre_largo(self):
        pass

    @abstractmethod
    def ordenar_artista(self):
        pass

    @abstractmethod
    def ordenar_fecha(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class PlayList(PlayListABC):

    def __init__(self, nombre: str):
        self.nombre = nombre
        self.canciones = []

    def agregar_cancion(self, cancion: Cancion):
        self.canciones.append(cancion)

    def ordenar_nombre(self):
        InsercionNombre().ordenar(self.canciones)

    def ordenar_artista(self):
        SeleccionArtista().ordenar(self.canciones)
    
    def ordenar_fecha(self):
        SeleccionFecha().ordenar(self.canciones)
    
    def nombre_largo(self):
        caracteres = 0
        for cancion in self.canciones:
            if len(cancion.nombre) > caracteres:
                caracteres = len(cancion.nombre)
        return caracteres

    def __str__(self):
        caracteres = self.nombre_largo()
        playlist = ""
        for i, cancion in enumerate(self.canciones, 1):
            espacios = caracteres - len(cancion.nombre) + 5
            playlist += f"{i:02d}. " + cancion.nombre + " "*espacios + cancion.duracion + "\n"
        return self.nombre + "\n\n" + playlist


# --------------------------------parte script---------------------------------
import csv

playlist = PlayList("Alternativo/Indie")
with open("canciones.csv") as file:
    readed = csv.reader(file)

    for row in readed:
        cancion = Cancion(row[0], row[1], row[2], row[3])
        playlist.agregar_cancion(cancion)



print()
#playlist.ordenar_nombre()
#playlist.ordenar_artista()
playlist.ordenar_fecha()
print(playlist)
        
        
        
        
        
        
        
        
        
        
        
