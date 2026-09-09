import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="AI Video & Pinterest Downloader", page_icon="🎬")

st.title("🎬 VUZA: AI Video & Pinterest Tool")

tab1, tab2 = st.tabs(["🤖 AI Video Generator", "📌 Pinterest Downloader"])

with tab1:
    st.subheader("1. AI Script & Voice Creator")
    api_key = st.text_input("Enter Google Gemini API Key:", type="password")
    topic = st.text_input("Enter Topic (e.g., 5 Facts about Space):")
    
    if st.button("Generate Script & Voiceover"):
        if not api_key or not topic:
            st.error("Please enter both API Key and Topic!")
        else:
            try:
                with st.spinner("AI is generating script & voice..."):
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel('gemini-2.0-flash')
                    response = model.generate_content(f"Write a short 30-second YouTube shorts script about: {topic}")
                    script_text = response.text
                    
                    st.success("Script Generated!")
                    st.text_area("Generated Script:", script_text, height=150)
                    
                    # Audio Generation
                    tts = gTTS(text=script_text, lang='en')
                    tts.save("voice.mp3")
                    st.audio("voice.mp3")
                    st.success("Voiceover Ready!")
            except Exception as e:
                st.error(f"Error: {e}")

with tab2:
    st.subheader("2. Pinterest Video Downloader")
    pin_url = st.text_input("Paste Pinterest Link:")
    if st.button("Fetch Video"):
        if pin_url:
            try:
                headers = {'User-Agent': 'Mozilla/5.0'}
                res = requests.get(pin_url, headers=headers)
                soup = BeautifulSoup(res.text, 'html.parser')
                video_tag = soup.find('video')
                if video_tag and video_tag.get('src'):
                    video_url = video_tag['src']
                    st.success("Video Found!")
                    st.video(video_url)
                else:
                    st.warning("Could not extract direct video. Make sure it's a video pin!")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.error("Please enter a URL")
