import requests
import pandas as pd
import matplotlib.pyplot as plt

# Fetch data from the API
url = 'https://servicodados.ibge.gov.br/api/v3/agregados/4712/periodos/2022/variaveis/382?localidades=N6[N3[11,12,13,14,15,16,17,21,22,23,24,25,26,27,28,29,31,32,33,35,41,42,43,50,51,52,53]]'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    # Flatten data
    flattened_data = []
    for item in data[0]['resultados'][0]['series']:
        id = item['localidade']['id']
        name = item['localidade']['nome']
        population = item['serie']['2022']
        flattened_data.append({'id': id, 'name': name, 'population': population})

    # Create DataFrame
    df = pd.DataFrame(flattened_data)
    df[['city', 'state']] = df['name'].str.split(' - ', expand=True)

    # Convert the population column to integers
    df['population'] = df['population'].astype(int)

    # Drop the 'id' and 'name' columns
    df = df.drop(columns=['id', 'name'])

    # Aggregate the population by state
    state_population = df.groupby('state')['population'].sum()

    # Create a bar chart
    plt.figure(figsize=(10, 8))
    state_population.sort_values().plot(kind='barh', color='skyblue')

    plt.title('Population by State')
    plt.xlabel('Population')
    plt.ylabel('State')

    plt.show()

else:
    print(f"Request failed with status code {response.status_code}")
