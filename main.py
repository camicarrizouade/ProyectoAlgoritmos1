# --- IMPORTS ---
from Inquilinos.datos import encabezado_inquilinos, matriz_inquilinos
from Inquilinos.crear import crear_matriz_inquilinos
from Inquilinos.modificar import modificar_inquilino
from Inquilinos.busqueda import busqueda_inquilino

from Propiedades.datos import encabezados_propiedades, matriz_propiedades
from Propiedades.crear import crear_matriz_propiedades
from Propiedades.modificar import modificar_propiedad
from Propiedades.busqueda import busqueda_propiedad

from Contratos.datos_contratos import encabezados_contratos, matriz_contratos
from Contratos.crear_contratos import crear_matriz_contrato  
from Contratos.modificar_contratos import modificar_contrato

from Pagos.datos import encabezados_pagos, matriz_pagos
from Pagos.crear import crear_matriz_pagos
from Pagos.modificar import modificar_pago

from FuncAux.mostrar import mostrar_matriz
from FuncAux.login import validar_usuario, iniciar_sesion

from Usuarios.crear import crear_usuario
from Usuarios.modificar import modificar_usuario

#=======Funciones auxiliares========
"""cosas genéricas que no dependen del dominio, ej: pedir_entero, formateos, validaciones comunes) """

def pedir_entero(mensaje):
    '''Pide un número entero y repite hasta que el usuario ingrese uno válido.'''
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un número válido, por favor.")

#=======Funciones para crear según seccion (acciones sobre datos)========

def crear_inquilinos():
    '''Pide cantidad y agrega nuevos inquilinos a la matriz.'''
    cantidad = pedir_entero("¿Cuántos inquilinos desea crear? ")
    nuevos = crear_matriz_inquilinos(cantidad, matriz_inquilinos)
    matriz_inquilinos.extend(nuevos)
    print("Inquilinos creados exitosamente.")

def crear_propiedades():
    '''Pide cantidad y agrega nuevas propiedades a la matriz.'''
    cant_propiedades = pedir_entero("¿Cuántas propiedades desea crear? ")
    nuevas_propiedades = crear_matriz_propiedades(cant_propiedades)
    matriz_propiedades.extend(nuevas_propiedades)
    print("Propiedades creadas exitosamente.")

def crear_contratos():
    '''Pide cantidad y agrega nuevos contratos a la matriz.'''
    cant_contratos = pedir_entero("¿Cuántos contratos desea crear? ")
    nuevos_contratos = crear_matriz_contrato(cant_contratos)
    matriz_contratos.extend(nuevos_contratos)
    print("Contratos creados exitosamente.")

def crear_pago():
    '''Pide cantidad y agrega nuevos pagos a la matriz.'''
    cant_pagos = pedir_entero("¿Cuántos pagos desea crear? ")
    nuevos_pagos = crear_matriz_pagos(cant_pagos)
    matriz_pagos.extend(nuevos_pagos)
    print("Pagos creados exitosamente.")


#=========Funciones de Menu==========

def mostrar_menu(opciones, titulo):
    '''Devuelve True si el usuario eligió salir/volver; False si sigue en el menú.'''
    while True:
        print(f"\n----- Menú de Gestión de {titulo} -----")
        for k, (texto, _) in opciones.items():
            print(f"{k}. {texto}")

        opcion_salida = str(len(opciones) + 1)
        print(f"{opcion_salida}. {'Salir' if titulo == 'Alquileres' else 'Volver al menú principal'}")

        op = input("Seleccione una opción: ").strip()
        if op == opcion_salida:
            if titulo == "Alquileres":
                print("Saliendo del programa...")
            return True  # <- señal de salida/volver
        accion = opciones.get(op)
        if accion:
            accion[1]()
        else:
            print("Opción no válida, intente de nuevo.")

def gestion_inquilinos():
    '''Menú principal de gestión de inquilinos.'''
    opciones = {
        "1": ("Crear Inquilinos", crear_inquilinos),
        "2": ("Mostrar Inquilinos", lambda: mostrar_matriz(encabezado_inquilinos, matriz_inquilinos[0:])),
        "3": ("Modificar Inquilinos", lambda: modificar_inquilino(matriz_inquilinos[0:])),
        "4": ("Buscar Inquilinos", lambda: busqueda_inquilino(matriz_inquilinos))
    }
    mostrar_menu(opciones, "Inquilinos")

def gestion_propiedades():
    '''Menú principal de gestión de propiedades.'''
    opciones = {
        "1": ("Crear Propiedades", crear_propiedades),
        "2": ("Mostrar Propiedades", lambda: mostrar_matriz(encabezados_propiedades, matriz_propiedades[0:])),
        "3": ("Modificar Propiedades", lambda: modificar_propiedad(matriz_propiedades[0:])),
        "4": ("Buscar Propiedades", lambda: busqueda_propiedad(matriz_propiedades[0:]))
    }
    mostrar_menu(opciones, "Propiedades")

def gestion_contratos():
    """ Menú principal de gestión de contratos."""
    opciones = {
        "1": ("Crear Contratos", crear_contratos),
        "2": ("Mostrar Contratos", lambda: mostrar_matriz(encabezados_propiedades, matriz_propiedades[0:])),
        "3": ("Modificar Contratos", lambda: modificar_contrato(matriz_contratos[0:])),
        "4": ("Buscar Contratos", lambda: busqueda_contratos(matriz_propiedades[0:]))
    }
    mostrar_menu(opciones, "Contratos")

def gestion_pagos():
    """ Menú principal de gestión de pagos."""
    opciones = {
        "1": ("Crear Pagos", crear_pagos),
        "2": ("Mostrar Pagos", lambda: mostrar_matriz(encabezados_pagos, matriz_pagos[0:],pos_mil={3})),
        "3": ("Modificar Pagos", lambda: modificar_pago(matriz_pagos[0:]))
    }
    mostrar_menu(opciones, "Pagos")


def gestion_usuarios():
    """ Menú principal de gestión de usuarios."""
    opciones = {
        "1": ("Crear Usuarios", crear_usuario),
        "2": ("Modificar Usuarios", modificar_usuario)
    }
    mostrar_menu(opciones, "Usuarios")

#Programa principal

def menu():
    opciones_menu = {
        "1": ("Gestión de Inquilinos",  gestion_inquilinos),
        "2": ("Gestión de Propiedades", gestion_propiedades),
        "3": ("Gestión de Contratos",   gestion_contratos),
        "4": ("Gestión de Pagos",       gestion_pagos),
        "5": ("Gestión de Usuarios",    gestion_usuarios),
    }
    while True:
        salir = mostrar_menu(opciones_menu, "Alquileres")
        if salir:  # usuario eligió "Salir"
            break

def iniciar_sistema():
    print("----- Bienvenido al sistema -----")
    
    # Solo permite entrar al menú si el login es correcto
    while not iniciar_sesion():
        pass  # sigue pidiendo login hasta que sea correcto

    # Una vez logueado, muestra el menú
    menu()

# --- EJECUCIÓN ---

if __name__ == "__main__":
    iniciar_sistema()
