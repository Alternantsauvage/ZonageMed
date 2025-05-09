import streamlit as st
import pandas as pd

st.set_page_config(page_title="Recherche Zonage Med")

# Titre
st.title("Recherche de zone medical par ville ou code postal")

# Chargement du fichier CSV
@st.cache_data
def charger_donnees():
    return pd.read_csv("zonmed.csv", sep=',')

df = charger_donnees()

# Zone de recherche
recherche = st.text_input("Tapez un nom de ville ou un code postal :")

# Affichage des résultats
if recherche:
    resultats = df[
        df['Nom_commune'].str.contains(recherche, case=False, na=False) |
        df['Code_postal'].astype(str).str.startswith(recherche)
    ]
    
    if not resultats.empty:
        st.write("Résultats :")
        st.dataframe(resultats)
    else:
        st.warning("Aucun résultat trouvé.")
