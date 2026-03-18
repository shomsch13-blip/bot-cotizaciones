import requests
import time

TOKEN = "8398040301:AAFPIPrqxcHiju4g5_qYR9r51GAIOSQGpiY"
CHAT_ID = "6971298078"

urls = [
"https://prod6.seace.gob.pe/buscador-publico/contrataciones",
"https://www.ima.org.pe/adquisiciones-bienes-servicios-v3/s---.html",
"https://prod6.seace.gob.pe/buscador-publico/contrataciones",
"https://cotizaciones.copesco.gob.pe/adquisicion-de-bienes-y-o-servicios-plan-copesco/",
"https://www.sutran.gob.pe/contrataciones-de-bienes-y-servicios/",
"https://cms.pvn.gob.pe:10443/PortalProceso/Forms/frmContratacionMenor8UIT_Ex",
"https://aplicacionespnsr.vivienda.gob.pe/spsPNSR/consulta",
"https://8uit.sunarp.gob.pe/portal",
"https://www.midagri.gob.pe/portal/contrataciones-menores-a-8-uit",
"https://www.senamhi.gob.pe/main.php?dp=arequipa&p=contrataciones-8uit",
"https://www.autodema.gob.pe/peims-autodema-promueve-transparencia-en-contrataciones-de-bienes-y-servicios/",
"https://apps.sangaban.com.pe/sgcotizaciones/cotizaciones-vigentes",
"https://www.senamhi.gob.pe/main.php?dp=puno&p=contrataciones-8uit",
"https://prod6.seace.gob.pe/buscador-publico/contrataciones",
"https://www.gob.pe/busquedas?contenido[]=publicacion",

# MADRE DE DIOS
"https://www.gob.pe/munitambopata",
"https://www.gob.pe/munimanumadrededios",
"https://www.gob.pe/munitahuamanu",
"https://www.gob.pe/regionmadrededios",

# CUSCO
"https://www.gob.pe/municusco",
"https://www.gob.pe/municanchis",
"https://www.gob.pe/muniquispicanchi",
"https://www.gob.pe/muniurubamba",
"https://www.gob.pe/municalca",
"https://www.gob.pe/muniantapaccay",
"https://www.gob.pe/muniespinar",
"https://www.gob.pe/munipaucartambo",
"https://www.gob.pe/regioncusco",

# PUNO
"https://www.gob.pe/munipuno",
"https://www.gob.pe/munisanroman",
"https://www.gob.pe/muniazangaro",
"https://www.gob.pe/munimelgar",
"https://www.gob.pe/muniyunguyo",
"https://www.gob.pe/munichucuito",
"https://www.gob.pe/munilampa",
"https://www.gob.pe/regionpuno",

# APURÍMAC
"https://www.gob.pe/muniabancay",
"https://www.gob.pe/muniandahuaylas",
"https://www.gob.pe/munichincheros",
"https://www.gob.pe/munigrau",
"https://www.gob.pe/muniantabamba",
"https://www.gob.pe/regionapurimac",

# AREQUIPA
"https://www.gob.pe/muniarequipa",
"https://www.gob.pe/municamanaa",
"https://www.gob.pe/municaraveli",
"https://www.gob.pe/municastilla",
"https://www.gob.pe/municaylloma",
"https://www.gob.pe/muniislaya",
"https://www.gob.pe/regionarequipa",

# MOQUEGUA
"https://www.gob.pe/munimoquegua",
"https://www.gob.pe/muniilo",
"https://www.gob.pe/munisanchezcerro",
"https://www.gob.pe/regionmoquegua",

# TACNA
"https://www.gob.pe/munitacna",
"https://www.gob.pe/munijorgebasadre",
"https://www.gob.pe/munitarata",
"https://www.gob.pe/municandarave",
"https://www.gob.pe/regiontacna",

# EXTRA
"https://www.gob.pe/contrataciones",
"https://www.gob.pe/instituciones",
"https://www.peru.gob.pe"
]

palabras = [
"topografia",
"levantamiento topografico",
"geodesico",
"catastro",
"georreferenciacion",
"puntos geodesicos",
"colocacion de puntos"
]

enviados = set()

def enviar(texto):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    requests.post(url, data={"chat_id": CHAT_ID, "text": texto})

def buscar():
    for url in urls:
        try:
            r = requests.get(url, timeout=10)
            contenido = r.text.lower()

            for palabra in palabras:
                if palabra in contenido:
                    
                    clave = f"{palabra}-{url}"

                    if clave not in enviados:
                        mensaje = f"🚨 NUEVA POSIBLE COTIZACIÓN\n\n🔎 {palabra}\n🌐 {url}"
                        enviar(mensaje)
                        enviados.add(clave)

        except:
            pass

# 🔁 LOOP AUTOMÁTICO
while True:
    print("Buscando cotizaciones...")
    buscar()
    
    time.sleep(28800)  # ⏰ cada 8 horas