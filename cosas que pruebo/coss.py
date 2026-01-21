import requests
from urllib.parse import unquote

def obtener_precio_steam(appid, nombre_item):
    url = f"https://steamcommunity.com/market/priceoverview/?country=US&currency=1&appid={appid}&market_hash_name={nombre_item}"
    response = requests.get(url)
    data = response.json()

    if data.get("success") and data.get("lowest_price"):
        precio_str = data["lowest_price"].replace("$", "").replace(",", "").strip()
        try:
            return float(precio_str)
        except:
            return None
    return None

# Entradas
link = input("🔗 Pegá el link del ítem de Steam: ")
nombre_encoded = link.strip().split("/")[-1]
item = unquote(nombre_encoded)
appid = 730  # CS2

precio_objetivo = float(input("💰 ¿A qué precio querés que te avise? (USD): "))

precio_actual = obtener_precio_steam(appid, item)
6
if precio_actual is not None:
    print(f"💰 Precio actual de '{item}': ${precio_actual:.2f} USD")

    if precio_actual <= precio_objetivo:
        print("🚨 ¡El precio bajó! Podés comprarlo ahora.")
    else:
        print("🔕 Todavía está caro. Esperá un poco más.")
else:
    print("❌ No se pudo obtener el precio.")
