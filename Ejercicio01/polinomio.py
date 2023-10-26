# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:30:05 2023

@author: HP
"""
from racional import *


from abc import ABC, abstractmethod


class PolinomioABC(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def partir_polinomio(self):
        pass

    @abstractmethod
    def formato(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def adicion(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

    @abstractmethod
    def __sub__(self, other):
        pass

    @abstractmethod
    def __mul__(self, other):
        pass


class Polinomio(PolinomioABC):

    def __init__(self, polinomio: str):
        self.terminos = {}
        self.partir_polinomio(polinomio)

    def partir_polinomio(self, polinomio: str) -> None:
        polinomio = polinomio.replace(" ", "")
        polinomio = polinomio.replace("-", " -").replace("+", " +")
        terms = polinomio.split()

        for term in terms:
            if "x" in term:
                coef, exp = map(lambda ch: ch + "1" if not ch.isdigit() and len(ch) <= 1 else ch,
                                term.split("x"))
                exp = int(exp.replace("^", ""))
            else:
                coef = term
                exp = 0

            coef = Racional(coef) if "/" in coef else int(coef)

            self.terminos[exp] = coef

    def formato(self, terminos: dict) -> str:
        result = ""
        for i, exp in enumerate(terminos, 0):
            coef = terminos[exp]
            if coef < 0:
                signo = " - "
                coef = abs(coef)
            else:
                signo = " + "

            var = "x^"

            # Condiciones de formato
            coef = "" if coef == 1 and exp > 0 else coef
            coef, signo, var, exp = [""]*4 if coef == 0 else (coef, signo, var, exp)
            exp, var = ("", "") if exp == 0 else (exp, var)
            exp, var = ("", var.replace("^", "")) if exp == 1 else (exp, var)
            signo = "" if i == 0 and signo == " + " else signo

            result += signo + str(coef) + var + str(exp)

        return result.strip()

    def __str__(self) -> str:
        return self.formato(self.terminos)

    def adicion(self, polinomio: PolinomioABC, aditivo: int = 1) -> dict:
        polinomio_resultado = self.terminos.copy()

        for exp, coef in polinomio.terminos.items():
            if exp in polinomio_resultado:
                try:
                    polinomio_resultado[exp] += polinomio.terminos[exp] * aditivo
                except TypeError:
                    polinomio_resultado[exp] = Racional(f"{polinomio_resultado[exp]}/1")\
                        + polinomio.terminos[exp] * aditivo
            else:
                polinomio_resultado[exp] = coef * aditivo

        polinomio_resultado = dict(reversed(sorted(polinomio_resultado.items())))
        return polinomio_resultado

    def __add__(self, polinomio: PolinomioABC) -> PolinomioABC:
        polinomio_resultado = self.adicion(polinomio)
        return Polinomio(self.formato(polinomio_resultado))

    def __sub__(self, polinomio: PolinomioABC) -> PolinomioABC:
        polinomio_resultado = self.adicion(polinomio, -1)
        return Polinomio(self.formato(polinomio_resultado))

    def __mul__(self, polinomio: PolinomioABC) -> PolinomioABC:
        polinomio_resultado = {}
        for exp1, coef1 in self.terminos.items():
            for exp2, coef2 in polinomio.terminos.items():
                if exp1 + exp2 in polinomio_resultado:
                    try:
                        polinomio_resultado[exp1 + exp2] += coef1 * coef2
                    except TypeError:
                        if isinstance(polinomio_resultado[exp1 + exp2], Racional):
                            polinomio_resultado[exp1 + exp2] += coef2 * coef1   
                        elif isinstance(coef1, Racional):
                            polinomio_resultado[exp1 + exp2] = (
                                Racional(f"{polinomio_resultado[exp1 + exp2]}/1")
                                + coef1 * coef2)
                        else:
                            polinomio_resultado[exp1 + exp2] = (
                                Racional(f"{polinomio_resultado[exp1 + exp2]}/1")
                                + coef2 * coef1)
                else:
                    try:
                        polinomio_resultado[exp1 + exp2] = coef1 * coef2
                    except TypeError:
                        polinomio_resultado[exp1 + exp2] = coef2 * coef1

        polinomio_resultado = dict(reversed(sorted(polinomio_resultado.items())))
        return Polinomio(self.formato(polinomio_resultado))


polinomio = Polinomio("2x^6 -3/2x^4 +5x^3 +x^2 -2x -1")
polinomio2 = Polinomio("-x^6 + 3x^5 +2/3x +3")
print("Polinomio 1: ", polinomio)
print("Polinomio 2: ", polinomio2, end="\n\n")
print("------------------------Operando----------------------------")
print("Polinomio 1 + polinomio 2: ", polinomio + polinomio2)
print("Polinomio 1 - polinomio 2: ", polinomio - polinomio2)
print("Polinomio 1 * polinomio 2: ", polinomio * polinomio2)
