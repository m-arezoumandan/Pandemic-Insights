import csv

def cleaning():

    '''

    :return:
    '''

    dict_data = {}
    country = ""

    with open(r'owid-covid-data.csv') as csvf:
        csv_reader = csv.DictReader(csvf)
        for row in csv_reader:
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
                        dict_data[row['location']].append(abs(int(row['new_cases'])))

            else:
                country = row['location']
                dict_data[country] = []
                flag = 0
                num_days = 0
                if row['new_cases'] != '':
                    if int(row['new_cases']) > 5:
                        flag = 1
                        num_days += 1
                        dict_data[row['location']].append(int(row['new_cases']))

    del dict_data['World']
    print(len(dict_data))
    for ec in dict_data.copy():
        if len(dict_data[ec]) != 300:
            del dict_data[ec]

    print(len(dict_data))
    return dict_data
