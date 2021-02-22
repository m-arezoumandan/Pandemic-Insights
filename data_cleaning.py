import pandas as pd
import math


def cleaning():
    dict_data = {}
    df = pd.read_csv("time_series_covid19_confirmed_global.csv")
    for row in df.iterrows():
        province = ""
        country = ""
        for index, day in enumerate(row[1]):
            if index == 0:
                if str(day) != "nan":
                    province = ", " + str(day)
            elif index == 1:
                country = day + province
                dict_data[country] = []
            elif index == 2:
                dict_data[country].append(day)
                yesterday = day
            else:
                daily = day - yesterday
                if daily < 0:
                    dict_data[country].append(0)
                else:
                    dict_data[country].append(daily)
                yesterday = day

    return dict_data


def cleaning2():
    dict_data = {}
    df = pd.read_csv("dpc-covid19-ita-regioni.csv")
    for row in df.iterrows():
        region = row[1]["denominazione_regione"]
        if region not in dict_data.keys():
            dict_data[region] = []
        if int(row[1]["nuovi_positivi"]) < 0:
            dict_data[region].append(0)
        else:
            dict_data[region].append(int(row[1]["nuovi_positivi"]))
    return dict_data


def cleaning3():
    dict_data = {}
    df = pd.read_csv("dpc-covid19-ita-province.csv")
    for row in df.iterrows():
        region = row[1]["denominazione_provincia"]
        if region == "In fase di definizione/aggiornamento" or region == "Fuori Regione / Provincia Autonoma":
            continue
        if region not in dict_data.keys():
            dict_data[region] = []
            dict_data[region].append(int(row[1]["totale_casi"]))
        else:
            cases = int(row[1]["totale_casi"])
            if cases - dict_data[region][-1] < 0:
                print(cases)
                print(region)
            dict_data[region].append(cases - dict_data[region][-1])
    return dict_data
