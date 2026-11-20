# Streamlit-dashboard

Maak een virtuele omgeving aan en installeer de afhankelijkheden:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Het dashboard toont het niveau van GPIO 17 en vernieuwt dit elke 2 seconden.
Het gebruikt hiervoor `pinctrl`, dat op de Raspberry Pi beschikbaar moet zijn.
De gebruiker die het dashboard start, heeft toegang tot `/dev/gpiomem` nodig
(bijvoorbeeld via de groep `gpio`). De checkbox geeft alleen de toestand weer;
de pin wordt niet aangestuurd.

Start het dashboard:

```bash
streamlit run app.py --server.headless true --server.address 0.0.0.0 --server.port 8501
```

Open `http://<ip-adres-van-de-pi>:8501` op een apparaat in hetzelfde netwerk.
Stel poort 8501 niet zonder beveiliging bloot aan het internet.
