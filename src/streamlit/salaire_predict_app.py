from narwhals import col
import streamlit as st
import pandas as pd
import joblib
import json

# == Configuration page
st.set_page_config(
    page_title="Prévisions des salaires dans la data",
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://mon-site-aide.com',
        'Report a bug': 'https://mon-site-bugs.com',
        'About': 'Application créée par Pauline'
    }
)

# Chargement du modèle et de l'encoder
model = joblib.load("modele_salaire.pkl")
encoder = joblib.load("encoder_ohe.pkl")

with open("encoded_columns.json", "r") as f:
    encoded_columns = json.load(f)

st.header("💰 Estimation de salaire dans la data")
st.write("Remplis les informations ci-dessous pour obtenir une estimation de salaire.")

# Chargement du dataset original pour récupérer les valeurs possibles
df = pd.read_csv("ai_job_dataset - ai_job_dataset.csv")

# Liste explicite des colonnes à renommer
skills_cols = [
    'Azure', 'Dataviz', 'Statistics', 'Git', 'Spark', 'Hadoop', 'Deep_learning',
    'Mlops', 'Tableau', 'Linux', 'Docker', 'Pytorch', 'Tensorflow',
    'Gcp', 'Aws', 'R', 'Sql', 'Python'
]

# Creation des filtres pour les sélecteurs
job_titles = sorted(df['job_title'].dropna().unique())
locations = sorted(df['company_location'].dropna().unique())
company_sizes = sorted(df['company_size'].dropna().unique())
education_levels = sorted(df['education_required'].dropna().unique())
industries = sorted(df['industry'].dropna().unique())
experience_levels = sorted(df['experience_level'].dropna().unique())



# Selectbox 
experience_levels = ['EN', 'MI', 'SE', 'EX']  # Débutant → Cadre
company_sizes = ['S', 'M', 'L']  # Small → Medium → Large

col1, col2 = st.columns(2)
with col1:
    selected_job = st.selectbox("Quel poste vises-tu ?", job_titles)
    selected_country = st.selectbox("Dans quel pays veux tu postuler?", locations)
    selected_experience = st.selectbox("Niveau d'expérience", experience_levels, help="EN (Débutant / junior) , MI (Intermédiaire / Confirmé), SE (Senior) , EX (Cadre dirigeant / Directeur)")
    

with col2:
    selected_company_size = st.selectbox("Taille de l'entreprise", company_sizes, help="S (Small <50), M (Medium 50-250), L (Large >250)")
    selected_education = st.selectbox("Niveau d'éducation", education_levels, help="Associate (Bac +2) , Bachelor (Bac +3), Master (Bac +4), PhD (Bac +8)")
    selected_industry = st.selectbox("Secteur d'activité", industries)
    

selected_skills = st.multiselect("🧠 Quelles compétences techniques maîtrises-tu ?", skills_cols)


skills_encoded = {}
for skill in skills_cols:
    col_name = skill.upper()  # le modèle s’attend à des noms en majuscules
    skills_encoded[col_name] = 1 if skill in selected_skills else 0

# Encodage des variables pour reconnaissance du modele
# Variables catégorielles à encoder
input_cat = pd.DataFrame({
    'job_title': [selected_job],
    'company_location': [selected_country],
    'company_size': [selected_company_size],
    'education_required': [selected_education],
    'industry': [selected_industry],
    'experience_level': [selected_experience]
})

# Étape 1 : encoder les variables catégorielles
encoded_input = encoder.transform(input_cat)
encoded_df = pd.DataFrame(encoded_input, columns=encoder.get_feature_names_out(), index=[0])

# Étape 2 : construire toutes les colonnes de skills attendues
with open("encoded_columns.json", "r") as f:
    expected_columns = json.load(f)

# Extraire les colonnes de compétences uniquement (en majuscules)
skills_expected = [col for col in expected_columns if col.isupper()]

# Initialiser toutes à 0
skills_encoded = {col: 0 for col in skills_expected}

# Cocher celles sélectionnées par l'utilisateur
for skill in selected_skills:
    col_name = skill.upper()
    if col_name in skills_encoded:
        skills_encoded[col_name] = 1

# Transformer en DataFrame
skills_df = pd.DataFrame([skills_encoded])

# Étape 3 : concaténer variables catégorielles + compétences
final_input = pd.concat([encoded_df, skills_df], axis=1)

# Étape 4 : s'assurer que l'ordre des colonnes est correct
final_input = final_input.reindex(columns=expected_columns, fill_value=0)

# Étape 5 : prédiction
prediction = model.predict(final_input)
st.success(f"💰 Salaire estimé : {int(prediction[0]):,} $")

