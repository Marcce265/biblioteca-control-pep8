"""
Script principal para ejecutar la lógica de control de la biblioteca.
"""
from biblioteca import Biblioteca, Libro

biblioteca_central = Biblioteca("Central")
libro_python = Libro("Python", "Guido van Rossum", 1)
libro_java = Libro("Java", "James Gosling", 2)

biblioteca_central.agregar_libro(libro_python)
biblioteca_central.agregar_libro(libro_java)
biblioteca_central.mostrar_inventario()

print(libro_python.prestar())
print(libro_python.prestar())
libro_python.devolver()
print(libro_python.prestar())
