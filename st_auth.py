import streamlit as st

def check_password():
    """Returns `True` if the user had the correct password."""

    skip_password = ("skip_password" in st.secrets) and st.secrets["skip_password"] == "true"
    if skip_password:
        return True

    def show_password_input():
        st.markdown("This application is password protected. Enter the password to continue.")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["password"] == st.secrets["password"]:
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store password
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show input for password.
        show_password_input()
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        show_password_input()
        st.error("😕 Password incorrect")
        return False
    else:
        # Password correct.
        return True
