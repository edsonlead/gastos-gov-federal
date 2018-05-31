## Gastos Diretos do Governo Federal 

Script de raspagem de dados dos gastos diretos do Governo Federal com órgão superiores

Raspagem de dados feita em Python com dados exportados para arquivo em formato CSV

A análise dos dados raspados permite a plotagem de gráficos, o valor máximo e mínimo gasto com cada órgão superior e os respectivos anos desses valores


### Fonte de Dados

Portal da Transparência: http://www.portaltransparencia.gov.br


### Estrutura do Arquivo CSV

* Código do órgão superior
* Nome do órgão superior
* Gastos de 2004 até 2018

Visualize o arquivo aqui: <a href="https://github.com/edsonlead/gastos-gov-federal/blob/master/result.csv">result.csv</a>


### Executando o Script

Para raspar os dados do Portal da Transparência e exportá-los para um CSV:

```
	$ python gastos-gov-federal.py
```

Para gerar os gráficos e algumas análises a partir do arquivo CSV:

```
	$ python analise.py
    
	ou
    
	$ python analise.py > analise.out
```


### Resultados

Para cada um dos 24 Órgãos Superiores existentes em 2018 foi gerado um gráfico

Adicionalmente, é gerado um gráfico com todos os dados

Visualize os gráficos aqui: <a href="https://github.com/edsonlead/gastos-gov-federal/tree/master/imgs">imgs/*</a>


Faz parte da análise, além dos gráficos, os valores de gastos mínimo e máximo de cada órgão superior

Cada órgão superior possui o seu 'Ano Inicial' que se trata do ano do primeiro gasto como registrado no Portal da Transparência

Visualize o arquivo de saída da análise aqui: <a href="https://github.com/edsonlead/gastos-gov-federal/blob/master/analise.out">analise.out</a>


#### Visite

http://edsonlead.com