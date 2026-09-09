import streamlit as st
import google.generativeai as genai
from gtts import gTTS

st.set_page_config(page_title="AI Video Tool", page_icon="🎬")
st.title("🎬 VUZA AI: Latest Version")

api_key = st.text_input("Gemini API Key:", type="password")
topic = st.text_input("Topic:")

if st.button("Generate Now"):
    if api_key and topic:
        try:
            genai.configure(api_key=api_key)
            
            # Hum bilkul LATEST experimental aur stable models try karenge
            # 1. Gemini 2.0 Flash (Latest)
            # 2. Gemini 1.5 Flash (Stable)
            model_name = 'gemini-1.5-flash' 
            
            model = genai.GenerativeModel(model_name)
            
            with st.spinner(f"Using {model_name} to generate..."):
                # Naya content generation method
                response = model.generate_content(topic)
                
                if response.text:
                    st.success("Success!")
                    st.write(response.text)
                    
                    # Voiceover
                    tts = gTTS(text=response.text, lang='en')
                    tts.save("voice.mp3")
                    st.audio("voice.mp3")
                else:
                    st.error("AI response was empty.")
                    
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Tip: Make sure your API Key is from 'Google AI Studio'.")
    else:
        st.warning("Enter Key and Topic!")
