'''
Configuración de una aplicación con **kwargs:
Consigna: Escribe una función que reciba configuraciones opcionales para una aplicación como modo oscuro, idioma, notificaciones, etc., usando **kwargs. 
La función debe devolver un diccionario con las configuraciones aplicadas.
configurar_app(modo_oscuro=True, idioma="es", notificaciones=False)
'''

from new_functions import create_dict

def app_configuration(**configuration):
    return create_dict(**configuration)

if __name__ == '__main__':
    print(app_configuration(modo_oscuro=True, idioma="es", notificaciones=False))