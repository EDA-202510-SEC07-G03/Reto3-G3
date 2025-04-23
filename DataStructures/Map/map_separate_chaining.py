from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
import DataStructures.Map.map_functions as map
import DataStructures.Map.map_entry as ent
import random as m
def new_map(num_elements, load_factor, prime=109345121):
    my_table =  al.new_list()
    my_table["prime"] = prime
    my_table["capacity"] = map.next_prime(num_elements/load_factor)
    my_table["scale"] = m.randint(1, prime - 1)
    my_table["shift"] = m.randint(0, prime - 1)
    my_table["table"] = al.new_list()
    for i in range(my_table["capacity"]):
        al.add_last(my_table["table"],sl.new_list())
    my_table["current_factor"] = 0
    my_table["limit_factor"] =  load_factor
    my_table["size"] = 0    
    return my_table

def put(my_map, key, value):
    indice = map.hash_value(my_map, key)
    entry = al.get_element(my_map["table"], indice)
    node = entry["first"]
    while node is not None:
        if ent.get_key(node["info"]) == key:
            ent.set_value(node["info"], value)
            return my_map
        node = node["next"]
    dicc = ent.new_map_entry(key, value)
    sl.add_last(entry, dicc)
    my_map["size"] += 1
    if my_map["size"] / my_map["capacity"] > my_map["limit_factor"]:
        rehash(my_map)
    return my_map

def default_compare(key, element):
   if (key == ent.get_key(element)):
      return 0
   elif (key > ent.get_key(element)):
      return 1
   return -1

def contains(my_map, key):
    indice = map.hash_value(my_map, key)
    entry = al.get_element(my_map["table"], indice)
    if sl.is_present(entry, key, default_compare) == -1:
        retorno = False
    else:
        retorno = True
    return retorno

def remove(my_map, key):
    indice = map.hash_value(my_map, key)
    entry = al.get_element(my_map["table"], indice)
    
    if entry["size"] == 0:
        return my_map

    node = entry["first"]
    previous = None

    while node is not None:
        if ent.get_key(node["info"]) == key:
            if previous is None:
                entry["first"] = node["next"]
            else:
                previous["next"] = node["next"]
                
            my_map["size"] -= 1
            return my_map
        
        previous = node
        node = node["next"]

    return my_map

def get(my_map, key):
    indice = map.hash_value(my_map, key)
    entry = al.get_element(my_map["table"], indice)
    if entry["size"] == 0:
        retorno = None
    else:
        node = entry["first"]
        while node != None:
            if ent.get_key(node["info"]) == key:
                return ent.get_value(node["info"])
            node = node["next"]
    return None

def size(my_map):
    return my_map["size"]

def is_empty(my_map):
    if my_map["size"] == 0:
        return True
    return False

def key_set(my_map):
    lista_claves = al.new_list()
    
    for i in range(my_map["capacity"]):
        entry = my_map["table"]["elements"][i]
        node = entry["first"]
        while node is not None:
            clave = ent.get_key(node["info"])
            al.add_first(lista_claves, clave)
            node = node["next"]
    
    return lista_claves

def value_set(my_map):
    lista_retorno = al.new_list()
    for i in range(my_map["capacity"]):
        entry = my_map["table"]["elements"][i]
        node = entry["first"]
        while node != None:
            valor = ent.get_value(node["info"])
            if valor != None:
                    al.add_first(lista_retorno, valor)
            node = node["next"]
    return lista_retorno

def rehash(my_map):
    old_table = my_map["table"]
    new_capacity = map.next_prime(my_map["capacity"] * 2)
    new_table = al.new_list()
    
    for i in range(new_capacity):
        al.add_last(new_table, sl.new_list())
    
    my_map["table"] = new_table
    my_map["capacity"] = new_capacity
    my_map["size"] = 0
    
    for i in range(len(old_table["elements"])):
        entry = old_table["elements"][i]
        node = entry["first"]
        while node is not None:
            llave = ent.get_key(node["info"])
            valor = ent.get_value(node["info"])
            put(my_map, llave, valor)
            node = node["next"]
    
    return my_map
                    
    
    

              
            
            
        

            
        
    
    

            
        
            
            
                    
        
    