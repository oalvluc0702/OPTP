from abc import ABC, abstractmethod
class Empleado(ABC):
    def __init__(self, nombre, sueldo_base):
        if nombre is None:
            raise ValueError("Nombre no puede estar vacío")
        if sueldo_base < 0 or sueldo_base > 200000:
            raise ValueError("No puedes tener un sueldo base menor que 0 o mayor que 200000 euros")
        self.__nombre = nombre
        self.__sueldo_base = sueldo_base
    @abstractmethod
    def calcular_sueldo(self):
        pass
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

    def __str__(self):
        return f'Empleado: "{self.__nombre}", {self.__sueldo_base} eur'

class Empleado_base(Empleado):
    def __init__(self, nombre, sueldo_base):
        super().__init__(nombre, sueldo_base)
    def calcular_sueldo(self):
        return self.sueldo_base
    
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
    def __str__(self):
        return f'Vendedor: "{self.nombre}", {self.sueldo_base}, {self.__comision}'
class Gerente(Empleado):
    def __init__(self, nombre, sueldo_base, bono_gestion):
        super().__init__(nombre, sueldo_base)
        if bono_gestion > (sueldo_base * 0.50):
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
    def __str__(self):
        return f'Gerente: "{self.nombre}", {self.sueldo_base} eur, {self.__bono_gestion} eur'
class Departamento:
    def __init__(self, nombre, gerente):
        self.__nombre = nombre
        self.__gerente = gerente
        self.__empleados = []

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @property
    def gerente(self):
        return self.__gerente

    @gerente.setter
    def gerente(self,gerente):
       self.__gerente = gerente
    @property
    def empleados(self):
        return self.__empleados

    def agregar_empleado(self,empleado):
        self.empleados.append(empleado)
    def resumen_formateado(self):
        nomina_total = self.gerente.calcular_sueldo()
        print(f"--- Departamento {self.nombre} ---")
        print(f"{type(self).__name__} {self.nombre}: {self.gerente.nombre}, {self.gerente.sueldo_base} eur, {self.gerente.bono_gestion} eur")
        print(f"Departamento: {self.nombre}, {self.gerente.nombre}")
        for empleado in self.empleados:
            print(empleado)
            nomina_total += empleado.calcular_sueldo()
        print(f"La nomina total del departamento {self.nombre} es: {nomina_total}")

#Empleados
ana = Empleado_base("Ana",1200)
carlos = Vendedor("Carlos",1200,350)
marta = Gerente("Marta",2000,500)
john = Gerente("John",2500,850)
marta2 = Gerente("Marta",2000,450)
#Departamentos
nacional = Departamento("Nacional",marta)
nacional.agregar_empleado(ana)
nacional.agregar_empleado(carlos)
internacional = Departamento("Internacional",john)
internacional.agregar_empleado(Vendedor("Sarah",1500,600))
internacional.agregar_empleado(Vendedor("Pierre",1500,550))

nuevos_productos = Departamento("Nuevos productos",marta2)
nuevos_productos.agregar_empleado(Empleado_base("Jaime",1200))
nuevos_productos.agregar_empleado(Vendedor("Secundino",1200,350))

departamentos = [nacional,internacional,nuevos_productos]
for departamento in departamentos:
    departamento.resumen_formateado()
    print("\n")
    

        
