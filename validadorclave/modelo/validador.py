from abc import abstractmethod


class ReglaValidación:
    
    def __init__(self, longitud_esperada: int):
        self.longitud_esperada: int = longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        if len(clave) > self.longitud_esperada:
            return True
        else:
            return False

    def _contiene_mayuscula(self, clave: str) -> bool:
        
        for i in clave:
            if i.isupper():
                return True
        return False
            
    def _contiene_minuscula(self, clave: str) -> bool:
        for i in clave:
            if i.islower():
                return True
        return False

    def _contiene_numero(self, clave: str) -> bool:
        for i in clave:
            if i.isdigit():
                return True
        return False

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionGanimedes:
    
    def __init__(self):
        pass
    
    def contiene_caracter_especial(self, clave: str) -> bool:
        for i in clave:
            if i == "@" or i == "#" or i == "_" or i == "$" or i == "%":
                return True
        return False

    def es_valida(self, clave: str) -> bool:
        pass


class ReglaValidacionCalisto:
    
    def __init__(self):
        pass

    def contiene_calisto(self, clave: str) -> bool:
        pass

    def es_valida(self, clave, str) -> bool:
        pass

class Validador:
    pass