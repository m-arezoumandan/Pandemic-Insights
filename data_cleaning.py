import csv


def cleaning():
    country = ''
    max_cases = 0
    elected_countries = []
    not_zero_cases = 0
    dict_data = {}

    with open(r'owid-covid-data.csv') as csvf:
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            if country != row['location']:
                if max_cases > 500 and not_zero_cases > 200:
                    elected_countries.append(country)
                country = row['location']
                not_zero_cases = 0
                if row['new_cases'] != '':
                    max_cases = int(row['new_cases'])
            elif row['new_cases'] != '':
                if row['new_cases'] != '0':
                    not_zero_cases = not_zero_cases + 1
                if max_cases < int(row['new_cases']):
                    max_cases = int(row['new_cases'])
    country = ''
    flag = 0
    num_days = 0
    for ec in elected_countries:
        dict_data[ec] = []

    with open(r'owid-covid-data.csv', encoding='utf-8') as csvf:
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
            if row['location'] in elected_countries:
                if country == row['location']:
                    if flag == 0:
                        if row['new_cases'] != '':
                            if int(row['new_cases']) > 5:
                                flag = 1
                                num_days += 1
                                dict_data[row['location']].append(int(row['new_cases']))
                    else:
                        if row['new_cases'] != '' and num_days < 300:
                            num_days += 1
                            dict_data[row['location']].append(int(row['new_cases']))

                else:
                    country = row['location']
                    flag = 0
                    num_days = 0
                    if row['new_cases'] != '':
                        if int(row['new_cases']) > 5:
                            flag = 1
                            num_days += 1
                            dict_data[row['location']].append(int(row['new_cases']))

    del dict_data['World']
    for ec in dict_data.copy():
        if len(dict_data[ec]) != 300:
            del dict_data[ec]

    return dict_data
