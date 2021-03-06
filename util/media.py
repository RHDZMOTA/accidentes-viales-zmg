from os.path import join

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from settings import FileConf


def create_general_annual_accidents_plot():
    df = pd.read_csv(FileConf.FileNames.accidents_per_year)

    accidentes_general = df["accidentes_general"].values
    accidentes_general_diff = -100*(accidentes_general[1:] - accidentes_general[:-1]) / accidentes_general[:-1]
    plt.plot(df["year"].values[1:], accidentes_general_diff)
    plt.show()


    accidentes_general_img = join(FileConf.Paths.img, "accidentes_general_img.png")
    df.plot.bar(x="year", y="accidentes_general", color="blue", alpha=0.65)
    plt.title("Accidentes por año en la ZMG")
    plt.grid()

    plt.savefig(accidentes_general_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()

    muertos_alcohol_img = join(FileConf.Paths.img, "muertos_alcohol_img.png")
    df.plot("year", "muertos_alcohol", color="blue", alpha=0.65)
    plt.title("Muertes por alcohol en la ZMG")
    plt.ylabel("Numero de muertes")
    plt.xlabel("años")
    plt.grid()

    plt.savefig(muertos_alcohol_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()

    accidentes_general_segregacion_img = join(FileConf.Paths.img, "accidentes_general_segregacion_img.png")
    fig, ax = plt.subplots(figsize=(12, 5))
    # Lesionados
    plt.subplot(1, 3, 1)
    plt.plot(df["year"], df["accidentes_lesionados"])
    plt.title("Accidentes con lesionados")
    plt.ylabel("Numero de incidentes")
    plt.xlabel("años")
    plt.grid()
    plt.xticks(df["year"])
    # Muertos
    plt.subplot(1, 3, 2)
    plt.plot(df["year"], df["muertos"])
    plt.title("Muertes totales")
    plt.xlabel("años")
    plt.grid()
    plt.xticks(df["year"])
    # Muertos en lugar de accidente
    plt.subplot(1, 3, 3)
    plt.plot(df["year"], df["muertos_en_lugar_de_accidente"])
    plt.title("Muertes en lugar de accidentes")
    plt.xlabel("años")
    plt.grid()
    plt.xticks(df["year"])

    plt.savefig(accidentes_general_segregacion_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()
    plt.close()


def create_distractions_plot():

    distractions = pd.read_csv(join(FileConf.Paths.data, "distacciones_2016.csv"))

    distractions_img = join(FileConf.Paths.img, "manejo_con_celular.png")
    distractions.plot.bar(x="municipio", stacked=True)
    plt.title("Conducción con distracciones por smart-phones en 2016")
    plt.ylabel("%")

    plt.savefig(distractions_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()

    distractions.mean()


def create_vehicles_plot():

    vehicles = pd.read_csv(join(FileConf.Paths.data, "vehiculos_en_circulacion.csv"))

    jalisco = vehicles.Jalisco.values
    years = vehicles.Anios.values
    jalisco_diff = jalisco[1:] / jalisco[:-1] - 1

    parque_vehicular_img = join(FileConf.Paths.img, "parque_vehicular.png")
    fig, ax = plt.subplots(figsize=(7, 5))
    plt.subplot(2, 1, 1)
    plt.plot(years, jalisco)
    plt.title("Parque vehicular en Jalisco")
    plt.ylabel("Vehículos")
    plt.subplot(4, 1, 4)
    plt.bar(years[1:], 100 * jalisco_diff)
    plt.title("Crecimiento porcentual")
    plt.ylabel("%")


    #plt.savefig(parque_vehicular_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    #plt.close()

    average_growth = np.mean(jalisco_diff[-5:])


def create_phone_usage_plot():

    phone_type = pd.read_csv(join(FileConf.Paths.data, "jaslico_tipo_celular.csv"))
    phone_users = pd.read_csv(join(FileConf.Paths.data, "usuarios_jalisco_celular.csv"))

    fig, ax = plt.subplots(figsize=(5, 5))
    phone_type_img = join(FileConf.Paths.img, "tipo_de_celular.png")
    phone_type[["smartphone", "celular_comun", "anio"]].plot.bar(x="anio", stacked=True)
    plt.title("Tipo de celular en Jalisco")
    plt.ylabel("%")
    plt.xlabel("")

    plt.savefig(phone_type_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()


def create_tech_plots():
    def create_exp_function(alpha, beta):
        return lambda x: -alpha*np.exp(-beta*x)+100
    f_g = create_exp_function(23.68, 0.26321)
    f_s = create_exp_function(30.2, 0.52864)
    step = 1/12
    initial_value = 0
    final_value = 3 + 3 + step
    years = np.arange(initial_value, final_value, step)

    gs = [f_g(x) for x in years]
    ss = [f_s(x) for x in years]

    print("gs[-1] = %f" % gs[-1])
    print("ss[-1] = %f" % ss[-1])

    result = [g * s / 100 for g, s in zip(gs, ss)]
    print("Smartphone percentage 2021: %f" % result[-1])

    forecast_usage_img = join(FileConf.Paths.img, "pronostico_adopcion.png")
    plt.plot(years + 2015, gs, label="Tecnología celular general")
    plt.plot(years + 2015, ss, label="Smartphones")
    plt.plot([2015, 2016], [76.32, 81.8], ".")
    plt.plot([2015, 2016], [69.8, 82.2], ".")
    plt.title("Pronóstico de adopción de tecnología celular")
    plt.xlabel("Años")
    plt.ylabel("%")
    plt.legend()

    plt.savefig(forecast_usage_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()

    smartphone_usage_img = join(FileConf.Paths.img, "smartphone_usage.png")
    plt.plot(years + 2015, result, label="Smartphones")
    plt.title("Porcentage de la población con Smartphones")
    plt.xlabel("Años")
    plt.ylabel("%")
    plt.legend()

    plt.savefig(smartphone_usage_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()

    # Driving with distractions

    k = 0.892459
    delta = lambda x: k * x
    delta_list = [delta(x) for x in result]

    df = pd.DataFrame([])
    df["years"] = years
    df["months"] = df.years * 12
    df["celphone_exposure"] = gs
    df["smartphone_proportion"] = ss
    df["smartphone_exposure"] = result
    df["delta"] = delta_list


    distraction_img = join(FileConf.Paths.img, "distraction.png")
    plt.plot(years + 2015, delta_list, label="Distracción por Smartphone")
    plt.title("Porcentaje de conductores con distracciones por Smartphone")
    plt.xlabel("Años")
    plt.ylabel("%")
    plt.legend()

    plt.savefig(distraction_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()

    delta_list[-1]

    # Driving with ditractions [project]
    k_t = lambda x: k - 0.02 * x
    new_delta = lambda s, y: k_t(y) * s
    df["delta_project"] = df.apply(lambda x: new_delta(x["smartphone_exposure"], x["years"]), 1)

    distraction_project_img = join(FileConf.Paths.img, "distraction_project.png")
    plt.plot(years + 2015, df.delta_project.values, label="Distracción por Smartphone después de proyecto")
    plt.title("Porcentaje de conductores con distracciones por Smartphone")
    plt.xlabel("Años")
    plt.ylabel("%")
    plt.legend()

    plt.savefig(distraction_project_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()

    df.to_csv("output/forecast_smartphone.csv", index=None)

    df["years"] = df.years + 2015
    # Combine plot

    smartphones_complete_forecast_img = join(FileConf.Paths.img, "smartphone_complete_forecast.png")
    df.drop(columns=["months", "delta_project"]).rename(
        columns={
            "delta": "Conductores con distracciones de Smartphone",
            "smartphone_proportion": "Proporción de Smartphones respecto a tec. celular",
            "smartphone_exposure": "Población expuesta a smartphones",
            "celphone_exposure": "Población expuesta a tec. celular."
        }).plot(x="years")
    plt.title("Pronóstico: tecnología celular")
    plt.ylabel("%")
    plt.xlabel("años")
    plt.savefig(smartphones_complete_forecast_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()

    # Plot with project
    distraction_compare_img = join(FileConf.Paths.img, "distraction_compare_img.png")
    df[["delta", "delta_project", "years"]].rename(
        columns={
            "delta": "[Antes]",
            "delta_project": "[Después]"
        }).plot(x="years")
    plt.title("Conductores con distracciones de Smartphone")
    plt.ylabel("%")
    plt.xlabel("años")
    #plt.show()
    plt.savefig(distraction_compare_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()




def create_cellphone_accidents():
    vehicle_forecast = pd.read_csv("output/forecast_vehicles.csv")
    smartphones_forecast = pd.read_csv("output/forecast_smartphone.csv")

    # df["accidentes"] = 7 * df["average"] / 1000

    def calculate_accidents(vehicles, distr):
        return 4.9 * vehicles * distr / (1000 * 60)

    smartphones_forecast["years"] = smartphones_forecast.years + 2015
    vehicle_forecast["years"] = vehicle_forecast.index + 2016
    results = pd.merge(vehicle_forecast[["average", "years"]], smartphones_forecast, on="years")
    results["smart_accidents"] = results.apply(lambda x: calculate_accidents(vehicles=x["average"], distr=x["delta"]), 1)
    results["smart_accidents_after"] = results.apply(lambda x: calculate_accidents(vehicles=x["average"], distr=x["delta_project"]), 1)

    # Accidents generated by smartphones per year
    smart_accidents_img = join(FileConf.Paths.img, "smart_accidents.png")
    results.plot.bar(x="years", y="smart_accidents", color="b", legend=None)
    plt.title("Pronósitco: Numero de choques generados por uso de celular")
    plt.ylabel("Accidentes")
    # plt.show()
    plt.savefig(smart_accidents_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()

    # Cost per accident.

    # After project
    smart_accidents_after_img = join(FileConf.Paths.img, "smart_accidents_after.png")
    results[["years", "smart_accidents", "smart_accidents_after"]].rename(columns={
        "smart_accidents": "[Antes]",
        "smart_accidents_after": "[Despues]"
    }).plot.bar(x="years")
    plt.title("Pronósitco: Numero de choques generados por uso de celular después del proyecto")
    plt.ylabel("Accidentes")
    plt.xlabel("Años")
    plt.savefig(smart_accidents_after_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()

    # Diff
    from matplotlib.ticker import FuncFormatter
    accident_savings_img = join(FileConf.Paths.img, "accident_savings.png")
    results["savings"] = 24603 * results.apply(lambda x: x["smart_accidents"] - x["smart_accidents_after"], 1)
    ax = results.plot.bar(x="years", y="savings", color="b", legend=None)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda y, _: '${:,.0f}'.format(y)))
    plt.title("Ahorro generado por reducción de accidentes")
    plt.xlabel("Años")
    plt.ylabel("MXN")
    plt.savefig(accident_savings_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()

def create_vehicle_forecast():
    vehicles = pd.read_csv(join(FileConf.Paths.data, "vehiculos_en_circulacion.csv"))
    jalisco = vehicles.Jalisco.values
    years = vehicles.Anios.values
    jalisco_diff = jalisco[1:] / jalisco[:-1] - 1

    growth_last_10 = jalisco_diff[-20:]

    def get_next_gowth():
        return np.random.choice(growth_last_10, 5)

    def get_next(last):
        forecast = [last]
        for r in get_next_gowth():
            forecast.append(forecast[-1] * (1 + r))
        return forecast

    last = jalisco[-1]
    df = pd.DataFrame([])
    for i in range(200):
        df[str(i)] = get_next(last)

    df.index = (df.index + 2016).values

    vehicle_forecast_img = join(FileConf.Paths.img, "vehicle_forecast_img.png")
    df.plot(legend=False)
    plt.plot(df.index.values, df.mean(1).values, "k", linewidth=3)
    plt.title("Simulación: parque vehicular")
    plt.xlabel("Años a partir del 2016")
    plt.ylabel("Número de vehículos")

    plt.savefig(vehicle_forecast_img, bbox_inches="tight", pad_inches=0.5, dpi=100)
    plt.close()

    df["average"] = df.mean(1)
    df["accidentes"] = 7 * df["average"] / 1000
    df["muertes"] = df["accidentes"] * 0.0226

    df.plot(x="accidentes", y="muertes")
    plt.title()
    plt.show()

    df.to_csv("output/forecast_vehicles.csv", index=False)

    df.iloc[-1].plot.kde()
    plt.show()

    df.iloc[-1].mean()
    df.iloc[-1].describe()



def create_media():
    return {}
