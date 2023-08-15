# Análise do Censo Brasileiro | Fonte: IBGE

> ## 'Este repositório está em construção.'



O objetivo desse repósitório é buscar as informações do Censo via API do SIDRA, até o momento consegui os dados dos Censos desde 1991.

## ETL

A extração dos é realizada com notebooks __GetData_Sidra_1991_2000_2010.ipynb__ e __GetData_SIDRA_2022.ipynb__ que requisitam via API do sistema SIDRA (IBGE) os dados, a segunda etapa é a seleção dos dados relevantes e posterimente a transformação para o formato em que os dados sejam dispostos em uma tabela com *year*, *population*, *city*, *state*; e, os salvam num arquivo csv.

