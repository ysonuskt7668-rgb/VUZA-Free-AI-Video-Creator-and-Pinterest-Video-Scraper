import streamlit as st
import google.generativeai as genai
from gtts import gTTS

st.set_page_config(page_title="VUZA AI LATEST", page_icon="🚀")
st.title("🚀 VUZA AI: Latest Version 2024-25")

# Settings
api_key = st.text_input("1. Paste Gemini API Key:", type="password")

# Latest model name (Aap ise change bhi kar sakte hain)
model_name = st.text_input("2. Model Name:", value="gemini-3.6-flash")

topic = st.text_input("3. Enter Topic:")

if st.button("Generate AI Content"):
    if api_key and topic:
        try:
            # Latest Configuration
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(model_name)
            
            with st.spinner(f"Using {model_name}..."):
                response = model.generate_content(topic)
                
                if response.text:
                    st.success("Mil gaya output!")
                    st.write(response.text)
                    
                    # Voiceover Generation
                    tts = gTTS(text=response.text, lang='en')
                    tts.save("voice.mp3")
                    st.audio("voice.mp3")
                else:
                    st.error("AI returned empty response.")
        except Exception as e:
            st.error(f"Error: {e}")
            st.info("Tip: If 404 occurs, try changing model name to 'gemini-1.5-flash' , 'lyria-3.5' , 'veo-3.1-lite' ,  ,or 'gemini-pro'.")
    else:
        st.warning("Please fill all fields!")
