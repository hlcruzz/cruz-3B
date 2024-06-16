import streamlit as st

def show_app_description():
    st.markdown("# APP DESCRIPTION")

    st.markdown("""
    Welcome to my Streamlit application portfolio! Here, I showcase three exciting projects that demonstrate my skills and interests in machine learning and data science.
    """)

    st.markdown("## Machine Learning Applications")

    st.markdown("### Crop Prediction 🌾")
    st.markdown("""
    This application leverages machine learning models to predict crop yields based on historical data, weather patterns, and soil conditions. It aims to assist farmers in making informed decisions for optimal crop planning and management.
    """)

    st.markdown("### Sentiment Analyzer 😊")
    st.markdown("""
    The sentiment analyzer uses natural language processing (NLP) techniques to analyze and classify text sentiment. It helps businesses understand customer feedback, social media sentiment, and review sentiments to derive actionable insights.
    """)

    st.markdown("### Image Classification 🖼️")
    st.markdown("""
    This application employs deep learning models to classify images into predefined categories. It can be used for tasks such as identifying objects in images, facial recognition, or medical image analysis. Explore the power of image recognition with this interactive tool!
    """)

    st.markdown("---")

    st.info("Explore each application to see demos and learn more about the underlying technology.")
    st.info("Connect with me on [Facebook](https://web.facebook.com/harold.gravela.cruz/) for collaborations and discussions.")

# Main function to run the app
def main():
    show_app_description()

if __name__ == "__main__":
    main()
