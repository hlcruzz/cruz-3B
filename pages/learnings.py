import streamlit as st

def show_learnings():
    st.markdown("# WHAT I HAVE LEARNED")

    st.markdown("""
    Developing these applications has been a rewarding journey, allowing me to delve into various aspects of machine learning and data science. Here are some key learnings from each project:
    """)

    st.markdown("## Crop Prediction 🌾")
    st.markdown("""
    - **Data Preprocessing**: I've gained expertise in cleaning and preprocessing agricultural data, including handling missing values and scaling features.
    - **Machine Learning Models**: Implemented regression models to predict crop yields based on factors such as weather data, soil quality, and crop type.
    - **Domain Knowledge**: Acquired insights into agricultural practices and the importance of data-driven decision-making in farming.
    """)

    st.markdown("## Sentiment Analyzer 😊")
    st.markdown("""
    - **Natural Language Processing (NLP)**: Explored NLP techniques for text preprocessing, feature extraction, and sentiment analysis using libraries like NLTK and spaCy.
    - **Model Evaluation**: Learned methods to evaluate sentiment analysis models, including accuracy metrics and handling sentiment polarity variations.
    - **Application in Business**: Understood the application of sentiment analysis in customer feedback analysis, brand monitoring, and social media sentiment analysis.
    """)

    st.markdown("## Image Classification 🖼️")
    st.markdown("""
    - **Deep Learning**: Delved into convolutional neural networks (CNNs) for image classification tasks, including model architectures like VGG, ResNet, and EfficientNet.
    - **Transfer Learning**: Applied transfer learning techniques using pre-trained models like ImageNet to boost classification accuracy with limited training data.
    - **Real-World Applications**: Explored practical applications of image classification in areas such as healthcare (medical imaging), object detection, and facial recognition.
    """)

    st.markdown("---")

    st.info("These projects have equipped me with practical skills in machine learning, data preprocessing, model evaluation, and domain-specific knowledge. Connect with me on [Facebook](https://web.facebook.com/harold.gravela.cruz/) to discuss more about these projects!")

# Main function to run the app
def main():
    show_learnings()

if __name__ == "__main__":
    main()
