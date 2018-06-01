#!/usr/bin/env python3
import csv
import matplotlib.pyplot as plt


def get_code_name_values(file_csv):
    with open(file_csv, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|', quotechar='|')
        next(csvreader)

        for row in csvreader:
            value_notrat = list()
            value_trat = list()
            code_name = dict()
            year_value = dict()
            years = range(2004, 2019)
            code = row[0]
            name = row[1]
            values = row[2:]
            code_name[code] = name

            for value in values:
                value = value.replace('.', '').replace(',', '.')
                value_notrat.append(float(value))
                value_trat.append(float(value)/1000000000)

            for i in range(len(value_notrat)):
                year_value[years[i]] = value_notrat[i]

            show_min_max(year_value, code_name[code])
            single_plot(years, value_trat, code_name[code], code)
            print('++++'*10)


def single_plot(years, values, name, code):
    plt.grid(True, linestyle="--")
    plt.plot(years, values, label=name)
    plt.title('Gastos Destinados pelo Governo Federal (2004-2018)\n')
    plt.xlabel('Anos')
    plt.ylabel('Em Bilhões (R$)')
    legend = plt.legend()
    plt.savefig('imgs/sinplot-{}.png'.format(code))
    plt.show()


def to_money(value):
    value = format(value, '5,.2f').replace('.', '-').replace(',', '.') \
            .replace('-', ',')
    return value


def show_min_max(year_value, name):
    values = year_value.values()
    values_nozero = dict()

    print('Órgão Superior: {}'.format(name))

    for key in year_value:
        if year_value[key] != 0.0:
            values_nozero[key] = year_value[key]

    for index, value in enumerate(values_nozero):
        if index == 0:
            print('Ano inicial: {}'.format(value))

    to_min_max = values_nozero.values()
    low = min(to_min_max)
    high = max(to_min_max)

    for key in values_nozero:
        if (values_nozero[key] == low):
            print('Gasto Mínimo: R$ {} em {}'.format(to_money(low), key))

        elif (values_nozero[key] == high):
            print('Gasto Máximo: R$ {} em {}'.format(to_money(high), key))

        else:
            pass


def main():
    get_code_name_values('result.csv')


if __name__ == '__main__':
    main()
