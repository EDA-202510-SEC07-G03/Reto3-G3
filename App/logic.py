import time
import csv
import os
from datetime import datetime
from tabulate import tabulate
from DataStructures.List import array_list as al
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



def load_data(catalog, filename=(data_dir+"Crime_in_LA_100.csv")):
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
            "AREA": row["AREA"],
            "AREA NAME": row["AREA NAME"],
            "Rpt Dist No": row["Rpt Dist No"],
            "Part 1-2": row["Part 1-2"],
            "Crm Cd": row["Crm Cd"],
            "Crm Cd Desc": row["Crm Cd Desc"],
            "Vict Age": row["Vict Age"],
            "Vict Sex": row["Vict Sex"],
            "Vict Descent": row["Vict Descent"],
            "Premise Cd": row["Premise Cd"]if "Premise CD" in row else "Unknown",
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
            "DATE OCC": crime["DATE OCC"].strftime("%Y-%m-%d") if crime["DATE OCC"] != "Unknown" else "Unknown",
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
            "DATE OCC": crime["DATE OCC"].strftime("%Y-%m-%d") if crime["DATE OCC"] != "Unknown" else "Unknown",
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


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


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


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


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