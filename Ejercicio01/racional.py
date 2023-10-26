# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 12:02:09 2023

@author: Fernando
"""

from abc import ABC, abstractmethod


class RacionalABC(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def mcd(self):
        pass

    @abstractmethod
    def tipo_valor(self):
        pass

    @abstractmethod
    def __add__(self):
        pass

    @abstractmethod
    def __sub__(self):
        pass

    @abstractmethod
    def __mul__(self):
        pass

    @abstractmethod
    def __lt__(self):
        pass

    @abstractmethod
    def __abs__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass


class Racional(RacionalABC):
    def __init__(self, racional: str):
        numerador, denominador = map(int, racional.split("/"))
        gcd = self.mcd(numerador, denominador)

        self.numerador = numerador // gcd
        self.denominador = denominador // gcd

    def mcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.mcd(b, a % b)

    def tipo_valor(self, valor) -> RacionalABC:
        if isinstance(valor, Racional):
            return valor
        else:
            return Racional(f"{valor}/1")

    def __add__(self, valor) -> RacionalABC:
        racional = self.tipo_valor(valor)
        num = self.numerador * racional.denominador\
            + self.denominador * racional.numerador
        den = self.denominador * racional.denominador
        return Racional(f"{num}/{den}")

    def __sub__(self, valor) -> RacionalABC:
        racional = self.tipo_valor(valor)
        num = self.numerador * racional.denominador\
            - self.denominador * racional.numerador
        den = self.denominador * racional.denominador
        return Racional(f"{num}/{den}")

    def __mul__(self, valor) -> RacionalABC:
        racional = self.tipo_valor(valor)
        num = self.numerador * racional.numerador
        den = self.denominador * racional.denominador
        return Racional(f"{num}/{den}")

    def __lt__(self, valor) -> bool:
        racional = self.tipo_valor(valor)
        return self.numerador * racional.denominador\
            < self.denominador * racional.numerador

    def __abs__(self) -> RacionalABC:
        return Racional(f"{abs(self.numerador)}/{self.denominador}")

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.denominador == 1:
            return str(self.numerador)
        else:
            return f"{self.numerador}/{self.denominador}"
