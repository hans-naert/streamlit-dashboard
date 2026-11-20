# Streamlit-dashboard

Maak een virtuele omgeving aan en installeer de afhankelijkheden:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Sluit de TC74 aan op de I²C-pinnen van de Raspberry Pi en schakel I²C in via
`sudo raspi-config` onder **Interface Options > I2C**. De app gebruikt I²C-bus 1
en sensoradres `0x48`, zoals in [tc74-python](https://github.com/hans-naert/tc74-python).
Pas deze instellingen in `app.py` aan als jouw sensor een ander adres gebruikt.
De temperatuur wordt elke 2 seconden vernieuwd.

Start het dashboard:

```bash
streamlit run app.py --server.headless true --server.address 0.0.0.0 --server.port 8501
```

Open `http://<ip-adres-van-de-pi>:8501` op een apparaat in hetzelfde netwerk.
Stel poort 8501 niet zonder beveiliging bloot aan het internet.
