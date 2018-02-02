from os.path import join

import matplotlib.pyplot as plt
import pandas as pd

from settings import FileConf


def create_general_annual_accidents_plot():
    df = pd.read_csv(FileConf.FileNames.accidents_per_year)

    df.head()

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


def create_media():
    return {}
