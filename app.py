import subprocess

import streamlit as st

st.title("Mijn dashboard")
st.write("Welkom op het dashboard!")


@st.fragment(run_every=2)
def show_gpio_17():
    try:
        result = subprocess.run(
            ["pinctrl", "lev", "17"],
            capture_output=True,
            text=True,
            check=True,
            timeout=3,
        )
    except subprocess.CalledProcessError as error:
        details = error.stderr.strip() or error.stdout.strip() or str(error)
        st.error(f"GPIO 17 uitlezen mislukt: {details}")
        return
    except (OSError, subprocess.TimeoutExpired) as error:
        st.error(f"GPIO 17 uitlezen mislukt: {error}")
        return

    level = result.stdout.strip()
    if level not in ("0", "1"):
        st.error(f"Onverwachte uitvoer van pinctrl: {level!r}")
        return

    st.checkbox("GPIO 17 hoog", value=level == "1", disabled=True)


show_gpio_17()
