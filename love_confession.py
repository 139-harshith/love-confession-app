import streamlit as st

# Initialize session state
if "page" not in st.session_state:
    st.session_state.page = 1

def go_to_next_page():
    st.session_state.page += 1
    st.rerun()

def go_to_crying_page():
    st.session_state.page = 5
    st.rerun()

def go_to_kiss_page():
    st.session_state.page = 6
    st.rerun()

# Custom CSS for styling
st.markdown(
    """
    <style>
        .stApp {
            background-color: #87CEEB; /* Sky Blue */
        }
        .yes-button {
            background-color: #FF69B4;
            color: white;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
        }
        .no-button {
            position: absolute;
            background-color: red;
            color: white;
            padding: 10px 20px;
            border-radius: 10px;
            border: none;
            cursor: pointer;
        }
        .heart-corner {
            position: fixed;
            bottom: 20px;
            right: 20px;
            font-size: 50px;
            color: red;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- PAGE 1 ----
if st.session_state.page == 1:
    st.title("Hii Monisha, can I ask you a question?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes", key="yes1"):
            go_to_next_page()
    with col2:
        if st.button("No", key="no1"):
            go_to_crying_page()

# ---- PAGE 2 ----
elif st.session_state.page == 2:
    st.title("I love you. Will you love me?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes", key="yes2"):
            go_to_next_page()
    with col2:
        if st.button("No", key="no2"):
            go_to_crying_page()

# ---- PAGE 3 ----
elif st.session_state.page == 3:
    st.title("Wait... Are you sure?")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Yes", key="yes3"):
            go_to_next_page()
    with col2:
        st.button("No", disabled=True)

# ---- PAGE 4 ----
elif st.session_state.page == 4:
    st.title("Yay! ❤️ You love me too!")
    st.balloons()
    st.markdown("<h3 style='color:pink;'>Forever Together!</h3>", unsafe_allow_html=True)
    st.markdown("<div class='heart-corner'>❤️</div>", unsafe_allow_html=True)
    if st.button("The End 💋"):
        go_to_kiss_page()

# ---- CRYING PAGE ----
elif st.session_state.page == 5:
    st.title("Oh no... You broke my heart! 💔")
    st.markdown("<h3 style='color:red; text-align: center;'>But I still love you...</h3>", unsafe_allow_html=True)
    if st.button("Okay, I accept your love", key="accept_love"):
        st.session_state.page = 3  # Directly go to Page 3
        st.rerun()

# ---- KISS PAGE ----
elif st.session_state.page == 6:
    st.title("Okiee... Now give me a kiss! 😘")
    st.markdown("<h1 style='text-align: center;'>💋💋💋</h1>", unsafe_allow_html=True)
    if st.button("Muah! 💋", key="kiss"):
        st.session_state.page = 1  # Restart the app
        st.rerun()

# ---- YouTube Song Embedding ----
st.markdown(
    """
    <iframe width="560" height="315" 
    src="https://www.youtube.com/embed/4adZ7AguVcw?autoplay=1&loop=1" 
    frameborder="0" allow="autoplay" allowfullscreen></iframe>
    """,
    unsafe_allow_html=True
)
