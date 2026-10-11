import streamlit as st
import whisper
import tempfile
import os

st.set_page_config(page_title="SpeakToNotes", page_icon="🎙️")
st.title("🎙️ SpeakToNotes: Multilingual Meeting Intelligence")
st.caption("Upload meeting audio to transcribe or translate using OpenAI Whisper.")

uploaded_file = st.file_uploader("Upload Audio (.mp3, .wav, .m4a)", type=["mp3", "wav", "m4a"])

col1, col2 = st.columns(2)
with col1:
    model_choice = st.selectbox("Select Model Tier", ["tiny", "base", "small"])
with col2:
    task_choice = st.selectbox("Task", ["transcribe", "translate"])

language_choice = st.selectbox("Spoken Language", ["Auto-detect", "English", "Telugu", "Hindi"])

lang_map = {"Auto-detect": None, "English": "en", "Telugu": "te", "Hindi": "hi"}

if uploaded_file and st.button("Process Audio", type="primary"):
    with st.spinner(f"Loading Whisper '{model_choice}' model and running audio..."):
        with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
            tmp.write(uploaded_file.read())
            tmp_path = tmp.name

        model = whisper.load_model(model_choice)
        options = {"task": task_choice}
        if lang_map[language_choice]:
            options["language"] = lang_map[language_choice]

        result = model.transcribe(tmp_path, **options)
        os.remove(tmp_path)

        st.success("Completed!")
        st.subheader("Result")
        st.text_area("Transcript / Translation", result["text"], height=250)