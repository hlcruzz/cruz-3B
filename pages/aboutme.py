import streamlit as st

def show_about_me():
    st.markdown("# ABOUT ME")
    st.markdown("""
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    """)
    st.markdown("---")

    st.image("./about_me_image.jpg")
    st.markdown("""
    Photo by [Your Name](https://example.com) on [Unsplash](https://unsplash.com)
    """)

    st.markdown("---")

    with st.expander("More about me"):
        st.markdown("""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla scelerisque ex sit amet risus fermentum, 
        vel tempor velit vestibulum. Cras in bibendum odio, in malesuada augue. Donec bibendum et elit nec 
        ultricies. Nulla facilisi. Fusce vel ex ut sapien feugiat eleifend. Vivamus nec justo eget nibh 
        placerat ultrices. Sed gravida, neque nec placerat tempus, nunc mauris vehicula est, et commodo 
        lacus sem nec libero. Suspendisse potenti. Duis sodales ligula vitae mauris vehicula, in finibus 
        purus venenatis. Nulla ullamcorper, orci sit amet varius bibendum, urna nisi interdum mi, nec 
        iaculis neque velit et velit. Phasellus mollis laoreet orci, vel volutpat sapien congue ac. 
        Praesent eget lectus vel quam condimentum tempus. Nam vel felis ut lectus interdum malesuada. 
        Nulla facilisi.
        """)

    st.markdown("---")

    st.info("Connect with me on [LinkedIn](https://www.linkedin.com)!")
    st.info("Visit my personal website [here](https://www.example.com)")

# Main function to run the app
def main():
    show_about_me()

if __name__ == "__main__":
    main()
