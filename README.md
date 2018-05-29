## Gastos Diretos do Governo Federal 

Script de raspagem de dados dos gastos diretos do Governo Federal com órgão superiores

Raspagem de dados feita em Python com dados exportados para arquivo em formato CSV


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
	$ python graficos.py
```

### Resultados

Para cada um dos 24 Órgãos Superiores existentes em 2018 foi gerado um gráfico

Visualize os gráficos aqui: <a href="https://github.com/edsonlead/gastos-gov-federal/tree/master/imgs">imgs/*</a>

#### Visite

http://edsonlead.com
