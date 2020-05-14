class Libro:

    def __init__(self, nombre=None, autor=None, documento=None):
        if documento is None:
            self.nombre = nombre
            self.autor = autor
        else:
            self.nombre = documento['nombre']
            self.autor = documento['autor']

    def pasar_a_diccionario(self):
        return {
            'autor': self.autor,
            'nombre': self.nombre
        }

    def __str__(self):
        return (
            f"Autor : {self.autor}\n"
            f"Titulo del Libro : {self.nombre}"
        )
