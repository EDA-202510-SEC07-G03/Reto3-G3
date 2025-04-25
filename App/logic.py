import time
import csv
import os
from datetime import datetime
from tabulate import tabulate
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Tree import binary_search_tree as bst
from DataStructures.Map import map_linear_probing as mp
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'


csv.field_size_limit(2147483647)

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    #TODO: Llama a las funciónes de creación de las estructuras de datos
    catalog = {
        "crimes": None,
        "date_tree": None,
        "area_map": None
    }
    catalog["crimes"] = al.new_list()
    catalog["date_tree"] = bst.new_map()
    catalog["area_map"] = mp.new_map(21, 0.7)
    
    return catalog



def load_data(catalog, filename=(data_dir+"Crime_in_LA_20.csv")):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    file = open(filename, encoding="utf-8")
    reader = csv.DictReader(file)
    for row in reader:
        crime={
            "DR_NO": row["DR_NO"], 
            "Date Rptd": datetime.strptime(row["Date Rptd"], "%m/%d/%Y %I:%M:%S %p"),
            "DATE OCC": datetime.strptime(row["DATE OCC"], "%m/%d/%Y %I:%M:%S %p"),
            "TIME OCC": row["TIME OCC"],
            "AREA": row["AREA"] if "AREA" in row else "Unknown",
            "AREA NAME": row["AREA NAME"],
            "Rpt Dist No": row["Rpt Dist No"],
            "Part 1-2": row["Part 1-2"],
            "Crm Cd": row["Crm Cd"],
            "Crm Cd Desc": row["Crm Cd Desc"],
            "Vict Age": row["Vict Age"],
            "Vict Sex": row["Vict Sex"],
            "Vict Descent": row["Vict Descent"],
            "Premise Cd": row["Premise Cd"] if "Premise CD" in row else "Unknown",
            "Premise Desc": row["Premise Desc"] if "Premise Desc" in row else "Unknown",
            "Status": row["Status"],
            "Status Desc": row["Status Desc"],
            "LOCATION": row["LOCATION"],
            "LAT": row["LAT"],
            "LON": row["LON"]
        }
        al.add_last(catalog["crimes"], crime)

    file.close()
    return catalog["crimes"]["size"]

def create_tree(catalog):
    """
    Crea el árbol binario de búsqueda para las fechas
    """
    for i in range(catalog["crimes"]["size"]):
        crime = catalog["crimes"]["elements"][i]
        bst.put(catalog["date_tree"], crime["Date Rptd"], crime["Vict Age"])
    return catalog["date_tree"]

def create_map(catalog):
    """
    Crea el mapa para las áreas
    """
    for i in range(1, 21): 
        if not mp.contains(catalog["area_map"], i):
            area_list = al.new_list()
            mp.put(catalog["area_map"], i, area_list)
        else:
            area_list = mp.get(catalog["area_map"], i)
        for j in range(catalog["crimes"]["size"]):  # Iterar por los crímenes
            crime = catalog["crimes"]["elements"][j]
            if crime["AREA"] is not "Unknown":
                if int(crime["AREA"]) == i:  # Verificar si el crimen pertenece al área actual
                    al.add_last(area_list, crime)

    return catalog["area_map"]
     
def primeros(catalog):
    info = {
        "DR_NO": None,
        "Date Rptd": None,
        "DATE OCC": None,
        "AREA NAME": None,
        "Crm Cd": None,
    }
    lista_retorno = al.new_list()
    for i in range(0,5):
        crime = catalog["crimes"]["elements"][i]
        info = {
            "DR_NO": crime["DR_NO"],
            "Date Rptd": crime["Date Rptd"],
            "DATE OCC": crime["DATE OCC"],
            "AREA NAME": crime["AREA NAME"],
            "Crm Cd": crime["Crm Cd"]
        }
        al.add_last(lista_retorno, info)
    return lista_retorno

def ultimos(catalog):
    info = {
        "DR_NO": None,
        "Date Rptd": None,
        "DATE OCC": None,
        "AREA NAME": None,
        "Crm Cd": None,
    }
    lista_retorno = al.new_list()
    for i in range(-6,-1):
        crime = catalog["crimes"]["elements"][i]
        info = {
            "DR_NO": crime["DR_NO"],
            "Date Rptd": crime["Date Rptd"],
            "DATE OCC": crime["DATE OCC"],
            "AREA NAME": crime["AREA NAME"],
            "Crm Cd": crime["Crm Cd"]
        }
        al.add_last(lista_retorno, info)
    return lista_retorno

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog, anno_0, anno_1):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    start_time = get_time()
    year0 = datetime.strptime(anno_0, "%Y-%m-%d")
    year1 = datetime.strptime(anno_1, "%Y-%m-%d")
    if year0 > year1:
        print("El año inicial no puede ser mayor al año final")
        return None
    filtro = bst.keys(catalog["date_tree"], year0, year1) 
    lista_retorno = al.new_list()
    current_node = filtro["first"]
    sl.merge_sort(filtro, True)
    while current_node is not None:
        for j in range(catalog["crimes"]["size"]):
            value = current_node["info"]
            crime = catalog["crimes"]["elements"][j]
            if crime["Date Rptd"] == value:
                info = {
                    "DR_NO": crime["DR_NO"],
                    "DATE OCC": crime["DATE OCC"],
                    "TIME OCC": crime["TIME OCC"],
                    "AREA NAME": crime["AREA NAME"],
                    "Crm Cd": crime["Crm Cd"],
                    "Crm Cd Desc": crime["Crm Cd Desc"],
                    "LOCATION": crime["LOCATION"],
                }
                al.add_last(lista_retorno, info)
        current_node = current_node["next"]
        if lista_retorno["size"] > 10:
            new_list = al.new_list()
            for i in range(0, 5):
                al.add_last(new_list, lista_retorno["elements"][i])
            for i in range(-6, -1):
                al.add_last(new_list, lista_retorno["elements"][i])
            lista_retorno = new_list
    end_time = get_time()
    elapsed_time = delta_time(start_time, end_time)
    return lista_retorno, filtro["size"], elapsed_time


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass

def sort_unresolved(unresolved):
    """
    Ordena la lista de crímenes no resueltos por 'Date Rptd' usando una lista auxiliar.
    """
    # Crear una lista auxiliar con las fechas de reporte
    date_list = al.new_list()
    for i in range(unresolved["size"]):
        al.add_last(date_list, unresolved["elements"][i]["Date Rptd"])

    # Ordenar la lista auxiliar y reorganizar 'unresolved' en el mismo orden
    al.selection_sort(date_list, lambda d1, d2: d1 < d2)

    # Reorganizar 'unresolved' según el orden de 'date_list'
    sorted_unresolved = al.new_list()
    for date in date_list["elements"]:
        for crime in unresolved["elements"]:
            if crime["Date Rptd"] == date:
                al.add_last(sorted_unresolved, crime)
                break

    return sorted_unresolved

def sort_stats(stats):
    """
    Ordena la lista de estadísticas por 'Crimes' (descendente) y 'AREA NAME' (ascendente).
    """
    # Crear una lista auxiliar con los valores de 'Crimes' y 'AREA NAME'
    crimes_list = al.new_list()
    for i in range(stats["size"]):
        al.add_last(crimes_list, (stats["elements"][i]["Crimes"], stats["elements"][i]["AREA NAME"]))

    # Ordenar la lista auxiliar
    al.selection_sort(crimes_list, lambda c1, c2: c1[0] > c2[0] or (c1[0] == c2[0] and c1[1] < c2[1]))

    # Reorganizar 'stats' según el orden de 'crimes_list'
    sorted_stats = al.new_list()
    for crimes, area_name in crimes_list["elements"]:
        for stat in stats["elements"]:
            if stat["Crimes"] == crimes and stat["AREA NAME"] == area_name:
                al.add_last(sorted_stats, stat)
                break

    return sorted_stats

def req_5(catalog, n, anno_0, anno_1):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    start_time = get_time()
    year0 = datetime.strptime(anno_0, "%Y-%m-%d")
    year1 = datetime.strptime(anno_1, "%Y-%m-%d")
    if year0 > year1:
        print("El año inicial no puede ser mayor al año final")
        return None
    areas = catalog["area_map"]
    stats = al.new_list()
    
    #for code in mp.key_set(areas):
    n = int(n)
    for code in range(1, 21):  
        crimes = mp.get(areas, code)
        unresolved = al.new_list()
        for i in range(crimes["size"]):
            crime = crimes["elements"][i]
            if year0 <= crime["Date Rptd"] <= year1 and crime["Status"] == "IC":
                if crime not in unresolved["elements"]:
                    al.add_last(unresolved, crime)
        if unresolved["size"] > 0:
            unresolved = sort_unresolved(unresolved)
            first = unresolved["elements"][-1]["DATE OCC"]
            last = unresolved["elements"][0]["DATE OCC"]
            info ={
                "AREA NAME": unresolved["elements"][0]["AREA NAME"],
                "AREA": code,
                "Crimes": unresolved["size"],
                "first": first,
                "last": last,
            }
            al.add_last(stats, info)
    stats = sort_stats(stats)
    if stats["size"] > n:
        new_stats = al.new_list()
        for i in range(0, n):
            al.add_last(new_stats, stats["elements"][i])
        stats = new_stats
    endtime = get_time()
    elapsed_time = delta_time(start_time, endtime)
    return stats, elapsed_time

def req_6(catalog, n, sex, mes):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    month = datetime.strptime(mes, "%m")
    areas = catalog["area_map"]
    stats = al.new_list()
    for code in range(1, 21):
        crimes = mp.get(areas, code)
        for i in range(crimes["size"]):
            crime = crimes["elements"][i]
            numb = al.new_list()
            if crime["DATE OCC"] == month and crime["Vict Sex"] == sex:
                al.add_last(numb, crime)
        if numb["size"] > 0:
            numb = sort_unresolved(numb)
            info = {
                "AREA NAME": numb["elements"][0]["AREA NAME"],
                "AREA": code,
                "Crimes": numb["size"],
            }
            if info not in stats["elements"]:
                al.add_last(stats, info)
    stats = sort_stats(stats)   
    if stats["size"] > int(n):
        new_stats = al.new_list()
        al.add_last(new_stats, stats["elements"][i])
        stats = new_stats
    return stats
                
        
    

def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

""""
def datos():
    doc = (data_dir+"crime_in_LA_100.csv")
    dicc = {}
    datos = open(doc, encoding="utf-8")
    reader = csv.reader(datos)
    columns = next(reader)
    
    for column in columns:
        dicc[column] = []
    for row in reader:
        for i in range(len(columns)):
            key = columns[i]
            data = row[i]
            dicc[key].append(data)
            
    datos.close()
    return dicc
    
# Funciones para la carga de datos

def carga(datos, catalog, columns:str):
    for i in datos[columns]:
        al.add_last(catalog["crimes"], i)
        """