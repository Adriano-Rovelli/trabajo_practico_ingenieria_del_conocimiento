def avg(value):
    #Verifica si el objeto es iterable y tiene este tipo de datos
    if isinstance(value, (list, tuple, dict)) or hasattr(value, '__iter__'):
        value = list(value)  # convierte dict_values en lista
        return sum(value) / len(value)
    else:
        return None

def avg_args(*args):
    if isinstance(args, (int, float)) or hasattr(args, '__iter__'):
        return sum(args) / len(args)
    

def is_empty(value):
    if isinstance(value, (dict, list, tuple)):
        if not value:
            return True
        else:
            return False
        
def create_dict(**kwargs):
    if is_empty(kwargs):
        return {}
    
    return kwargs