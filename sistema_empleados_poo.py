import json
from abc import ABC, abstractmethod
from datetime import datetime
from functools import wraps 

def log_operacion(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Ejecutando: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

class Empleado(ABC):
    def __init__(self, nombre, salario):
        self._nombre = nombre   
        self._salario = salario 

    @property 
    def salario(self):
        return self._salario

    @salario.setter
    def salario(self, nuevo_salario):
        if nuevo_salario > 0:
            self._salario = nuevo_salario
    
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre.strip():
            self._nombre = nuevo_nombre

 
    @abstractmethod
    def mostrar_info(self):
        pass

    @log_operacion
    def aumentar_salario(self, porcentaje):
        if porcentaje > 0:
            self._salario *= (1 + porcentaje / 100)

    def to_dict(self):
        return {
            "tipo": self.__class__.__name__,
            "nombre": self.nombre,
            "salario": self._salario
        }

    def __str__(self):
        return f"Empleado: {self.nombre}, Salario: ${self._salario:.2f}"

class Gerente(Empleado):
    def __init__(self, nombre, salario, bono):
        super().__init__(nombre, salario)
        self.__bono = bono  

    def mostrar_info(self):
        print(self)

    def obtener_salario_total(self):
        return self._salario + self.__bono

    def to_dict(self):
        data = super().to_dict()
        data["bono"] = self.__bono
        return data

    def __str__(self):
        return f"Gerente: {self.nombre}, Salario: ${self._salario:.2f}, Bono: ${self.__bono:.2f}"


class Desarrollador(Empleado):
    def __init__(self, nombre, salario, tecnologia):
        super().__init__(nombre, salario)
        self._tecnologia = tecnologia

    @property
    def tecnologia(self):
        return self._tecnologia

    @tecnologia.setter
    def tecnologia(self, nueva_tecno):
        if nueva_tecno.strip():
            self._tecnologia = nueva_tecno

    def mostrar_info(self):
        print(self)

    def to_dict(self):
        data = super().to_dict()
        data["tecnologia"] = self._tecnologia
        return data

    def __str__(self):
        return f"Desarrollador: {self.nombre}, Salario: ${self._salario:.2f}, Tecnología: {self._tecnologia}"

def crear_empleado(data):
    tipo = data.get("tipo")
    if tipo == "Gerente":
        return Gerente(data["nombre"], data["salario"], data["bono"])
    elif tipo == "Desarrollador":
        return Desarrollador(data["nombre"], data["salario"], data["tecnologia"])

@log_operacion
def guardar_empleados(empleados, archivo="empleados.json"):
    with open(archivo, "w", encoding="utf-8") as f:
        json.dump([emp.to_dict() for emp in empleados], f, indent=4)

@log_operacion
def cargar_empleados(archivo="empleados.json"):
    empleados = []
    try:
        with open(archivo, "r", encoding="utf-8") as f:
            data = json.load(f)
            empleados = [crear_empleado(emp) for emp in data if crear_empleado(emp)]
    except FileNotFoundError:
        print("Archivo no encontrado. Iniciando lista vacía.")
    return empleados


def agregar_gerente():
    try:
        nombre = input("Nombre: ")
        salario = float(input("Salario: "))
        bono = float(input("Bono: "))
        return Gerente(nombre, salario, bono)
    except ValueError:
        print("Entrada inválida. Intente nuevamente.")


def agregar_desarrollador():
    try:
        nombre = input("Nombre: ")
        salario = float(input("Salario: "))
        tecnologia = input("Tecnología principal: ")
        return Desarrollador(nombre, salario, tecnologia)
    except ValueError:
        print("Entrada inválida. Intente nuevamente.")

def menu():
    empleados = cargar_empleados()

    while True:
        print("\n--- MENÚ ---")
        print("1. Ver empleados")
        print("2. Agregar Gerente")
        print("3. Agregar Desarrollador")
        print("4. Aumentar salario a todos")
        print("5. Guardar y salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            for emp in empleados:
                print(emp)
        elif opcion == "2":
            nuevo = agregar_gerente()
            if nuevo: empleados.append(nuevo)
        elif opcion == "3":
            nuevo = agregar_desarrollador()
            if nuevo: empleados.append(nuevo)
        elif opcion == "4":
            try:
                porcentaje = float(input("Ingrese porcentaje de aumento: "))
                for emp in empleados:
                    emp.aumentar_salario(porcentaje)
            except ValueError:
                print("Porcentaje inválido.")
        elif opcion == "5":
            guardar_empleados(empleados)
            print("Datos guardados. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

if __name__ == "__main__":
    menu()
