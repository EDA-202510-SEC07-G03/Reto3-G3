import sys
import os
from tabulate import tabulate
import App.logic as log
from DataStructures.List import array_list as al
data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Data')
default_name = os.path.join(data_dir, 'Crime_in_LA_100.csv')

def new_logic():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función de la lógica donde se crean las estructuras de datos
    catalog = log.new_logic()
    return catalog

def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Carga de informacion en estructuras auxiliares")
    print("3- Ejecutar Requerimiento 1")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    size, time = log.load_data(control)
    first = log.primeros(control)
    last = log.ultimos(control)
    line_name={
        "DR_NO": "ID Reporte",
        "Date Rptd": "Fecha Reportado",
        "DATE OCC": "Fecha Ocurrencia",
        "AREA NAME": "Área",
        "Crm Cd": "Código Crimen"
    }
    print("Numero de registros: ", size)
    print("Tiempo en ejecutar: ", time)
    print("Primeros 5 registros cargados: ")
    print("...")
    print(tabulate(first["elements"],
                   headers= line_name,
                   tablefmt="grid",
                   stralign="center"))
    print("...")
    print("Ultimos 5 registros cargados: ")
    print("...")
    print(tabulate(last["elements"],
                   headers= line_name,
                   tablefmt="grid",
                   stralign="center"))
    print("...")
    return control

    
def auxiliary_data(control):
    """
        Carga los datos en estructuras auxiliares
    """
    log.create_tree(control)
    log.create_area_map(control)
    log.create_area_name_map(control)
    print("Estructuras auxiliares cargadas")
    print("...")


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    anno0 = input("Ingrese la fecha inicial: ")
    anno1 = input("Ingrese la fecha final: ")
    data = log.req_1(control, anno0, anno1)
    line_name={
        "DR_NO": "ID Reporte",
        "DATE OCC": "Fecha Ocurrencia",
        "TIME OCC": "Hora Ocurrencia",
        "AREA NAME": "Área",
        "Crm Cd": "Código Crimen",
        "Crm Cd Desc": "Descripción Crimen",
        "LOCATION": "Ubicación",
    }
    print("Un total de ", data[1], "registros pasaron el filtro.")
    print("...")
    print("Listado de registros: ")
    print("...")
    print(tabulate(data[0]["elements"],
                   headers= line_name,
                   tablefmt="grid",
                   stralign="center"))
    print("...")
    print("La accion Tomo ", data[2], "ms")
    

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    area_name = input("Ingrese el nombre del área: ")
    N = int(input("Ingrese el número de crímenes más recientes que desea ver: "))

    data = log.req_3(control, N, area_name)

    if data is None:
        print("No se encontraron crímenes para el área especificada.")
        return

    recent_crimes, total_crimes, elapsed_time = data

    line_name = {
        "DR_NO": "ID Reporte",
        "DATE OCC": "Fecha Ocurrencia",
        "TIME OCC": "Hora Ocurrencia",
        "AREA NAME": "Área",
        "Rpt Dist No": "Distrito Reporte",
        "Part 1-2": "Parte 1-2",
        "Crm Cd": "Código Crimen",
        "Status": "Estado",
        "LOCATION": "Ubicación"
    }

    print(f"\nUn total de {total_crimes} crímenes fueron encontrados en el área '{area_name}'.")
    print(f"\nListado de los {len(recent_crimes['elements'])} crímenes más recientes:\n")
    print("...")
    print(tabulate(recent_crimes["elements"],
                   headers=line_name,
                   tablefmt="grid",
                   stralign="center"))
    print("...")
    print(f"La acción tomó {elapsed_time} ms")


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 4
    pass


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    anno0 = input("Ingrese la fecha inicial: ")
    anno1 = input("Ingrese la fecha final: ")
    n = input("Ingrese cuantas areas desea ver: ")
    data = log.req_5(control, n, anno0, anno1)   
    line_name={
        "AREA NAME": "Área",
        "AREA": "Codigo Área",
        "Crimes": "Cantidad de Crímenes",
        "First": "Primer Crimen",
        "Last": "Ultimo Crimen",
    }
    print("Listado de registros: ")
    print("...")
    print(tabulate(data[0]["elements"],
                   headers= line_name,
                   tablefmt="grid",
                   stralign="center"))
    print("...")
    print("La accion Tomo ", data[1], "ms")
    


def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    mes = input("Ingrese el mes: ")
    sex = input("Ingrese el sexo: ")
    n = input("Ingrese cuantas areas desea ver: ")
    data = log.req_6(control, n, sex, mes)
    line_name={
        "AREA NAME": "Área",
        "AREA": "Codigo Área",
        "Crimes": "Crimenes en el mes dado",
        "Tuples": "Tuplas de crimenes" 
    }
    print("Listado de registros: ")
    print("...")
    print(tabulate(data[0]["elements"],
                   headers= line_name,
                   tablefmt="grid",
                   stralign="center"))
    print("...")
    print("La accion Tomo ", data[1], "ms")


def print_req_7(control):
    print("🔎 Requerimiento 7: Crímenes más comunes por sexo y rango de edad")
    N = int(input("Ingrese la cantidad de crímenes más comunes a mostrar (N): "))
    sex = input("Ingrese el sexo de la víctima (M/F): ").upper()
    age_min = int(input("Edad mínima: "))
    age_max = int(input("Edad máxima: "))

    result, elapsed = log.req_7(control, N, sex, age_min, age_max)
    print(f"\n✅ Tiempo de ejecución: {elapsed:.3f} ms\n")

    for i in range(al.size(result)):
        crime = al.get_element(result, i)
        print(f"🔸 Crimen #{i+1}")
        print(f"  - Código: {crime['code']}")
        print(f"  - Total crímenes: {crime['count']}")

        by_age = sorted(crime["By Age"].items(), key=lambda x: x[1], reverse=True)
        by_year = sorted(crime["By Year"].items(), key=lambda x: x[1], reverse=True)

        print("  - Crímenes por edad:")
        print("    " + "; ".join([f"{count}@{age}" for age, count in by_age]))

        print("  - Crímenes por año:")
        print("    " + "; ".join([f"{count}@{year}" for year, count in by_year]))
        print("")


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
            
        elif int(inputs) == 2:
            print("...")
            auxiliary_data(control)
            
        elif int(inputs) == 3:
            print_req_1(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
