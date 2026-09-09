import streamlit as st
import google.generativeai as genai
from gtts import gTTS

st.set_page_config(page_title="VUZA AI Success", page_icon="🎬")
st.title("🎬 VUZA AI: Final Attempt")

api_key = st.text_input("Paste your API Key here:", type="password")
topic = st.text_input("Enter Topic (e.g., Space):")

if st.button("Generate Now"):
    if api_key and topic:
        try:
            genai.configure(api_key=api_key)
            
            # Auto-detect available models to fix 404
            available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            
            if not available_models:
                st.error("No models found for this API Key. Check your Google AI Studio permissions.")
            else:
                # Pick the first available model
                selected_model = available_models[0]
                st.info(f"Using model: {selected_model}")
                
                model = genai.GenerativeModel(selected_model)
                
                with st.spinner("AI is thinking..."):
                    response = model.generate_content(topic)
                    if response.text:
                        st.success("Mil Gaya!")
                        st.write(response.text)
                        
                        tts = gTTS(text=response.text, lang='en')
                        tts.save("voice.mp3")
                        st.audio("voice.mp3")
        except Exception as e:
            st.error(f"Technical Detail: {e}")
            st.info("If you see 404, your API key might be restricted or regional.")
    else:
        st.warning("Please enter key and topic.")
