import streamlit as st

st.set_page_config(page_title="Demo Video", layout="centered")

st.title("🎥 Demo Video")
st.video("https://smuevruvxkvsuzhvwhqd.supabase.co/storage/v1/object/public/images/geospatial_images/Demo.mp4")

if st.button("⬅️ Back to App"):
    st.switch_page("Streamlit_app.py")
