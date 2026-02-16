import requests

TITLE_ID = "420D7"
SECRET_KEY = "6SPMIKT5HNPKGAUXQJIBOBN76154JWYJKUP6ZOTAN9EAA3H8KJ"

BASE_URL = f"https://420D7.playfabapi.com"

HEADERS = {
    "Content-Type": "application/json",
    "X-SecretKey": SECRET_KEY
}

def call(endpoint, payload=None):
    try:
        r = requests.post(
            f"{BASE_URL}/{endpoint}",
            headers=HEADERS,
            json=payload or {}
        )
        return r.json()
    except Exception as e:
        return {"error": str(e)}
