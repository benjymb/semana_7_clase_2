from atributos_conexion import (
    CADENA_DE_CONEXION, BASE_DATOS, COLECCION
)
from conexion_mdb import Conexion
from modelos import Libro

CADENA_DE_CONEXION = CADENA_DE_CONEXION

BASE_DATOS = BASE_DATOS

COLECCION = COLECCION


def insertar_libros(cx):
    nombre = input('Ingrese el titulo del nuevo libro : ')
    autor = input('Ingrese el autor del nuevo libro : ')
    nuevo_libro = Libro(nombre, autor)
    cx.insertar_registro(
        nuevo_libro.pasar_a_diccionario()
    )


def buscar_libros(cx):
    autor = input('Ingrese el nombre del autor a buscar : ')
    documentos = cx.obtener_registros({
        'autor': autor
    })
    for i, documento in enumerate(documentos):
        libro = Libro(documento=documento)
        print(f'---- Libro {i + 1} -------')
        print(libro)
        print('--------------------------')
    else:
        print('No se encontraron coincidencias')


def buscar_libro(cx):
    autor = input('Ingrese el nombre del autor a buscar : ')
    documento = cx.obtener_registro({
        'autor': autor
    })
    if documento:
        libro = Libro(documento=documento)
        print('Libro encontrado!')
        print(libro)
    else:
        print('No se encontraron coincidencias')


def actualizar_libro(cx):
    nombre = input('Ingrese el nombre del libro a actualizar : ')
    nuevo_nombre = input('Ingrese el nuevo nombre : ')
    nuevo_autor = input('Ingre el nuevo autor :')
    documento = cx.obtener_registro({
        'nombre': nombre
    })
    if documento:
        cx.actualizar_registro(
            {
                '_id': documento['_id']
            },
            {"nombre": nuevo_nombre, "autor": nuevo_autor}
        ) 
    else:
        print('No se encontro el libro para actualizar')

def eliminar_libro(cx):
    nombre = input('Ingrese el nombre del libro a eliminar : ')
    documento = cx.obtener_registro({
        'nombre': nombre
    })
    if documento:
        cx.eliminar_registro(
            {
                '_id': documento['_id']
            }
        ) 
    else:
        print('No se encontro el libro para eliminar')



def main():
    cx = Conexion(
        CADENA_DE_CONEXION, BASE_DATOS,
        COLECCION
    )
    print('Bienvenido a tu biblioteca!')
    continuar = True
    while continuar:
        print('Ingresa una opcion')
        print('Ingresa 1 para insertar un nuevo libro')
        print('Ingresa 2 para ver los libros en la biblioteca')
        print('Ingresa 3 para obtener un solo libro')
        print('Ingresa 4 para modificar un solo libro')
        print('Ingresa 5 para eliminar un solo libro')
        print('Ingresa 6 para salir')
        opcion = input('Ingresa la opcion : ')
        if opcion == '1':
            insertar_libros(cx)
        elif opcion == '2':
            buscar_libros(cx)
        elif opcion == '3':
            buscar_libro(cx)
        elif opcion == '4':
            actualizar_libro(cx)
        elif opcion == '5':
            eliminar_libro(cx)
        elif opcion == '6':
            continuar = False


main()
