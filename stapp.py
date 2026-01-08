import streamlit as st
import requests
import pandas as pd
from io import StringIO
from io import BytesIO
import base64


# personal access token
token = "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"
headers = {'Authorization': f'token {token}'}

# Function to fetch image from GitHub
def fetch_image_from_github(url, tokenn):
    headers = {'Authorization': f'token {tokenn}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return BytesIO(response.content)

# Function to read CSV files from a private GitHub repository
def read_github_csv(url, token, cols=None):
    headers = {'Authorization': f'token {token}'}
    response = requests.get(url, headers=headers)
    
    # Debug: print response status code and content for troubleshooting
    # st.write(f"Response status code: {response.status_code}")

    if response.status_code == 200:
        try:
            # Attempt to parse the response as JSON
            file_content = response.json()
            if 'content' in file_content and file_content['encoding'] == 'base64':
                file_decoded = base64.b64decode(file_content['content']).decode('utf-8')
                df = pd.read_csv(StringIO(file_decoded), usecols=cols)
                return df
            else:
                st.error("Error decoding the file content from GitHub.")
                return None
        except ValueError:
            # If JSON parsing fails, assume the content is raw CSV
            # st.write("Response content is not JSON, attempting to read as raw CSV.")
            file_decoded = response.content.decode('utf-8')
            df = pd.read_csv(StringIO(file_decoded), usecols=cols)
            return df
    else:
        st.error(f"Error fetching the file from GitHub. Status code: {response.status_code}")
        return None

old_naftal_distance_from_last_point = {'Oued romane': 3.7826,
    'Lot michel': 9.2127,
    'Blida': 42.1884,
    'Larbaa': 18.3339,
    'Salembier': 15.9907,
    'Soumaa': 18.7811,
    'Mahelma': 3.7468000000000004,
    'Ouled chebel': 16.8165,
    'Cherchell': 21.293,
    'Oued smar': 23.031299999999998,
    'Hraoua': 48.8799,
    'Baba hassen': 2.322,
    'Ain naadja': 14.7274,
    'Mauritania': 11.1606,
    'Douera': 8.2083,
    'Fouka': 14.299100000000001,
    'Ain beniane 1': 4.7551000000000005,
    'Ain beniane 2': 1.3439,
    'Bouinane': 36.7425,
    'Sidi abdellah': 14.1105,
    'Zeralda': 5.2835,
    'Khmiss el khechna ': 22.7907,
    'Bouzereah 1': 6.143,
    'Bouzereah 2': 13.0624,
    'Boumerdes': 43.5339,
    'Alger centre': 7.831300000000001,
    'Shaoula': 11.4395,
    'Tamenfoust': 38.9041,
    'Ruisseau': 11.9824,
    'H-dey': 15.4296,
    'Bachdjerah': 17.6958,
    'El hamiz': 29.3209,
    'Bab el oued': 8.8619,
    'Ain malha': 15.3396,
    'Souidania': 4.2082,
    'Alger plage': 28.0263}

    
def data_res():
    # title
    st.title('Récolte de données')
    # get naftal image from github
    image_url = 'https://github.com/SWS-ZERBOUT/data-str-app/blob/main/images/naftal.png?raw=true'
    image_data = fetch_image_from_github(image_url, token)
    column1, column2, column3= st.columns(3)
    with column1:
        st.write(' ')
    with column2:
        st.image(image_data)
    with column3:
        st.write(' ')
     # get routimize image from github
    image_url = 'https://github.com/SWS-ZERBOUT/data-str-app/blob/main/images/routimize.png?raw=true'
    image_data = fetch_image_from_github(image_url, token)
    column1, column2, column3= st.columns(3)
    with column1:
        st.write(' ')
    with column2:
        st.image(image_data)
    with column3:
        st.write(' ')
    st.markdown('\n')
    # context
    st.markdown('### Contexte')
    st.markdown("""
    Dans le cadre de la première phase du projet relatif à **l’optimisation logistique et financière du plan de transport du personnel** de l’entreprise **Naftal**, l’équipe de **Routimize** a entrepris un travail de récolte de données sur la mise en œuvre du plan de transport actuel.
        
    Cette récolte réalisée du **8 juillet 2024** au **18 juillet 2024** a porté sur l’étude des lignes, des points de ramassage et des bus. L’ensemble des **36** lignes a été couvert par des questionnaires administrés aux chauffeurs pour déterminer la position GPS exacte de chaque point de ramassage et estimer le nombre de passagers à chaque arrêt. De plus, l'équipe a testé **5** de ces lignes pour s'assurer davantage de la qualité des données récoltées.
    """)
    st.markdown('\n')
    
    st.markdown('### Lignes')
    # URL of the CSV file
    # urldf = "https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees-data/main/data/Donn%C3%A9es%20collect%C3%A9es%20-%20Liste%20compl%C3%A9te.csv?token=GHSAT0AAAAAACNFGRWUM4Q7PQQ5V3UBCC7OZVCWZEA" 
    # # Read the CSV file into a DataFrame
    # df = read_github_csv(urldf, token,  cols = range(1, 13))
    # df = df.dropna(axis=1, how='all')
    # # Set the first row as the column headers
    # df.columns = df.iloc[0]
    # df = df[1:]
    # # # Reset the index
    # df.reset_index(drop=True, inplace=True)
    # df['n min'] = df['n min'].astype(int)
    # df['n max'] = df['n max'].astype(int)
    # # Function to convert the string of coordinates into a tuple of floats
    # def convert_to_tuple(coord_str):
    #     # print(coord_str, type(coord_str))
    #     new =  str(coord_str).split(',')
    #     # if len(new) != 4: print(f"c{coord_str}, n{new}")
    #     # print([float(new[0]+"." + new[1]), float(new[2] + "."+new[3])])
    #     new = [float(new[0]+"." + new[1]), float(new[2] + "."+new[3])]
    #     return new
    # df["Localisation Coordonnées GPS"] = df["Localisation Coordonnées GPS"].apply(convert_to_tuple)
    # # Split the values in the "Population" column by a comma and convert them into lists
    # df['Population'] = df['Population'].apply(lambda x: [item.strip() for item in x.split(',')] if pd.notna(x) else [])
    urldf = "https://github.com/SWS-ZERBOUT/data-str-app/blob/main/naftal-recolte-donnees-data-main/data/old_df.csv"
    # Read the CSV file into a DataFrame
    df = read_github_csv(urldf, token,  cols = range(1, 10))
    df['Population'] = df['Population'].apply(lambda x: [item.strip() for item in x.split(',')] if pd.notna(x) else [])
    # df["Localisation Coordonnées GPS"] = df["Localisation Coordonnées GPS"].apply(lambda x: [item.strip() for item in x.split(',')])
    df["Localisation Coordonnées GPS"] = df["Localisation Coordonnées GPS"].apply(lambda x: [float(coord) for coord in x.strip("[]").split(',')])
    df.drop("temps de départ", axis=1, inplace=True)
    # display df
    # choose ligne to display
    ligne_options = list(set(df["Ligne"]))
    ligne_options.append("Toutes les lignes")
    ligne_to_display = st.selectbox('Choisissez une ligne à afficher', ligne_options, index=ligne_options.index("Toutes les lignes"))
    if ligne_to_display == "Toutes les lignes":
        st.dataframe(df)
        dist_total = df["Distance(km)"].sum()
        dist_total += sum([old_naftal_distance_from_last_point[ligne] for ligne in old_naftal_distance_from_last_point.keys()])
        st.markdown(f"Distance totale: {round(dist_total,2)} km") 
        st.markdown('\n')
        st.markdown(f"Distance moyenne par ligne: {round(dist_total/36,2)} km")
    else: 
        st.dataframe(df[df["Ligne"] == ligne_to_display])
        dist_total = df[df["Ligne"] == ligne_to_display]["Distance(km)"].sum()
        dist_total += old_naftal_distance_from_last_point[ligne_to_display]
        st.markdown(f"Distance totale: {round(dist_total,2)} km")   
    st.markdown('\n')
    
    # Population
    st.markdown('### Population')
    # Sum the 'n min' and 'n max' columns
    n_min_sum = df['n min'].astype(float).sum()
    n_max_sum = df['n max'].astype(float).sum()
    st.markdown(f"Le nombre total de personnes utilisant actuellement le service de transport est entre **{int(n_min_sum)}** et **{int(n_max_sum)}**. Contrairement aux données reçues où le nombre total de la population était entre **{619}** et **{759}**.")
    st.markdown("La population peut être divisée en plusieurs catégories, D'après nos échanges avec les chauffeurs, nous avons identifié les catégories suivantes:")
    population = {
        "G": ["Gendarme", 0],
        "S": ["Stagiaire", 0],
        "M": ["Personnel de ménage", 0],
        "P": ["Personnel du ministere de l'industrie pharmaceutique", 0],
        "E": ["Enfants de creche", 0],
        "V": ["Personnel véhiculé", 0],
        "B": ["Personnel de la banque", 0],
        "C": ["Personnel de la cantine", 0], 
        "A": ["Apprenti", 0],
        "N": ["Missionnaire", 0]
    }   
    popdict = { "Code": [code for code in population.keys()],
            "Description": [value[0] for value in population.values()]}
    popdf = pd.DataFrame(popdict).T
    popdf.columns = popdf.iloc[0]
    popdf = popdf[1:]
    st.dataframe(popdf)
    pop_number = st.selectbox('Choisissez le nombre totale de la population à considerer', [n_min_sum, n_max_sum], index=1)
    st.markdown("Voici la visualisation de la distribution des catégories de la population selon le nombre total choisi:")
    # Population info dictionary with type and count
    # for every population row, count the number of subpopulations
    for i in list(df["Population"]):
        # as long as not empty
        if i != [] and i != ['']:
            # for every subpopulation
            for j in i:
                # according to the population code add the number of subpopulation
                population[j[0]][1] += int(j[1:])
    # add subpopulation ratio
    for key in population.keys():
        population[key].append(population[key][1] / pop_number)
    # add Naftal personnel population
    population["Naftal"] = ["Personnel de Naftal",
                            pop_number - sum(population[key][1] for key in population.keys()),
                            1 - sum(population[key][2] for key in population.keys())]
    # pie chart
    if pop_number == n_max_sum:
        image_url = 'https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/charts/pie%20chart%20max.png'
        image_data = fetch_image_from_github(image_url, token)
    else:
        image_url = 'https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/charts/pie%20chart%20min.png'
        image_data = fetch_image_from_github(image_url, token)
    st.image(image_data)
    # bar chart
    image_url = 'https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/charts/bar%20chart.png'
    image_data = fetch_image_from_github(image_url, token)
    st.image(image_data)
    st.markdown("\n")

    # Bus
    st.markdown('### Bus')
    st.markdown("La flotte actuelle est représentée par le tableau suivant:")
    # URL of the CSV file
    urlbus = "https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/data/Donn%C3%A9es%20collect%C3%A9es%20-%20Types%20de%20v%C3%A9hicules.csv"
    # Read the CSV file into a DataFrame
    dfbus = read_github_csv(urlbus, token,  cols=range(1, 5))
    # Set the first row as the column headers
    dfbus.columns = dfbus.iloc[0]
    dfbus = dfbus[1:9]
    st.dataframe(dfbus)
    st.markdown('\n')

    # Taux de saturation
    st.markdown('### Taux de saturation')   
    st.markdown("Le taux de saturation de la capacité du bus pour chaque ligne peut être représenté par le tableau suivant:")
    # 1. Aggregate data: Sum of n min and n max for each Ligne
    df_sum = df.groupby('Ligne').agg({'n min': 'sum', 'n max': 'sum'}).reset_index()
    df_sum.columns = ['Ligne', 'Sum n min', 'Sum n max']
    # 2. Match bus data and calculate bus capacity and occupancy rate
    result = []
    for i, row in df_sum.iterrows():
        ligne = row['Ligne']
        sum_n_min = row['Sum n min']
        sum_n_max = row['Sum n max']
        if ligne == "Khmiss el khechna ":
            ligne = "Khmiss el khechna"
        bus_info = dfbus[dfbus['Lignes'].apply(lambda x: ligne in x)]
        for _, bus in bus_info.iterrows():
            model = bus['Modèle']
            capacity = int(bus['Capacité'])
            bus_count = bus['Nombre']
            occupancy_rate_min = sum_n_min / capacity if capacity > 0 else 0
            occupancy_rate_max = sum_n_max / capacity if capacity > 0 else 0
            
            result.append({
                'Ligne': ligne,
                'Sum n min': sum_n_min,
                'Sum n max': sum_n_max,
                'Bus Used': model,
                'Bus Capacity': capacity,
                'Occupancy Rate Min': occupancy_rate_min,
                'Occupancy Rate Max': occupancy_rate_max
            })
    df_result = pd.DataFrame(result)
    df_result["Occupancy Rate Max"] = df_result["Occupancy Rate Max"] * 100
    df_result["Occupancy Rate Min"] = df_result["Occupancy Rate Min"] * 100
    # Rename the columns
    df_result.rename(columns={
        'Ligne': 'Ligne',
        'Sum n min': 'Somme min',
        'Sum n max': 'Somme max',
        'Bus Used': 'Bus',
        'Bus Capacity': 'Capacité bus',
        'Occupancy Rate Min': 'Taux Min %',
        'Occupancy Rate Max': 'Taux Max %'
    }, inplace=True)
    df_sorted = df_result.sort_values(by='Taux Max %', ascending=True)
    st.dataframe(df_sorted)
    st.markdown("\n")
    st.markdown(f"Le taux de saturation moyen (avec n max) {round(df_sorted['Taux Max %'].mean(), 2)}%")
    st.markdown("\n")
    st.markdown(f"Le taux de saturation moyen (avec n min) {round(df_sorted['Taux Min %'].mean(), 2)}%")
    st.markdown("\n")
    st.markdown("On peut aussi visualiser la variation du taux de saturation avec le diagramme suivant:")
    image_url = 'https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/charts/taux%20de%20saturation.png'
    image_data = fetch_image_from_github(image_url, token)
    st.image(image_data)
    st.markdown("La couleur rouge indique le taux de saturation basé sur une population totale de **896**, tandis que la couleur bleue représente le taux de saturation pour une population de **801**.")
 
    st.markdown("\n")
    st.markdown("Les taux de saturation dépassant **100%** sont attribuables à une surestimation du nombre de passagers par les chauffeurs. De plus, certaines anomalies, telles que les passagers utilisant plusieurs points de ramassage en raison de préférences personnelles (comme une ligne habituelle versus une ligne pour le week-end ou un changement de point de ramassage en cas de retard le matin), contribuent également à cette surestimation. Pour obtenir des données fiables, il est nécessaire d'utiliser un logiciel capable de gérer l'ensemble du processus, offrant ainsi une visibilité complète et un contrôle sur toutes les données de transport.")

def maps():
    st.title('Anciennes Lignes')
    # Loading old routes data
    # urlmaps = 'https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees-data/main/old%20maps/alldatamodified%20-%20Sheet1.csv?token=GHSAT0AAAAAACNFGRWUTQVSQK6OEGTYPVYGZVCW7HA'
    # df = read_github_csv(urlmaps, token, cols= range(0,4))
    urldf = "https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/data/old_df.csv"
    # Read the CSV file into a DataFrame
    df = read_github_csv(urldf, token,  cols = range(1, 10))
    df['Population'] = df['Population'].apply(lambda x: [item.strip() for item in x.split(',')] if pd.notna(x) else [])
    # df["Localisation Coordonnées GPS"] = df["Localisation Coordonnées GPS"].apply(lambda x: [item.strip() for item in x.split(',')])
    df["Localisation Coordonnées GPS"] = df["Localisation Coordonnées GPS"].apply(lambda x: [float(coord) for coord in x.strip("[]").split(',')])
    df.drop("temps de départ", axis=1, inplace=True)
    # getting the name of the lines
    old_lines = df['Ligne'].unique()

    # separating the data by line
    old_routes = {elem : pd.DataFrame for elem in old_lines}

    for key in old_routes.keys():
        old_routes[key] = df[:][df['Ligne'] == key]
        old_routes[key].drop(['Ligne'], axis=1, inplace=True)

    # Loading each line map
    old_maps = {'Oued romane' :"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Oued%20romane.html"
                , 'Lot michel' :"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Lot%20michel.html"
                , 'Blida' :"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Blida.html"
                , 'Larbaa':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Larbaa.html"
                , 'Salembier':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Salembier.html"
                ,'Soumaa':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Soumaa.html"
                , 'Mahelma':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Mahelma.html"
                , 'Ouled chebel':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Ouled%20chebel.html"
                , 'Cherchell':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Cherchell.html"
                , 'Oued smar':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Oued%20smar.html"
                ,'Hraoua':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Hraoua.html"
                , 'Baba hassen':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Baba%20hassen.html"
                , 'Ain naadja':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Ain%20naadja.html"
                , 'Mauritania':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Mauritania.html"
                , 'Douera':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Douera.html"
                ,'Fouka':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Fouka.html"
                , 'Ain beniane 1':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Ain%20beniane%201.html"
                , 'Ain beniane 2':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Ain%20beniane%202.html"
                , 'Bouinane':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Bouinane.html"
                ,'Sidi abdellah':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Sidi%20abdellah.html"
                , 'Zeralda':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Zeralda.html"
                , 'Khmiss el khechna ':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Khmiss%20el%20khechna%20.html"
                , 'Bouzereah 1':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Bouzereah%201.html"
                ,'Bouzereah 2':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Bouzereah%202.html"
                , 'Boumerdes':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Boumerdes.html"
                , 'Alger centre':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Alger%20centre.html"
                , 'Shaoula':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Shaoula.html"
                ,'Tamenfoust':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Tamenfoust.html"
                , 'Ruisseau':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Ruisseau.html"
                , 'H-dey':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/H-dey.html"
                , 'Bachdjerah':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Bachdjerah.html"
                , 'El hamiz':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/El%20hamiz.html"
                ,'Bab el oued':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Bab%20el%20oued.html"
                , 'Ain malha':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Ain%20malha.html"
                , 'Souidania':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Souidania.html"
                , 'Alger plage':"https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/old%20maps/Alger%20plage.html"
                , "Anciens et nouveaux points de ramassage": "https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/oldvsnew.html"
    }


    old_lines = list(old_lines)
    old_lines .insert(len(old_lines),"Anciens et nouveaux points de ramassage")
    # Select box to choose a route
    selected_old_line = st.selectbox('Choisissez une carte à visualiser', old_lines)

    if selected_old_line:
        # Display the corresponding map
        # Fetch the content from the URL
        response = requests.get(old_maps[selected_old_line], headers=headers)
        response.raise_for_status()  # Ensure we notice bad responses
        html_content = response.text
        # Use Streamlit's components.html to display the HTML
        st.components.v1.html(html_content, height = 400, width = 800)
        st.markdown('\n')
        if selected_old_line != "Anciens et nouveaux points de ramassage":
            # Display the corresponding DataFrame
            st.dataframe(df[df["Ligne"] == selected_old_line])
            dist_total = df[df["Ligne"] == selected_old_line]["Distance(km)"].sum()
            dist_total += old_naftal_distance_from_last_point[selected_old_line]
            st.markdown(f"Distance totale: {round(dist_total,2)} km")
        else:
            st.markdown('les points en vert sont les nouveaux points de ramassage récoltés et les points en rouge sont les anciens points de ramassage reçus')

def requested_maps():
    st.title('Nouvelles Lignes')
    st.markdown("Les nouvelles lignes demandées par le responsable du transport")
    urldf = "https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/data/requested_lines_info.csv"
    infodf = read_github_csv(urldf, token,  cols = range(0, 3))
    infodf.rename(columns={"Unnamed: 0": "Line"}, inplace=True)
    # st.dataframe(infodf)
    urldf = "https://raw.githubusercontent.com/SWS-ZERBOUT/data-str-app/refs/heads/main/naftal-recolte-donnees-data-main/data/requested_lines.csv"
    df = read_github_csv(urldf, token,  cols = range(0, 5))
    df["Localisation Coordonnées GPS"] = df["Localisation Coordonnées GPS"].apply(lambda x: [float(coord) for coord in x.strip("[]").split(',')])
    lines = df['Ligne'].unique()
    # separating the data by line
    routes = {elem : pd.DataFrame for elem in lines}
    for key in routes.keys():
        routes[key] = df[:][df['Ligne'] == key]
        routes[key].drop(['Ligne'], axis=1, inplace=True)
    # Loading each line map
    maps = {'Oued romane' :"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees-data/main/old%20maps/Oued%20romane.html?token=GHSAT0AAAAAACNFGRWVG6NO3JICS44BTY72ZVCOPFA"
                , 'Lot michel' :"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees-data/main/old%20maps/Lot%20michel.html?token=GHSAT0AAAAAACNFGRWVCY5QFCFFSGUM55HCZVCOPXA"
                , 'Blida' :"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees-data/main/old%20maps/Blida.html?token=GHSAT0AAAAAACNFGRWUWIMYFUCPD2AWV3HSZVCOQFA"
                , 'Larbaa':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees-data/main/old%20maps/Larbaa.html?token=GHSAT0AAAAAACNFGRWUFHMBAHGKGUKFS2BIZVCOQYQ"
                ,'Soumaa':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Soumaa.html?token=GHSAT0AAAAAACVE2G5MVCBZWCU7T7Z7ZBTIZVCGLMQ"
                , 'Mahelma':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Mahelma.html?token=GHSAT0AAAAAACVE2G5NP5VTRIGQ2LDZIF5UZVCGMUA"
                , 'Ouled chebel':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Ouled%20chebel.html?token=GHSAT0AAAAAACVE2G5MNQLUAN7CHVZSHC3WZVCGLZA"
                , 'Cherchell':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Cherchell.html?token=GHSAT0AAAAAACVE2G5MYUBSXFVD7NNIO5V2ZVCGFJA"
                ,'Hraoua':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Hraoua.html?token=GHSAT0AAAAAACVE2G5MUR3XCNNSYNVHXD2IZVCGIQA"
                , 'Baba hassen':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Baba%20hassen.html?token=GHSAT0AAAAAACVE2G5NT5JIM2FRDZWZJY3UZVCGCRA"
                , 'Ain naadja':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Ain%20naadja.html?token=GHSAT0AAAAAACVE2G5NHYLPRN7DKG5BOULUZVCGA4Q"
                , 'Douera':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Douera.html?token=GHSAT0AAAAAACVE2G5MIY7BZBRLSHYPWFAIZVCGFXA"
                ,'Fouka':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Fouka.html?token=GHSAT0AAAAAACVE2G5M2AVGXJ4L4J5EDU3SZVCGHJQ"
                , 'Ain beniane 1':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Ain%20beniane%201.html?token=GHSAT0AAAAAACVE2G5NGMNVLOAIJC2K2WZEZVCF7IQ"
                , 'Ain beniane 2':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Ain%20beniane%202.html?token=GHSAT0AAAAAACVE2G5MBRGU6VAFKJHH46FMZVCGAFA"
                , 'Bouinane':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Bouinane.html?token=GHSAT0AAAAAACVE2G5NBITJR7XFFF5AK4HIZVCGDZQ"
                ,'Sidi abdellah':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Sidi%20abdellah.html?token=GHSAT0AAAAAACVE2G5NCMPPDGXQZY56VKPCZVCGJZA"
                , 'Zeralda':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Zeralda.html?token=GHSAT0AAAAAACVE2G5NPJKIFEFV3SXZSUOEZVCGKJA"
                , 'Khmiss el khechna ':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Khmiss%20el%20khechna%20.html?token=GHSAT0AAAAAACVE2G5NGIU2U4AZYQFJYUMKZVCGKTQ"
                , 'Bouzereah 1':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Bouzereah%201.html?token=GHSAT0AAAAAACVE2G5NI53WR2U3UTHWIYBUZVCGERA"
                ,'Bouzereah 2':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Bouzereah%202.html?token=GHSAT0AAAAAACVE2G5MCYETMRRUSTKGV6JMZVCGE4Q"
                , 'Boumerdes':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Boumerdes.html?token=GHSAT0AAAAAACVE2G5NEP4GCO6HJUDFLBTYZVCGEEQ"
                , 'Alger centre':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees-data/refs/heads/main/requested%20maps/Alger%20centre.html?token=GHSAT0AAAAAAC25IUTP7PSQ5EYI2HURDKVAZ2CMOLA"
                , 'Shaoula':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Shaoula.html?token=GHSAT0AAAAAACVE2G5NKYDWDSFML7FSGBUWZVCGNCA"
                ,'Tamenfoust':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees-data/refs/heads/main/requested%20maps/Tamenfoust.html?token=GHSAT0AAAAAAC25IUTOWT4AJ6HBU35IYXJEZ2CMQJQ"
                , 'Ruisseau':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Ruisseau.html?token=GHSAT0AAAAAACVE2G5MVXBNL4LR5AA3UMLWZVCGOSA"
                , 'H-dey':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/H-dey.html?token=GHSAT0AAAAAACVE2G5NZMQH6EJPAE5IYPSCZVCGO3Q"
                , 'Bachdjerah':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Bachdjerah.html?token=GHSAT0AAAAAACVE2G5MG3PSCYU6HWZGWPIQZVCGC5Q"
                , 'El hamiz':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees-data/refs/heads/main/requested%20maps/El%20hamiz.html?token=GHSAT0AAAAAAC25IUTOISW2GR7SQUGCRMJKZ2CMPYA"
                ,'Bab el oued':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees-data/refs/heads/main/requested%20maps/Bab%20el%20oued.html?token=GHSAT0AAAAAAC25IUTPSW5NJFPZXBVVQJ62Z2CMPDQ"
                , 'Ain malha':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Ain%20malha.html?token=GHSAT0AAAAAACVE2G5NYXVYJGO4AWQAWVQAZVCGASA"
                , 'Souidania':"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees/main/old%20maps/Souidania.html?token=GHSAT0AAAAAACVE2G5NBYDN3O6FUW675AKQZVCGGXA"
                ,"Plan complet":"https://raw.githubusercontent.com/malikbf5/naftal-recolte-donnees-data/refs/heads/main/requested%20maps/full%20map.html?token=GHSAT0AAAAAAC25IUTOLJZI3MMF4IMGUKO4Z2CMQZA"
    }

    lines = list(lines)
    # insert
    lines.insert(len(lines),"Plan complet")
    # Select box to choose a route
    selected_old_line = st.selectbox('Choisissez une carte à visualiser', lines)

    if selected_old_line:
        # Display the corresponding map
        # Fetch the content from the URL
        response = requests.get(maps[selected_old_line], headers=headers)
        response.raise_for_status()  # Ensure we notice bad responses
        html_content = response.text
        # Use Streamlit's components.html to display the HTML
        st.components.v1.html(html_content, height = 400, width = 800)
        st.markdown('\n')
        if selected_old_line != "Plan complet":
            # Display the corresponding DataFrame
            st.dataframe(df[df["Ligne"] == selected_old_line])
            dist = float(infodf[infodf['Line'] == selected_old_line]['total_distance'])
            dur = float(infodf[infodf['Line'] == selected_old_line]['total_duration'])
            st.markdown(f"Distance totale: {round(dist,2)} km")
            st.markdown(f"Durée totale: {round(dur,2)} min")
            st.markdown(f"Nombre de places: {df[df['Ligne'] == selected_old_line]['n max'].sum()}")            
        else:
            st.dataframe(df)
            dist = float(infodf[infodf['Line'] == 'total_distance']['total_distance'])
            dur = float(infodf[infodf['Line'] == 'total_duration']['total_duration'])
            st.markdown(f"Distance totale: {round(dist,2)} km")
            st.markdown(f"Distance totale: {round(dur,2)} min")



page_names_to_funcs = {
    "Récolte de données": data_res,
    "Visualisation des anciennes lignes": maps,
    "Visualisation des lignes demandées": requested_maps
}
demo_name = st.sidebar.selectbox(" ", page_names_to_funcs.keys())
page_names_to_funcs[demo_name]()
