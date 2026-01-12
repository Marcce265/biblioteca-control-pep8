"""
Módulo que define las clases base para el sistema de gestión de bibliotecas.
"""

class Libro:
    """Representa un libro con título, autor y estado de préstamo."""

    def __init__(self, titulo, autor, id_libro):
        self.titulo = titulo
        self.autor = autor
        self.id_libro = id_libro
        self.disponible = True

    def prestar(self):
        """Cambia el estado del libro a no disponible si está libre."""
        if self.disponible:
            self.disponible = False
            return True
        return False

    def devolver(self):
        """Cambia el estado del libro a disponible."""
        self.disponible = True

class Biblioteca:
    """Gestiona una colección de objetos de la clase Libro."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.catalogo = []

    def agregar_libro(self, libro):
        """Añade un ejemplar de Libro al catálogo de la biblioteca."""
        self.catalogo.append(libro)

    def mostrar_inventario(self):
        """Imprime la lista de todos los libros en la consola."""
        for libro in self.catalogo:
            print(libro.titulo, libro.autor, libro.id_libro)
