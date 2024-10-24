pip install streamlit gTTS
import streamlit as st
from gtts import gTTS
import os

def text_to_audio(text, language='en'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=language, slow=False)
    
    # Save the audio file
    filename = "output.mp3"
    tts.save(filename)
    
    return filename

# Streamlit app
def main():
    st.title("Text to Speech Converter")
    
    text = st.text_area("Enter text to convert to audio:")
    
    if st.button("Convert to Audio"):
        if text:
            filename = text_to_audio(text)
            st.success("Conversion successful!")
            
            # Provide download link for the audio file
            with open(filename, "rb") as audio_file:
                st.audio(audio_file.read(), format='audio/mp3')
                st.download_button(label="Download Audio", data=audio_file, file_name=filename)
        else:
            st.warning("Please enter some text.")

if __name__ == "__main__":
    main()
