# Sistema de Gestión de Empleados - Python OOP

Este proyecto es parte del Trabajo Práctico Integrador para la materia **Programación Avanzada**. Modela una jerarquía de empleados utilizando **Programación Orientada a Objetos** en Python e incluye conceptos avanzados como **clases abstractas**, **decoradores**, **encapsulamiento**, **serialización** y **persistencia en archivos JSON**.

---

## 🧩 Funcionalidades principales

- Clases con herencia: `Empleado` (abstracta), `Gerente`, `Desarrollador`
- Decorador personalizado para loguear operaciones
- Menú interactivo por consola
- Aumento de salario configurable
- Persistencia de empleados en `empleados.json`
- Validación de entrada de usuario
- Serialización/deserialización de objetos con JSON

---

## 🏗️ Estructura de clases

- **Empleado**: clase abstracta con nombre y salario. Métodos:
  - `mostrar_info()` (abstracto)
  - `aumentar_salario(porcentaje)`
  - `to_dict()`, `__str__`
- **Gerente**: hereda de `Empleado`, agrega `bono`
- **Desarrollador**: hereda de `Empleado`, agrega `tecnología`

---

## 🧪 Uso del programa

### ▶️ Ejecutar el sistema
```bash
python sistema_empleados_poo.py
