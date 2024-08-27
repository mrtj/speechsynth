import streamlit as st

from st_auth import check_password

if not check_password():
    st.stop()

from attsila import synthesize

st.title("SpeechSynth")

text = st.text_area("Enter text to synthesize:", height=200)

output_prefix_uri = st.secrets["output_prefix_uri"]

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
    st.markdown(f"[Right-click here and select 'Save As' to download the audio]({public_uri})")
