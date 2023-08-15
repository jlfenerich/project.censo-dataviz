# Análise do Censo Brasileiro 
### Fonte: IBGE

> 🚧 **Este repositório está em construção.**

## Objetivo

O principal propósito deste repositório é buscar e analisar informações do Censo Brasileiro por meio da API do SIDRA. Até o momento, os dados dos censos desde 1991 foram coletados e processados.

## ETL (Extração, Transformação e Carga)

O processo de ETL é realizado em duas etapas principais:

1. **Extração:** Esta etapa é executada usando os notebooks:
   - `GetData_Sidra_1991_2000_2010.ipynb`
   - `GetData_SIDRA_2022.ipynb`
   
   Os notebooks são responsáveis por fazer requisições à API do sistema SIDRA (IBGE) para coletar os dados do censo.

2. **Transformação:** Após a extração, os dados são selecionados e transformados para um formato mais adequado. O objetivo é organizar os dados em uma tabela contendo as colunas *year*, *population*, *city* e *state*.

3. **Carga:** Os dados transformados são então salvos em um arquivo CSV para análises posteriores.
