# %%
import pandas as pd
import requests


# %%

api_url = 'https://rickandmortyapi.com/api/character/'

# %%
characters = []

# Hacer la petición a la API para obtener los personajes y guardarlos en la lista
page = 1
while True:
    response = requests.get(f'{api_url}?page={page}')
    data = response.json()
    characters.extend(data['results'])
    
    # Verificar si hay más páginas
    if data['info']['next'] is None:
        break
    page += 1

# %%
# Convertir la lista de personajes en un DataFrame de pandas
df_characters = pd.DataFrame(characters)

# %%
# filtra los personajes que son humanos
df_humans = df_characters[df_characters['species'] == 'Human']
# quiero mostrar solo nombre , genero
humanos = df_humans[['name','gender']]

# %%
# mostrar genero y cantidad de personajes
humanos.groupby('gender').size()


# %%
# si el genero es unknown-======== limpiar la data y poner Desconocido
humanos_clean = humanos.replace('unknown','Desconocido')



# %%
humans_group_by_gender =humanos_clean.groupby('gender').size()
humans_group_by_gender = humans_group_by_gender.reset_index(name='count')

humans_group_by_gender.columns = ['Genero','Cantidad']


# %%
print(humans_group_by_gender)



# %%



