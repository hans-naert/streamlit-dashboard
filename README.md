# Streamlit-dashboard

Maak een virtuele omgeving aan en installeer de afhankelijkheden:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

Start het dashboard:

```bash
streamlit run app.py --server.headless true --server.address 0.0.0.0 --server.port 8501
```

Open `http://<ip-adres-van-de-pi>:8501` op een apparaat in hetzelfde netwerk.
Stel poort 8501 niet zonder beveiliging bloot aan het internet.
