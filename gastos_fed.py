#!/usr/bin/env python3
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup as bs

import requests
import numpy as np
import csv
import matplotlib.pyplot as plt

url_values = 'http://www.portaltransparencia.gov.br/PortalComprasDiretasOEOr' \
        'gaoSubordinado.asp?Ano=%i&CodigoOS=%s'
url_code_name = 'http://www.portaltransparencia.gov.br/PortalComprasDiretasO' \
        'EOrgaoSuperior.asp?Ano=2018&Pagina=%i'

years = range(2004, 2019)

file_csv = 'datas.csv'

codes = list()
names = list()


def simple_get(url):
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content

            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200
            and content_type is not None
            and content_type.find('html') > -1)


def log_error(e):
    print(e)


def get_codes_names(url):
    pages = [1, 2]

    for page in pages:
        url_code = url_code_name % (page)
        req = requests.get(url_code)
        html = bs(req.content, 'html.parser')
        tr = html.find_all('tr')
        del tr[:3]

        for i in range(len(tr)):
            td = tr[i].find_all('td')
            code = td[0].text.strip()
            name = td[1].text.strip()
            codes.append(code)
            names.append(name)
    return codes, names


def get_values(code):
    values = list()

    for year in years:
        url_orgao = url_values % (year, code)
        req = requests.get(url_orgao)
        html = bs(req.content, 'html.parser')
        value = html.find_all('td', class_='colunaValor')

        if not value:
            value = '0,0'
            print('Verificar se o Ministério de código {} existia no ano'
                  '{} .'.format(code, year))

        if value is not None:
            value = value[1].text.strip()
            value = (str(value))
        
        values.append(value)
    return values


def save_datas(codes, names, years):
    csvfile = open(file_csv, 'a')
    years = list(map(str, years))
    header = ['Código', 'Órgão']
    header.extend(years)
    datas = csv.writer(csvfile,
                       delimiter='|',
                       quotechar='|',
                       quoting=csv.QUOTE_MINIMAL)
    datas.writerow(header)

    for code in range(len(codes)):
        result_values = get_values(codes[code])
        result_codes_names = [codes[code], names[code]]
        result_codes_names.extend(result_values)
        datas.writerow(result_codes_names)


def main():
    simple_get(url_values)
    simple_get(url_code_name)
    get_codes_names(url_code_name)
    save_datas(codes, names, years)


if __name__ == '__main__':
    main()
