from abc import ABC, abstractmethod

class Expresion(ABC):
    @abstractmethod
    def evaluar(self):
        pass


# Hoja
class Numero(Expresion):
    def __init__(self, valor):
        self.valor = valor

    def evaluar(self):
        return self.valor


class Operacion(Expresion):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha


class Suma(Operacion):
    def evaluar(self):
        return self.izquierda.evaluar() + self.derecha.evaluar()


class Resta(Operacion):
    def evaluar(self):
        return self.izquierda.evaluar() - self.derecha.evaluar()


class Multiplicacion(Operacion):
    def evaluar(self):
        return self.izquierda.evaluar() * self.derecha.evaluar()


class Division(Operacion):
    def evaluar(self):
        if self.derecha.evaluar() == 0:
            raise ValueError("División por cero")
        return self.izquierda.evaluar() / self.derecha.evaluar()



# Parte izquierda: (3 * 5) + 4
parte_izquierda = Suma(
    Multiplicacion(Numero(3), Numero(5)),
    Numero(4)
)

# Parte derecha: (10 - 6) / 2
parte_derecha = Division(
    Resta(Numero(10), Numero(6)),
    Numero(2)
)

# arbol completo
arbol = Multiplicacion(parte_izquierda, parte_derecha)

resultado = arbol.evaluar()

print("Resultado:", resultado)