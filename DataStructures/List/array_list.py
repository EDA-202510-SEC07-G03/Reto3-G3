def new_list():
    newlist = {
        "size": 0,"elements": []
    }
    return newlist

def get_element(my_list, index):
    if 0<=index<=my_list["size"]:
        return my_list["elements"][index]
    else:
        return "IndexError: list index out of range"


def is_present(my_list, element, cmp_function):
    
    size = my_list["size"]
    if size > 0:
        keyexist = False
        for keypos in range(0,size):
            info = my_list["elements"][keypos]
            if cmp_function(element, info) == 0:
                keyexist = True
                break
        if keyexist:
            return keypos
    return -1

def add_first(my_list, element):
    my_list["elements"].insert(0, element)
    my_list["size"] += 1
    return my_list
    
def add_last(my_list, element):
    my_list["elements"].append(element)
    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

def is_empty(my_list):
    if my_list["size"] == 0:
        result = True
    else:
        result = False
    return result

def first_element(my_list):
    if my_list["elements"][0] == None:
        return "IndexError: list index out of range"
    else:
        return my_list["elements"][0]

def last_element(my_list):
    if my_list["elements"][0] == None:
        return "IndexError: list index out of range"
    else:
        return my_list["elements"][-1]

def remove_first(my_list):
    if my_list == None:
        return "IndexError: list index out of range"
    else:
        first_element = my_list["elements"][0]
        my_list["elements"].pop(0)
        my_list["size"] -= 1
        return first_element

def remove_last(my_list):
    if my_list == None:
        return "IndexError: list index out of range"
    else:
        last_element = my_list["elements"][-1]
        my_list["elements"].pop()
        my_list["size"] += 1
        return last_element

def insert_element(my_list, element, pos):
    my_list["elements"].insert(pos,element)
    my_list["size"] += 1
    return my_list

def delete_element(my_list, pos):
    if 0<=pos<=my_list["size"]:
        my_list["elements"].pop(pos)
        my_list["size"] -= 1
        return my_list
    else:
        return "IndexError: list index out of range"

def change_info(my_list, pos, new_info):
    if 0<=pos<=my_list["size"]:
        my_list["elements"][pos] = new_info
        return my_list
    else:
        return "IndexError: list index out of range"

def exchange(my_list, pos_1, pos_2):
    if 0<=pos_1<=my_list["size"] and 0<=pos_2<=my_list["size"]:
        pos1 = my_list["elements"][pos_1]
        pos2 = my_list["elements"][pos_2]
        my_list["elements"][pos_1] = pos2
        my_list["elements"][pos_2] = pos1
        return my_list
    else:
        return "IndexError: list index out of range"
    
def sub_list(my_list, pos_i, num_elements):
    if 0<=pos_i<=my_list["size"]:
        sub_list = new_list()
        sub_list["size"] = num_elements
        for i in range(pos_i, pos_i+num_elements):
            sub_list["elements"].append(my_list["elements"][i])
        return sub_list
    else:
        return "IndexError: list index out of range"
    
def default_sort_criteria(element_1, element_2):

   is_sorted = False
   if element_1 < element_2:
      is_sorted = True
   return is_sorted

def selection_sort(my_list, sort_criteria):
    size = my_list["size"]
    if sort_criteria == True:
        for i in range(size):
            min_pos = i
            for j in range(i + 1, size):
                if my_list["elements"][j] < my_list["elements"][min_pos]:
                    min_pos = j
            if min_pos != i:
                exchange(my_list, i, min_pos)
    else:
        for i in range(size):
            min_pos = i
            for j in range(i + 1, size):
                if my_list["elements"][j] > my_list["elements"][min_pos]:
                    min_pos = j
            if min_pos != i:
                exchange(my_list, i, min_pos)
    return my_list

def insertion_sort(my_list, sort_criteria):
    size = my_list["size"]
    if sort_criteria == True:
        for i in range(1, size):
            llave = my_list["elements"][i]
            j = i - 1
            while j >= 0 and my_list["elements"][j] > llave:
                my_list["elements"][j + 1] = my_list["elements"][j]
                j -= 1
            my_list["elements"][j+1] = llave
    else:
        for i in range(1, size):
            llave = my_list["elements"][i]
            j = i - 1
            while j >= 0 and my_list["elements"][j] < llave:
                my_list["elements"][j + 1] = my_list["elements"][j]
                j -= 1
            my_list["elements"][j+1] = llave
    return my_list

def shell_sort(my_list, sort_criteria):
    size = my_list["size"]
    if size == 0 or size == 1:
        return my_list
    else:
        h = 1
        while h < size//2:
            h = 3* h + 1
        if sort_criteria == True:
            while h > 0:
                for i in range(h , size):
                    llave = my_list["elements"][i]
                    j = i
                    while j >= h and my_list["elements"][j - h] > llave:
                        my_list["elements"][j] = my_list["elements"][j - h]
                        j -= h
                    my_list["elements"][j] = llave
        else:
            while h > 0:
                for i in range(h , size):
                    llave = my_list["elements"][i]
                    j = i
                    while j >= h and my_list["elements"][j - h] < llave:
                        my_list["elements"][j] = my_list["elements"][j - h]
                        j -= h
                    my_list["elements"][j] = llave
                    
                h=h//3
    return my_list
   
def quick_sort(my_list, sort_criteria, low=0, high=None):
    if high is None:
        high = size(my_list) - 1
    def partition(my_list, low, high):
        pivot = my_list["elements"][high]
        k = low
        if sort_criteria == True:
            for i in range(low, high):
                if my_list["elements"][i] < pivot:
                    exchange(my_list, k, i)
                    k += 1
            exchange(my_list, k, high)
            return k
        else:
            for i in range(low, high):
                if my_list[i] > pivot:
                    exchange(my_list, my_list[k], my_list[i])
                    k += 1
            exchange(my_list, my_list[k], my_list[high])
            return k


def merge(left, right, sort_criteria):
    sorted_list = new_list()
    i = j = 0
    if sort_criteria == True:
        while i < size(left) and j < size(right):
            if left["elements"][i] <= right["elements"][j]:
                add_last(sorted_list, left["elements"][i])
                i += 1
            else:
                add_last(sorted_list, right["elements"][j])
                j += 1
        return sorted_list
    else:
        while i < size(left) and j < size(right):
            if left["elements"][i] >= right["elements"][j]:
                add_last(sorted_list, left["elements"][i])
                i += 1
            else:
                add_last(sorted_list, right["elements"][j])
                j += 1
        return sorted_list       

def merge_sort(my_list, sort_criteria):
    if size(my_list) <= 1:
        return my_list
    mid = size(my_list) // 2
    l_half = merge_sort(sub_list(my_list, 0, mid), sort_criteria)
    r_half = merge_sort(sub_list(my_list, mid, size(my_list) - mid), sort_criteria)
    return merge(l_half, r_half,sort_criteria)
    
         
    
    