from DataStructures.List import list_node as ln

def new_list():
    newlist={"size":0,"first":None,"last":None,}
    return(newlist)

def get_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:  
        raise IndexError("Index out of range")

    searchpos = 0
    node = my_list["first"]

    while searchpos < pos:
        if node is None or node["next"] is None:
            raise IndexError("Invalid list structure: encountered None unexpectedly")
        node = node["next"]
        searchpos += 1

    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp= my_list["first"]
    count=0
    while not is_in_array and temp is not None:
        if cmp_function(element,temp["info"]) == 0:
            is_in_array = True
        else:
            temp =temp["next"]
            count+=1
    if not is_in_array:
        count=-1
    return (count)


def add_first(my_list,element):
    """
    Añade un elemento al principio de la estructura de datos: single linked list.
    """
    new_node=ln.new_single_node(element)
    new_node["next"]=my_list["first"]
    my_list["first"]=new_node
    
    if my_list["size"] == 0:
        my_list["last"]=new_node
        
    my_list["size"]+=1
    return(my_list)

def add_last(my_list,element):
    """
    Añade un elemento al final de la estructura de datos
    """
    new_node=ln.new_single_node(element)
    
    if my_list["size"] == 0:
        my_list["first"] = new_node
        my_list["last"] = new_node
    else:
        my_list["last"]["next"] = new_node
        my_list["last"] = new_node
    
    my_list["size"]+=1
    
    return my_list

def size(my_list):
    return my_list["size"]

def first_element(my_list):
    if size(my_list) == 0:
        raise Exception('IndexError: list index out of range')
    return my_list["first"]

def is_empty(my_list):
    return my_list["size"]==0

def last_element(my_list):
    
    if is_empty(my_list)==True:
        raise Exception('IndexError: list index out of range')
    return my_list["last"]

def remove_first(my_list):
    if is_empty(my_list)==True:
        my_list["last"]=None
    node=my_list["first"]
    removed_info=node["info"]
    
    my_list["first"]=node["next"]
    my_list["size"]-=1
    
    return removed_info

def remove_last(my_list):
    removed_info=0
    if is_empty(my_list)==True:
         raise Exception('IndexError: list index out of range')
    else:
         if size(my_list)==1:
             removed_info=remove_first(my_list)
         else:
             current=my_list["first"]
             removed_info=my_list["last"]
             while current != my_list["last"]:
                 current=current["next"]
                 if current["next"]==my_list["last"]:
                    current["next"]=None
                    my_list["last"]=current
                    my_list["size"]-=1
    return removed_info

def insert_element(my_list,element,pos):
    conteo=0
    a_cambiar={"info":element,"next":None}
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    elif pos==0:
        add_first(my_list,element)
    else:
        actual=my_list["first"]
        while conteo < pos-1:
            conteo+=1
            actual=actual["next"]
        a_cambiar["next"]=actual["next"]
        actual["next"]=a_cambiar
    return my_list

def delete_element(my_list,pos):
    conteo=0
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    elif pos==0:
        remove_first(my_list)
    else:
        actual=my_list["first"]
        while conteo < pos-1:
            conteo+=1
            actual=actual["next"]
        actual["next"]=actual["next"]["next"]
    return my_list
            
def change_info(my_list,pos,new_info):
    conteo=0
    if pos < 0 or pos > size(my_list):
        raise Exception('IndexError: list index out of range')
    else:
        actual=my_list["first"]
        while conteo < pos-1:
            conteo+=1
            actual=actual["next"]
        actual["info"]=actual["info"]
    return my_list

def exchange(my_list,pos1,pos2):
    conteo=0
    if (pos1 < 0 or pos1 > size(my_list)) or (pos2 < 0 or pos2 > size(my_list)):
        raise Exception('IndexError: list index out of range')
    else:
        primero=my_list["first"]
        segundo=my_list["first"]
        while conteo < pos1-1:
            conteo+=1
            primero=primero["next"]
        while conteo < pos2-1:
            conteo+=1
            segundo=segundo["next"]
        primero["next"]=segundo["next"]
        segundo["next"]=primero["next"]
    return my_list
    
def sub_list(my_list, pos, num_elements):
    conteo = 0
    conteo2 = 0
    
    nueva_lista = new_list()

    if pos < 0 or pos >= my_list["size"]:
        raise Exception('IndexError: list index out of range')

    actual = my_list["first"]
    while conteo < pos:
        conteo += 1
        actual = actual["next"]

    nueva_lista["first"] = actual
    
    while conteo2 < num_elements and actual is not None:
        conteo2 += 1
        actual = actual["next"]
        if conteo2 < num_elements and actual is not None:
            add_last(nueva_lista, actual)

    if actual is not None:
        actual["next"] = None
    
    return nueva_lista

def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

def selection_sort (my_list,sort_crit):
    long=my_list["size"]
    
    current=my_list["first"]
    
    if my_list["size"]==0:
        return my_list
    elif my_list["size"]==1:
        return my_list
    
    if sort_crit == True:
        while current is not None:
            minimo=current
            sig=current["next"]
            while sig is not None:
                if sig["info"] < minimo["info"]:
                    minimo=sig
                sig=sig["next"]
            if minimo != current:
                current["info"],minimo["info"] = minimo["info"], current["info"]
            
            current=current["next"]
    else:
        while current is not None:
            minimo=current
            sig=current["next"]
            while sig is not None:
                if sig["info"] > minimo["info"]:
                    minimo=sig
                sig=sig["next"]
            if minimo != current:
                current["info"],minimo["info"] = minimo["info"], current["info"]
            
            current=current["next"]
    return my_list

def insertion_sort(my_list,sort_crit):
    long=my_list["size"]
    
    current=my_list["first"]
    
    if my_list["size"]==0:
        return my_list
    elif my_list["size"]==1:
        return my_list
    
    if sort_crit==True:
        while current is not None:
            llave=current["info"]
            sig=current["next"]
            while sig is not None:
                if sig["info"] < llave:
                    current["info"]=sig["info"]
            prev=current
            current=current["next"]
            sig=sig["next"]
            
    if sort_crit==False:
        while current is not None:
            llave=current["info"]
            sig=current["next"]
            while sig is not None:
                if sig["info"] < llave:
                    current["info"]=sig["info"]
            prev=current
            current=current["next"]
            sig=sig["next"]
    
    return my_list

def shell_sort(my_list, sort_crit):
    if my_list["size"] == 0 or my_list["size"] == 1:
        return my_list
    n = my_list["size"]
    h = 1
    reference3 = my_list["first"]
    reference4 = my_list["first"]
    
    while h < n // 3:
        h = 3 * h + 1
    
    while h > 0:
        for i in range(h, n):
            reference = my_list["first"]
            for k in range(i):
                reference = reference["next"]
            key = reference["info"]
            
            j = i
            reference2 = my_list["first"]
            for i in range(j-h):
                reference2 = reference2["next"]
                
            while j >= h and reference2["info"] > key:
                reference3 = my_list["first"]
                for i in range(j):
                    reference3 = reference3["next"]
                reference3 = reference2
                j -= h
                reference4 = my_list["first"]
                for i in range(j):
                    reference4 = reference4["next"]
            reference4["info"] = key
        h //= 3
    return my_list

def merge(left, right, sort_crit):
    result = new_list()
    
    while not is_empty(left) and not is_empty(right):
        if (sort_crit and left["first"]["info"] <= right["first"]["info"]) or (not sort_crit and left["first"]["info"] >= right["first"]["info"]):
            add_last(result, remove_first(left))
        else:
            add_last(result, remove_first(right))
    
    while not is_empty(left):
        add_last(result, remove_first(left))
    while not is_empty(right):
        add_last(result, remove_first(right))
    
    return result

def merge_sort(my_list, sort_crit):
    if size(my_list) <= 1:
        return my_list
    
    mid = size(my_list) // 2
    left = sub_list(my_list, 0, mid)
    right = sub_list(my_list, mid, size(my_list) - mid)
    
    left = merge_sort(left, sort_crit)
    right = merge_sort(right, sort_crit)
    
    return merge(left, right, sort_crit)


def partition(my_list, sort_crit, low, high):
    """
    Reordena los elementos de la lista alrededor de un pivote y devuelve su posición final.
    """
    pivot_node = my_list["first"]
    for _ in range(high):
        if pivot_node["next"] is None:
            raise IndexError("High index out of bounds")
        pivot_node = pivot_node["next"]
    
    pivot_value = pivot_node["info"]
    i = low - 1
    current = my_list["first"]
    
    for j in range(low, high):
        j_node = my_list["first"]
        for _ in range(j):
            j_node = j_node["next"]

        if (sort_crit and j_node["info"] <= pivot_value) or (not sort_crit and j_node["info"] >= pivot_value):
            i += 1
            i_node = my_list["first"]
            for _ in range(i):
                i_node = i_node["next"]
            i_node["info"], j_node["info"] = j_node["info"], i_node["info"]
    
    i += 1
    i_node = my_list["first"]
    for _ in range(i):
        i_node = i_node["next"]
    i_node["info"], pivot_node["info"] = pivot_node["info"], i_node["info"]
    
    return i

def quick_sort(my_list, sort_crit=True, low=0, high=None):
    """
    Implementa Quick Sort para ordenar una lista enlazada simple.
    """
    if high is None:
        high = size(my_list) - 1

    if low < high:
        pi = partition(my_list, sort_crit, low, high)

        quick_sort(my_list, sort_crit, low, pi - 1)
        quick_sort(my_list, sort_crit, pi + 1, high)

    return my_list