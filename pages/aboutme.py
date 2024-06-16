import streamlit as st

def show_about_me():
    st.markdown("# ABOUT ME")
    st.markdown("""
    Hey there! 👋 I'm a third-year BSIS student with a passion for technology and a love for exploring new ideas. When I'm not buried in code or studying, you'll often find me on the basketball court, strumming my guitar, or lost in the world of music. These hobbies are not just pastimes for me; they are avenues for relaxation and creative expression.
    """)

    st.markdown("---")

    st.image("pages/about_me_image.jpg")
    st.markdown("""
    Photo by [Your Name](https://example.com) on [Unsplash](https://unsplash.com)
    """)

    st.markdown("---")

    with st.expander("More about me"):
        st.markdown("""
        My journey in BSIS has been filled with exciting challenges and rewarding experiences. I'm particularly interested in exploring machine learning applications and developing solutions that make a difference. Learning about AI and its real-world applications has been a fascinating part of my academic journey so far.

        ### Personal Interests

        - **Basketball**: I'm passionate about basketball and enjoy playing both casually with friends and competitively.
        - **Guitar**: Playing the guitar is my creative outlet. It allows me to unwind and explore my musical interests.
        - **Music**: I have a diverse taste in music, ranging from classic rock to contemporary pop. Music is my constant companion during study sessions and leisure time.

        ### Future Goals

        Looking ahead, I'm eager to continue learning and growing in the field of information systems. My goal is to leverage my skills and knowledge to contribute meaningfully to the tech industry and beyond.
        """)

    st.markdown("---")

    st.info("Connect with me on [Facebook](https://web.facebook.com/harold.gravela.cruz/)")
    st.info("Visit my personal website [here](https://web.facebook.com/harold.gravela.cruz/)")

# Main function to run the app
def main():
    show_about_me()

if __name__ == "__main__":
    main()
