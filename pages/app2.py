
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

emotions = {
    'happy': ['happy', 'joyful', 'delighted', 'pleased', 'ecstatic', 'content', 'cheerful', 'satisfied', 'joyous'],
    'sad': ['sad', 'depressed', 'gloomy', 'miserable', 'heartbroken', 'unhappy', 'despair', 'downcast', 'melancholy'],
    'angry': ['angry', 'furious', 'outraged', 'irritated', 'enraged', 'indignant', 'infuriated', 'annoyed', 'frustrated'],
    'excited': ['excited', 'thrilled', 'enthusiastic', 'eager', 'animated', 'elated', 'pumped', 'energetic', 'excitement'],
    'nervous': ['nervous', 'anxious', 'apprehensive', 'worried', 'unsettled', 'tense', 'edgy', 'jittery', 'restless'],
    'scared': ['scared', 'fearful', 'terrified', 'panicked', 'alarmed', 'frightened', 'petrified', 'anxious', 'apprehensive']
}

train_data = []
for emotion, words_list in emotions.items():
    for words in words_list:
        train_data.append((words, emotion))

vectorizer = CountVectorizer(token_pattern=r'\b\w+\b')
X_train = vectorizer.fit_transform([data[0] for data in train_data])
y_train = [data[1] for data in train_data]

classifier = MultinomialNB()
classifier.fit(X_train, y_train)


st.title("Sentiment Analysis")

sentence = st.text_input("Enter a sentence for sentiment analysis:")

if st.button("Analyze"):
    if sentence:
        X_test = vectorizer.transform([sentence])
        emotion = classifier.predict(X_test)[0]
        st.write(f"Sentence: {sentence}")
        st.write(f"Emotion: {emotion}")
    else:
        st.warning("Please enter a sentence.")
