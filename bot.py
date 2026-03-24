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
    "https://cotizaciones.copesco.gob.pe/adquisicion-de-bienes-y-o-servicios-plan-copesco/",
    "https://aplicacionespnsr.vivienda.gob.pe/spsPNSR/consulta",
    "https://www.midagri.gob.pe/portal/contrataciones-menores-a-8-uit",
    "https://cms.pvn.gob.pe:10443/PortalProceso/Forms/frmContratacionMenor8UIT_Ex",
    "https://apps.proviasdes.gob.pe/pvdsgc/publicacionweb?Page_No=88",
    "https://8uit.sunarp.gob.pe/portal/zona-registral/zona-registral-n-x-sede-cusco"
]

# =========================
# 🔹 PALABRAS CLAVE
# =========================
palabras = [
    "topografia",
    "levantamiento topografico",
    "geodesico",
    "catastro",
    "georreferenciacion",
    "Puntos de Control",
    "Orden C",
    "Dibujo cad",
    "Cadista",
    "Fotogrametria",
    "Ortofoto"
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
