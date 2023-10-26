# -*- coding: utf-8 -*-
"""
Created on Thu Sep 21 11:04:18 2023

@author: Fernando
"""

from abc import ABC, abstractmethod


class OrdenableIterativoAbstractClass(ABC):

    @abstractmethod
    def ordenar(elementos):
        pass


class InsercionNombre(OrdenableIterativoAbstractClass):

    def ordenar(self, elementos):
        for i in range(1, len(elementos)):
            aux = elementos[i]
            indice = i
            while indice > 0 and aux.nombre < elementos[indice - 1].nombre:
                elementos[indice] = elementos[indice - 1]
                indice -= 1
            elementos[indice] = aux


class SeleccionArtista(OrdenableIterativoAbstractClass):

    def ordenar(self, elementos):
        for i in range(len(elementos)):
            for j in range(i+1, len(elementos)):
                if elementos[i].artista.lower() > elementos[j].artista.lower():
                    elementos[i], elementos[j] = elementos[j], elementos[i]
                elif elementos[i].artista.lower() == elementos[j].artista.lower():
                    if elementos[i].nombre > elementos[j].nombre:
                        elementos[i], elementos[j] = elementos[j], elementos[i]


class SeleccionFecha(OrdenableIterativoAbstractClass):

    def ordenar(self, elementos):
        for i in range(len(elementos)):
            for j in range(i+1, len(elementos)):
                if elementos[i].release_date > elementos[j].release_date:
                    elementos[i], elementos[j] = elementos[j], elementos[i]
                elif elementos[i].release_date == elementos[j].release_date:
                    if elementos[i].nombre > elementos[j].nombre:
                        elementos[i], elementos[j] = elementos[j], elementos[i]
