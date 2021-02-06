import pandas as pd


def cleaning():
    dict_data = {}
    df = pd.read_csv("time_series_covid19_confirmed_global.csv")
    for row in df.iterrows():
        province = ""
        country = ""
        for index, day in enumerate(row[1]):
            if index == 0:
                if str(day) != "nan":
                    province = " - " + str(day)
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
