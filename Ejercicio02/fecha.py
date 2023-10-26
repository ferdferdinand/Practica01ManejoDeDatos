# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 00:39:50 2023

@author: Fernando
"""
from abc import ABC, abstractmethod


class FechaABC(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def __lt__(self, otra_fecha: object) -> bool:
        pass

    @abstractmethod
    def __gt__(self, otra_fecha: object) -> bool:
        pass

    @abstractmethod
    def __eq__(self, otra_fecha: object) -> bool:
        pass


class Fecha(FechaABC):

    def __init__(self, fecha: str):
        """
        Constructor de un dato Fecha

        Parameters
        ----------
        fecha : str
            Fecha str en formato dd/mm/aaaa

        Returns
        -------
        None.

        """
        fecha = fecha.split("/")
        self.dia = int(fecha[0])
        self.mes = int(fecha[1])
        self.anio = int(fecha[2])

    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.anio}"

    def __lt__(self, otra_fecha: FechaABC) -> bool:
        if self.anio != otra_fecha.anio:
            return self.anio < otra_fecha.anio
        elif self.mes != otra_fecha.mes:
            return self.mes < otra_fecha.mes
        return self.dia < otra_fecha.dia

    def __gt__(self, otra_fecha: FechaABC) -> bool:
        if self.anio != otra_fecha.anio:
            return self.anio > otra_fecha.anio
        elif self.mes != otra_fecha.mes:
            return self.mes > otra_fecha.mes
        return self.dia > otra_fecha.dia

    def __eq__(self,  otra_fecha: FechaABC) -> bool:
        return self.anio == otra_fecha.anio\
                and self.mes == otra_fecha.mes\
                and self.dia == otra_fecha.dia
