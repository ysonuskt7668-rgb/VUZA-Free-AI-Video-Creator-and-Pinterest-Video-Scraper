import streamlit as st
import google.generativeai as genai
from gtts import gTTS
import os

st.set_page_config(page_title="AI Video Tool", page_icon="🎬")
st.title("🎬 VUZA: AI Video & Pinterest Tool")

api_key = st.text_input("Enter Google Gemini API Key:", type="password")
topic = st.text_input("Enter Topic (e.g., Facts about India):")

if st.button("Generate Script & Voice"):
    if not api_key or not topic:
        st.error("API Key and Topic are required!")
    else:
        try:
            genai.configure(api_key=api_key)
            # Try to use the most stable model name
            model = genai.GenerativeModel('gemini-pro')
            
            with st.spinner("AI is thinking..."):
                response = model.generate_content(f"Write a short 3-line fun fact about {topic}")
                script_text = response.text
                
                st.success("Script Generated!")
                st.write(script_text)
                
                # Audio
                tts = gTTS(text=script_text, lang='en')
                tts.save("voice.mp3")
                st.audio("voice.mp3")
                st.success("Voice is ready to play!")
        except Exception as e:
            st.error(f"Try again! Error details: {e}")
