import requests

# =========================
# 🔹 CONFIG TELEGRAM
# =========================
TOKEN = "8398040301:AAFPIPrqxcHiju4g5_qYR9r51GAIOSQGpiY"
CHAT_ID = "6971298078"

# =========================
# 🔹 URLS
# =========================
urls = [
    "https://prod6.seace.gob.pe/buscador-publico/contrataciones",
    "https://www.ima.org.pe/adquisiciones-bienes-servicios-v3/s---.html",
    "https://cotizaciones.copesco.gob.pe/adquisicion-de-bienes-y-o-servicios-plan-copesco/"
]

# =========================
# 🔹 PALABRAS CLAVE
# =========================
palabras = [
    "topografia",
    "levantamiento topografico",
    "geodesico",
    "catastro",
    "georreferenciacion"
]

# =========================
# 🔹 TELEGRAM
# =========================
def enviar(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": texto})

# =========================
# 🔹 BOT (UNA SOLA EJECUCIÓN)
# =========================
print("🔍 Buscando cotizaciones...")

encontrado = False

for url in urls:
    try:
        r = requests.get(url, timeout=10)
        contenido = r.text.lower()

        for palabra in palabras:
            if palabra in contenido:
                enviar(f"⚠ Posible cotización encontrada\n{palabra}\n{url}")
                encontrado = True

    except Exception as e:
        print(f"Error en {url}: {e}")

if not encontrado:
    enviar("✅ Bot activo, sin cotizaciones nuevas")

print("✅ Fin del proceso")
