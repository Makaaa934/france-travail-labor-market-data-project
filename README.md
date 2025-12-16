# 🇫🇷 France Travail — Data & BI Labor Market Analysis (Bloc 6)

---

## 🇬🇧 English summary

**Objective**  
Analyze how Data skills demand evolves in France using France Travail data, enriched with international comparisons, BI dashboards, and machine learning.

**Outcome**  
A complete end-to-end data project combining analysis, visualization, and prediction to support better job offer calibration and candidate orientation.

---

> **Positionnement** : *Data Analyst / BI — Junior reconverti avec expérience anterieur*  
>  
> Projet data complet visant à analyser l’évolution de la demande en compétences Data en France, à partir des données **France Travail**, enrichies par une **comparaison internationale**, des **dashboards BI**, et un **dispositif analytique et prédictif**.

---

## 🎯 Problématique métier

**Comment évolue la demande en compétences Data sur le marché français, et comment mieux calibrer les offres d’emploi ?**

Les données publiques existent, mais elles sont souvent :
- hétérogènes
- peu standardisées
- difficiles à exploiter pour la décision

Ce projet vise à transformer ces données en **leviers d’analyse clairs**, exploitables par :
- des recruteurs
- des institutions publiques
- des candidats en reconversion ou en évolution

---

## 🧩 Contenu du projet

- 🔍 **Analyse exploratoire (EDA)**  
  Domaines d’activité, entreprises, compétences, niveaux d’expérience

- 🌍 **Comparaison France vs Monde**  
  Structuration des offres, standardisation des compétences, écarts de salaires

- 📊 **Dashboard Power BI**  
  KPIs métiers, filtres dynamiques, visualisations décisionnelles

- 🐍 **Pipeline Python (API)**  
  Collecte, nettoyage et structuration des données

- 🧠 **Machine Learning (Dataiku)**  
  Modèle prédictif / scoring pour appuyer l’analyse et la cohérence des offres

- 🚀 **Application Streamlit**  
  Démonstrateur interactif orienté usage métier

---

## 📊 Dashboard Power BI

📁 Dossier : `powerbi/`

Le dashboard permet notamment :
- d’identifier les **compétences les plus demandées**
- de comparer les attentes selon le **niveau d’expérience**
- de visualiser les **écarts France / International**
- d’explorer les données par **domaine et type d’entreprise**

---

## 🧠 Machine Learning — Dataiku

📁 Dossier : `dataiku/`

- Type de modèle : *(à ajuster si besoin : Random Forest / Régression / autre)*
- Variables clés : poste, pays, compétences, expérience, domaine
- Objectif métier :  
  → **Aider au calibrage des offres et à la compréhension des niveaux d’exigence**

---

## 🐍 Collecte & traitement des données (Python)

📁 Dossier : `src/api/`

- Requêtage API
- Normalisation des champs
- Préparation des datasets pour l’analyse et la BI

---

## 🚀 Démonstrateur Streamlit

📁 Dossier : `src/streamlit/`

L’application permet à l’utilisateur de renseigner :
- le poste visé
- le pays
- les compétences clés
- le niveau d’expérience  

afin d’obtenir une **estimation cohérente** selon le profil.

### Lancer l’application :

 [Prédiction de salaire](https://mlsalairespredictions-mg3mrvnyju2rxfqdmwhqfv.streamlit.app/)
 

## 🔍 Insights clés

Voir le fichier [`INSIGHTS.md`](INSIGHTS.md)

Exemples :

- Le **niveau d’expérience** structure davantage le marché que l’intitulé de poste.
- Certaines compétences sont **transversales** (SQL, Python), tandis que d’autres révèlent la **maturité data** des organisations.
- La comparaison **France / Monde** met en évidence des écarts de **structuration des offres**, de **standardisation des compétences** et de **salaires**.

---

## 🛠️ Stack technique

- Python (API, traitement, Streamlit)
- Power BI (visualisation & KPIs)
- Dataiku (Machine Learning)
- Pandas, scikit-learn, requests

---

## 👥 Équipe projet

Projet réalisé en collaboration avec :

- **Pauline Maurin** – Data Analyst  
  GitHub : https://github.com/Pauline29121990

- **Anthony Giacobi** – Data Analyst  
  GitHub : https://github.com/Ant-gcb

- **Thomas Dimek** – Data Analyst  
  GitHub : https://github.com/FastCapybara31

---

## 📌 À propos

Ce projet s’inscrit dans un parcours de **reconversion vers les métiers de la Data**, avec une forte attention portée à :
- la compréhension métier
- la lisibilité des analyses
- la capacité à transformer la donnée en décision

## 📚 Sources de données

Les analyses présentées dans ce projet s’appuient sur des données publiques et ouvertes :

- **France Travail**  
  Offres d’emploi, compétences, domaines d’activité  
  https://www.francetravail.fr  
  https://api.francetravail.io  

- **Données internationales (job market / salaries)**  
  Agrégation de jeux de données ouverts issus de plateformes internationales scrappés par [Luke Barousse](https://github.com/lukebarousse)
 et Kaggle, sources open data publiques — (utilisées à des fins comparatives)

- **Traitements & enrichissements**  
  Nettoyage, normalisation et agrégation réalisés par l’équipe projet  
  à des fins d’analyse, de visualisation et de modélisation.

> ⚠️ Ce projet est réalisé à des fins pédagogiques et analytiques.  
> Les résultats présentés ne constituent ni une vérité absolue, ni une recommandation officielle de France Travail.


