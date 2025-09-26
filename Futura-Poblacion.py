
#1.	Cálculo de tasas de crecimiento
#2.	Proyección de población
#3.	Visualización
#4.	Análisis adicional

menu = '''
______________________________________
| 1. Cálculo de tasas de crecimiento |
| 2. Proyección de población         |
| 3. Visualización                   |
| 4. Análisis adicional              |
| 0. Salir del sistema               |
|____________________________________|
'''

#1.	Cálculo de tasas de crecimiento:
# Implementar un algoritmo para calcular la tasa de crecimiento poblacional anual utilizando
# la fórmula de tasa de crecimiento compuesto: TCC=(Vf/Vi)^1/n -1
def calculo_de_tasas_de_crecimiento():
    #Solo utlizo el primer y el ultimo año
    # ya que con la formulase necesita un valor inial y uno final
    #TCC=(Vf/Vi)^1/n -1

    poblacion_2018 = {
        "Bogotá": 7830,
        "Antioquia": 6420,
        "Valle del Cauca": 4840
    }

    poblacion_2022 = {
        "Bogotá": 8120,
        "Antioquia": 6645,
        "Valle del Cauca": 5090
    }

    # n son los años transcurridos de un año al proximo
    n = 4

    tasa_crecimiento = {}
    for region in poblacion_2018:
        p0 = poblacion_2018[region]
        pf = poblacion_2022[region]
        r = (pf / p0) ** (1 / n) - 1
        tasa_crecimiento[region] = r

    print("Tasa de Crecimiento Anual Compuesto:")
    for region, r in tasa_crecimiento.items():
        print(f"{region}: {r * 100:.2f}% anual")

#2.	Proyección de población: Proyectar
# la población de cada región para los próximos 5 años usando
# la tasa de crecimiento anual calculada.
def proyeccion_de_poblacion():

    # utilizo el mismo diccionario para abreviar
    poblacion_2018 = {
        "Bogotá": 7830,
        "Antioquia": 6420,
        "Valle del Cauca": 4840
    }

    poblacion_2022 = {
        "Bogotá": 8120,
        "Antioquia": 6645,
        "Valle del Cauca": 5090
    }
    n= 4
    tasa_crecimiento = {}
    for region in poblacion_2018:
        p0 = poblacion_2018[region]
        pf = poblacion_2022[region]
        r = (pf / p0) ** (1 / n) - 1
        tasa_crecimiento[region] = r

    # Proyecion de la población para los próximos 5 años (2023-2027)
    proyecciones = {region: [] for region in poblacion_2022}
    años_proyeccion = [2023, 2024, 2025, 2026, 2027]

    for region in poblacion_2022:
        p_actual = poblacion_2022[region]
        r = tasa_crecimiento[region]
        for año in años_proyeccion:
            p_actual = p_actual * (1 + r)
            proyecciones[region].append(round(p_actual, 2))


    print("\nProyecciones de población:")
    for region in proyecciones:
        print(f"\n{region}:")
        for año, poblacion in zip(años_proyeccion, proyecciones[region]):
            print(f"  {año}: {poblacion}")


#3.	Visualización: Graficar los resultados de
# la población proyectada para cada región
# utilizando matplotlib o seaborn.
def visualizacion():
    import matplotlib.pyplot as plt
    poblacion_2018 = {
        "Bogotá": 7830,
        "Antioquia": 6420,
        "Valle del Cauca": 4840
    }

    poblacion_2022 = {
        "Bogotá": 8120,
        "Antioquia": 6645,
        "Valle del Cauca": 5090
    }

    n = 4

    tasa_crecimiento = {}
    for region in poblacion_2018:
        p0 = poblacion_2018[region]
        pf = poblacion_2022[region]
        r = (pf / p0) ** (1 / n) - 1
        tasa_crecimiento[region] = r

    # Proyecion población para los próximos 5 años (2023-2027)
    proyecciones = {region: [] for region in poblacion_2022}
    años_proyeccion = [2023, 2024, 2025, 2026, 2027]

    for region in poblacion_2022:
        p_actual = poblacion_2022[region]
        r = tasa_crecimiento[region]
        for año in años_proyeccion:
            p_actual = p_actual * (1 + r)
            proyecciones[region].append(p_actual)
    #para ver la grafica
    plt.figure(figsize=(10, 6))

    # Grafico de los datos históricos
    años_historicos = [2018, 2019, 2020, 2021, 2022]
    for region, valores in poblacion_2018.items():
        plt.plot([2018, 2022], [poblacion_2018[region], poblacion_2022[region]], "o--", label=f"{region} (Histórico)")

    # Grafica proyecciones de la problacion
    for region in proyecciones:
        plt.plot(años_proyeccion, proyecciones[region], "o-", label=f"{region} (Proyección)")

    plt.title("Proyección de Población por Región (2018-2027)")
    plt.xlabel("Año")
    plt.ylabel("Población (miles de habitantes)")
    plt.legend()
    plt.grid(True)
    plt.show()


#4.	Análisis adicional: El aprendiz deberá investigar y comentar sobre factores
# que pudieron haber influido en el crecimiento o decrecimiento poblacional de
# las regiones seleccionadas (Bogotá, Antioquia y Valle del Cauca)
# durante el período analizado. Ejemplos de eventos que podrían influir
# son desplazamientos forzados, políticas públicas de salud, o la pandemia de COVID-19.
def analisis_adicional():
    print("Haciendo una investigacion breve lo princpical que pude ver es que por la migracion ha incrementado la poblacion en estas 3 regiones\n")
    print("Bogotá sigue creciendo por migración interna e internacional, aunque la pandemia y los altos costos han frenado ese ritmo\n")
    print("Antioquia mantiene dinamismo por el atractivo de Medellín y la reducción del conflicto armado, con movimientos hacia ciudades intermedias.\n")
    print("Valle del Cauca combina atracción (por oportunidades en Cali) con expulsión (por violencia e inseguridad), y tuvo un fuerte impacto de la pandemia y la crisis social de 2021.")

#incio del programa:
while True:
    print(menu)
    opcion = int(input("ingrese una de las opciones del menu: "))
    try:
        if opcion == 1:
            calculo_de_tasas_de_crecimiento()
        elif opcion == 2:
            proyeccion_de_poblacion()
        elif opcion == 3:
            visualizacion()
        elif opcion == 4:
            analisis_adicional()
        elif opcion == 0:
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida")
    except KeyboardInterrupt:
        print("ha ocurrido un error inesperado")