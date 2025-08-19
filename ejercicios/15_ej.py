'''
Manejo de parámetros variables con *args:Consigna: Escribe una función que reciba un número variable de notas de estudiantes y devuelva la nota promedio. 
Utiliza *args para recibir las notas.calcular_promedio(85, 90, 78, 92)
'''

from new_functions import avg_args

def calculate_avg(*args):
    return avg_args(*args)


if __name__ == '__main__':
    print(calculate_avg(85, 90, 78, 92))
    