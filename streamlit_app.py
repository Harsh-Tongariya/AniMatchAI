import streamlit as st
import pandas as pd

# Load datasets (update paths if needed)
@st.cache_data
def load_data():
    anime_df = pd.read_csv('data/anime.csv')
    ratings_df = pd.read_csv('data/rating.csv')
    return anime_df, ratings_df

anime_df, ratings_df = load_data()

# Sample data for demo recommendations
sampleAnimeData = [
    {"id": 1, "title": "Steins;Gate", "genres": ["Sci-Fi", "Thriller", "Drama"], "moodTags": ["thoughtful", "exciting"], "personalityMatch": ["INTJ", "INFJ"]},
    {"id": 2, "title": "My Neighbor Totoro", "genres": ["Slice of Life", "Fantasy", "Family"], "moodTags": ["relaxed", "happy", "comforting"], "personalityMatch": ["ISFP", "INFP"]},
    {"id": 3, "title": "Naruto", "genres": ["Action", "Adventure", "Fantasy"], "moodTags": ["excited", "energetic"], "personalityMatch": ["ESTP", "ENFP"]},
    {"id": 4, "title": "Clannad", "genres": ["Drama", "Romance", "Slice of Life"], "moodTags": ["sad", "emotional", "nostalgic"], "personalityMatch": ["INFJ", "INFP"]},
    {"id": 5, "title": "One Punch Man", "genres": ["Action", "Comedy", "Supernatural"], "moodTags": ["funny", "excited"], "personalityMatch": ["ENTP", "ESTP"]},
    {"id": 6, "title": "Your Lie in April", "genres": ["Drama", "Romance", "Music"], "moodTags": ["emotional", "sad"], "personalityMatch": ["INFP", "ISFP"]},
    {"id": 7, "title": "Cowboy Bebop", "genres": ["Sci-Fi", "Action", "Adventure"], "moodTags": ["cool", "thoughtful"], "personalityMatch": ["INTP", "ENTP"]},
    {"id": 8, "title": "K-On!", "genres": ["Slice of Life", "Comedy", "Music"], "moodTags": ["happy", "relaxed"], "personalityMatch": ["ESFP", "ENFP"]}
]

def recommend_by_mood(mood):
    return [a for a in sampleAnimeData if mood in a['moodTags']]

def recommend_by_personality(mbti):
    return [a for a in sampleAnimeData if mbti in a['personalityMatch']]

def generate_mock_bot_reply(user_query):
    user_query = user_query.lower()
    if "time travel" in user_query:
        return "If you like time-travel anime, I recommend 'Steins;Gate'."
    if "action" in user_query and "less drama" in user_query:
        return "For action with less drama, try 'One Punch Man' or 'Mob Psycho 100'."
    if "comedy" in user_query:
        return "'K-On!' and 'Gintama' are excellent comedy anime."
    return "Sorry, I couldn’t find matching recommendations, but 'Steins;Gate' is highly rated!"

st.title("AI Anime Recommendation")

# Mood Recommender
st.header("Anime Mood Recommender")
mood = st.selectbox("Choose your mood", ['', 'happy', 'sad', 'relaxed', 'excited', 'nostalgic'])
if st.button("Get Mood-Based Recommendations"):
    if mood:
        recs = recommend_by_mood(mood)
        if recs:
            for anime in recs:
                st.markdown(f"**{anime['title']}** — *{', '.join(anime['genres'])}*")
        else:
            st.write("No recommendations found for your selected mood.")
    else:
        st.warning("Please select a mood.")

# Personality Recommender
st.header("Anime Personality Match")
mbti_types = ["", "INTJ", "INFJ", "INFP", "INTP", "ENTJ", "ENFJ", "ENFP", "ENTP",
              "ISTJ", "ISFJ", "ISFP", "ISTP", "ESTJ", "ESFJ", "ESFP", "ESTP"]
personality = st.selectbox("Select your MBTI type", mbti_types)
if st.button("Get Personality-Based Recommendations"):
    if personality:
        recs = recommend_by_personality(personality)
        if recs:
            for anime in recs:
                st.markdown(f"**{anime['title']}** — *{', '.join(anime['genres'])}*")
        else:
            st.write("No recommendations found for your selected personality type.")
    else:
        st.warning("Please select a personality type.")

# Chatbot
st.header("Chat with AI Anime Bot")
query = st.text_input("Type your query here")
if st.button("Send Query"):
    if query:
        reply = generate_mock_bot_reply(query)
        st.markdown(f"**AI Bot:** {reply}")
    else:
        st.warning("Please enter a query.")
