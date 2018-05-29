import csv
import matplotlib.pyplot as plt

billion = 1000000000
years = range(2004,2019)

def capture_code_name_values(file_csv):

    with open(file_csv, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter='|', quotechar='|')
        next(csvreader)
        for row in csvreader:
            value_trat = list()
            codes = list()
            names = list()
            
            code = row[0]
            name = row[1]
            values = row[2:]
            
            codes.append(int(code))
            names.append(name)
            
            for value in values:
                value = value.replace('.','').replace(',','.')
                value_trat.append(float(value)/billion)
            
            sinplot(value_trat, code, name)
            #multplot(value_trat, code, name)

def plot(value_trat, code, name):
    plt.grid(True, linestyle="--")
    plt.plot(years, value_trat, label=name)
    plt.title('Gastos Destinados pelo Governo Federal (2004-2018)\n')
    plt.xlabel('Anos')
    plt.ylabel('Em Bilhões (R$)')


def sinplot(value_trat, code, name):
    plot(value_trat, code, name)
    legend = plt.legend()
    plt.savefig('imgs/sinplot-{}.png'.format(code))
    plt.show()
        
def multplot(value_trat, code, name):
    plot(value_trat, code, name)
    #legend = plt.legend()
    plt.savefig('imgs/multplot.png')

def main():
    capture_code_name_values('result.csv')


if __name__ == '__main__':
    main()
