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
        "area_map": None,
        "area_name_map": None
    }
    catalog["crimes"] = al.new_list()
    catalog["date_tree"] = bst.new_map()
    catalog["area_map"] = mp.new_map(21, 0.7)
    catalog["area_name_map"] = mp.new_map(21, 0.7)
    
    return catalog



def load_data(catalog, filename=(data_dir+"Crime_in_LA_20.csv")):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    start_time = get_time()
    file = open(filename, encoding="utf-8")
    reader = csv.DictReader(file)
    for row in reader:
        crime={
            "DR_NO": row["DR_NO"], 
            "Date Rptd": datetime.strptime(row["Date Rptd"], "%m/%d/%Y %I:%M:%S %p"),
            "DATE OCC": datetime.strptime(row["DATE OCC"], "%m/%d/%Y %I:%M:%S %p"),
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
    end_time = get_time()
    time = delta_time(start_time,end_time)
    return catalog["crimes"]["size"],time

def create_tree(catalog):
    """
    Crea el árbol para las fechas
    """
    for i in range(catalog["crimes"]["size"]):
        crime = catalog["crimes"]["elements"][i]
        bst.put(catalog["date_tree"], crime["Date Rptd"], crime["Vict Age"])
    return catalog["date_tree"]

def create_area_map(catalog):
    """
    Crea el mapa para las áreas
    """
    for i in range(1, 21): 
        if not mp.contains(catalog["area_map"], i):
            area_list = al.new_list()
            mp.put(catalog["area_map"], i, area_list)
        else:
            area_list = mp.get(catalog["area_map"], i)
        for j in range(catalog["crimes"]["size"]):  
            crime = catalog["crimes"]["elements"][j]
            if crime["AREA"] is not "Unknown":
                if int(crime["AREA"]) == i: 
                    al.add_last(area_list, crime)

    return catalog["area_map"]

def create_area_name_map(catalog):
    for j in range(catalog["crimes"]["size"]):  
        crime = catalog["crimes"]["elements"][j]
        area_name = crime["AREA NAME"]
        if area_name != "Unknown":
            if not mp.contains(catalog["area_name_map"], area_name.lower()):
                area_list = al.new_list()
                mp.put(catalog["area_name_map"], area_name.lower(), area_list)
            else:
                area_list = mp.get(catalog["area_name_map"], area_name.lower())
            al.add_last(area_list, crime)
    return catalog["area_name_map"]
     
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
    sl.merge_sort(filtro, True)
    current_node = filtro["first"]
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


def compare_by_date_desc(crime1, crime2):
    """
    Compara dos crímenes por la fecha 'DATE OCC' en orden descendente.
    """
    d1 = crime1["DATE OCC"]
    d2 = crime2["DATE OCC"]
    if d1 > d2:
        return -1
    elif d1 < d2:
        return 1
    else:
        return 0

def req_3(catalog, N: int, area_name: str):
    """
    Retorna el resultado del requerimiento 3
    """
    start_time = get_time()
    
    area_name_map = catalog["area_name_map"]
    crimes_list_entry = mp.get(area_name_map, area_name.lower())

    if crimes_list_entry is None:
        print(f"No se encontraron crímenes reportados en el área: {area_name}")
        return None

    crimes_list = crimes_list_entry
    total_crimes = al.size(crimes_list)

    if total_crimes == 0:
        print(f"No se encontraron crímenes reportados en el área: {area_name}")
        return None

    sorted_crimes = al.merge_sort(crimes_list, cmp_function=compare_by_date_desc)

    if al.size(sorted_crimes) > N:
        sorted_crimes["elements"] = sorted_crimes["elements"][:N]
        sorted_crimes["size"] = N

    recent_crimes = al.new_list()
    for i in range(al.size(sorted_crimes)):
        crime = sorted_crimes["elements"][i]
        crime_info = {
            "DR_NO": crime["DR_NO"],
            "DATE OCC": crime["DATE OCC"],
            "TIME OCC": crime["TIME OCC"],
            "AREA NAME": crime["AREA NAME"],
            "Rpt Dist No": crime["Rpt Dist No"],
            "Part 1-2": crime["Part 1-2"],
            "Crm Cd": crime["Crm Cd"],
            "Status": crime["Status"],
            "LOCATION": crime["LOCATION"]
        }
        al.add_last(recent_crimes, crime_info)

    end_time = get_time()
    elapsed_time = (end_time - start_time)

    return recent_crimes, total_crimes, elapsed_time


def sort_unresolved(unresolved):

    date_list = al.new_list()
    for i in range(unresolved["size"]):
        al.add_last(date_list, unresolved["elements"][i]["Date Rptd"])
    al.selection_sort(date_list, lambda u1, u2: u1 < u2)
    sorted_unresolved = al.new_list()
    for date in date_list["elements"]:
        added = False  
        for crime in unresolved["elements"]:
            if not added and crime["Date Rptd"] == date:
                al.add_last(sorted_unresolved, crime)
                added = True 
    return sorted_unresolved

def sort_stats(stats):
    
    crimes_list = al.new_list()
    for i in range(stats["size"]):
        al.add_last(crimes_list, (stats["elements"][i]["Crimes"], stats["elements"][i]["AREA NAME"]))
    al.selection_sort(crimes_list, lambda c1, c2: 
        (c1[0] > c2[0]) or (c1[0] == c2[0] and c1[1] < c2[1]))
    sorted_stats = al.new_list()
    processed = al.new_list() 
    for crimes, area_name in crimes_list["elements"]:
        already_added = False
        for stat in stats["elements"]:
            for processed_stat in processed["elements"]:
                if processed_stat == stat:
                    already_added = True
            if not already_added and stat["Crimes"] == crimes and stat["AREA NAME"] == area_name:
                al.add_last(sorted_stats, stat)
                al.add_last(processed, stat)  
                already_added = True  
    return sorted_stats

def extended_sort_stats(stats):
    
    data_list = al.new_list()
    for i in range(stats["size"]):
        stat = stats["elements"][i]
        crimes = stat["Crimes"]
        tuples = al.size(stat["Tuples"])
        area_name = stat["AREA NAME"]
        al.add_last(data_list, (crimes, tuples, area_name, i))
    al.selection_sort(data_list, lambda c1, c2: (c1[0] > c2[0]) or 
        (c1[0] == c2[0] and c1[1] > c2[1]) or 
        (c1[0] == c2[0] and c1[1] == c2[1] and c1[2] < c2[2])
    )
    sorted_stats = al.new_list()
    for _, _, _, index in data_list["elements"]:
        al.add_last(sorted_stats, stats["elements"][index])
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
    start_time = get_time()
    mes = datetime.strptime(mes, "%m")
    areas = catalog["area_map"]
    stats = al.new_list()
    n = int(n)
    for code in range(1, 21):
        crimes = mp.get(areas, code)
        counts = {}
        numb = al.new_list()
        for i in range(crimes["size"]):
            crime = crimes["elements"][i]
            if crime["Vict Sex"] == sex:
                year = crime["Date Rptd"].year
                if year not in counts:
                    counts[year] = 0
                counts[year] += 1
                if crime["Date Rptd"].month == mes.month:
                    al.add_last(numb, crime)

        if numb["size"] > 0:
            tuplas = al.new_list()
            for year, count in counts.items():
                al.add_last(tuplas, (count, year))
            info = {
                "AREA NAME": numb["elements"][0]["AREA NAME"],
                "AREA": code,
                "Crimes": numb["size"],
                "Tuples": tuplas,
            }
            if info not in stats["elements"]:
                al.add_last(stats, info)
    stats = extended_sort_stats(stats)   
    if stats["size"] > n:
        new_stats = al.new_list()
        for i in range(0, n):
            al.add_last(new_stats, stats["elements"][i])
        stats = new_stats
    end_time = get_time()
    elapsed_time = delta_time(start_time, end_time)   
    return stats, elapsed_time
                
        
    

def req_7(catalog, N, sex, age_min, age_max):
    """
    Determina los N crímenes más comunes para víctimas de un sexo específico en un rango de edad dado.
    """
    start_time = get_time()
    
    # Usaremos un mapa para contar por código de crimen
    crime_stats = {}
    
    # Recorrer todos los crímenes
    crimes_list = catalog["crimes"]
    size = al.size(crimes_list)
    
    for i in range(size):
        crime = al.get_element(crimes_list, i)
        
        try:
            # Verificar campos necesarios
            if (not crime["Vict Sex"] or not crime["Vict Age"] or 
                not crime["Crm Cd"] or not crime["DATE OCC"]):
                continue
                
            victim_sex = crime["Vict Sex"].upper()
            victim_age = int(crime["Vict Age"])
            crime_code = crime["Crm Cd"]
            crime_year = crime["DATE OCC"].year
            
            # Filtrar por sexo y rango de edad
            if victim_sex == sex.upper() and age_min <= victim_age <= age_max:
                # Inicializar estructura si no existe
                if crime_code not in crime_stats:
                    crime_stats[crime_code] = {
                        "code": crime_code,
                        "total": 0,
                        "ages": {},
                        "years": {}
                    }
                
                # Actualizar estadísticas
                crime_stats[crime_code]["total"] += 1
                
                # Actualizar conteo por edad
                if victim_age in crime_stats[crime_code]["ages"]:
                    crime_stats[crime_code]["ages"][victim_age] += 1
                else:
                    crime_stats[crime_code]["ages"][victim_age] = 1
                
                # Actualizar conteo por año
                if crime_year in crime_stats[crime_code]["years"]:
                    crime_stats[crime_code]["years"][crime_year] += 1
                else:
                    crime_stats[crime_code]["years"][crime_year] = 1
                    
        except (ValueError, TypeError, AttributeError, KeyError):
            continue
    
    # Convertir a lista
    crime_list = al.new_list()
    for code in crime_stats:
        crime_data = crime_stats[code]
        
        # Convertir diccionarios a listas de tuplas
        ages_list = [(age, count) for age, count in crime_data["ages"].items()]
        years_list = [(year, count) for year, count in crime_data["years"].items()]
        
        al.add_last(crime_list, {
            "code": crime_data["code"],
            "total": crime_data["total"],
            "ages": ages_list,
            "years": years_list
        })
    
    # Ordenar la lista por total de crímenes (descendente)
    def compare_crimes(crime1, crime2):
        return crime2["total"] - crime1["total"]
    
    sorted_crimes = al.merge_sort(crime_list, sort_criteria=False, cmp_function=compare_crimes)
    
    # Tomar los primeros N elementos
    result_size = min(N, al.size(sorted_crimes))
    result = al.sub_list(sorted_crimes, 0, result_size)
    
    end_time = get_time()
    return result, delta_time(start_time, end_time)



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