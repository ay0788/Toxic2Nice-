import streamlit as st
from toxic2nice import detoxify
from model.emotion import detect_emotion  # if you added emotion detection

st.set_page_config(page_title="Toxic2Nice", page_icon="💖")

st.title("💖 Toxic2Nice: Make It Polite")
st.markdown("Transform any toxic comment into a respectful version with personality!")

user_input = st.text_area("Enter a toxic message:")
style = st.selectbox("Choose a response style:", ["Empathetic", "Professional", "Funny"])

if user_input.strip():
    emotion, score = detect_emotion(user_input)
    st.markdown(f"**💡 Detected Emotion:** {emotion} ({score:.2f})")

if st.button("Transform"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        clean_version = detoxify(user_input, style)
        st.success(clean_version)
