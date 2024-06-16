import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "ITEQMT Machine Learning Application Portfolio", "💻"),
        Section("Machine Learning UI App", "🧙‍♂️"),
        Page("pages/aboutme.py", "ABOUT HAROLD", "1️⃣", in_section=True),
        Page("pages/discription.py", "APP DESCRIPTION", "2️⃣", in_section=True),
        Page("pages/learnings.py", "WHAT I HAVE LEARN?", "3️⃣", in_section=True),
    
  
        Section("PROJECTS", "💾"),
        Page("pages/predict.py", "PREDICTION", "1️⃣", in_section=True),
        Page("pages/sentiment.py", "SENTIMENT ANALYZER", "2️⃣", in_section=True),
        Page("pages/image.py", "IMAGE CLASSIFICATION", "3️⃣", in_section=True),


         Section("SOURCE CODE", "💾"),
        Page("pages/predict_src.py", "PREDICTION", "1️⃣", in_section=True),
        Page("pages/sentiment_src.py", "SENTIMENT ANALYZER", "2️⃣", in_section=True),
        Page("pages/image_src.py", "IMAGE CLASSIFICATION", "3️⃣", in_section=True),
    

    ]
)

hide_pages(["Thank you"])

st.markdown("### 👨‍🔧 ML Learning by [koalatech](https://github.com/koalatech)")

st.image("./p1.jpg")
st.markdown("""<a href="/photographer/thinkstock-83786">Thinkstock</a> on <a href="/">Freeimages.com</a>""",unsafe_allow_html=True,)

st.info("Visit the project [Github](https://github.com/koalatech/streamlit_web_app)")
st.info("👨‍🔧 Please take note when on streamlit.app the [Image Classification] pages are not working due to Memory Limitation of 'Free Tier' hosting of Streamlit") 
st.markdown("---")

with st.expander("Sample ""st.expander"""):
    st.markdown("""
    
    <a href=""><img src="https://user-images.githubusercontent.com/875246/185755203-17945fd1-6b64-46f2-8377-1011dcb1a444.png" height="50" /></a>

    #

        HISTORY, PURPOSE AND USAGE
        Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. 
        The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book. It usually begins with:
        “Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.”
        The purpose of lorem ipsum is to create a natural looking block of text (sentence, paragraph, page, etc.) that doesn't distract from the layout. 
        A practice not without controversy, laying out pages with meaningless filler text can be very useful when the focus is meant to be on design, not content.
        The passage experienced a surge in popularity during the 1960s when Letraset used it on their dry-transfer sheets, and again during the 90s as desktop publishers bundled the text with their software. 
        Today it's seen all around the web; on templates, websites, and stock designs. Use our generator to get your own, or read on for the authoritative history of lorem ipsum.
        
    #""", unsafe_allow_html=True)

st.markdown("""
### 👨‍🎓 Sample Header Title

##### 👨‍👦‍👦 Subheader Title

* Bullet 1
* Bullet 2
* Bullet 3


##### 👨‍🔧 More Content

   HISTORY, PURPOSE AND USAGE
        Lorem ipsum, or lipsum as it is sometimes known, is dummy text used in laying out print, graphic or web designs. 
        The passage is attributed to an unknown typesetter in the 15th century who is thought to have scrambled parts of Cicero's De Finibus Bonorum et Malorum for use in a type specimen book. It usually begins with:
        “Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.”
        The purpose of lorem ipsum is to create a natural looking block of text (sentence, paragraph, page, etc.) that doesn't distract from the layout. 
        A practice not without controversy, laying out pages with meaningless filler text can be very useful when the focus is meant to be on design, not content.
        The passage experienced a surge in popularity during the 1960s when Letraset used it on their dry-transfer sheets, and again during the 90s as desktop publishers bundled the text with their software. 
        Today it's seen all around the web; on templates, websites, and stock designs. Use our generator to get your own, or read on for the authoritative history of lorem ipsum.

### 🔎 Overview""", unsafe_allow_html=True)


st.image("./p1.jpg")


st.markdown("""
In my Machine Learning Application Portfolio, I showcase a diverse range of applications designed to solve real-world challenges using advanced machine learning techniques. One prominent example is the Fruits Classification Model, which leverages image processing and classification algorithms to accurately identify various fruits from uploaded images. Users can interactively upload images through a sidebar uploader, view predictions alongside the uploaded image, and explore the application's capabilities in real-time.

Another notable tool is the Sentiment Analysis Tool, tailored to analyze the emotional tone of input sentences. This application employs a Naive Bayes classifier trained on labeled emotional expressions, offering users immediate feedback on predicted emotions such as happiness, sadness, anger, excitement, nervousness, and fear. It provides a simple yet effective way to gauge sentiment in text, enhancing communication analysis and customer feedback processing.

For agricultural applications, the Crop Recommendation Predictor assists farmers in making informed decisions by recommending suitable crops based on soil nutrient levels. Using a pre-trained Naive Bayes classifier loaded from a pickle file, this tool adjusts sliders for nitrogen, phosphorus, and potassium inputs to predict the best crop match. It serves as a valuable resource for optimizing crop yield and ensuring sustainable farming practices.

Additionally, the Image Style Transfer application merges artistic styles from one image onto the content of another, enabling creative transformations of visual content. Users upload two images—one for content and another for style—and customize style transfer parameters to achieve unique artistic effects. This application harnesses the power of machine learning to blend artistic creativity with digital imagery.

Lastly, the Disease Diagnosis from Medical Images tool aids in medical diagnostics by analyzing medical images such as X-rays or MRIs to detect and classify diseases. Using convolutional neural networks (CNNs) trained on annotated medical datasets, this application provides accurate diagnoses and visual feedback on detected diseases. It supports healthcare professionals in making informed decisions and improving patient care outcomes.

In conclusion, each application in my portfolio demonstrates the practical application of machine learning across diverse domains, from agriculture and healthcare to creative arts and communication analysis. These tools illustrate the versatility and impact of machine learning in enhancing decision-making, automation, and creativity, catering to various user needs and driving innovation in their respective fields.

This structured paragraph provides an overview of each application's purpose, functionality, and the benefits it offers, showcasing your proficiency in applying machine learning to address specific challenges across different sectors.
            
### ⭐ Star the project on Github  <iframe src="https://ghbtns.com/github-btn.html?user=koalatech&repo=streamlit_web_app&type=star&count=true"  width="150" height="20" title="GitHub"></iframe>   
""", unsafe_allow_html=True)

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
"""

# st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
