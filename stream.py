import streamlit as st

import pandas as pd

import matplotlib.pyplot as plt

import seaborn as sns

st.set_page_config(page_title="IRIS Listing",layout="wide")
 
 
st.write("""
 
 # *IRIS DB* app
 
 *
 
 """) 
    
df = pd.read_csv("IRIS.csv")


st.subheader("Listes des donnees dans la DB IRIS")
st.dataframe(df)



st.subheader("Statistiques descriptives")
st.write("Statistiques générales de la base :")
st.write(df.describe())

st.write("Statistiques descriptives par espèce :")
st.write(df.groupby('setosa').describe())


# Filtrage des données
st.subheader("Filtrage des données")
species_selected = st.multiselect(
    "Choisissez les espèces à afficher :",
    options=df['setosa'].unique(),
    default=df['setosa'].unique()
)

df_filtered = df[df['setosa'].isin(species_selected)]
st.write(f"Données filtrées ({len(df_filtered)} lignes) :")
st.dataframe(df_filtered)

st.subheader("Graphiques")

# Sélection des variables pour le graphe
x_axis = st.selectbox("Choisissez l'axe X :", df.columns[:-1])
y_axis = st.selectbox("Choisissez l'axe Y :", df.columns[:-1])

# Création d'un graphe avec seaborn
fig, ax = plt.subplots()
sns.scatterplot(data=df_filtered, x=x_axis, y=y_axis, hue="setosa", ax=ax)
ax.set_title("Graphe interactif : Scatter Plot")
st.pyplot(fig)


