'''
Creación de un perfil de usuario con **kwargs:
Consigna: Escribe una función que reciba datos de un usuario como nombre, edad, correo electrónico, y cualquier otro dato adicional usando **kwargs. 
La función debe devolver un diccionario con toda la información del usuario.
crear_perfil(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza")
'''
from new_functions import create_dict

def create_profile(**profile_properties):
    return create_dict(**profile_properties)

if __name__ == '__main___':
    print(create_profile(nombre="Luis", edad=25, email="juan@mail.com", ciudad="Mendoza"))

