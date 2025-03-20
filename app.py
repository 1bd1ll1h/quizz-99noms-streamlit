import streamlit as st

#st.warning("🚧 Cette application est en cours de construction. Revenez bientôt pour plus de contenu !")
import streamlit as st
import random

# ======= Données (exemple sur 4 noms) =======
noms_allah = [
    {"nom_ar": "الرَّحْمَن", "nom": "Ar-Rahman", "signification": "Le Tout Miséricordieux"},
    {"nom_ar": "الرَّحِيم", "nom": "Ar-Rahim", "signification": "Le Très Miséricordieux"},
    {"nom_ar": "الْمَلِك", "nom": "Al-Malik", "signification": "Le Souverain"},
    {"nom_ar": "الْقُدُّوس", "nom": "Al-Quddus", "signification": "Le Très Saint"},
]

# ======= Session state pour la navigation =======
if "index_apprentissage" not in st.session_state:
    st.session_state.index_apprentissage = 0

if "score" not in st.session_state:
    st.session_state.score = 0
if "questions_posées" not in st.session_state:
    st.session_state.questions_posées = 0

# ======= Sidebar navigation =======
mode = st.sidebar.radio("Choisis un mode :", ["Accueil", "Apprendre", "Quiz"])

# ======= Accueil =======
if mode == "Accueil":
    st.title("🌿 Les 99 Noms d'Allah ﷻ")
    st.write("Apprends et teste tes connaissances sur les 99 noms d'Allah.")
    st.image("/home/abdallah/Bureau/quizz-99noms-streamlit/images/OrangeَAllahCentre.png", width=200)

# ======= Mode Apprentissage =======
elif mode == "Apprendre":
    st.title("📖 Mode Apprentissage")
    i = st.session_state.index_apprentissage
    nom = noms_allah[i]
    
    st.header(f"{nom['nom_ar']} ({nom['nom']})")
    st.subheader(f"🌸 Signification : {nom['signification']}")

    # Tu peux ajouter un audio si tu as des fichiers
    # st.audio(f"audios/{nom['nom']}.mp3")

    # Navigation dans les noms
    col1, col2, col3 = st.columns(3)
    
    if col1.button("⬅️ Précédent") and i > 0:
        st.session_state.index_apprentissage -= 1
    if col3.button("➡️ Suivant") and i < len(noms_allah) - 1:
        st.session_state.index_apprentissage += 1
    
    st.markdown(f"**Nom {i + 1} sur {len(noms_allah)}**")

# ======= Mode Quiz =======
elif mode == "Quiz":
    st.title("📝 Quiz : Les 99 Noms d'Allah ﷻ")

    # Générer une question
    question = random.choice(noms_allah)
    bonnes_reponses = [n["nom"] for n in noms_allah]
    propositions = random.sample(bonnes_reponses, 3)

    # Assure que la bonne réponse est dedans
    if question["nom"] not in propositions:
        propositions[random.randint(0, 2)] = question["nom"]

    st.write(f"Quel est le nom qui signifie : **{question['signification']}** ?")
    reponse = st.radio("Choisis une réponse :", propositions)

    if st.button("Valider"):
        if reponse == question["nom"]:
            st.success("✅ Bonne réponse !")
            st.session_state.score += 1
        else:
            st.error(f"❌ Mauvaise réponse. La bonne réponse était **{question['nom']}**.")
        
        st.session_state.questions_posées += 1

    # Afficher le score courant
    st.info(f"Score : {st.session_state.score} / {st.session_state.questions_posées}")

    if st.button("🔄 Recommencer le Quiz"):
        st.session_state.score = 0
        st.session_state.questions_posées = 0
