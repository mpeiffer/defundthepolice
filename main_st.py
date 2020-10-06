import streamlit as st
import streamlit_theme as stt

from apps import home, county_compare

PAGES = {
    "Home": home.view,
    "County Compare": county_compare.view,
}


def show_menu():
    st.sidebar.title("Social Media Toolkit Generator")
    st.sidebar.header("Defund the Police")
    dark_theme = st.checkbox('Dark theme')
    if dark_theme:
        show_dark_theme()
    else:
        show_light_theme()

    st.sidebar.markdown(
        "“Defund the police” means reallocating or redirecting funding away from the "
        "police department to other government agencies funded by the local municipality."
    )

    st.sidebar.markdown(
        "The goal of this tool is to highlight how much money local communities spend on "
        "Police, and then how reallocating funds can make a direct impact into their community"
    )

    # TODO add more "apps" such as county compare tool
    selection = st.sidebar.selectbox("Go To", list(PAGES.keys()))
    page = PAGES.get(selection)
    page()

def show_dark_theme():
    stt.set_theme({'primary': '#1b3388'})

def show_light_theme():
    stt.set_theme({'primary': '#e6e6ff'})

def main():
    show_menu()


if __name__ == "__main__":
    main()
