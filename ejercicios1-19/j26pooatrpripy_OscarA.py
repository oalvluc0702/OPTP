class Empleado:
    def __init__(self, nombre, sueldo_base):
        if nombre is None:
            raise ValueError("Nombre no puede estar vacío")
        if sueldo_base < 0 or sueldo_base > 200000:
            raise ValueError("No puedes tener un sueldo base menor que 0 o mayor que 200000 euros")
        self.__nombre = nombre
        self.__sueldo_base = sueldo_base
    def calcular_sueldo(self):
        return self.sueldo_base
    @property
    def nombre(self):
        return self.__nombre
    @property
    def sueldo_base(self):
        return self.__sueldo_base
    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre
    @sueldo_base.setter
    def sueldo_base(self,sueldo_base):
        self.__sueldo_base = sueldo_base 

class Vendedor(Empleado):
    def __init__(self, nombre, sueldo_base, comision):
        super().__init__(nombre, sueldo_base)
        if comision > (sueldo_base * 0.50):
            raise ValueError("la comisión no puede ser mayor que el 50% del sueldo base")
        self.__comision = comision
    @property
    def comision(self):
        return self.__comision
    @comision.setter
    def comision(self,comision):
        self.__comision = comision

    def calcular_sueldo(self):
        return self.sueldo_base + self.comision
    
class Gerente(Empleado):
    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)
        if bono_gestion < (sueldo_base * 0.50):
            raise ValueError("El bono de gestión no puede ser mayor que el 50% del sueldo base") 
        
        self.__bono_gestion = bono_gestion
    @property
    def bono_gestion(self):
        return self.__bono_gestion
    @bono_gestion.setter
    def bono_gestion(self,bono_gestion):
        self.__bono_gestion = bono_gestion

    def calcular_sueldo(self):
        return self.sueldo_base + self.bono_gestion
empleado = Vendedor("Ana",1200,400)

