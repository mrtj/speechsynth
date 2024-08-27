import streamlit as st
import boto3

from attsila import synthesize

polly = boto3.client("polly")

st.title("SpeechSynth")

text = st.text_area("Enter text to synthesize:", height=200)

output_prefix_uri = "s3://aws-panorama.janos.experiments.euwest1.neosperience.com/private/attila/tts"


def disable(b):
    st.session_state["synthesizing"] = b

st.session_state.setdefault("synthesizing", False)

if st.button(
    "Synthesize",
    disabled=st.session_state["synthesizing"],
    on_click=disable,
    args=(True,)
):
    with st.spinner("Synthesizing..."):
        st.session_state["public_uri"] = synthesize(output_prefix_uri, text)
    st.session_state["synthesizing"] = False
    st.rerun()

if public_uri := st.session_state.get("public_uri"):
    st.subheader("Audio preview")
    st.audio(public_uri, format="audio/mp3")
    st.markdown(f"[Download the audio with right click -> Save as]({public_uri})")
