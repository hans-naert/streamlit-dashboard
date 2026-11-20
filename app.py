import streamlit as st
from smbus2 import SMBus

TEMPERATURE_REGISTER = 0x00
I2C_BUS = 1
TC74_ADDRESS = 0x48

st.title("Mijn dashboard")
st.write("Welkom op het dashboard!")


@st.fragment(run_every=2)
def show_temperature():
    try:
        with SMBus(I2C_BUS) as bus:
            value = bus.read_byte_data(TC74_ADDRESS, TEMPERATURE_REGISTER)
        temperature = value - 256 if value >= 128 else value
        st.metric("TC74-temperatuur", f"{temperature} °C")
    except OSError as error:
        st.error(f"TC74 uitlezen mislukt: {error}")


show_temperature()
