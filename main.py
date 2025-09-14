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

def pedir_entero(mensaje):
    '''Pide un número entero y repite hasta que el usuario ingrese uno válido.'''
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Ingrese un número válido, por favor.")

#=========Funciones de Menu==========

def gestion_inquilinos():
    '''Menú principal de gestión de inquilinos.'''
    opciones = {
        "1": ("Crear Inquilinos", crear_inquilinos),
        "2": ("Mostrar Inquilinos", lambda: mostrar_matriz(encabezado_inquilinos, matriz_inquilinos[0:])),
        "3": ("Modificar Inquilinos", lambda: modificar_inquilino(matriz_inquilinos[0:])),
        "4": ("Buscar Inquilinos", lambda: busqueda_inquilino(matriz_inquilinos)),
        "5":("Volver al Menú principal.", menu()),
    }
    mostrar_menu(opciones, "Inquilinos")

def gestion_propiedades():
    '''Menú principal de gestión de propiedades.'''
    opciones = {
        "1": ("Crear Propiedades", crear_propiedades),
        "2": ("Mostrar Propiedades", lambda: mostrar_matriz(encabezados_propiedades, matriz_propiedades[0:])),
        "3": ("Modificar Propiedades", lambda: modificar_propiedad(matriz_propiedades[0:])),
        "4": ("Buscar Propiedades", lambda: busqueda_propiedad(matriz_propiedades[0:])),
        "5":("Volver al Menú principal.", menu()),
    }
    mostrar_menu(opciones, "Propiedades")

def gestion_contratos():
    opciones = {
        "1": ("Crear Contratos", crear_contratos),
        "2": ("Mostrar Contratos", lambda: mostrar_matriz(encabezados_propiedades, matriz_propiedades[0:])),
        "3": ("Modificar Contratos", lambda: modificar_contrato(matriz_contratos[0:])),
        "4": ("Buscar Contratos", lambda: busqueda_contratos(matriz_propiedades[0:])),
        "5":("Volver al Menú principal.", menu()),
    }
    mostrar_menu(opciones, "Contratos")

def gestion_pagos():
    opciones = {
        "1": ("Crear Pagos", crear_pagos),
        "2": ("Mostrar Pagos", lambda: mostrar_matriz(encabezados_pagos, matriz_pagos[0:],pos_mil={3})),
        "3": ("Modificar Pagos", lambda: modificar_pago(matriz_pagos[0:])),
        "4":("Volver al Menú principal.", menu()),
    }
    mostrar_menu(opciones, "Pagos")


def gestion_usuarios():
    print("----- Gestión de Usuarios -----")
    print("1. Crear Usuario")
    print("2. Modificar Usuario")
    opcion = input("Seleccione una opción (1-2): ")
    if opcion == '1':
        crear_usuario()
    elif opcion == '2':
        modificar_usuario()
    else:
        print("Opción no válida. Intente nuevamente.")
        gestion_usuarios()

#Programa principal

def menu():
    while True:
        print("----- Menú de Gestión de Alquileres -----")
        print("1. Gestión de Inquilinos")
        print("2. Gestión de Propiedades")
        print("3. Gestión de Contratos")
        print("4. Gestión de Pagos")
        print("5. Gestión de Usuarios")
        print("6. Salir")
        opcion = input("Seleccione una opción (1-6): ")
        if opcion == '1':
            gestion_inqiuilinos()
        elif opcion == '2':
            gestion_propiedades()
        elif opcion == '3':
            gestion_contratos()
        elif opcion == '4':
            gestion_pagos()
        elif opcion == '5':
            gestion_usuarios()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

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
