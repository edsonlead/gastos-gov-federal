#!/usr/bin/env python3
import csv
import matplotlib.pyplot as plt


def capture_code_name_values(file_csv):

    with open(file_csv, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|', quotechar='|')
        next(csvreader)
        for row in csvreader:
            value_notrat = list()
            value_trat = list()

            d = dict()
            d_yv = dict()

            years = range(2004, 2019)

            code = row[0]
            name = row[1]
            values = row[2:]

            d[code] = name

            for value in values:
                value = value.replace('.', '').replace(',', '.')
                value_notrat.append(float(value))
                value_trat.append(float(value)/1000000000)

            for i in range(len(value_notrat)):
                d_yv[years[i]] = value_notrat[i]

            min_max(d_yv, d[code])
#            sinplot(value_trat, code, d[code], years)
            multplot(value_trat, code, d[code], years)
            print('++++'*10)


def plot(value_trat, code, name, years):

    plt.grid(True, linestyle="--")
    plt.plot(years, value_trat, label=name)
    plt.title('Gastos Destinados pelo Governo Federal (2004-2018)\n')
    plt.xlabel('Anos')
    plt.ylabel('Em Bilhões (R$)')


def sinplot(value_trat, code, name, years):

    plot(value_trat, code, name, years)
    legend = plt.legend()
    plt.savefig('imgs/sinplot-{}.png'.format(code))
    plt.show()


def multplot(value_trat, code, name, years):
    #   esse 'code' do def plot não é utilizado aqui... rs
    plot(value_trat, code, name, years)
#   legend = plt.legend(bbox_to_anchor=(1.05, 1), loc=6, borderaxespad=0.)
    plt.savefig('imgs/multplot.png')


def toreal(value):

    value = format(value, '5,.2f').replace('.', '-').replace(',', '.') \
            .replace('-', ',')
    return value


def min_max(d_yv, name):

    d_v = d_yv.values()

    new = dict()

    print('Órgão Superior: {}'.format(name))
    for key in d_yv:
        if d_yv[key] != 0.0:
            new[key] = d_yv[key]

    for index, value in enumerate(new):
        if index == 0:
            print('Ano inicial: {}'.format(value))

    nw = new.values()
    low = min(nw)
    high = max(nw)

    for key in new:
        if (new[key] == low):
            money = toreal(low)
            print('Gasto Mínimo: R$ {} em {}'.format(money, key))

        elif (new[key] == high):
            money = toreal(high)
            print('Gasto Máximo: R$ {} em {}'.format(money, key))

        else:
            pass


def main():

    capture_code_name_values('result.csv')


if __name__ == '__main__':

    main()
