from DataStructures.List import array_list as al
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
        al.add_last(my_table["table"],ent.new_map_entry(None,None))
    my_table["current_factor"] = 0
    my_table["limit_factor"] =  load_factor
    my_table["size"] = 0
    return my_table

def put(my_map, key, value):
    hash_value = map.hash_value(my_map, key)

    ocupied, slot = find_slot(my_map, key, hash_value)

    entry = al.get_element(my_map["table"], slot)
    if ent.get_key(entry) is None or ent.get_key(entry) == "__EMPTY__":

        ent.set_key(entry, key)
        ent.set_value(entry, value)
        my_map["size"] += 1
    else:
        if ocupied:
            ent.set_value(entry, value)
            
    if my_map["size"] / my_map["capacity"] > my_map["limit_factor"]:
        rehash(my_map)
    return my_map

def rehash(my_map):
    new_capacity = map.next_prime(my_map["capacity"] * 2)
    new_table = al.new_list()
    
    for i in range(new_capacity):
        al.add_last(new_table, ent.new_map_entry(None, None))
    
    old_table = my_map["table"]
    my_map["table"] = new_table
    my_map["capacity"] = new_capacity
    my_map["size"] = 0

    for i in range(old_table["size"]):
        entry = al.get_element(old_table, i)
        if ent.get_key(entry) not in [None, "__EMPTY__"]:
            key = ent.get_key(entry)
            value = ent.get_value(entry)

            put(my_map, key, value)
    return my_map
    
def is_available(table, pos):

   entry = al.get_element(table, pos)
   if ent.get_key(entry) is None or ent.get_key(entry) == "__EMPTY__":
      return True
   return False

def default_compare(key, entry):

   if key == ent.get_key(entry):
      return 0
   elif key > ent.get_key(entry):
      return 1
   return -1

def find_slot(my_map, key, hash_value):
   first_avail = None
   found = False
   ocupied = False
   while not found:
      if is_available(my_map["table"], hash_value):
            if first_avail is None:
               first_avail = hash_value
            entry = al.get_element(my_map["table"], hash_value)
            if ent.get_key(entry) is None:
               found = True
      elif default_compare(key, al.get_element(my_map["table"], hash_value)) == 0:
            first_avail = hash_value
            found = True
            ocupied = True
      hash_value = (hash_value + 1) % my_map["capacity"]
   return ocupied, first_avail

def get(my_map, key):
    hash = map.hash_value(my_map,key)
    element = ent.get_value(my_map["table"]["elements"][hash])
    return element

def contains(my_map, key):
    hash = map.get_hash(my_map,key)
    if my_map["table"]["elements"][hash]["key"] == key:
        return True
    return False

def size(my_map):
    return my_map["size"]

def remove(my_map,key):
    hash = map.hash_value(my_map,key)
    my_map["table"]["elements"][hash]["value"] = None
    my_map["table"]["elements"][hash]["key"] = None
    my_map["size"] -= 1
    return my_map

def is_empty(my_map):
    if my_map["size"] == 0:
        return True
    return False

def key_set(my_map):
    lista = al.new_list()
    for i in range(my_map["table"]["size"]):
        if my_map["table"]["elements"][i]["key"] is not None:
            al.add_last(lista,my_map["table"]["elements"][i]["key"])
    return lista

def value_set(my_map):
    lista = al.new_list()
    for i in range(my_map["table"]["size"]):
        if my_map["table"]["elements"][i]["value"] is not None:
            al.add_last(lista,my_map["table"]["elements"][i]["value"])
    return lista