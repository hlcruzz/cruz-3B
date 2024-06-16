import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title, hide_pages

add_page_title()
show_pages(
    [   
        Page("home.py", "ITEQMT Machine Learning Application Portfolio", "💻"),
        Section("Machine Learning UI App", "🧙‍♂️"),
        Page("pages/aboutme.py", "ABOUT HAROLD CRUZ", "1️⃣", in_section=True),
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
       In my Machine Learning Application Portfolio, I present a collection of innovative tools designed to address diverse challenges using advanced machine learning techniques. The Fruits Classification Model was developed to automate the identification of fruits in images, leveraging cutting-edge image processing and classification algorithms. This application not only enhances efficiency in fruit categorization but also supports agricultural research, inventory management, and consumer applications by providing accurate and automated fruit recognition capabilities.

The Sentiment Analysis Tool emerged from the increasing need for automated sentiment analysis in textual data. Built upon natural language processing and machine learning advancements, this tool analyzes the emotional content of text inputs to extract insights into customer feedback, social media sentiment, and communication patterns. Its purpose is to streamline sentiment analysis processes across various domains, aiding decision-making and enhancing understanding of textual data dynamics.

The Crop Recommendation Predictor serves as a crucial tool for farmers seeking optimal crop selection based on soil nutrient levels. Developed with insights from precision agriculture and sustainable farming practices, this application recommends suitable crops by analyzing inputs of nitrogen, phosphorus, and potassium levels. It supports farmers in maximizing crop yield and resource management, thereby promoting sustainable agricultural practices and improved productivity.

For creative applications, the Image Style Transfer application leverages neural style transfer techniques to blend artistic styles between images. Inspired by advancements in computer vision and deep learning, this tool enables users to create visually compelling compositions by transferring the style of one image onto the content of another. It empowers artists, photographers, and digital creators to explore new dimensions of creativity in visual media and digital artistry.

Lastly, the Disease Diagnosis from Medical Images application revolutionizes medical diagnostics by automating disease detection and classification from medical imaging data. Built upon convolutional neural networks (CNNs) and annotated medical datasets, this tool supports healthcare professionals in making informed decisions by accurately identifying diseases from X-rays and MRIs. It aims to enhance diagnostic accuracy, expedite treatment planning, and improve patient outcomes through advanced machine learning technologies.

In conclusion, each application in my portfolio represents a blend of innovation, practicality, and impact across various domains. From agriculture and healthcare to digital art and sentiment analysis, these tools showcase the transformative potential of machine learning in solving real-world challenges. By leveraging state-of-the-art technologies and research, these applications contribute to smarter decision-making, enhanced automation, and creative expression, driving progress in their respective fields and shaping a more connected and intelligent future.
    #""", unsafe_allow_html=True)

st.markdown("""
### 👨‍🎓 Sample Header Title

##### 👨‍👦‍👦 Subheader Title

* Bullet 1
* Bullet 2
* Bullet 3


##### 👨‍🔧 More Content

   HISTORY, PURPOSE AND USAGE
      In my Machine Learning Application Portfolio, I present a collection of innovative tools designed to address diverse challenges using advanced machine learning techniques. The Fruits Classification Model was developed to automate the identification of fruits in images, leveraging cutting-edge image processing and classification algorithms. This application not only enhances efficiency in fruit categorization but also supports agricultural research, inventory management, and consumer applications by providing accurate and automated fruit recognition capabilities.

The Sentiment Analysis Tool emerged from the increasing need for automated sentiment analysis in textual data. Built upon natural language processing and machine learning advancements, this tool analyzes the emotional content of text inputs to extract insights into customer feedback, social media sentiment, and communication patterns. Its purpose is to streamline sentiment analysis processes across various domains, aiding decision-making and enhancing understanding of textual data dynamics.

The Crop Recommendation Predictor serves as a crucial tool for farmers seeking optimal crop selection based on soil nutrient levels. Developed with insights from precision agriculture and sustainable farming practices, this application recommends suitable crops by analyzing inputs of nitrogen, phosphorus, and potassium levels. It supports farmers in maximizing crop yield and resource management, thereby promoting sustainable agricultural practices and improved productivity.

For creative applications, the Image Style Transfer application leverages neural style transfer techniques to blend artistic styles between images. Inspired by advancements in computer vision and deep learning, this tool enables users to create visually compelling compositions by transferring the style of one image onto the content of another. It empowers artists, photographers, and digital creators to explore new dimensions of creativity in visual media and digital artistry.

Lastly, the Disease Diagnosis from Medical Images application revolutionizes medical diagnostics by automating disease detection and classification from medical imaging data. Built upon convolutional neural networks (CNNs) and annotated medical datasets, this tool supports healthcare professionals in making informed decisions by accurately identifying diseases from X-rays and MRIs. It aims to enhance diagnostic accuracy, expedite treatment planning, and improve patient outcomes through advanced machine learning technologies.

In conclusion, each application in my portfolio represents a blend of innovation, practicality, and impact across various domains. From agriculture and healthcare to digital art and sentiment analysis, these tools showcase the transformative potential of machine learning in solving real-world challenges. By leveraging state-of-the-art technologies and research, these applications contribute to smarter decision-making, enhanced automation, and creative expression, driving progress in their respective fields and shaping a more connected and intelligent future.

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
