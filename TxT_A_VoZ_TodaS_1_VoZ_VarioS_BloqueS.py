# Programa Creado Por M8AX Para Pasar Texto A Voz, Imitando Cualquier WAV Usado, Para La Clonación De Voz.
# ( Puedes Grabar Un WAV Con Tu Voz Y El Fichero Final Generado En Formato OPUS, Imitará Tu Voz Diciendo El Texto Del Fichero M8AX.TXT ).
# Se Usarán Todas Las Muestras WAV Disponibles En M8AX-Voces.
# Al Final Se Generará Una Gráfica Con Métricas Y Estadísticas Varias.
# También Se Puede Generar Un Vídeo MP4 Con Subtítulos Integrados Automáticamente, Narrador Activo En El Vídeo ON - OFF Y Vumetros Varios.
# Los Subtítulos Se Incrustarán Directamente En El Vídeo Final MP4.
# El Vídeo De Fondo Será Seleccionado Aleatoriamente Desde La Carpeta "M8AX-Vídeo_Subtítulos".
# Los Subtítulos En Formato SRT Siempre Se Generarán Automáticamente, Incluso Aunque No Se Cree El Vídeo MP4.
# El Fichero SRT Generado Será Compatible Con YouTube, VLC, FFmpeg, Editores De Vídeo Y Otros Programas Externos.
# Puedes Utilizar El Fichero SRT Para Crear Tus Propios Vídeos, Añadir Efectos, Editar Subtítulos O Hacer Montajes Personalizados.
# El Audio Final, Con O Sin Música De Fondo, Se Generará En Formato OPUS Optimizado Con FFmpeg, Reduciendo Muchísimo El Tamaño Del WAV Original.
# Compatible Tanto Con CPU Como Con GPU CUDA.
# Incluye Métricas Avanzadas, Estadísticas Técnicas, Gráficas PRO, Detección De Posibles Glitches Y Monitorización Del Sistema.
# Durante Todo El Proceso Se Generará Automáticamente El Fichero De Log "M8AX-LoG-XTTS.log".
# El Log Se Guardará En Tiempo Real En Disco Duro Usando Modo APPEND, Conservando Procesos Anteriores.
# El Fichero De Log Nunca Se Borrará Automáticamente Y Puede Crecer Muchísimo Con El Tiempo.
# Si El Fichero "M8AX-LoG-XTTS.log" Ocupa Demasiado Espacio, Tendrás Que Borrarlo Manualmente.
# Formato De Salida Del Fichero OPUS ➤ M8AX_DD-MM-YYYY_HH-MM-SS_NombreFondo.opus.
# Formato De Salida Del Fichero MP4 ➤ M8AX_DD-MM-YYYY_HH-MM-SS_NombreFondo_NombreVídeo.mp4.
# Si El Vídeo Final Supera El Límite Configurado En SEGUNDOS_SEGMENTO, El MP4 Se Dividirá Automáticamente En Varias Partes.
# Formato Multipartes MP4 ➤ M8AX_DD-MM-YYYY_HH-MM-SS_NombreFondo_NombreVídeo_Parte_XXX.mp4.
# Cuando Existan Varias Partes, Se Generará Automáticamente Una Playlist M3U Compatible Con VLC, Media Player, MPC-HC, PotPlayer Y Otros Reproductores.
# Formato De La Playlist Multipartes M3U ➤ M8AX_DD-MM-YYYY_HH-MM-SS_NombreFondo_NombreVídeo_PlayList.m3u.
# Actualmente SEGUNDOS_SEGMENTO Está Configurado A 41400 Segundos ( 11h 30m ) Para Poder Subir Las Partes A YouTube Sin Acercarse Al Límite Máximo De 12 Horas Por Vídeo.
# Formato De Salida Del Fichero SRT ➤ M8AX_Subtitulos_DD-MM-YYYY_HH-MM-SS.srt.
# Formato De Salida Del Fichero De Gráficas ➤ M8AX_Gráficas_DD-MM-YYYY_HH-MM-SS.webp.
# Formato Del Fichero De Log Permanente ➤ M8AX-LoG-XTTS.log.
# Formato Temporal De Bloques WAV ➤ MvIiIaX_Bloque_XXXXXX.wav.
# Fichero Temporal De Debug De Bloques ➤ M8AX-Bloques_Debug.TxT.
# Contiene Todos Los Bloques Generados Con Su Número, Longitud Y Texto Completo.
# Se Genera Automáticamente Si DEBUG = True.
# Al Final Del Script Se Te Preguntará Si Quieres Borrarlo O Conservarlo.
# Formato Temporal Del WAV De Unión Final ➤ m8ax.wav.
# Integración Con Telegram ➤ Envío Automático De Estadísticas Por Bloque Y Resumen Final En Audio XTTS.
# Fichero Temporal WAV De Estadísticas Para Telegram ➤ M8AX_Final.wav.
# Contiene El Audio Con El Resumen Final De Estadísticas Generado Por XTTS.
# Se Convierte A OPUS Y Se Envía A Tu Telegram Al Final Del Proceso.
# Se Elimina Automáticamente Al Final Del Script.
# Fichero Temporal OPUS De Estadísticas Para Telegram ➤ M8AX_Final.opus.
# Versión Comprimida En OPUS Del Audio De Estadísticas Finales.
# Se Envía Directamente A Tu Telegram Como Mensaje De Audio.
# Se Elimina Automáticamente Al Final Del Script.
# Script Temporal Filter Complex De FFmpeg ➤ M8AX_Filtro_Complejo.TxT.
# Contiene Todo El Pipeline Visual Del Vídeo Final MP4.
# Incluye Subtítulos, HUDs, Narradores Dinámicos, Logos, QRs Dinámicos, Vumetros Y Efectos Visuales.
# Se Genera Automáticamente Y Se Elimina Al Final Del Script.
# HUD Y Narrador Realtime Via ZeroMQ ➤ Sin Ficheros En Disco, Sin Bloqueos, Sin reload=1 En FFmpeg.
# QRs Pregenerados Como Vídeo ➤ M8AX-QRs/M8AX_QR_Final.mp4 ( Generado Durante El Proceso XTTS En Paralelo ).
# Cada QR Dura Lo Que Dura Su Bloque + La Pausa Posterior, Manteniendo El FadeOut Y Cuadrando Con El OPUS Final.
# Compatible Con AudioLibros De Cualquier Tamaño Sin Saturar El Filter Complex.
# El Vídeo QR Final Se Elimina Automáticamente Al Terminar El Script.
# Mensaje Animado De Suscripción ➤ Texto Aleatorio Entre 15 Mensajes En Los Primeros Bloques Del Vídeo.

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creado El 01/06/2026 A Las 00:00:00 En 115h De Programación.
# By M8AX.
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

from datetime import datetime, timedelta
from TTS.api import TTS
from PIL import Image
from PIL import ImageDraw
import soundfile as _sf
import re as _re
import numpy as _np
import subprocess
import warnings
import statistics
import logging
import qrcode
import bisect
import cpuinfo
import requests
import contextlib
import msvcrt
import threading
import torch
import wave
import random
import psutil
import shutil
import ephem
import time
import sys
import zmq
import os

def telegram_m8ax(mensaje):
    try:
        requests.post(
            f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage",
            data={
                "chat_id": CHAT_ID_TELEGRAM,
                "text": mensaje,
            },
            timeout=10,
        )
    except:
        pass

def tamano_m8ax(fichero):
    size = os.path.getsize(fichero) / (1024 * 1024)

    if size >= 500:
        return f"{size / 1024:.2f} GB"
    else:
        return f"{size:.2f} MB"

def fuego_m8ax():
    os.system("cls" if os.name == "nt" else "clear")
    ancho = 110
    alto = 32
    texto = "M 8 A X     X T T S     E N G I N E   -   T O D A S  1  V O Z  V A R I O S  B L O Q U E S"

    colores = [
        "\033[38;2;20;20;20m",
        "\033[38;2;120;0;0m",
        "\033[38;2;180;30;0m",
        "\033[38;2;255;80;0m",
        "\033[38;2;255;140;0m",
        "\033[38;2;255;220;40m",
        "\033[38;2;255;255;255m",
    ]

    reset = "\033[0m"
    fuego = [[0 for _ in range(ancho)] for _ in range(alto)]
    chars = " .:-=+*#%@"
    ejecutando = True

    while ejecutando:

        for x in range(ancho):
            fuego[alto - 1][x] = random.randint(3, 6)

        for y in range(alto - 1):

            for x in range(ancho):
                abajo = fuego[y + 1][x]
                izquierda = fuego[y + 1][x - 1] if x > 0 else abajo
                derecha = fuego[y + 1][x + 1] if x < ancho - 1 else abajo
                valor = int((abajo + izquierda + derecha) / 3)

                if valor > 0 and random.random() > 0.45:
                    valor -= 1

                fuego[y][x] = max(0, valor)

        salida = []

        for y in range(alto):
            linea = ""

            for x in range(ancho):
                valor = fuego[y][x]
                idx_char = min(len(chars) - 1, valor + random.randint(0, 2))
                char = chars[idx_char]
                color = colores[min(valor, len(colores) - 1)]
                linea += f"{color}{char}{reset}"

            salida.append(linea)

        y_texto = alto // 2
        x_texto = (ancho // 2) - (len(texto) // 2)
        limpio = "".join(
            [chars[min(len(chars) - 1, fuego[y_texto][x] + 1)] for x in range(ancho)]
        )
        limpio = list(limpio)

        for i, c in enumerate(texto):

            if 0 <= x_texto + i < len(limpio):
                limpio[x_texto + i] = f"\033[38;2;255;255;255m{c}{reset}"

        salida[y_texto] = "".join(limpio)

        print("\033[H", end="")
        print("\n".join(salida))
        print(
            f"\n\033[38;2;255;180;0m>>> Pulsa Cualquier Tecla Para Continuar <<<\033[0m"
        )

        time.sleep(0.045)

        if msvcrt.kbhit():
            msvcrt.getch()
            ejecutando = False

    os.system("cls" if os.name == "nt" else "clear")

def tiempo_srt(segundos):
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segundos_rest = int(segundos % 60)
    milisegundos = int((segundos % 1) * 1000)

    return f"{horas:02d}:{minutos:02d}:{segundos_rest:02d},{milisegundos:03d}"

def fecha_espanol():

    dias = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo",
    ]

    meses = [
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre",
    ]

    ahora = datetime.now()

    dia = dias[ahora.weekday()]
    mes = meses[ahora.month - 1]

    return f"{dia}, {ahora.day:02d} De {mes} De {ahora.year} ➤ {ahora.strftime('%H:%M:%S')}"

def generar_graficas_pro(
    duraciones,
    duraciones_audio,
    chars_por_bloque,
    voces_usadas,
    rtf,
    pausas,
):
    try:
        import matplotlib.pyplot as plt
        import numpy as np
    except ImportError:
        print("\n- MatPlotLib O Numpy No Están Instalados, Se Omiten Gráficas\n")
        return

    if not duraciones or not duraciones_audio or not chars_por_bloque:
        print("\n- Datos Insuficientes Para Generar Gráficas\n")
        return

    n = min(len(duraciones), len(duraciones_audio), len(chars_por_bloque))
    n_original = n
    duraciones = duraciones[:n]
    duraciones_audio = duraciones_audio[:n]
    chars_por_bloque = chars_por_bloque[:n]
    bloques = np.arange(1, n + 1)

    vel_gen = np.array(
        [c / d if d > 0 else 0 for c, d in zip(chars_por_bloque, duraciones)]
    )

    vel_audio = np.array(
        [c / d if d > 0 else 0 for c, d in zip(chars_por_bloque, duraciones_audio)]
    )

    media_vel_audio = np.mean(vel_audio)
    dur_audio = np.array(duraciones_audio)

    def suavizar(data, ventana=7):

        if len(data) < ventana:
            return data

        kernel = np.ones(ventana) / ventana
        pad = ventana // 2
        data_pad = np.pad(data, (pad, pad), mode="edge")
        return np.convolve(data_pad, kernel, mode="valid")

    vel_gen_s = suavizar(vel_gen)
    dur_audio_s = suavizar(dur_audio)
    media_vel_gen = np.mean(vel_gen)

    media_dur_audio = (
        (np.sum(dur_audio) + sum(pausas)) / len(dur_audio) if len(dur_audio) > 0 else 0
    )

    duracion_total = np.sum(dur_audio) + sum(pausas)
    MAX_TICKS = 25

    if duracion_total < 300:
        intervalo = max(5, duracion_total / MAX_TICKS)
    else:
        intervalo = max(60, duracion_total / MAX_TICKS)

    ticks_tiempo = np.arange(0, duracion_total + 1, intervalo)

    ticks_bloques = np.linspace(1, n, len(ticks_tiempo)).round().astype(int)

    def tiempo_eje(seg):
        h = int(seg // 3600)
        m = int((seg % 3600) // 60)
        s = int(seg % 60)

        if h > 0:
            return f"{h:02d}h {m:02d}m"
        elif m > 0:
            return f"{m:02d}m {s:02d}s"
        else:
            return f"{s:02d}s"

    def detectar_outliers(data):

        return np.array([i for i, v in enumerate(data) if v < 0.2 or v > 20], dtype=int)

    dur_audio_completo = np.array(duraciones_audio)
    out_audio_completo = detectar_outliers(dur_audio_completo)

    MAX_PUNTOS = 3000

    if n > MAX_PUNTOS:
        idx = np.linspace(0, n - 1, MAX_PUNTOS).astype(int)
        bloques = bloques[idx]
        vel_gen_s = vel_gen_s[idx]
        dur_audio_s = dur_audio_s[idx]
        dur_audio = dur_audio[idx]

    ticks_bloques = np.unique(ticks_bloques)

    ticks_bloques = ticks_bloques[
        (ticks_bloques >= bloques.min()) & (ticks_bloques <= bloques.max())
    ]

    ticks_tiempo = np.linspace(0, duracion_total, len(ticks_bloques))

    if n > MAX_PUNTOS:
        idx_set = set(idx.tolist())
        idx_map = {v: k for k, v in enumerate(idx)}
        out_audio = np.array(
            [idx_map[i] for i in out_audio_completo if i in idx_set], dtype=int
        )
    else:
        out_audio = out_audio_completo

    plt.style.use("dark_background")
    fig, axs = plt.subplots(4, 1, figsize=(19.2, 10.8))

    for ax in axs:
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)

    fig.patch.set_facecolor("#0d1117")

    axs[0].plot(bloques, vel_gen_s, linewidth=1)
    axs[0].axhline(np.mean(vel_gen), linestyle="--", alpha=0.5)

    axs[0].set_title(
        "Velocidad De Generación ( Caract / Seg )",
        color="#ffd166",
    )

    axs[0].set_xlabel("Número De Bloque\nTiempo Real Del Audiolibro")
    axs[0].set_xticks(ticks_bloques)

    axs[0].set_xticklabels(
        [f"{b}\n{tiempo_eje(t)}" for b, t in zip(ticks_bloques, ticks_tiempo)],
        rotation=25,
        fontsize=8,
    )

    axs[0].set_ylabel("Caract / Seg")
    axs[0].grid(True, alpha=0.2)

    chars_s = suavizar(np.array(chars_por_bloque))

    if n > MAX_PUNTOS:
        chars_s = chars_s[idx]

    axs[1].plot(bloques, chars_s, linewidth=1)

    axs[1].axhline(
        np.mean(chars_por_bloque),
        linestyle="--",
        alpha=0.5,
    )

    axs[1].set_title(
        "Cantidad De Caracteres Por Bloque",
        color="#ffd166",
    )

    axs[1].set_xlabel("Número De Bloque")
    axs[1].set_ylabel("Caracteres")
    axs[1].grid(True, alpha=0.2)

    axs[2].plot(bloques, dur_audio_s, linewidth=1)
    axs[2].axhline(media_dur_audio, linestyle="--", alpha=0.5)

    if len(out_audio) > 0:
        axs[2].scatter(bloques[out_audio], dur_audio[out_audio], s=10)

    axs[2].set_title(
        "Duración De Audio Por Bloque ( Seg )",
        color="#ffd166",
    )

    axs[2].set_xlabel("Número De Bloque")
    axs[2].set_ylabel("Segundos")
    axs[2].grid(True, alpha=0.2)

    for ax in axs[:3]:
        ax.margins(x=0.02)

    if n <= 20:
        axs[0].set_xticks(bloques)
        axs[1].set_xticks(bloques)
        axs[2].set_xticks(bloques)

    axs[3].hist(
        duraciones_audio,
        bins=min(30, max(5, len(duraciones_audio) // 2)),
        color=(random.uniform(0.4, 1), random.uniform(0.4, 1), random.uniform(0.4, 1)),
    )

    axs[3].set_title(
        "Distribución De Duraciones De Audio",
        color="#ffd166",
    )

    axs[3].set_xlabel("Duración Del Audio ( Segundos )")
    axs[3].set_ylabel("Bloques Por Rango")
    axs[3].yaxis.get_major_locator().set_params(integer=True)
    axs[3].grid(True, alpha=0.2)

    resumen = (
        f"Bloques Totales ➤ {n_original} | Voces Distintas ➤ {len(voces_usadas)} | Bloques Sospechosos ➤ {len(out_audio_completo)}\n"
        f"RTF ➤ {rtf:.2f}x ( Velocidad Real De Generación ) | Vel.Gen Media ➤ {media_vel_gen:.2f} Caract / Seg\n"
        f"Vel.Habla Media ➤ {media_vel_audio:.2f} Caract / Seg | Dur.Audio Media ➤ {media_dur_audio:.3f} Seg / Bloque"
        f"\nHardware Usado ➤ {device_nombre} | Gráfica ➤ {'Completa' if n_original <= 3000 else f'Submuestreada ( {3000} Puntos De {n_original} )'}"
    )

    plt.figtext(0.5, 0.02, resumen, ha="center", fontsize=9)
    plt.tight_layout(rect=[0, 0.06, 1, 1])

    plt.figtext(
        0.995,
        0.01,
        f"M8AX © XTTS Engine - {datetime.now().year}",
        ha="right",
        va="bottom",
        fontsize=15,
        alpha=0.7,
    )

    nombre = f"M8AX_Gráficas_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.webp"

    plt.savefig(nombre, dpi=200, format="webp", pil_kwargs={"quality": 95, "method": 6})

    plt.close()

    print(f"- Gráficas PRO Generadas ➤ {nombre}\n")

    return nombre

def aviso(inicio):
    contador = 0

    while not stop_event.is_set():
        contador += 1
        r = random.randint(100, 255)
        g = random.randint(100, 255)
        b = random.randint(100, 255)
        color = f"\033[38;2;{r};{g};{b}m"
        reset = "\033[0m"

        if contador % 2 == 0:
            ahora = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            transcurrido = time.time() - inicio
            d = int(transcurrido // 86400)
            h = int((transcurrido % 86400) // 3600)
            m = int((transcurrido % 3600) // 60)
            s = int(transcurrido % 60)

            if d > 0:
                tiempo = f"{d:02d}d {h:02d}h {m:02d}m {s:02d}s"
            else:
                tiempo = f"{h:02d}h {m:02d}m {s:02d}s"

            print(
                f"\n{color}M8AX ... ESPERA ... Generando Audio Por Partes ... {ahora} ... Tiempo Procesando ➤ {tiempo} ... Puede Tardar Bastante Según CPU O GPU ... M8AX{reset}\n",
                flush=True,
            )
        else:
            print(
                f"\n{color}M8AX ... ESPERA ... Generando Audio Por Partes ... Usando Todas Las Muestras WAV Disponibles ... Puede Tardar Bastante Según CPU O GPU ... M8AX{reset}\n",
                flush=True,
            )

        stop_event.wait(10)

def dividir_texto(texto, max_chars=220, min_chars=80, hard_limit=235):
    texto = texto.replace("«", '"').replace("»", '"')
    texto = texto.replace("\r\n", "\n").replace("\r", "\n")
    lineas = texto.split("\n")
    bloques = []

    for linea in lineas:

        linea = linea.strip()

        if not linea:
            continue

        while len(linea) > max_chars:
            bloque = None
            sub = linea[:max_chars]
            sub_ext = linea[:hard_limit]

            corte_base = max(
                sub.rfind("."),
                sub.rfind("!"),
                sub.rfind("?"),
                sub.rfind(";"),
                sub.rfind(":"),
            )

            corte_ext = max(
                sub_ext.rfind("."),
                sub_ext.rfind("!"),
                sub_ext.rfind("?"),
                sub_ext.rfind(";"),
                sub_ext.rfind(":"),
            )

            if corte_ext == -1:
                corte_ext = sub_ext.rfind(" ")

            if corte_ext > corte_base and corte_ext != -1:
                corte = corte_ext
            elif corte_base >= min_chars:
                corte = corte_base
            else:
                corte_alt = sub.rfind(" ")

                if corte_alt != -1:
                    corte = corte_alt
                    bloque = linea[:corte].rstrip() + ";"
                else:
                    corte = max_chars - 1
                    bloque = linea[: corte + 1].strip()

            if bloque is None:

                if linea[corte] == " ":
                    bloque = linea[:corte].rstrip() + ";"
                else:
                    bloque = linea[: corte + 1].strip()

            if bloque:
                bloques.append(bloque)

            linea = linea[corte + 1 :].lstrip()

        if linea:
            bloques.append(linea)

    return bloques

def formatear_tiempo_completo(segundos):
    d = int(segundos // 86400)
    h = int((segundos % 86400) // 3600)
    m = int((segundos % 3600) // 60)
    s = int(segundos % 60)

    return f"{d:02d}d:{h:02d}h:{m:02d}m:{s:02d}s"

def formatear_tiempo(segundos):
    d = int(segundos // 86400)
    h = int((segundos % 86400) // 3600)
    m = int((segundos % 3600) // 60)
    s = int(segundos % 60)

    if d > 0:
        return f"{d:02d}d:{h:02d}h:{m:02d}m:{s:02d}s"
    else:
        return f"{h:02d}h:{m:02d}m:{s:02d}s"

def generar_qr_transparente(texto, salida, color=(255, 255, 255)):

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=6,
        border=1,
    )

    qr.add_data(texto)

    qr.make(fit=True)

    img = qr.make_image(fill_color="white", back_color="black").convert("RGBA")

    datos = img.get_flattened_data()

    nuevos = []

    for item in datos:

        if item[:3] == (0, 0, 0):

            nuevos.append((0, 0, 0, 0))

        else:

            nuevos.append((color[0], color[1], color[2], 255))

    img.putdata(nuevos)

    draw = ImageDraw.Draw(img)
    grosor = 3
    draw.rectangle(
        [0, 0, img.width - 1, img.height - 1],
        outline=(color[0], color[1], color[2], 255),
        width=grosor,
    )

    img.save(salida)

logging.basicConfig(level=logging.DEBUG)
logging.getLogger("TTS").setLevel(logging.DEBUG)
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("PIL").setLevel(logging.WARNING)
warnings.filterwarnings("ignore", module="PIL")
warnings.filterwarnings("ignore", message=".*getdata is deprecated.*")

LENGUAJE = "es"

stop_event = threading.Event()

os.system("cls" if os.name == "nt" else "clear")

print("... Cargando M8AX XTTS | Creador De AudioLibros ...")

time.sleep(2)

fuego_m8ax()

os.system("cls" if os.name == "nt" else "clear")

shutil.rmtree("M8AX-WAVs", ignore_errors=True)
shutil.rmtree("M8AX-QRs", ignore_errors=True)

os.makedirs("M8AX-WAVs", exist_ok=True)
os.makedirs("M8AX-QRs", exist_ok=True)

if not os.path.exists("m8ax.txt"):
    print(
        "❌ Error ➤ El Archivo 'm8ax.txt' No Se Encuentra En El Directorio Raíz Del Proyecto. 'm8ax.txt' Es El Texto Que Quieres Pasar A Voz..."
    )
    print(
        "👉 Asegúrate De Que El Archivo 'm8ax.txt' Esté En El Directorio Raíz Donde Se Ejecuta El Script."
    )
    exit()

if not shutil.which("ffmpeg"):
    print("❌ Error ➤ FFmpeg No Está Instalado O No Está En PATH")
    print("👉 Instálalo Y Añádelo Al PATH Antes De Continuar...")
    exit()

if not shutil.which("ffprobe"):
    print("❌ Error ➤ FFprobe No Está Instalado O No Está En PATH")
    print("👉 Instálalo Y Añádelo Al PATH Antes De Continuar...")
    exit()

os.environ["TTS_HOME"] = r"C:\Utilidades-Pc\M8AX-IA\M8AX-TTS-M8AX\M8AX_TTS_Models"

TOKEN_TELEGRAM = "PON AQUÍ TUS CREDENCIALES"
CHAT_ID_TELEGRAM = "PON AQUÍ TUS CREDENCIALES"
INTERVALO_TELEGRAM = 3600

print(
    "========================== M8AX TTS ENGINE CON XTTS v2 ==========================\n"
)

LOG_M8AX_TEMP = "M8AX-LoG-XTTS.log"

if os.path.exists(LOG_M8AX_TEMP):
    tam_log = os.path.getsize(LOG_M8AX_TEMP) / (1024 * 1024)

    if tam_log >= 10:
        print(
            f"----- El Fichero De Log Permanente ➤ {LOG_M8AX_TEMP} Ocupa Ya {tam_log:.2f} MB -----\n"
        )
        print("1. ➤ Borrar El Fichero De Log Y Empezar Limpio\n")
        print("2. ➤ Conservar El Fichero De Log Y Seguir Acumulando Datos\n")
        print("----- Selecciona Opción ----- ", end="")

        opcion_log = input().strip()

        if opcion_log == "1":
            try:
                os.remove(LOG_M8AX_TEMP)
                print(
                    f"\n---/// Fichero De Log Eliminado Correctamente ➤ {LOG_M8AX_TEMP} \\\\\\---\n\n--------------------------------------------------------------------------------\n"
                )
            except Exception as e:
                print(
                    f"\n---/// Error Al Borrar El Fichero De Log ➤ {e} \\\\\\---\n\n--------------------------------------------------------------------------------\n"
                )
        else:
            print(
                "\n---/// El Fichero De Log Se Mantendrá Y Seguirá Creciendo... \\\\\\---\n\n--------------------------------------------------------------------------------\n"
            )

print("----- ¿ Quieres Usar CPU O GPU ? -----\n")
print("1. ➤ Usa La CPU\n")
print("2. ➤ Usa La GPU\n")

opcion = input("----- Selecciona Opción ----- ").strip()

if opcion == "2":
    if torch.cuda.is_available():
        device = "cuda"
        device_nombre = f"GPU - {torch.cuda.get_device_name(0)}"
    else:
        print("\n❌ Error ➤ No Tienes GPU Compatible Con CUDA... Lo Siento :(")
        exit()
elif opcion == "1":
    device = "cpu"
    device_nombre = f"CPU - {cpuinfo.get_cpu_info()['brand_raw']}"
else:
    print("\n⚠️ Opción Inválida, Usando La CPU Por Defecto...")
    device = "cpu"
    device_nombre = f"CPU - {cpuinfo.get_cpu_info()['brand_raw']}"

device_nombre_corto = "GPU" if device == "cuda" else "CPU"

device_nombre_ffmpeg = " ".join(
    device_nombre.replace("(R)", "")
    .replace("(TM)", "")
    .replace("\\", " ")
    .replace(":", " ")
    .replace("%", " ")
    .replace("'", " ")
    .replace('"', " ")
    .replace(",", " ")
    .replace("[", " ")
    .replace("]", " ")
    .replace(";", " ")
    .replace("@", " ")
    .replace("|", " ")
    .replace("=", " ")
    .replace("(", " ")
    .replace(")", " ")
    .replace("{", " ")
    .replace("}", " ")
    .replace("➤", " ")
    .split()
)

print(
    f"\n---/// Usando ➤ {device_nombre} \\\\\\---\n\n--------------------------------------------------------------------------------\n"
)

titulocmd = f"M8AX XTTS ENGINE v2 ➤ {device_nombre}"

os.system(f"title {titulocmd}")

print("----- ¿ Quieres Música De Fondo ? -----\n")
print("1. ➤ Sí\n")
print("2. ➤ No\n")

opcion_musica = input("----- Selecciona Opción ----- ").strip()
usar_musica = opcion_musica == "1"
ruta_musica = None

if usar_musica:
    num = random.randint(1, 16)
    ruta_musica = os.path.join("M8AX-Música_Fondo", f"MúsicaFondo{num}.mp3")
    print(
        f"\n---/// Música Seleccionada ➤ {os.path.basename(ruta_musica)} \\\\\\---\n\n--------------------------------------------------------------------------------\n"
    )
    if not os.path.exists(ruta_musica):
        print(f"❌ Error ➤ No Se Encuentra La Música ➤ {ruta_musica}")
        print(
            "👉 Asegúrate De Que Existan Ficheros MP3 En La Carpeta M8AX-Música_Fondo"
        )
        exit()
else:
    print(
        f"\n---/// Sin Música De Fondo \\\\\\---\n\n--------------------------------------------------------------------------------\n"
    )

print("----- ¿ Quieres Generar Un Vídeo MP4 Con La Voz Y Subtítulos ? -----\n")
print("1. ➤ Sí\n")
print("2. ➤ No\n")

opcion_video = input("----- Selecciona Opción ----- ").strip()

usar_video = opcion_video == "1"

if usar_video:
    print(
        "\n---/// Se Generará Un Vídeo MP4 Con Subtítulos Integrados \\\\\\---\n\n--------------------------------------------------------------------------------\n"
    )
    print(
        "----- ¿ Quieres Mostrar El Narrador En El Vídeo Cuando Cambie La Voz ? -----\n"
    )
    print("1. ➤ Sí\n")
    print("2. ➤ No\n")

    opcion_narrador = input("----- Selecciona Opción ----- ").strip()
    mostrar_narrador = opcion_narrador == "1"

    if mostrar_narrador:
        print(
            f"\n---/// El Vídeo Se Generará Con Identificación Del Narrador \\\\\\---\n\n--------------------------------------------------------------------------------"
        )
    else:
        print(
            f"\n---/// El Vídeo Se Generará Sin Identificación Del Narrador \\\\\\---\n\n--------------------------------------------------------------------------------"
        )

    print("\n----- ¿ Quieres Mostrar Un Vumetro En El Vídeo ? -----\n")
    print("1. ➤ Sí\n")
    print("2. ➤ No\n")

    opcion_vumeter = input("----- Selecciona Opción ----- ").strip()
    mostrar_vumeter = opcion_vumeter == "1"

    if mostrar_vumeter:
        print(
            "\n---/// El Vídeo Se Generará Con Vumetro \\\\\\---\n\n--------------------------------------------------------------------------------"
        )
    else:
        print(
            "\n---/// El Vídeo Se Generará Sin Vumetro \\\\\\---\n\n--------------------------------------------------------------------------------"
        )

    print("\n----- ¿ Quieres Mostrar QRs Dinámicos En El Vídeo ? -----\n")
    print("1. ➤ Sí\n")
    print("2. ➤ No\n")

    opcion_qr = input("----- Selecciona Opción ----- ").strip()

    usar_qr = opcion_qr == "1"

    if usar_qr:
        print(
            "\n---/// El Vídeo Se Generará Con QR Dinámicos Por Bloque \\\\\\---\n\n-------------------------------A R R A N C A N D O------------------------------"
        )
    else:
        print(
            "\n---/// El Vídeo Se Generará Sin QR Dinámicos \\\\\\---\n\n-------------------------------A R R A N C A N D O------------------------------"
        )
else:
    mostrar_narrador = False
    mostrar_vumeter = False
    usar_qr = False
    print("\n---/// No Se Generará Vídeo MP4 \\\\\\---")

time.sleep(5)
os.system("cls" if os.name == "nt" else "clear")

VOCES = [
    "m8ax-voces/Aitana_Ocaña.wav",
    "m8ax-voces/Alberto_Mieza.wav",
    "m8ax-voces/Ana_Mena.wav",
    "m8ax-voces/Ana_Olivares.wav",
    "m8ax-voces/Ariana_Grande.wav",
    "m8ax-voces/Azucena.wav",
    "m8ax-voces/Carles_Porta.wav",
    "m8ax-voces/Carmelo_Eleven.wav",
    "m8ax-voces/Chiquito.wav",
    "m8ax-voces/Clara_Lago.wav",
    "m8ax-voces/Claudio_Serrano.wav",
    "m8ax-voces/Constantino_R1.wav",
    "m8ax-voces/Constantino_R2.wav",
    "m8ax-voces/Constantino_R3.wav",
    "m8ax-voces/CortoCircuito.wav",
    "m8ax-voces/Cristina_Segui.wav",
    "m8ax-voces/Dani_Garcia.wav",
    "m8ax-voces/David_Robles.wav",
    "m8ax-voces/Donald_Trump.wav",
    "m8ax-voces/Dr_Sbaitso.wav",
    "m8ax-voces/Emilia_Mernes.wav",
    "m8ax-voces/Eva_Isanta.wav",
    "m8ax-voces/Felipe_Gonzalez.wav",
    "m8ax-voces/Gloria_Serra.wav",
    "m8ax-voces/Gollum.wav",
    "m8ax-voces/Hal9000.wav",
    "m8ax-voces/Hector_Cantolla.wav",
    "m8ax-voces/Iker_Jimenez.wav",
    "m8ax-voces/Irene_Escolar.wav",
    "m8ax-voces/Irene_Montero.wav",
    "m8ax-voces/Joel_Mulachs.wav",
    "m8ax-voces/Jordi_Boixaderas.wav",
    "m8ax-voces/Jordi_Brau.wav",
    "m8ax-voces/Jose_Coronado.wav",
    "m8ax-voces/Jose_Maria_Del_Rio.wav",
    "m8ax-voces/Jose_Miguel_Villarroya.wav",
    "m8ax-voces/Jose_Sacristan.wav",
    "m8ax-voces/Juan_Antonio_Bernal.wav",
    "m8ax-voces/Juan_Carlos_Gustems.wav",
    "m8ax-voces/Juan_Carlos-I.wav",
    "m8ax-voces/Luis_Posada.wav",
    "m8ax-voces/M8AX_Robot.wav",
    "m8ax-voces/Maestro_Yoda.wav",
    "m8ax-voces/Mama.wav",
    "m8ax-voces/Marcos_Ochoa.wav",
    "m8ax-voces/Marcos_Ochoa_Voz_Pito.wav",
    "m8ax-voces/Marcos_Ochoa_Voz_Tonto.wav",
    "m8ax-voces/Maria_Luisa_Sola1.wav",
    "m8ax-voces/Maria_Luisa_Sola2.wav",
    "m8ax-voces/Mariano_Rajoy.wav",
    "m8ax-voces/Maribel_Verdu.wav",
    "m8ax-voces/Martin_Osborne.wav",
    "m8ax-voces/Matias_Prats.wav",
    "m8ax-voces/Mercedes_Montala1.wav",
    "m8ax-voces/Mercedes_Montala2.wav",
    "m8ax-voces/Michelle_Jenner.wav",
    "m8ax-voces/Miguel_Angel_Jenner.wav",
    "m8ax-voces/Miguel_Eleven.wav",
    "m8ax-voces/MvIiIaX-1.wav",
    "m8ax-voces/MvIiIaX-2.wav",
    "m8ax-voces/MvIiIaX-3.wav",
    "m8ax-voces/MvIiIaX-4.wav",
    "m8ax-voces/MvIiIaX-5.wav",
    "m8ax-voces/Nuria_Mediavilla.wav",
    "m8ax-voces/Nuria_Trifol.wav",
    "m8ax-voces/Optimus_Prime.wav",
    "m8ax-voces/Pablo_Iglesias.wav",
    "m8ax-voces/Pedro_Sanchez1.wav",
    "m8ax-voces/Pedro_Sanchez2.wav",
    "m8ax-voces/Princesa_Leonor.wav",
    "m8ax-voces/Ramon_Langa.wav",
    "m8ax-voces/Raul_Llorens.wav",
    "m8ax-voces/Ricardo_Solans1.wav",
    "m8ax-voces/Ricardo_Solans2.wav",
    "m8ax-voces/Robocop.wav",
    "m8ax-voces/Ruben_Gisbert.wav",
    "m8ax-voces/Santiago_Segura_Torrente.wav",
    "m8ax-voces/Sara_Heras.wav",
    "m8ax-voces/Sara_Martin_Eleven.wav",
    "m8ax-voces/Sara_Vivas.wav",
    "m8ax-voces/Sheldon_Cooper.wav",
    "m8ax-voces/Teresa_Baro.wav",
    "m8ax-voces/Victor_Endrino.wav",
    "m8ax-voces/Virginia_Maestro.wav",
    "m8ax-voces/Voz_Universo.wav",
]

for wav in VOCES:
    if not os.path.exists(wav):
        print(f"❌ Error ➤ No Se Encuentra El WAV De Voz ➤ {wav}")
        print("👉 Asegúrate De Que El Fichero WAV Esté En La Carpeta m8ax-voces")
        exit()

TXT_ENTRADA = "m8ax.txt"
SALIDA_WAV = "m8ax.wav"

class Tee:

    def fileno(self):
        return self.terminal.fileno()

    def __init__(self, archivo):
        self.terminal = sys.stdout
        self.log = open(archivo, "a", encoding="utf-8", buffering=1)
        self.ultima_ffmpeg = ""

    def write(self, mensaje):
        self.terminal.write(mensaje)

        if "M8AX ... ESPERA ..." in mensaje:
            return

        limpio = mensaje

        while "\033[" in limpio:
            ini = limpio.find("\033[")
            fin = limpio.find("m", ini)

            if fin == -1:
                break

            limpio = limpio[:ini] + limpio[fin + 1 :]

        limpio = limpio.replace("\r", "")

        if "frame=" in limpio or "size=" in limpio:
            self.ultima_ffmpeg = limpio.strip()
            return

        self.log.write(limpio)
        self.log.flush()

    def flush(self):
        self.terminal.flush()
        self.log.flush()

    def guardar_ffmpeg_final(self):

        if self.ultima_ffmpeg:
            self.log.write(self.ultima_ffmpeg.strip())
            self.log.flush()
            self.ultima_ffmpeg = ""

sys.stdout = Tee("M8AX-LoG-XTTS.log")
sys.stderr = sys.stdout

print(f"{'-'*175}\n")

print(
    f"--- Cargando Modelo XTTS En RAM, Usando {device_nombre} ➤ ( Programado Por MarcoS OchoA DieZ - MvIiIaX.M8AX ) ---\n"
)

print(f"{'-'*175}\n")

tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(device)

print(f"\n{'-'*175}")
print(f"\n- Leyendo Texto Desde ➤ {TXT_ENTRADA}\n")

try:
    with open(TXT_ENTRADA, "r", encoding="utf-8-sig") as f:
        texto = f.read()
except:
    try:
        with open(TXT_ENTRADA, "r", encoding="utf-8") as f:
            texto = f.read()
    except:
        try:
            with open(TXT_ENTRADA, "r", encoding="cp1252") as f:
                texto = f.read()
        except:
            with open(TXT_ENTRADA, "r", encoding="latin-1", errors="replace") as f:
                texto = f.read()

print(f"- Generando Audio Con Muestra(s) ➤ {', '.join(VOCES)}\n")
print(f"- Usando {len(VOCES)} Muestra(s) De Voz\n")

texto = texto.strip()

if not texto:
    texto = (
        "El fichero de texto está vacío... "
        "Haz el favor de ponerme un texto en condiciones."
    )

if texto.strip().upper().rstrip(".!?").endswith("FIN"):
    texto += (
        f" del audiolibro por Eme viax, guión, Eme ocho a equis. "
        f"Procesado usando {device_nombre_ffmpeg}. "
        "En honor a EMEDEDEDEDE. Mi Madre."
    )
else:
    texto += (
        f"\n\nFin del audiolibro por Eme viax, guión, Eme ocho a equis. "
        f"Procesado usando {device_nombre_ffmpeg}. "
        "En honor a EMEDEDEDEDE. Mi Madre."
    )

bloques = dividir_texto(texto)
total_bloques = len(bloques)

DEBUG = True

if DEBUG:
    with open("M8AX-Bloques_Debug.TxT", "w", encoding="utf-8") as f:

        for i, b in enumerate(bloques, 1):
            f.write(f"--- BLOQUE {i:06d} ---\n")
            f.write(f"Longitud: {len(b)} Caracteres\n")
            f.write(b + "\n\n")

    print(
        "- Bloques Guardados En M8AX-Bloques_Debug.TxT Para Análisis. Al Terminar El Script Python, Se Te Preguntará Si Quieres Borrar El Fichero O No...\n"
    )

print(f"- Texto Dividido En {total_bloques} Bloques")

inicio = time.time()
inicio2 = inicio
luna_inicio = ephem.Moon()
luna_inicio.compute()
fecha_luna_inicio = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
momento_inicio_luna = ephem.now()
edad_luna_inicio = momento_inicio_luna - ephem.previous_new_moon(momento_inicio_luna)
distancia_inicio_km = luna_inicio.earth_distance * 149597870.7

t = threading.Thread(target=aviso, args=(inicio,), daemon=True)
t.start()

duraciones = []
duraciones_audio = []
archivos = []
chars_por_bloque = []
pausas = [random.uniform(0.015, 0.035) for _ in range(total_bloques - 1)]
voces_disponibles = VOCES.copy()
random.shuffle(voces_disponibles)
ultima_voz = None
voces_usadas = []
conteo_voces = []
tiempo_por_bloque = []
voz_actual = None
bloques_restantes_con_voz = 0
timeline = 0
psutil.cpu_percent(interval=None)
bloques_fallidos = []
luna = ephem.Moon()
bloques_sospechosos_total = 0
tam_wavs_total = 0
subtitulos_srt = []
qr_por_bloque = []
encoder_video = "N/A"
encoder_qr = "N/A"
partes_mp4 = []
SEGMENTAR_MP4 = False
SALIDA_MP4 = ""
EFECTO_VIDEO = "N/A"
visualizador = "N/A"
qr_video_final = os.path.join("M8AX-QRs", "M8AX_QR_Final.mp4")
chars_totales_actual = 0
ultimo_telegram = time.time()

if usar_qr:
    encoders_qr = [
        ("hevc_nvenc", ["-preset", "p5"]),
        ("h264_nvenc", ["-preset", "p5"]),
        ("hevc_qsv", ["-preset", "fast"]),
        ("h264_qsv", ["-preset", "fast"]),
        ("hevc_amf", ["-quality", "balanced"]),
        ("libx265", ["-preset", "medium"]),
    ]
    encoder_qr = "libx264"
    for enc, args in encoders_qr:
        test_cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-f",
            "lavfi",
            "-i",
            "testsrc=size=1280x720:rate=30",
            "-t",
            "1",
            "-c:v",
            enc,
            "-f",
            "null",
            "-",
        ]
        test = subprocess.run(test_cmd, capture_output=True, text=True)
        if test.returncode == 0:
            encoder_qr = enc
            break

m8ax_qr_desfase_acumulado = 0.0

for i, bloque in enumerate(bloques, 1):

    inicio_bloque = time.time()

    if bloques_restantes_con_voz <= 0:
        bloque_anterior = bloques[i - 2].rstrip() if i >= 2 else ""
        fin_frase = bloque_anterior.endswith(".") and not bloque_anterior.endswith(
            "..."
        )

        if not fin_frase and i >= 2:
            pass

        else:
            if not voces_disponibles:
                voces_disponibles = VOCES.copy()
                random.shuffle(voces_disponibles)

            if ultima_voz and voces_disponibles[0] == ultima_voz:

                for j in range(len(voces_disponibles)):

                    if voces_disponibles[j] != ultima_voz:
                        voces_disponibles[0], voces_disponibles[j] = (
                            voces_disponibles[j],
                            voces_disponibles[0],
                        )
                        break

            voz_actual = voces_disponibles.pop(0)
            ultima_voz = voz_actual
            min_bloques = random.randint(5, 8)
            max_bloques = random.randint(min_bloques + 1, 20)
            bloques_restantes_con_voz = random.randint(min_bloques, max_bloques)

    bloques_restantes_con_voz -= 1

    if voz_actual is None:
        voz_actual = voces_disponibles[0] if voces_disponibles else VOCES[0]

    nombre = os.path.basename(voz_actual)

    if nombre not in voces_usadas:
        voces_usadas.append(nombre)

    nombre_salida = os.path.join("M8AX-WAVs", f"MvIiIaX_Bloque_{i:06d}.wav")

    print(
        f"⬤ ⬤ ⬤ - | | |  B L O Q U E  ➤  {i:06d}  D E  {total_bloques:06d}  | | | - ⬤ ⬤ ⬤\n",
        flush=True,
    )

    idioma_bloque = LENGUAJE

    if i == total_bloques:

        idioma_bloque = "es"

    try:
        tts.tts_to_file(
            text=bloque,
            speaker_wav=voz_actual,
            language=idioma_bloque,
            file_path=nombre_salida,
            split_sentences=False,
        )

        fin_bloque = time.time()

    except Exception as e:
        print(f"\n- Error En Bloque {i:06d} ➤ {e}\n\n")

        if i not in bloques_fallidos:
            bloques_fallidos.append(i)

        continue

    if not os.path.exists(nombre_salida):
        print(f"\n- Error Generando {nombre_salida}\n\n")

        if i not in bloques_fallidos:
            bloques_fallidos.append(i)

        continue

    chars = len(bloque)
    chars_por_bloque.append(chars)
    conteo_voces.append(nombre)
    archivos.append(nombre_salida)

    with wave.open(nombre_salida, "rb") as w:
        frames = w.getnframes()
        rate = w.getframerate()
        duracion_audio = frames / float(rate)
        duraciones_audio.append(duracion_audio)
        tiempo_por_bloque.append(duracion_audio)

    inicio_real = timeline
    fin_real = inicio_real + duracion_audio
    subtitulos_srt.append((i, inicio_real, fin_real, bloque.strip()))

    if usar_qr:

        texto_qr = (
            f"[ Bloque {i} De {total_bloques} ]\n\n"
            + (
                (
                    "Fin Del Audiolibro Por MvIiIaX-M8AX. "
                    f"Procesado Usando {device_nombre_ffmpeg}. "
                    "En Honor A MDDD. Mi Madre."
                )
                if i == total_bloques
                else bloque.strip()
            )
            + "\n\nSi Te Apetece Apoyar El Canal..."
            + "\n\nPayPal ➤ https://www.paypal.com/paypalme/m8ax"
            + "\n\nTarjeta ➤ https://buy.stripe.com/eVq8wPdnI2ewggLaaIbEA01"
        )

        r_qr = random.randint(150, 255)
        g_qr = random.randint(150, 255)
        b_qr = random.randint(150, 255)

        qr_path = os.path.join("M8AX-QRs", f"MvIiIaX_QR_{i:06d}.png")

        generar_qr_transparente(
            texto=texto_qr, salida=qr_path, color=(r_qr, g_qr, b_qr)
        )

        duracion_qr = duracion_audio

        if i - 1 < len(pausas):
            duracion_qr += round(rate * pausas[i - 1]) / rate

        duracion_qr_raw = round(duracion_qr * 30) / 30

        error = duracion_qr_raw - duracion_qr

        m8ax_qr_desfase_acumulado += error

        if m8ax_qr_desfase_acumulado >= (1 / 30):
            duracion_qr_raw -= 1 / 30
            m8ax_qr_desfase_acumulado -= 1 / 30

        elif m8ax_qr_desfase_acumulado <= -(1 / 30):
            duracion_qr_raw += 1 / 30
            m8ax_qr_desfase_acumulado += 1 / 30

        duracion_qr = duracion_qr_raw

        fade_start_qr = max(0, duracion_qr - 0.5)
        qr_clip_path = os.path.join("M8AX-QRs", f"MvIiIaX_QR_{i:06d}.mp4")

        cmd_qr_clip = [
            "ffmpeg",
            "-loop",
            "1",
            "-r",
            "30",
            "-i",
            qr_path,
            "-t",
            str(duracion_qr),
            "-vf",
            f"scale=200:200:flags=neighbor,fade=t=out:st={fade_start_qr:.3f}:d=0.5",
            "-c:v",
            encoder_qr,
            "-pix_fmt",
            "yuv420p",
            "-r",
            "30",
            "-an",
            "-y",
            qr_clip_path,
        ]

        for intento in range(300):

            try:

                subprocess.run(
                    cmd_qr_clip,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=120,
                    check=True,
                )

                break

            except Exception as e:

                print(
                    f"- Error Generando QR Vídeo Del Bloque "
                    f"{i:06d} | Intento {intento + 1} / 300\n"
                )

                time.sleep(5)

        else:

            raise RuntimeError(f"\n- No Se Pudo Generar El QR Vídeo Del Bloque {i:06d}")

        qr_por_bloque.append(
            {
                "path": qr_path,
                "inicio": inicio_real,
                "fin": fin_real,
                "bloque": i,
            }
        )

    timeline = fin_real

    if i - 1 < len(pausas):
        timeline += pausas[i - 1]

    duracion_bloque = fin_bloque - inicio_bloque
    rtf_bloque = duracion_bloque / duracion_audio if duracion_audio > 0 else 0
    duraciones.append(duracion_bloque)
    progreso = (i / total_bloques) * 100
    tiempo_transcurrido = time.time() - inicio
    bloques_procesados = len(archivos)
    throughput = bloques_procesados / tiempo_transcurrido
    restantes = total_bloques - i
    eta = restantes / throughput if throughput > 0 else 0
    fin_estimado = datetime.now() + timedelta(seconds=eta)
    velocidad = chars / duracion_audio if duracion_audio > 0 else 0
    velocidad_gen_bloque = chars / duracion_bloque if duracion_bloque > 0 else 0
    kmh_proceso = velocidad_gen_bloque * 0.002 * 3600 / 1000
    cpu_cores = psutil.cpu_percent(percpu=True)
    cpu_avg = sum(cpu_cores) / len(cpu_cores)
    core_max = max(cpu_cores)
    cores_str = " | ".join(f"{c:.1f}%" for c in cpu_cores)
    ram = psutil.virtual_memory()
    ram_usada = ram.used / (1024**3)
    ram_total = ram.total / (1024**3)
    ram_pct = ram.percent
    fecha_bloque = fecha_espanol()
    total_barra = 60
    relleno = int((progreso / 100) * total_barra)
    restante_pct = 100 - progreso
    barra = "◼" * relleno + "◻" * (total_barra - relleno)
    luna.compute()
    edad_luna = ephem.now() - ephem.previous_new_moon(ephem.now())
    distancia_km = luna.earth_distance * 149597870.7

    if device == "cuda":
        vram_usada = torch.cuda.memory_allocated() / (1024**3)
        vram_total = torch.cuda.get_device_properties(0).total_memory / (1024**3)
        vram_texto = (
            f"\033[38;2;255;100;255m > VRAM ➤ "
            f"{vram_usada:.2f} GB / {vram_total:.2f} GB\033[0m\n"
        )
    else:
        vram_texto = ""

    audio_total_actual = timeline
    tam_wav_actual = os.path.getsize(nombre_salida) / (1024 * 1024)
    tam_wavs_total += tam_wav_actual
    chars_totales_actual += chars

    if duracion_audio < 0.2 or duracion_audio > 20:
        bloques_sospechosos_total += 1
        estado_bloque = "⚠️ POSIBLE GLITCH"
    else:
        estado_bloque = "✅ OK"

    print(
        f"\n{'-'*175}\n\n"
        f"\033[38;2;120;190;255m > • • • • • • • • • •  {fecha_bloque} | Luna Visible ➤ {luna.phase:.2f}% | Edad Lunar ➤ {edad_luna:.1f} Días | Distancia A La Luna ➤ {distancia_km:,.0f} KM • • • • • • • • • • \033[0m\n\n"
        f"\033[38;2;255;255;255m > PR ➤ {restante_pct:06.2f}% | {barra} | PC ➤ {progreso:06.2f}%\033[0m\n"
        f"\033[38;2;255;0;255m > Bloque ➤ [ {i:06d} / {total_bloques:06d} ] | Progreso ➤ {progreso:.2f}% | ETA ➤ {formatear_tiempo(eta)} | Fin Previsto ➤ {fin_estimado.strftime('%d-%m-%Y A Las %H:%M:%S')}\033[0m\n"
        + (
            f"\033[38;2;255;200;0m > Código QR ➤ Generado Correctamente Para El Bloque {i:06d}\033[0m\n"
            if usar_qr
            else ""
        )
        + f"\033[38;2;0;255;255m > Tiempo De Proceso Del Bloque ➤ {duracion_bloque:.2f} Segs | Tiempo Necesario Para Generar 1 Seg De Audio ➤ {rtf_bloque:.2f} Segs\n"
        f"\033[38;2;255;80;80m > Estado Del Bloque ➤ {estado_bloque}\033[0m\n"
        f"\033[38;2;255;120;120m > Bloques Sospechosos Detectados ➤ {bloques_sospechosos_total}\033[0m\n"
        f"\033[38;2;180;90;255m > Bloques Por Segundo ➤ {(len(archivos) / (time.time() - inicio) if (time.time() - inicio) > 0 else 0):.5f}\033[0m\n"
        f"\033[38;2;0;255;180m > Bloques Por Minuto ➤ {(len(archivos) / (time.time() - inicio) * 60 if (time.time() - inicio) > 0 else 0):.2f}\033[0m\n"
        f"\033[38;2;255;90;180m > Bloques Por Hora ➤ {(len(archivos) / (time.time() - inicio) * 3600 if (time.time() - inicio) > 0 else 0):.2f}\033[0m\n"
        f"\033[38;2;120;255;40m > Bloques Por Semana ➤ {(len(archivos) / (time.time() - inicio) * 604800 if (time.time() - inicio) > 0 else 0):.2f}\033[0m\n"
        f"\033[38;2;0;255;120m > Voz ➤ {os.path.basename(voz_actual)}\033[0m\n"
        f"\033[38;2;255;180;0m > Audio Total Generado ➤ {formatear_tiempo(audio_total_actual)}\033[0m\n"
        f"\033[38;2;255;120;255m > WAV Actual ➤ {tam_wav_actual:.2f} MB | WAVS Totales ➤ {tam_wavs_total:.2f} MB\033[0m\n"
        f"\033[38;2;255;255;0m > Caracteres ➤ {chars} | Duración ➤ {duracion_audio:.2f} Segs\033[0m\n"
        f"\033[38;2;120;255;120m > Caracteres Totales Procesados ➤ {chars_totales_actual:,}\033[0m\n"
        f"\033[38;2;255;50;50m > Velocidad De Habla ➤ {velocidad:.2f} Caract / Seg | Velocidad De Generación ➤ {velocidad_gen_bloque:.2f} Caract / Seg | Velocidad De Generación Km/h ➤ {kmh_proceso:.4f} Km/h\033[0m\n"
        f"\033[38;2;0;200;255m > Inicio ➤ {formatear_tiempo(inicio_real)} | Fin ➤ {formatear_tiempo(fin_real)}\033[0m\n"
        f"\033[38;2;140;220;255m > Hardware ➤ {device_nombre}\033[0m\n"
        f"\033[38;2;0;120;255m > Cores ➤ [{cores_str}]\033[0m\n"
        f"\033[38;2;255;140;0m > CPU ( Avg ) ➤ {cpu_avg:.1f}% | Core ( Máx ) ➤ {core_max:.1f}% | RAM ➤ {ram_usada:.2f} GB / {ram_total:.2f} GB ➤ ( {ram_pct:.2f}% )\033[0m\n"
        f"{vram_texto}"
        f"\033[38;2;0;170;0m > Fichero Generado ➤ {nombre_salida}\033[0m\n\n"
        f"{'-'*175}\n",
        flush=True,
    )

    if (
        (time.time() - ultimo_telegram >= INTERVALO_TELEGRAM) or i == total_bloques
    ) and (
        TOKEN_TELEGRAM != "PON AQUÍ TUS CREDENCIALES"
        and CHAT_ID_TELEGRAM != "PON AQUÍ TUS CREDENCIALES"
    ):

        print("- Enviando Mensaje A Tu Telegram Con Estadísticas Del Bloque\n")

        telegram_m8ax(
            f"{fecha_bloque}\n"
            f"Luna Visible ➤ {luna.phase:.2f}%\n"
            f"Edad Lunar ➤ {edad_luna:.1f} Días\n"
            f"Distancia A La Luna ➤ {distancia_km:,.0f} KM\n\n"
            f"Texto Del Bloque ➤\n"
            f'"{bloque}"\n\n'
            f"P.Res ➤ {restante_pct:.2f}%\n"
            f"P.Com ➤ {progreso:.2f}%\n\n"
            f"Bloque ➤ [ {i:06d} / {total_bloques:06d} ]\n"
            + (f"Código QR ➤ Correcto Para El Bloque {i:06d}\n" if usar_qr else "")
            + f"ETA ➤ {formatear_tiempo(eta)}\n"
            + f"Fin Previsto ➤ {fin_estimado.strftime('%d-%m-%Y A Las %H:%M:%S')}\n\n"
            f"Tiempo De Proceso Del Bloque ➤ {duracion_bloque:.2f} Segs\n"
            f"RTF ➤ {rtf_bloque:.2f}x\n\n"
            f"Estado ➤ {estado_bloque}\n"
            f"Bloques Sospechosos ➤ {bloques_sospechosos_total}\n"
            f"Bloques Por Segundo ➤ {(len(archivos) / (time.time() - inicio) if (time.time() - inicio) > 0 else 0):.5f}\n"
            f"Bloques Por Minuto ➤ {(len(archivos) / (time.time() - inicio) * 60 if (time.time() - inicio) > 0 else 0):.2f}\n"
            f"Bloques Por Hora ➤ {(len(archivos) / (time.time() - inicio) * 3600 if (time.time() - inicio) > 0 else 0):.2f}\n"
            f"Bloques Por Semana ➤ {(len(archivos) / (time.time() - inicio) * 604800 if (time.time() - inicio) > 0 else 0):.2f}\n\n"
            f"Voz ➤ {os.path.basename(voz_actual)}\n"
            f"Audio Total ➤ {formatear_tiempo(audio_total_actual)}\n\n"
            f"WAV Actual ➤ {tam_wav_actual:.2f} MB\n"
            f"WAVS Totales ➤ {tam_wavs_total:.2f} MB\n\n"
            f"Caracteres ➤ {chars}\n"
            f"Duración Audio ➤ {duracion_audio:.2f} Segs - ( {formatear_tiempo(duracion_audio)} )\n"
            f"Caracteres Totales ➤ {chars_totales_actual:,}\n\n"
            f"Vel.Habla ➤ {velocidad:.2f} Caract / Seg\n"
            f"Vel.Generación ➤ {velocidad_gen_bloque:.2f} Caract / Seg\n"
            f"Vel.Generación Km/h ➤ {kmh_proceso:.4f} Km/h\n\n"
            f"Inicio ➤ {formatear_tiempo(inicio_real)}\n"
            f"Fin ➤ {formatear_tiempo(fin_real)}\n\n"
            f"Hardware ➤ {device_nombre}\n"
            f"CPU Avg ➤ {cpu_avg:.1f}%\n"
            f"Core Máx ➤ {core_max:.1f}%\n"
            f"RAM ➤ {ram_usada:.2f} GB / {ram_total:.2f} GB ({ram_pct:.2f}%)\n\n"
            + (
                f"VRAM ➤ {vram_usada:.2f} GB / {vram_total:.2f} GB\n\n"
                if device == "cuda"
                else ""
            )
            + (f"Fichero ➤ {nombre_salida}\n\n")
        )
        ultimo_telegram = time.time()

stop_event.set()

fin_xtts = time.time()

print("--- Uniendo WAVS ---", flush=True)

pausas = pausas[: len(archivos) - 1]

inicios_hud = [sub[1] for sub in subtitulos_srt]

if not archivos:
    print("\n- No Se Generaron Archivos WAV")
    exit()

with _sf.SoundFile(archivos[0], "r") as _primer:
    _samplerate = _primer.samplerate
    _channels = _primer.channels
    _subtype = _primer.subtype

with _sf.SoundFile(
    SALIDA_WAV,
    "w",
    samplerate=_samplerate,
    channels=_channels,
    subtype=_subtype,
    format="WAV",
) as salida_sf:

    for i, archivo in enumerate(archivos):
        datos, _ = _sf.read(archivo, dtype="int16", always_2d=True)
        salida_sf.write(datos)

        if i < len(archivos) - 1:
            duracion_pausa = pausas[i]
            muestras = round(_samplerate * duracion_pausa)
            silencio = _np.zeros((muestras, _channels), dtype="int16")
            salida_sf.write(silencio)

print(f"\n- Archivo Unido ➤ {SALIDA_WAV}", flush=True)

print(
    "\n--- Convirtiendo De Formato WAV A OPUS, Para Que Ocupe Mucho Menos Espacio ---\n",
    flush=True,
)

tiempo_base_proceso = time.time() - inicio
album_voces = ", ".join(voces_usadas)
fecha_archivo = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
fecha_bonita_opus = fecha_espanol().replace(" ➤ ", " A Las ")

tamano = (
    os.path.getsize(SALIDA_WAV) / (1024 * 1024) if os.path.exists(SALIDA_WAV) else 0
)

if usar_musica:
    nombre_fondo = os.path.splitext(os.path.basename(ruta_musica))[0]
    SALIDA_OPUS = f"M8AX_{fecha_archivo}_{nombre_fondo}.opus"
else:
    SALIDA_OPUS = f"M8AX_{fecha_archivo}_SoloVoz.opus"

if usar_musica:

    cmd = [
        "ffmpeg",
        "-nostdin",
        "-loglevel",
        "error",
        "-stats",
        "-y",
        "-threads",
        "0",
        "-i",
        SALIDA_WAV,
        "-stream_loop",
        "-1",
        "-i",
        ruta_musica,
        "-filter_complex",
        "[0:a]aformat=channel_layouts=mono,pan=stereo|c0=c0|c1=c0[voz];[1:a]volume=0.15[a2];[a2][voz]sidechaincompress=threshold=0.03:ratio=5:attack=40:release=400[a3];[voz][a3]amix=inputs=2:duration=first",
        "-ac",
        "2",
        "-ar",
        "24000",
        "-c:a",
        "libopus",
        "-b:a",
        "48k",
        "-vbr",
        "on",
        "-compression_level",
        "10",
        "-application",
        "audio",
        "-frame_duration",
        "20",
        "-mapping_family",
        "1",
        "-metadata",
        f"title=M8AX - {TXT_ENTRADA} A XTTS - M8AX",
        "-metadata",
        "artist=--- MvIiIaX ---",
        "-metadata",
        f"album={album_voces}",
        "-metadata",
        f"date={fecha_archivo}",
        "-metadata",
        f"comment=Generado Por M8AX Con XTTS | Fecha ➤ {fecha_bonita_opus} | Procesado Automáticamente Usando ➤ {device_nombre} | Tiempo Total De Procesamiento ➤ {formatear_tiempo(tiempo_base_proceso)}",
        "-metadata",
        f"BG_Musical_De_Fondo=Fondo Musical ➤ {os.path.basename(ruta_musica)} | Volumen Base ➤ 0.15 | Reducción Automática ( Ducking ) ➤ Activado | Umbral ➤ 0.03 | Intensidad ➤ 5 | Ataque ➤ 40ms | Recuperación ➤ 400ms | Voz ➤ Mono A Estéreo ( Centrada ) | Mezcla ➤ amix | Duración Final ➤ Igual A La Voz | Música En Bucle ➤ Sí | Formato ➤ Opus 48kbps | Frecuencia ➤ 24kHz | Canales ➤ Estéreo",
        "-metadata",
        "genre=--- M8AX XTTS VoZ ---",
        "-metadata",
        "disc=1",
        "-metadata",
        "track=10031977",
        "-metadata",
        "album_artist=MarcoS OchoA DieZ",
        "-metadata",
        "albumartist=MarcoS OchoA DieZ",
        "-metadata",
        "composer=M8AX - The Algorithm Man - M8AX",
        "-metadata",
        "Lema_M8AX=... Por Muchas Vueltas Que Demos, Siempre Tendremos El Culo Atrás ... | El Futuro No Está Establecido, No Hay Destino... Solo Existe El Que Nosotros Hacemos. | La Fuerza Es Lo Que Le Da Al Jedi Su Poder, Es Un Campo De Energía Formado Por Todas Las Cosas Vivientes, Nos Rodea... Penetra En Nosotros Y Mantiene Unida La Galaxia... | El Miedo Es El Camino Hacia El Lado Oscuro, El Miedo Lleva A La Ira, La Ira Lleva Al Odio, El Odio Lleva Al Sufrimiento... | Yo He Visto Cosas Que Vosotros No Creeríais. Atacar Naves En Llamas Más Allá De Orión. He Visto Rayos-C Brillar En La Oscuridad Cerca De La Puerta De Tannhäuser. Todos Esos Momentos Se Perderán En El Tiempo, Como Lágrimas En La Lluvia. Es Hora De Morir... | AudioLibro Compilado En Honor A MDDD...",
        SALIDA_OPUS,
    ]

else:

    cmd = [
        "ffmpeg",
        "-nostdin",
        "-loglevel",
        "error",
        "-stats",
        "-y",
        "-threads",
        "0",
        "-i",
        SALIDA_WAV,
        "-ac",
        "1",
        "-ar",
        "24000",
        "-c:a",
        "libopus",
        "-b:a",
        "48k",
        "-vbr",
        "on",
        "-compression_level",
        "10",
        "-application",
        "voip",
        "-frame_duration",
        "20",
        "-mapping_family",
        "0",
        "-metadata",
        f"title=M8AX - {TXT_ENTRADA} A XTTS - M8AX",
        "-metadata",
        "artist=--- MvIiIaX ---",
        "-metadata",
        f"album={album_voces}",
        "-metadata",
        f"date={fecha_archivo}",
        "-metadata",
        f"comment=Generado Por M8AX Con XTTS | Fecha ➤ {fecha_bonita_opus} | Procesado Automáticamente Usando ➤ {device_nombre} | Tiempo Total De Procesamiento ➤ {formatear_tiempo(tiempo_base_proceso)}",
        "-metadata",
        f"BG_Musical_De_Fondo=No Hay Música De Fondo | Canales ➤ Mono | Opus 48kbps",
        "-metadata",
        "genre=--- M8AX XTTS VoZ ---",
        "-metadata",
        "disc=1",
        "-metadata",
        "track=10031977",
        "-metadata",
        "album_artist=MarcoS OchoA DieZ",
        "-metadata",
        "albumartist=MarcoS OchoA DieZ",
        "-metadata",
        "composer=M8AX - The Algorithm Man - M8AX",
        "-metadata",
        "Lema_M8AX=... Por Muchas Vueltas Que Demos, Siempre Tendremos El Culo Atrás ... | El Futuro No Está Establecido, No Hay Destino... Solo Existe El Que Nosotros Hacemos. | La Fuerza Es Lo Que Le Da Al Jedi Su Poder, Es Un Campo De Energía Formado Por Todas Las Cosas Vivientes, Nos Rodea... Penetra En Nosotros Y Mantiene Unida La Galaxia... | El Miedo Es El Camino Hacia El Lado Oscuro, El Miedo Lleva A La Ira, La Ira Lleva Al Odio, El Odio Lleva Al Sufrimiento... | Yo He Visto Cosas Que Vosotros No Creeríais. Atacar Naves En Llamas Más Allá De Orión. He Visto Rayos-C Brillar En La Oscuridad Cerca De La Puerta De Tannhäuser. Todos Esos Momentos Se Perderán En El Tiempo, Como Lágrimas En La Lluvia. Es Hora De Morir... | AudioLibro Compilado En Honor A MDDD...",
        SALIDA_OPUS,
    ]

res = subprocess.Popen(
    cmd,
    stderr=subprocess.PIPE,
    stdout=subprocess.DEVNULL,
    text=True,
    bufsize=1,
)

ultima_linea_ffmpeg = ""

while True:
    linea = res.stderr.readline()

    if not linea:
        break

    if "frame=" in linea or "size=" in linea:
        ultima_linea_ffmpeg = linea.strip()
        print(f"\r{ultima_linea_ffmpeg}", end="", flush=True)
    else:
        print(linea, end="", flush=True)

res.wait()
sys.stdout.guardar_ffmpeg_final()

if res.returncode != 0:
    print("\n- Error En FFmpeg, No Se Borrarán Los Ficheros WAV", flush=True)
    exit()

print(f"\n\n- Archivo OPUS Creado ➤ {SALIDA_OPUS}", flush=True)

if not os.path.exists(SALIDA_OPUS):
    print("\n- El Fichero OPUS No Existe, Cancelando Limpieza", flush=True)
    exit()

print("\n--- Limpiando Archivos Temporales ---", flush=True)

wavs_borrados = 0

for archivo in archivos:

    try:
        if os.path.basename(archivo).startswith("MvIiIaX_Bloque_") and archivo.endswith(
            ".wav"
        ):
            os.remove(archivo)
            wavs_borrados += 1

    except Exception as e:
        print(f"\n- Error Al Borrar {archivo} ➤ {e}", flush=True)

print(f"\n- Bloques WAV Eliminados ➤ {wavs_borrados}", flush=True)

try:
    os.remove(SALIDA_WAV)
    print(f"\n- Fichero Eliminado ➤ {SALIDA_WAV}", flush=True)
except Exception as e:
    print(f"\n- Error Al Borrar Fichero ➤ {SALIDA_WAV} ➤ {e}", flush=True)

fin = time.time()
duracion_proceso = fin - inicio
luna_fin = ephem.Moon()
luna_fin.compute()
fecha_luna_fin = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
momento_fin_luna = ephem.now()
edad_luna_fin = momento_fin_luna - ephem.previous_new_moon(momento_fin_luna)
distancia_fin_km = luna_fin.earth_distance * 149597870.7

probe_cmd = [
    "ffprobe",
    "-v",
    "error",
    "-show_entries",
    "format=duration",
    "-of",
    "default=noprint_wrappers=1:nokey=1",
    SALIDA_OPUS,
]

resultado = subprocess.run(probe_cmd, capture_output=True, text=True)

try:
    duracion_opus = float(resultado.stdout.strip())
except:
    duracion_opus = 0

sample_rate = 24000
bitrate = 48
tamano_opus = os.path.getsize(SALIDA_OPUS) / (1024 * 1024)
total_chars = sum(chars_por_bloque)
km_totales_texto = (total_chars * 2) / 1_000_000
velocidad_chars = total_chars / duracion_proceso if duracion_proceso > 0 else 0
comp = ((1 - (tamano_opus / tamano)) * 100) if tamano > 0 else 0
ratio = (tamano / tamano_opus) if tamano_opus > 0 else 0
rtf = duracion_proceso / duracion_opus if duracion_opus > 0 else 0
eficiencia = duracion_opus / duracion_proceso if duracion_proceso > 0 else 0

audio_por_minuto = (
    duracion_opus / (duracion_proceso / 60) if duracion_proceso > 0 else 0
)

tiempo_medio_bloque = sum(duraciones) / len(duraciones) if duraciones else 0
bloques_por_seg = len(archivos) / duracion_proceso if duracion_proceso > 0 else 0
total_pausas = sum(pausas) if pausas else 0

media_audio = (
    (sum(duraciones_audio) + total_pausas) / len(duraciones_audio)
    if duraciones_audio
    else 0
)

bloques_raros = [d for d in duraciones_audio if d < 0.2 or d > 20]
chars_por_seg_audio = total_chars / duracion_opus if duracion_opus > 0 else 0
desviacion = statistics.stdev(duraciones_audio) if len(duraciones_audio) > 1 else 0
media_chars = sum(chars_por_bloque) / len(chars_por_bloque) if chars_por_bloque else 0
max_chars_b = max(chars_por_bloque) if chars_por_bloque else 0
min_chars_b = min(chars_por_bloque) if chars_por_bloque else 0

desviacion_chars = (
    statistics.stdev(chars_por_bloque) if len(chars_por_bloque) > 1 else 0
)

ratio_chars_audio = media_chars / media_audio if media_audio > 0 else 0
max_duracion = max(duraciones_audio) if duraciones_audio else 0
min_duracion = min(duraciones_audio) if duraciones_audio else 0
tiempo_por_1000 = (duracion_proceso / total_chars) * 1000 if total_chars > 0 else 0

porcentaje_sospechosos = (
    (len(bloques_raros) / len(archivos)) * 100 if len(archivos) > 0 else 0
)

porcentaje_fallidos = (
    (len(bloques_fallidos) / total_bloques) * 100 if total_bloques > 0 else 0
)

duracion_xtts_total = sum(duraciones_audio)
rtf_xtts = (fin_xtts - inicio) / duracion_xtts_total if duracion_xtts_total > 0 else 0

print("\n--- MÉTRICAS ---\n")

print(
    f"- Inicio Del Procesamiento ➤ {fecha_luna_inicio} | "
    f"Luna Visible ➤ {luna_inicio.phase:.2f}% | "
    f"Edad Lunar ➤ {edad_luna_inicio:.1f} Días | "
    f"Distancia A La Luna ➤ {distancia_inicio_km:,.0f} KM\n"
)

print(
    f"- Fin Del Procesamiento ➤ {fecha_luna_fin} | "
    f"Luna Visible ➤ {luna_fin.phase:.2f}% | "
    f"Edad Lunar ➤ {edad_luna_fin:.1f} Días | "
    f"Distancia A La Luna ➤ {distancia_fin_km:,.0f} KM\n"
)

print(
    f"- Tiempo Total De Procesamiento ➤ {duracion_proceso:.2f} Segs - ( {formatear_tiempo(duracion_proceso)} )\n"
)

print(
    f"- Real-Time Factor ➤ {rtf:.2f}x - "
    f"( XTTS Necesita {rtf:.2f} Segundos Reales De Procesamiento Para Generar 1 Segundo De Audio )\n"
)

print(
    f"- Real-Time Factor XTTS Puro ➤ {rtf_xtts:.2f}x - "
    f"( Solo Incluye La Generación De Bloques XTTS, Sin FFmpeg Ni Procesos Finales )\n"
)

print(f"- Eficiencia De Generación ➤ {eficiencia:.2f} Segs Audio / Seg\n")

print(
    f"- Rendimiento ➤ {audio_por_minuto:.2f} Segs Audio / Min - ( {formatear_tiempo(audio_por_minuto)} )\n"
)

print(f"- Total Nº Bloques TXT ➤ {total_bloques}\n")
print(f"- Total Nº Bloques Generados ➤ {len(archivos)}\n")
print(f"- Bloques Por Segundo ➤ {bloques_por_seg:.5f}\n")
print(f"- Bloques Por Minuto ➤ {bloques_por_seg * 60:.2f}\n")
print(f"- Bloques Por Hora ➤ {bloques_por_seg * 3600:.2f}\n")
print(f"- Bloques Por Semana ➤ {bloques_por_seg * 604800:.2f}\n")

print(
    f"- Tiempo Medio De Procesado Por Bloque ➤ {tiempo_medio_bloque:.2f} Segs - ( {formatear_tiempo(tiempo_medio_bloque)} )\n"
)

print(
    f"- Duración Media De Cada Bloque De Audio ➤ {media_audio:.3f} Segs - ( {formatear_tiempo(media_audio)} )\n"
)

print(f"- Caracteres Medios Por Bloque ➤ {media_chars:.2f}\n")

print(
    f"- Variabilidad De Caracteres ➤ {desviacion_chars:.2f} - ( Entre {max(0, media_chars - desviacion_chars):.0f} Y {(media_chars + desviacion_chars):.0f} Caracteres )\n"
)

print(f"- Bloque Más Largo ( Texto ) ➤ {max_chars_b} Caracteres\n")
print(f"- Bloque Más Corto ( Texto ) ➤ {min_chars_b} Caracteres\n")

print(
    f"- Variabilidad De Duración ➤ {desviacion:.2f} Segs - "
    f"( {formatear_tiempo(desviacion)} ) - "
    f"( Entre {max(0, media_audio - desviacion):.2f} Y {(media_audio + desviacion):.2f} Segs | "
    f"Bajo < 2 = Fluido | Alto > 5 = Irregular )\n"
)

print(
    f"- Bloque Más Largo ( Duración ) ➤ {max_duracion:.2f} Segs - "
    f"( {formatear_tiempo(max_duracion)} ) - "
    f"( Puede Indicar Frases Demasiado Largas )\n"
)

print(
    f"- Bloque Más Corto ( Duración ) ➤ {min_duracion:.2f} Segs - "
    f"( {formatear_tiempo(min_duracion)} ) - "
    f"( Detecta Cortes Muy Pequeños O Posibles Glitches )\n"
)

print(
    f"- Total De Caracteres Originales ( TXT ) ➤ {len(texto)} - ( Incluye Saltos De Línea Y Formato Original )\n"
)

print(
    f"- Total De Caracteres Procesados ➤ {total_chars} - "
    f"( Cantidad Total De Texto Convertido A Voz )\n"
)

print(
    f"- Distancia Equivalente Del Texto ➤ {km_totales_texto:.3f} KM - "
    f"( Asumiendo 2 mm Por Carácter )\n"
)

print(
    f"- Tiempo Por 1000 Caracteres ➤ {tiempo_por_1000:.2f} Segs - ( {formatear_tiempo(tiempo_por_1000)} ) - "
    f"( Velocidad Real De Generación, Ideal Para Comparar CPUs / GPUs )\n"
)

if bloques_fallidos:
    print(f"- Bloques Fallidos ➤ {len(bloques_fallidos)}\n")
    print(f"- Lista De Bloques Fallidos ➤ {bloques_fallidos}\n")
else:
    print(f"- Ningún Bloque Fallido - ( Generación Perfecta )\n")

print(
    f"- Porcentaje De Bloques Fallidos ➤ {porcentaje_fallidos:.2f}% - "
    f"( Nivel De Bloques Que Han Fallado Durante La Generación )\n"
)

print(
    f"- Porcentaje De Bloques Sospechosos ➤ {porcentaje_sospechosos:.2f}% - "
    f"( Nivel De Problemas Detectados En El Audio )\n"
)

print(
    f"- Bloques Sospechosos Detectados ➤ {len(bloques_raros)} - ( Fragmentos Demasiado Cortos O Largos, Posibles Glitches O Errores De Voz )\n"
)

contador = 1
tiempo_acumulado = 0
idx_audio = 0
bloques_fallidos_set = set(bloques_fallidos)

for i in range(total_bloques):

    if (i + 1) in bloques_fallidos_set:
        continue

    d = duraciones_audio[idx_audio]

    if d < 0.2 or d > 20:
        timestamp = formatear_tiempo(tiempo_acumulado)

        print(
            f"  · {contador} · Bloque Nº ➤ {i+1} | Duración ➤ {d:.2f} Segs | Posición ➤ {timestamp} Hasta {formatear_tiempo(tiempo_acumulado + d)}\n"
        )

        print(f"    ↳ Texto ➤ {bloques[i]}\n")
        contador += 1

    tiempo_acumulado += d

    if idx_audio < len(pausas):
        tiempo_acumulado += pausas[idx_audio]

    idx_audio += 1

print(
    f"- Velocidad De Habla ➤ {chars_por_seg_audio:.2f} Caract / Seg - ( Ritmo Al Que Se Pronuncia El Texto )\n"
)

print(
    f"- Voces Distintas Utilizadas ➤ {len(voces_usadas)} - ( Número Real De Voces Diferentes Usadas En Todo El Audio )\n"
)

total = len(conteo_voces) if conteo_voces else 1
total_audio = sum(duraciones_audio)
total_pausas = sum(pausas) if pausas else 0
tiempo_por_voz = {}

for voz, duracion in zip(conteo_voces, tiempo_por_bloque):

    if voz not in tiempo_por_voz:
        tiempo_por_voz[voz] = 0

    tiempo_por_voz[voz] += duracion

if total_audio > 0:
    for voz in tiempo_por_voz:
        proporcion = tiempo_por_voz[voz] / total_audio
        tiempo_por_voz[voz] += total_pausas * proporcion

for v in voces_usadas:
    veces = conteo_voces.count(v)
    porcentaje = (veces / total) * 100 if total > 0 else 0
    tiempo_total = tiempo_por_voz.get(v, 0)

    print(
        f"  · {v} ➤ {veces}/{len(archivos)} Bloques Leídos | ( {porcentaje:.2f}% ) | {formatear_tiempo(tiempo_total)} - ( {tiempo_total:.2f} Segs ) Tiempo Leyendo"
    )

print(
    f"\n- Tiempo Total Hablado Por Todas Las Voces ➤ {sum(tiempo_por_voz.values()):.2f} Segs - "
    f"( {formatear_tiempo(sum(tiempo_por_voz.values()))} )"
)

print(
    f"\n- Duración Total OPUS ➤ {duracion_opus:.2f} Segs - "
    f"( {formatear_tiempo(duracion_opus)} )"
)

print(
    f"\n- Diferencia ➤ {abs(sum(tiempo_por_voz.values()) - duracion_opus):.2f} Segs - ( {'Excelente' if abs(sum(tiempo_por_voz.values()) - duracion_opus) < 0.02 else 'Muy Preciso' if abs(sum(tiempo_por_voz.values()) - duracion_opus) < 0.1 else 'Aceptable' if abs(sum(tiempo_por_voz.values()) - duracion_opus) < 0.5 else 'Descuadre Alto'} )\n"
)

print(
    f"- Velocidad De Generación De Texto ➤ {velocidad_chars:.2f} Caract / Seg | Velocidad De Generación Km/h ➤ {velocidad_chars * 0.002 * 3600 / 1000:.4f} Km/h\n"
)

print(
    f"- Ratio Caracteres / Segundo Real De Audio ➤ {ratio_chars_audio:.2f} - ( Esta Métrica Indica La Cantidad De Caracteres Procesados Por Cada Segundo De Audio Generado )\n"
)

print(f"- Tamaño Del Fichero WAV ➤ {tamano:.2f} MB\n")
print(f"- Tamaño Del Fichero OPUS ➤ {tamano_opus:.2f} MB\n")

nombre = os.path.basename(ruta_musica) if ruta_musica else ""

try:
    canales_opus = int(
        subprocess.run(
            [
                "ffprobe",
                "-v",
                "error",
                "-select_streams",
                "a:0",
                "-show_entries",
                "stream=channels",
                "-of",
                "default=noprint_wrappers=1:nokey=1",
                SALIDA_OPUS,
            ],
            capture_output=True,
            text=True,
        ).stdout.strip()
    )
except:
    canales_opus = 0

if usar_musica:
    print(
        f"- Duración Del Audio OPUS Con Música De Fondo ( {nombre} ) ➤ {duracion_opus:.2f} Segs - ( {formatear_tiempo(duracion_opus)} )\n"
    )
else:
    print(
        f"- Duración Del Audio OPUS Sin Música De Fondo ➤ {duracion_opus:.2f} Segs - ( {formatear_tiempo(duracion_opus)} )\n"
    )

print(
    f"- Tiempo Total De Pausas Entre Bloques ➤ {total_pausas:.2f} Segs - ( {formatear_tiempo(total_pausas)} )\n"
)

print(
    f"- Compresión WAV A OPUS ➤ {comp:.2f}% Menos Tamaño | {ratio:.2f}x Más Pequeño\n"
)

print(
    f"- Frecuencia Del Fichero OPUS ➤ {sample_rate} Hz | {canales_opus} Canal(es) | {bitrate} Kbps\n"
)

logging.disable(logging.CRITICAL)

SRT_SALIDA = f"M8AX_Subtitulos_{fecha_archivo}.srt"

with open(SRT_SALIDA, "w", encoding="utf-8") as srt:

    for idx, (num, inicio_sub, fin_sub, texto_sub) in enumerate(subtitulos_srt):

        if idx == len(subtitulos_srt) - 1:
            continue

        srt.write(f"{num}\n")
        srt.write(f"{tiempo_srt(inicio_sub)} --> {tiempo_srt(fin_sub)}\n")
        srt.write(f"{texto_sub}\n\n")

print(
    f"- Fichero SRT De Subtítulos Generado ➤ {SRT_SALIDA} - ( Compatible Con YouTube, VLC, Media Player, FFmpeg, Etc... )\n"
)

nombre_grafica = generar_graficas_pro(
    duraciones,
    duraciones_audio,
    chars_por_bloque,
    voces_usadas,
    rtf,
    pausas,
)

if usar_qr:

    print(f"- Pregenerando Video De Códigos QR ( Concatenando )\n")

    lista_clips_qr = os.path.join("M8AX-QRs", "M8AX-Lista_Clips_QR.TxT")

    with open(lista_clips_qr, "w", encoding="utf-8") as f:
        for qr in qr_por_bloque:
            clip_path = qr["path"].replace(".png", ".mp4")
            f.write(f"file '{os.path.abspath(clip_path)}'\n")

    cmd_concat_qr = [
        "ffmpeg",
        "-f",
        "concat",
        "-safe",
        "0",
        "-i",
        lista_clips_qr,
        "-c",
        "copy",
        "-y",
        qr_video_final,
    ]

    subprocess.run(cmd_concat_qr, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    probe = subprocess.run(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1",
            qr_video_final,
        ],
        capture_output=True,
        text=True,
    )

    try:
        dur_qr_final = float(probe.stdout.strip().split("=")[1])
    except:
        dur_qr_final = 0.0

    print(
        f"- Vídeo QR Pregenerado ➤ {qr_video_final} - ( {tamano_m8ax(qr_video_final)} ) - {formatear_tiempo(dur_qr_final)} - ( {dur_qr_final:.2f} Segs )\n"
    )

if usar_video:

    print("--- Generando Vídeo MP4 Con Subtítulos Integrados ---\n")

    num_video = random.randint(1, 60)
    video_fondo = os.path.join("M8AX-Vídeo_Subtítulos", f"VídeoFondo{num_video}.mp4")
    nombre_video = os.path.splitext(os.path.basename(video_fondo))[0]
    SALIDA_MP4 = f"{os.path.splitext(SALIDA_OPUS)[0]}_{nombre_video}.mp4"

    print(
        f"- Vídeo Seleccionado Como Fondo Del Vídeo Final ➤ {os.path.basename(video_fondo)}\n"
    )

    print(f"- QRs Dinámicos Con Texto Del Bloque ➤ {'ON' if usar_qr else 'OFF'}\n")

    if not os.path.exists(video_fondo):
        print(f"❌ Error ➤ No Se Encuentra El Vídeo De Fondo ➤ {video_fondo}")
        print(
            "👉 Asegúrate De Que Existan Ficheros MP4 En La Carpeta M8AX-Vídeo_Subtítulos"
        )
        exit()

    SRT_FFMPEG = SRT_SALIDA.replace("\\", "/").replace(":", "\\:")

    encoders = [
        ("hevc_nvenc", ["-preset", "p5"]),
        ("h264_nvenc", ["-preset", "p5"]),
        ("hevc_qsv", ["-preset", "fast"]),
        ("h264_qsv", ["-preset", "fast"]),
        ("hevc_amf", ["-quality", "balanced"]),
        ("libx265", ["-preset", "medium"]),
    ]

    encoder_video = "libx264"
    args_encoder = ["-preset", "medium"]

    for enc, args in encoders:

        test_cmd = [
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-f",
            "lavfi",
            "-i",
            "testsrc=size=1280x720:rate=30",
            "-t",
            "1",
            "-c:v",
            enc,
            "-f",
            "null",
            "-",
        ]

        test = subprocess.run(test_cmd, capture_output=True, text=True)

        if test.returncode == 0:
            encoder_video = enc
            args_encoder = args
            print(f"- Encoder Compatible Detectado ➤ {encoder_video}\n")
            break

    num_logo = random.randint(1, 20)

    logo_m8ax = None

    for ext in [".png", ".mp4"]:
        ruta_test = os.path.join("M8AX-Logos", f"M8AX-{num_logo}{ext}")

        if os.path.exists(ruta_test):
            logo_m8ax = ruta_test
            break

    if not logo_m8ax:
        print("- No Se Encontró Ningún Logo...")
        exit()

    print(
        f"- Logo Seleccionado Para Parte Superior Derecha Del Vídeo Final ➤ {os.path.basename(logo_m8ax)}\n"
    )

    print(f"- HUD En Vídeo ➤ ON\n")

    color_hud = (
        f"#{random.randint(100,255):02X}"
        f"{random.randint(100,255):02X}"
        f"{random.randint(100,255):02X}"
    )

    filtro_hud_m8ax = (
        "drawtext@hud="
        "text=' ':"
        "expansion=none:"
        "fontfile='C\\:/Windows/Fonts/consola.ttf':"
        "fontsize=22:"
        f"fontcolor={color_hud}:"
        "x=58:"
        "y=5:"
        "box=1:"
        "boxcolor=black@0.12:"
        "boxborderw=6:"
        "borderw=1:"
        "bordercolor=black@0.7:"
        "shadowx=2:"
        "shadowy=2:"
        "shadowcolor=black@0.7"
    )

    filtro_hud_m8ax_dias = (
        "drawtext@dias="
        "text=' ':"
        "expansion=none:"
        "fontfile='C\\:/Windows/Fonts/consola.ttf':"
        "fontsize=22:"
        f"fontcolor={color_hud}:"
        "x=5:"
        "y=5:"
        "box=1:"
        "boxcolor=black@0.12:"
        "boxborderw=6:"
        "borderw=1:"
        "bordercolor=black@0.7:"
        "shadowx=2:"
        "shadowy=2:"
        "shadowcolor=black@0.7"
    )

    color_restante = (
        f"#{random.randint(100,255):02X}"
        f"{random.randint(100,255):02X}"
        f"{random.randint(100,255):02X}"
    )

    filtro_restante = (
        "drawtext@restante="
        "text=' ':"
        "expansion=none:"
        "fontfile='C\\:/Windows/Fonts/consola.ttf':"
        "fontsize=22:"
        f"fontcolor={color_restante}:"
        "x=w-text_w-224:"
        "y=5:"
        "box=1:"
        "boxcolor=black@0.12:"
        "boxborderw=6:"
        "borderw=1:"
        "bordercolor=black@0.7:"
        "shadowx=2:"
        "shadowy=2:"
        "shadowcolor=black@0.7"
    )

    filtro_qrs = ""

    if usar_qr:

        filtro_qrs = (
            "[3:v]"
            "format=rgba,"
            "colorchannelmixer=aa=0.70"
            "[qr];"
            "[sub]drawbox="
            "x=25:"
            "y=50:"
            "w=200:"
            "h=200:"
            "color=black@0.45:"
            "t=fill"
            "[qrbg];"
            "[qrbg][qr]"
            "overlay=25:50"
            "[qrout];"
        )

        video_input_final = "[qrout]"

    else:

        video_input_final = "[sub]"

    ultimo_inicio = subtitulos_srt[-1][1]
    ultimo_fin = subtitulos_srt[-1][2]

    if total_bloques > 1:
        inicio_suscribete = subtitulos_srt[0][1]
        fin_suscribete = subtitulos_srt[min(4, total_bloques - 2)][2]
        fin_suscribete = min(fin_suscribete, ultimo_inicio - 0.5)

        drawtext_suscribete = (
            f"drawtext="
            f"text='{random.choice(['¡ Suscríbete A Mi Canal !', '¡ Dale Like Y Suscríbete !', '¡ Disfruta De La Lectura !', '¡ Apoya Mi Canal !', '¡ No Olvides Escanear El QR !', '¡ Activa La Campana !', '¡ Comparte Este AudioLibro !', '¡ Déjame Tu Comentario !', '¡ Gracias Por Estar Aquí !', '¡ Comparte Si Te Gusta !', '¡ Apoya El Canal Con Un Like !', '¡ Nos Vemos En El Siguiente !', '¡ Sigue Escuchando Con M8AX !', '¡ Que Disfrutes La Lectura !', '¡ Leer Es Bueno !'])}':"
            f"fontcolor=#{random.randint(120,255):02X}{random.randint(120,255):02X}{random.randint(120,255):02X}@0.95:"
            f"fontsize=38:"
            f"fontfile='C\\:/Windows/Fonts/segoeuib.ttf':"
            f"x=W-text_w-210:"
            f"y=245:"
            f"borderw=3:"
            f"bordercolor=black@0.85:"
            f"shadowx=4:"
            f"shadowy=4:"
            f"shadowcolor=black@0.85:"
            f"enable='between(t,{inicio_suscribete:.3f},{fin_suscribete:.3f})'"
        )
    else:
        drawtext_suscribete = "null"

    mostrar_duracion = total_bloques >= 7

    if mostrar_duracion:
        inicio_duracion = subtitulos_srt[min(5, total_bloques - 2)][1]
        fin_duracion = subtitulos_srt[-2][2]
    else:
        inicio_duracion = 99999999999
        fin_duracion = 99999999999

    drawtext_duracion = (
        f"drawtext="
        f"text='%{{eif\\:trunc(t/86400)\\:d\\:2}}d\\:%{{eif\\:trunc(mod(t\\,86400)/3600)\\:d\\:2}}h\\:%{{eif\\:trunc(mod(t\\,3600)/60)\\:d\\:2}}m\\:%{{eif\\:trunc(mod(t\\,60))\\:d\\:2}}s':"
        f"fontcolor=#{random.randint(120,255):02X}{random.randint(120,255):02X}{random.randint(120,255):02X}@0.85:"
        f"fontsize=32:"
        f"fontfile='C\\:/Windows/Fonts/segoeuib.ttf':"
        f"x=W-text_w-276:"
        f"y=245:"
        f"borderw=2:"
        f"bordercolor=black@0.85:"
        f"shadowx=3:"
        f"shadowy=3:"
        f"shadowcolor=black@0.85:"
        f"enable='between(t,{inicio_duracion:.3f},{fin_duracion:.3f})'"
    )

    r = random.randint(65, 255)
    g = random.randint(65, 255)
    b = random.randint(65, 255)

    fecha_bonita = fecha_espanol().replace(" ➤ ", " A Las ")
    fecha_bonita = fecha_bonita.replace(":", r"\:")
    fecha_bonita2 = fecha_bonita.replace(r"\:", ":")
    tiempo_drawtext = formatear_tiempo(tiempo_base_proceso)
    tiempo_drawtext = tiempo_drawtext.replace(":", r"\:")

    drawtext_final = (
        f"drawtext="
        f"text='FIN\nDEL   AUDIOLIBRO\nPOR   MvIiIaX - M8AX':"
        f"fontcolor=#{r:02X}{g:02X}{b:02X}:"
        f"fontsize=150:"
        f"fontfile='C\\:/Windows/Fonts/segoeui.ttf':"
        f"x=(w-text_w)/2:"
        f"y=(h-text_h)/2-20:"
        f"borderw=4:"
        f"bordercolor=black@0.9:"
        f"shadowx=6:"
        f"shadowy=6:"
        f"shadowcolor=black@0.9:"
        f"alpha='if(lt(t,{ultimo_inicio}),0,"
        f"if(lt(t,{ultimo_fin}),1,0))',"
        f"drawtext="
        f"text='Generado Por ( M8AX - XTTS ) - El {fecha_bonita} - Procesado Automáticamente Usando {device_nombre_corto} En {tiempo_drawtext}':"
        f"fontcolor=#{random.randint(85,255):02X}{random.randint(85,255):02X}{random.randint(85,255):02X}@0.93:"
        f"fontsize=25:"
        f"fontfile='C\\:/Windows/Fonts/segoeui.ttf':"
        f"x=(w-text_w)/2:"
        f"y=h-text_h-10:"
        f"borderw=2:"
        f"bordercolor=black@0.8:"
        f"shadowx=3:"
        f"shadowy=3:"
        f"shadowcolor=black@0.8:"
        f"alpha='if(lt(t,{ultimo_inicio}),0,"
        f"if(lt(t,{ultimo_fin}),1,0))'"
    )

    drawtext_gracias = (
        f"drawtext="
        f"text='Gracias Por Escuchar...':"
        f"fontcolor=#{random.randint(120,255):02X}{random.randint(120,255):02X}{random.randint(120,255):02X}@0.95:"
        f"fontsize=38:"
        f"fontfile='C\\:/Windows/Fonts/segoeuib.ttf':"
        f"x=W-text_w-210:"
        f"y=245:"
        f"borderw=3:"
        f"bordercolor=black@0.85:"
        f"shadowx=4:"
        f"shadowy=4:"
        f"shadowcolor=black@0.85:"
        f"alpha='if(lt(t,{ultimo_inicio}),0,"
        f"if(lt(t,{ultimo_fin}),1,0))'"
    )

    drawtext_extra = (
        f"drawtext="
        f"text='Procesado Usando {device_nombre_ffmpeg} | En Honor A MDDD - ( Mi Madre )':"
        f"fontcolor=#{random.randint(120,255):02X}{random.randint(120,255):02X}{random.randint(120,255):02X}@0.88:"
        f"fontsize=25:"
        f"fontfile='C\\:/Windows/Fonts/segoeui.ttf':"
        f"x=(w-text_w)/2:"
        f"y=h-text_h-49:"
        f"borderw=2:"
        f"bordercolor=black@0.8:"
        f"shadowx=3:"
        f"shadowy=3:"
        f"shadowcolor=black@0.8:"
        f"alpha='if(lt(t,{ultimo_inicio}),0,"
        f"if(lt(t,{ultimo_fin}),1,0))'"
    )

    visualizador = random.choice(
        [
            "avectorscope",
            "showwaves",
            "showspectrum",
            "barras",
            "waveform",
            "soundforge",
            "showcqt",
            "kaleidoscope",
            "showcwt",
            "oscilloscope",
            "retroeq",
        ]
    )

    print(
        f"- Vumetro En Vídeo Final ➤ "
        f"{'ON' if mostrar_vumeter else 'OFF'}"
        f"{f' | Visualizador ➤ {visualizador.capitalize()}' if mostrar_vumeter else ''}\n"
    )

    print(
        f"- Nombre Del Narrador En El Vídeo ➤ {'ON' if mostrar_narrador else 'OFF'}\n"
    )

    r_nar = random.randint(50, 255)
    g_nar = random.randint(50, 255)
    b_nar = random.randint(50, 255)
    color_nar = f"#{r_nar:02X}{g_nar:02X}{b_nar:02X}"

    filtro_narrador_realtime = (
        "drawtext@narrador="
        "text=' ':"
        "expansion=none:"
        "fontfile='C\\:/Windows/Fonts/segoeuib.ttf':"
        "fontsize=42:"
        f"fontcolor={color_nar}:"
        "x=(w-text_w)/2:"
        "y=40:"
        "borderw=2:"
        "bordercolor=black@0.9:"
        "shadowx=4:"
        "shadowy=4:"
        "shadowcolor=black@0.85"
    )

    r = random.randint(80, 255)
    g = random.randint(80, 255)
    b = random.randint(80, 255)

    if visualizador == "avectorscope":

        filtro_visual = (
            f"[1:a]avectorscope="
            f"s=360x180:"
            f"draw=line:"
            f"rc={r}:"
            f"gc={g}:"
            f"bc={b}"
            f"[vu];"
        )

    elif visualizador == "showwaves":

        color_wave = random.choice(
            [
                "cyan",
                "lime",
                "yellow",
                "orange",
                "red",
                "magenta",
                "white",
            ]
        )

        filtro_visual = (
            f"[1:a]showwaves="
            f"s=360x180:"
            f"mode=cline:"
            f"colors={color_wave}"
            f"[vu];"
        )

    elif visualizador == "barras":

        filtro_visual = (
            f"[1:a]showfreqs="
            f"s=360x180:"
            f"mode=bar:"
            f"fscale=log:"
            f"ascale=log:"
            f"win_size=2048:"
            f"overlap=0.85:"
            f"[vu];"
        )

    elif visualizador == "waveform":

        color_wave = random.choice(
            [
                "white",
                "cyan",
                "lime",
                "yellow",
                "orange",
            ]
        )

        filtro_visual = (
            f"[1:a]showwaves="
            f"s=360x180:"
            f"mode=line:"
            f"colors={color_wave}:"
            f"scale=lin:"
            f"rate=30"
            f"[vu];"
        )

    elif visualizador == "soundforge":

        filtro_visual = (
            f"[1:a]showwaves="
            f"s=360x180:"
            f"mode=cline:"
            f"rate=60:"
            f"split_channels=1:"
            f"scale=lin:"
            f"colors=#{random.randint(50,255):02X}{random.randint(50,255):02X}{random.randint(50,255):02X}99|#{random.randint(50,255):02X}{random.randint(50,255):02X}{random.randint(50,255):02X}99"
            f"[vu];"
        )

    elif visualizador == "showcqt":

        filtro_visual = f"[1:a]showcqt=" f"s=1920x1080," f"scale=360:180" f"[vu];"

    elif visualizador == "kaleidoscope":

        filtro_visual = (
            f"[1:a]showspectrum="
            f"s=360x180:"
            f"mode=combined:"
            f"color=rainbow:"
            f"slide=scroll,"
            f"split=4[a][b][c][d];"
            f"[a]hflip[aa];"
            f"[b]vflip[bb];"
            f"[c]hflip,vflip[cc];"
            f"[d][aa]hstack[top];"
            f"[bb][cc]hstack[bottom];"
            f"[top][bottom]vstack,"
            f"scale=360:180"
            f"[vu];"
        )

    elif visualizador == "showcwt":

        filtro_visual = f"[1:a]showcwt=s=360x180[vu];"

    elif visualizador == "oscilloscope":

        filtro_visual = (
            f"[1:a]showwaves="
            f"s=360x180:"
            f"mode=cline:"
            f"rate=60:"
            f"split_channels=1:"
            f"colors=cyan|blue,"
            f"format=yuv420p"
            f"[wave];"
            f"[wave]oscilloscope="
            f"x=0.5:"
            f"y=0.5:"
            f"s=1:"
            f"t=0.8:"
            f"o=0.9:"
            f"tx=0.5:"
            f"ty=0.9:"
            f"tw=1:"
            f"th=0.7:"
            f"g=0:"
            f"st=0:"
            f"sc=1"
            f"[vu];"
        )

    elif visualizador == "retroeq":

        filtro_visual = (
            f"[1:a]showfreqs="
            f"s=24x180:"
            f"mode=bar:"
            f"fscale=log:"
            f"ascale=log:"
            f"colors="
            f"#{random.randint(80,255):02X}{random.randint(80,255):02X}{random.randint(80,255):02X}|"
            f"#{random.randint(80,255):02X}{random.randint(80,255):02X}{random.randint(80,255):02X}|"
            f"#{random.randint(80,255):02X}{random.randint(80,255):02X}{random.randint(80,255):02X}|"
            f"#{random.randint(80,255):02X}{random.randint(80,255):02X}{random.randint(80,255):02X}"
            f"[small];"
            f"[small]scale=360:180:"
            f"flags=neighbor"
            f"[vu];"
        )

    else:

        filtro_visual = (
            f"[1:a]showspectrum="
            f"s=360x180:"
            f"mode=combined:"
            f"color=rainbow:"
            f"slide=scroll"
            f"[vu];"
        )

    if duracion_opus < 60:
        fade_inicio = 2
        fade_duracion = 3
    else:
        fade_inicio = 5
        fade_duracion = 10

    indice_grafica = 4 if usar_qr else 3

    EFECTO_VIDEO = "Blanco Y Negro" if random.random() >= 0.85 else "Normal"

    print(f"- Efecto Visual En Video Final ➤ {EFECTO_VIDEO.upper()}\n")

    filtro_final_vu = ""
    filtro_final_sinvu = ""

    salida_vu = "v"
    salida_sinvu = "v"

    if EFECTO_VIDEO == "Blanco Y Negro":

        filtro_final_vu = "[vtmp]hue=s=0[v];"
        filtro_final_sinvu = "[vtmp]hue=s=0[v];"

        salida_vu = "vtmp"
        salida_sinvu = "vtmp"

    filtro_completo = (
        f"{filtro_qrs}"
        f"{filtro_visual}"
        f"[0:v]subtitles='{SRT_FFMPEG}':"
        f"force_style='FontName=Segoe UI,FontSize=20,"
        f"PrimaryColour=&H00FFFFFF&,OutlineColour=&H00000000&,"
        f"BorderStyle=1,Outline=1,Shadow=1,Alignment=2,MarginV=42,MarginL=25,MarginR=25'"
        f"{',' + filtro_narrador_realtime if mostrar_narrador else ''},{drawtext_final},{drawtext_extra},{filtro_hud_m8ax},{filtro_hud_m8ax_dias},{filtro_restante},{drawtext_suscribete},{drawtext_duracion},{drawtext_gracias},zmq=bind_address=tcp\\\\://127.0.0.1\\\\:55555[sub];"
        f"[2:v]scale=180:-1,format=rgba,colorchannelmixer=aa=0.65[logo_small];"
        f"[2:v]format=yuva420p,scale=950:-1,colorchannelmixer=aa=0.22,fade=t=out:st={fade_inicio}:d={fade_duracion}:alpha=1[logo_big];"
        f"{video_input_final}drawbox="
        f"x=iw-590:"
        f"y=30:"
        f"w=370:"
        f"h=190:"
        f"color=#{r:02X}{g:02X}{b:02X}@0.35:"
        f"t=1[box];"
        f"[box][vu]overlay=W-w-224:36[tmp];"
        f"[tmp][logo_small]overlay=W-w-25:36:format=auto[tmp2];"
        f"[tmp2][logo_big]overlay=(W-w)/2:(H-h)/2:format=auto[tmp3];"
        f"[{indice_grafica}:v]scale=1920:1080[graf];"
        f"[tmp3][graf]overlay=0:0:enable='gte(t,{duracion_opus-3.5})'[{salida_vu}];"
        f"{filtro_final_vu}"
    )

    filtro_completo_sinvu = (
        f"{filtro_qrs}"
        f"[0:v]subtitles='{SRT_FFMPEG}':"
        f"force_style='FontName=Segoe UI,FontSize=20,"
        f"PrimaryColour=&H00FFFFFF&,OutlineColour=&H00000000&,"
        f"BorderStyle=1,Outline=1,Shadow=1,Alignment=2,MarginV=42,MarginL=25,MarginR=25'"
        f"{',' + filtro_narrador_realtime if mostrar_narrador else ''},{drawtext_final},{drawtext_extra},{filtro_hud_m8ax},{filtro_hud_m8ax_dias},{filtro_restante},{drawtext_suscribete},{drawtext_duracion},{drawtext_gracias},zmq=bind_address=tcp\\\\://127.0.0.1\\\\:55555[sub];"
        f"[2:v]scale=180:-1,format=rgba,colorchannelmixer=aa=0.65[logo_small];"
        f"[2:v]format=yuva420p,scale=950:-1,colorchannelmixer=aa=0.22,fade=t=out:st={fade_inicio}:d={fade_duracion}:alpha=1[logo_big];"
        f"{video_input_final}[logo_small]overlay=W-w-25:25:format=auto[tmp];"
        f"[tmp][logo_big]overlay=(W-w)/2:(H-h)/2:format=auto[tmp2];"
        f"[{indice_grafica}:v]scale=1920:1080[graf];"
        f"[tmp2][graf]overlay=0:0:enable='gte(t,{duracion_opus-3.5})'[{salida_sinvu}];"
        f"{filtro_final_sinvu}"
    )

    filtro_final = ""

    if mostrar_vumeter:
        filtro_final = filtro_completo
    else:
        filtro_final = filtro_completo_sinvu

    with open("M8AX_Filtro_Complejo.TxT", "w", encoding="utf-8") as f:
        f.write(filtro_final)

    SEGUNDOS_SEGMENTO = 41400

    SEGMENTAR_MP4 = duracion_opus > SEGUNDOS_SEGMENTO

    SALIDA_MP4_PARTES = SALIDA_MP4.replace(".mp4", "_Parte_%03d.mp4")

    cmd_video = [
        "ffmpeg",
        "-nostdin",
        "-hide_banner",
        "-loglevel",
        "error",
        "-progress",
        "pipe:1",
        "-stats_period",
        "0.1",
        "-stats",
        "-y",
        "-stream_loop",
        "-1",
        "-i",
        video_fondo,
        "-i",
        SALIDA_OPUS,
        *(
            ["-stream_loop", "-1", "-i", logo_m8ax]
            if logo_m8ax.lower().endswith(".mp4")
            else ["-loop", "1", "-i", logo_m8ax]
        ),
        *(["-i", qr_video_final] if usar_qr else []),
        "-loop",
        "1",
        "-i",
        nombre_grafica,
        "-/filter_complex",
        "M8AX_Filtro_Complejo.TxT",
        "-map",
        "[v]",
        "-map",
        "1:a:0",
        "-c:v",
        encoder_video,
        "-b:v",
        "2000k",
        "-maxrate",
        "2000k",
        "-bufsize",
        "4000k",
        "-threads",
        "0",
        *args_encoder,
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "copy",
        "-shortest",
        "-movflags",
        "+faststart",
        "-metadata",
        f"title=M8AX - {TXT_ENTRADA} A XTTS - M8AX",
        "-metadata",
        "artist=--- MvIiIaX ---",
        "-metadata",
        f"album={album_voces}",
        "-metadata",
        f"date={fecha_archivo}",
        "-metadata",
        f"comment=Generado Por M8AX Con XTTS | Fecha ➤ {fecha_bonita2} | Procesado Automáticamente Usando ➤ {device_nombre} | Tiempo Total De Procesamiento ➤ {formatear_tiempo(tiempo_base_proceso)}",
        "-metadata",
        f"description={'No Hay Música De Fondo | Formato ➤ Opus 48kbps | Frecuencia ➤ 24kHz | Canales ➤ Mono' if not usar_musica else f'Fondo Musical ➤ {os.path.basename(ruta_musica)} | Volumen Base ➤ 0.15 | Reducción Automática ( Ducking ) ➤ Activado | Umbral ➤ 0.03 | Intensidad ➤ 5 | Ataque ➤ 40ms | Recuperación ➤ 400ms | Voz ➤ Mono A Estéreo ( Centrada ) | Mezcla ➤ amix | Duración Final ➤ Igual A La Voz | Música En Bucle ➤ Sí | Formato ➤ Opus 48kbps | Frecuencia ➤ 24kHz | Canales ➤ Estéreo'}",
        "-metadata",
        f"synopsis=Vídeo De Fondo ➤ {os.path.basename(video_fondo)} | Logo ➤ {os.path.basename(logo_m8ax)} | Bucle Infinito ➤ Sí | Subtítulos Integrados ➤ Sí | QRs Dinámicos ➤ {'ON' if usar_qr else 'OFF'} | Vumetro ➤ {'ON' if mostrar_vumeter else 'OFF'} | Modo VU ➤ {visualizador.capitalize() if mostrar_vumeter else 'OFF'} | HUD ➤ ON | Narrador ➤ {'ON' if mostrar_narrador else 'OFF'} | Codec ➤ {encoder_video} | Bitrate Vídeo ➤ 2000k | Pixel Format ➤ yuv420p | Efecto Visual ➤ {EFECTO_VIDEO}",
        "-metadata",
        "genre=--- M8AX XTTS VoZ ---",
        "-metadata",
        "disc=1",
        "-metadata",
        "track=1/10031977",
        "-metadata",
        "copyright=M8AX-MvIiIaX ➤ FN-10031977",
        "-metadata",
        "album_artist=MarcoS OchoA DieZ",
        "-metadata",
        "albumartist=MarcoS OchoA DieZ",
        "-metadata",
        "composer=M8AX - The Algorithm Man - M8AX",
        "-metadata",
        "lyrics=... Por Muchas Vueltas Que Demos, Siempre Tendremos El Culo Atrás ... | El Futuro No Está Establecido, No Hay Destino... Solo Existe El Que Nosotros Hacemos. | La Fuerza Es Lo Que Le Da Al Jedi Su Poder, Es Un Campo De Energía Formado Por Todas Las Cosas Vivientes, Nos Rodea... Penetra En Nosotros Y Mantiene Unida La Galaxia... | El Miedo Es El Camino Hacia El Lado Oscuro, El Miedo Lleva A La Ira, La Ira Lleva Al Odio, El Odio Lleva Al Sufrimiento... | Yo He Visto Cosas Que Vosotros No Creeríais. Atacar Naves En Llamas Más Allá De Orión. He Visto Rayos-C Brillar En La Oscuridad Cerca De La Puerta De Tannhäuser. Todos Esos Momentos Se Perderán En El Tiempo, Como Lágrimas En La Lluvia. Es Hora De Morir... | AudioLibro Compilado En Honor A MDDD...",
        *(
            [
                "-f",
                "segment",
                "-segment_time",
                str(SEGUNDOS_SEGMENTO),
                "-reset_timestamps",
                "1",
                "-segment_start_number",
                "1",
                SALIDA_MP4_PARTES,
            ]
            if SEGMENTAR_MP4
            else [SALIDA_MP4]
        ),
    ]

    ffmpeg_clock = 0.0

    def leer_progress_ffmpeg():

        global ffmpeg_clock

        while True:

            linea = res_video.stdout.readline()

            if not linea:
                break

            linea = linea.strip()

            if linea.startswith("out_time_ms="):

                try:
                    valor_str = linea.split("=")[1].strip()

                    if valor_str and valor_str != "N/A":
                        valor = int(valor_str)

                        if valor > 0:
                            ffmpeg_clock = valor / 1000000.0

                except:
                    pass

    zmq_ctx = zmq.Context()
    zmq_sock = zmq_ctx.socket(zmq.REQ)
    zmq_sock.setsockopt(zmq.LINGER, 0)
    zmq_sock.setsockopt(zmq.RCVTIMEO, 2000)
    zmq_sock.setsockopt(zmq.SNDTIMEO, 2000)
    zmq_lock = threading.Lock()

    def escapar_zmq(texto):
        return (
            texto.replace("\\", "\\\\")
            .replace("'", "\\'")
            .replace(":", "\\:")
            .replace("[", "\\[")
            .replace("]", "\\]")
        )

    def zmq_cmd(comando):
        global zmq_sock
        with zmq_lock:
            for _ in range(3):
                try:
                    zmq_sock.send_string(comando)
                    respuesta = zmq_sock.recv_string()
                    if respuesta:
                        return True
                except Exception:
                    try:
                        zmq_sock.close()
                    except:
                        pass
                    try:
                        zmq_sock = zmq_ctx.socket(zmq.REQ)
                        zmq_sock.setsockopt(zmq.LINGER, 0)
                        zmq_sock.setsockopt(zmq.RCVTIMEO, 2000)
                        zmq_sock.setsockopt(zmq.SNDTIMEO, 2000)
                        zmq_sock.connect("tcp://127.0.0.1:55555")
                    except:
                        pass
        return False

    def actualizar_hud_realtime():

        fecha_hud_rt = datetime.now().strftime("%d%m%Y")

        ultimo_hud = ""

        ultimo_hud_dias = ""

        while res_video.poll() is None:

            tiempo_actual = ffmpeg_clock

            duracion_total_libro = duracion_opus

            restante = max(0, duracion_total_libro - tiempo_actual)

            texto_restante = (
                "| RESTANTE > " + formatear_tiempo_completo(restante) + " |"
            )

            idx_hud = bisect.bisect_right(inicios_hud, tiempo_actual) - 1

            if idx_hud < 0:
                time.sleep(0.01)
                continue

            num_hud, inicio_hud, fin_hud, texto_hud_sub = subtitulos_srt[idx_hud]

            if inicio_hud <= tiempo_actual <= fin_hud:

                hud_timeline_txt = formatear_tiempo(inicio_hud)

                hud_fin_txt = formatear_tiempo(fin_hud)

                hud_progreso_audio = (
                    ((idx_hud + 1) / total_bloques) * 100 if total_bloques > 0 else 0
                )

                hud_chars = len(texto_hud_sub)

                hud_duracion_audio = duraciones_audio[idx_hud]

                hud_velocidad_habla = (
                    hud_chars / hud_duracion_audio if hud_duracion_audio > 0 else 0
                )

                hud_texto_final = (
                    f"M8AX XTTS - [ {fecha_hud_rt} ] | "
                    f"[ {idx_hud+1:06d} / {total_bloques:06d} ] | "
                    f"[ {hud_timeline_txt} > {hud_fin_txt} ] | "
                    f"{hud_progreso_audio:.2f} % | "
                    f"{hud_velocidad_habla:.2f} CPS"
                )

                if "d" in hud_timeline_txt or "d" in hud_fin_txt:

                    if hud_texto_final != ultimo_hud_dias:
                        zmq_cmd(
                            f"drawtext@dias reinit text='{escapar_zmq(hud_texto_final)}'"
                        )
                        zmq_cmd("drawtext@hud reinit text=''")
                        ultimo_hud_dias = hud_texto_final

                else:

                    if hud_texto_final != ultimo_hud:
                        zmq_cmd(
                            f"drawtext@hud reinit text='{escapar_zmq(hud_texto_final)}'"
                        )
                        zmq_cmd("drawtext@dias reinit text=''")
                        ultimo_hud = hud_texto_final

                zmq_cmd(
                    f"drawtext@restante reinit text='{escapar_zmq(texto_restante)}'"
                )

            time.sleep(0.01)

    def actualizar_narrador():

        ultimo_narrador = ""
        tiempo_cambio = 0
        SEGUNDOS_VISIBLE = 5
        ya_vaciado = False

        while res_video.poll() is None:

            tiempo_actual = ffmpeg_clock

            idx_n = bisect.bisect_right(inicios_hud, tiempo_actual) - 1

            if idx_n < 0:
                time.sleep(0.01)
                continue

            if idx_n >= len(conteo_voces):
                time.sleep(0.01)
                continue

            inicio_n = subtitulos_srt[idx_n][1]
            fin_n = subtitulos_srt[idx_n][2]

            if inicio_n <= tiempo_actual <= fin_n:

                voz = conteo_voces[idx_n]

                nombre_n = os.path.splitext(voz)[0].replace("_", " ").replace("-", " ")

                texto_narrador = f"--- Narrador {nombre_n} ---"

                if texto_narrador != ultimo_narrador:

                    color_nar_rt = f"#{random.randint(100,255):02X}{random.randint(100,255):02X}{random.randint(100,255):02X}"
                    zmq_cmd(
                        f"drawtext@narrador reinit text='{escapar_zmq(texto_narrador)}':fontcolor={color_nar_rt}"
                    )
                    ultimo_narrador = texto_narrador
                    tiempo_cambio = tiempo_actual
                    ya_vaciado = False

                elif tiempo_actual - tiempo_cambio > SEGUNDOS_VISIBLE:

                    if not ya_vaciado:
                        zmq_cmd("drawtext@narrador reinit text=''")
                        ya_vaciado = True

            time.sleep(0.01)

    res_video = subprocess.Popen(
        cmd_video,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        bufsize=1,
    )

    time.sleep(1.0)

    zmq_sock.connect("tcp://127.0.0.1:55555")

    threading.Thread(target=leer_progress_ffmpeg, daemon=True).start()

    threading.Thread(target=actualizar_hud_realtime, daemon=True).start()

    if mostrar_narrador:

        threading.Thread(target=actualizar_narrador, daemon=True).start()

    ultima_linea_ffmpeg = ""

    _telegram_ffmpeg_ultimo_envio = time.time()

    while True:
        linea = res_video.stderr.readline()

        if not linea:
            break

        if "frame=" in linea or "size=" in linea:
            ultima_linea_ffmpeg = linea.strip()
            print(f"\r{ultima_linea_ffmpeg}", end="", flush=True)
            if time.time() - _telegram_ffmpeg_ultimo_envio >= 3600:
                try:
                    _m = _re.search(r'time=(\d+):(\d+):(\d+)', ultima_linea_ffmpeg)
                    _me = _re.search(r'elapsed=(\d+):(\d+):(\d+)', ultima_linea_ffmpeg)
                    if _m and _me:
                        _seg_actual = int(_m.group(1))*3600 + int(_m.group(2))*60 + int(_m.group(3))
                        _pct = min(100.0, _seg_actual / duracion_opus * 100) if duracion_opus > 0 else 0
                        _elapsed = int(_me.group(1))*3600 + int(_me.group(2))*60 + int(_me.group(3))
                        _eta_seg = (_elapsed / _pct) * (100 - _pct) if _pct > 0 else 0
                        _eta = formatear_tiempo(max(0, _eta_seg))
                    else:
                        _pct = 0.0
                        _eta = "?"
                    requests.post(
                        f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendMessage",
                        data={"chat_id": CHAT_ID_TELEGRAM, "text": f"🎥 FFmpeg MP4 En Proceso...\n\n📊 {_pct:.2f}% | ETA ➤ {_eta} | Duración Total Del Video ➤ {formatear_tiempo(duracion_opus)}\n\n{ultima_linea_ffmpeg}"},
                        timeout=10,
                    )
                except Exception:
                    pass
                _telegram_ffmpeg_ultimo_envio = time.time()
        else:
            print(linea, end="", flush=True)

    res_video.wait()

    partes_mp4 = []

    if SEGMENTAR_MP4:

        nombre_base_actual = os.path.splitext(os.path.basename(SALIDA_MP4))[0]

        for fichero in os.listdir("."):

            if fichero.startswith(nombre_base_actual + "_Parte_") and fichero.endswith(
                ".mp4"
            ):
                partes_mp4.append(fichero)

    partes_mp4.sort()

    sys.stdout.guardar_ffmpeg_final()

    if res_video.returncode == 0:

        estado_narrador = (
            "Con Nombre Del Narrador ON"
            if mostrar_narrador
            else "Con Nombre Del Narrador OFF"
        )

        if SEGMENTAR_MP4:

            print(
                f"\n\n- Vídeos MP4 Generados Correctamente ➤ "
                f"{len(partes_mp4)} Partes | "
                f"{estado_narrador}\n"
            )

        else:

            print(
                f"\n\n- Vídeo MP4 Generado Correctamente ➤ "
                f"{SALIDA_MP4} | "
                f"{estado_narrador}\n"
            )

    else:

        print("\n- Error Generando El Vídeo MP4\n")

    try:
        zmq_sock.close()
        zmq_ctx.term()
    except:
        pass

try:
    if os.path.exists("M8AX_Filtro_Complejo.TxT"):
        os.remove("M8AX_Filtro_Complejo.TxT")
        print("- Fichero Eliminado ➤ M8AX_Filtro_Complejo.TxT\n")
except Exception as e:
    print(f"- Error Al Borrar M8AX_Filtro_Complejo.TxT ➤ {e}\n")

try:

    if nombre_grafica and os.path.exists(nombre_grafica):

        os.startfile(nombre_grafica)

        print(f"- Abriendo Gráficas PRO Automáticamente ➤ " f"{nombre_grafica}\n")

except Exception as e:

    print(f"- No Se Pudieron Abrir Las Gráficas ➤ {e}\n")

try:

    if usar_video:

        if SEGMENTAR_MP4 and len(partes_mp4) > 1:

            playlist_m3u = SALIDA_MP4.replace(".mp4", "_PlayList.m3u")

            with open(playlist_m3u, "w", encoding="utf-8") as f:

                for parte_mp4 in partes_mp4:
                    f.write(parte_mp4 + "\n")

            os.startfile(playlist_m3u)

            print(f"- Reproduciendo Playlist Multipartes ➤ " f"{playlist_m3u}\n")

        elif SEGMENTAR_MP4 and partes_mp4:

            os.startfile(partes_mp4[0])

            print(f"- Reproduciendo Primera Parte Del Vídeo ➤ " f"{partes_mp4[0]}\n")

        else:

            os.startfile(SALIDA_MP4)

            print(f"- Reproduciendo Vídeo Final ➤ " f"{SALIDA_MP4}\n")

    else:

        os.startfile(SALIDA_OPUS)

        print(f"- Reproduciendo Archivo Final ➤ " f"{SALIDA_OPUS}\n")

except Exception as e:

    print(f"- No Se Pudo Reproducir Automáticamente ➤ {e}\n")

fin_total = time.time()
duracion_total_final = fin_total - inicio2
rtf_total_final = duracion_total_final / duracion_opus if duracion_opus > 0 else 0
tiempo_extra_produccion = duracion_total_final - duracion_proceso

print(f"{'-'*175}\n")

print("- ¡ Listo, Trabajo Realizado !\n")

print(
    f"- Archivo Final De Audio OPUS ➤ {SALIDA_OPUS} - ( {tamano_m8ax(SALIDA_OPUS)} )\n"
)

if usar_video:

    if SEGMENTAR_MP4:

        print(f"- Vídeos MP4 Generados ➤ " f"{len(partes_mp4)} Partes\n")

        tam_total_partes = 0

        for idx_parte, parte_mp4 in enumerate(partes_mp4, start=1):

            print(
                f"  · Parte {idx_parte:03d} ➤ "
                f"{parte_mp4} - "
                f"( {tamano_m8ax(parte_mp4)} )"
            )

            tam_total_partes += os.path.getsize(parte_mp4)

        print()

        tam_total_partes = tam_total_partes / (1024 * 1024)

        if tam_total_partes >= 500:
            tam_total_txt = f"{tam_total_partes / 1024:.2f} GB"
        else:
            tam_total_txt = f"{tam_total_partes:.2f} MB"

        print(f"- Tamaño Total Multipartes ➤ " f"{tam_total_txt}\n")

    else:

        print(
            f"- Fichero Del Vídeo Final ➤ "
            f"{SALIDA_MP4} - "
            f"( {tamano_m8ax(SALIDA_MP4)} )\n"
        )

if os.path.exists(SRT_SALIDA):

    print(
        f"- Fichero SRT De Subtítulos ➤ {SRT_SALIDA} - ( {tamano_m8ax(SRT_SALIDA)} )\n"
    )

else:

    print("- No Se Generó El Fichero SRT De Subtítulos\n")

if nombre_grafica:

    print(
        f"- Fichero De Gráficas PRO ➤ {nombre_grafica} - ( {tamano_m8ax(nombre_grafica)} )\n"
    )

else:

    print("- No Se Generaron Gráficas PRO\n")

if os.path.exists("M8AX-LoG-XTTS.log"):

    print(
        f"- Fichero De Log ➤ M8AX-LoG-XTTS.log - ( {tamano_m8ax('M8AX-LoG-XTTS.log')} )\n"
    )

else:

    print("- No Se Generó El Fichero De Log\n")

print(f"--- RTFs Del Sistema Usando ➤ {device_nombre} ---\n")

print(
    f"- RTF XTTS Puro ➤ {rtf_xtts:.2f}x - "
    f"( Solo Generación De Texto A Voz | Motor XTTS | )\n"
)

print(
    f"- RTF Audio Final ➤ {rtf:.2f}x - "
    f"( Motor XTTS + Audio WAV + Conversión A OPUS )\n"
)

if usar_video:

    print(
        f"- RTF Producción Final ➤ {rtf_total_final:.2f}x - "
        f"( Motor XTTS + Audio WAV + Conversión A OPUS + Vídeo Final MP4 + Pipeline Completo )\n"
    )

    print(
        f"- Tiempo Extra Pipeline Final ➤ "
        f"{formatear_tiempo(tiempo_extra_produccion)} - "
        f"( Vídeo Final MP4 + Pipeline Completo )\n"
    )

if usar_qr:

    for archivo_qr in os.listdir("M8AX-QRs"):

        try:
            ruta_qr = os.path.join("M8AX-QRs", archivo_qr)
            if os.path.isfile(ruta_qr):
                os.remove(ruta_qr)
        except Exception as e:
            print(f"\n- Error Al Borrar QR ➤ {e}\n", flush=True)

    print("- Vídeo QR, Clips Temporales Y Lista Concat Eliminados Correctamente\n")

if (
    TOKEN_TELEGRAM != "PON AQUÍ TUS CREDENCIALES"
    and CHAT_ID_TELEGRAM != "PON AQUÍ TUS CREDENCIALES"
):

    print("- Enviando Mensaje Final De Estadísticas, A Tu Telegram.\n")

    fecha_luna_fin_total = fecha_espanol()
    luna_fin_total = ephem.Moon()
    luna_fin_total.compute()
    edad_luna_fin_total = ephem.now() - ephem.previous_new_moon(ephem.now())
    distancia_fin_total_km = luna_fin_total.earth_distance * 149597870.7

    telegram_m8ax(
        f"✅ M8AX XTTS ENGINE v2 ➤ AUDIOLIBRO FINALIZADO\n\n"
        f"🖥️ HARDWARE Y SISTEMA\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• Hardware ➤ {device_nombre}\n"
        f"• Frecuencia Audio OPUS ➤ {sample_rate} Hz\n"
        f"• Canales ➤ {canales_opus}\n"
        f"• Bitrate ➤ {bitrate} Kbps\n"
        f"• Encoder Vídeo ➤ {encoder_video if usar_video else 'Sin Vídeo'}\n"
        f"• Encoder QR ➤ {encoder_qr if usar_qr else 'Sin QR'}\n\n"
        f"🌙 DATOS LUNARES\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• Inicio Del Procesamiento ➤ {fecha_luna_inicio}\n"
        f"• Luna Visible Al Inicio ➤ {luna_inicio.phase:.2f}%\n"
        f"• Edad Lunar Al Inicio ➤ {edad_luna_inicio:.1f} Días\n"
        f"• Distancia A La Luna Al Inicio ➤ {distancia_inicio_km:,.0f} KM\n"
        f"• Fin De Generación Del Audio OPUS ➤ {fecha_luna_fin}\n"
        f"• Luna Visible Al Final Del Audio OPUS ➤ {luna_fin.phase:.2f}%\n"
        f"• Edad Lunar Al Final Del Audio OPUS ➤ {edad_luna_fin:.1f} Días\n"
        f"• Distancia A La Luna Al Final Del Audio OPUS ➤ {distancia_fin_km:,.0f} KM\n"
        f"• Fin De Producción Final ➤ {fecha_luna_fin_total}\n"
        f"• Luna Visible Al Final De La Producción ➤ {luna_fin_total.phase:.2f}%\n"
        f"• Edad Lunar Al Final De La Producción ➤ {edad_luna_fin_total:.1f} Días\n"
        f"• Distancia A La Luna Al Final De La Producción ➤ {distancia_fin_total_km:,.0f} KM\n\n"
        f"⏱️ TIEMPOS Y DURACIONES\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• Tiempo Total De Procesamiento ➤ {duracion_total_final:.2f} Segs - ( {formatear_tiempo(duracion_total_final)} )\n"
        f"• Tiempo Extra Pipeline Final ➤ {tiempo_extra_produccion:.2f} Segs - ( {formatear_tiempo(tiempo_extra_produccion)} )\n"
        f"• Duración OPUS ➤ {duracion_opus:.2f} Segs - ( {formatear_tiempo(duracion_opus)} )\n"
        f"• Tiempo Pausas ➤ {total_pausas:.2f} Segs - ( {formatear_tiempo(total_pausas)} )\n"
        f"• Tiempo / 1000 Caracteres ➤ {tiempo_por_1000:.2f} Segs - ( {formatear_tiempo(tiempo_por_1000)} )\n\n"
        f"⚡ RENDIMIENTO XTTS\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• RTF XTTS ➤ {rtf_xtts:.2f}x\n"
        f"• RTF Audio Final ➤ {rtf:.2f}x\n"
        + (f"• RTF Producción Final ➤ {rtf_total_final:.2f}x\n" if usar_video else "")
        + f"• Eficiencia ➤ {eficiencia:.2f} Segs Audio / Seg Procesado\n"
        f"• Rendimiento ➤ {audio_por_minuto:.2f} Segs / Min - ( {formatear_tiempo(audio_por_minuto)} )\n"
        f"• Bloques / Segundo ➤ {bloques_por_seg:.5f}\n"
        f"• Bloques / Minuto ➤ {bloques_por_seg * 60:.2f}\n"
        f"• Bloques / Hora ➤ {bloques_por_seg * 3600:.2f}\n"
        f"• Bloques / Semana ➤ {bloques_por_seg * 604800:.2f}\n"
        f"• Velocidad Texto ➤ {velocidad_chars:.2f} Caract / Seg\n"
        f"• Velocidad De Generación Km/h ➤ {velocidad_chars * 0.002 * 3600 / 1000:.4f} Km/h\n"
        f"• Velocidad Habla ➤ {chars_por_seg_audio:.2f} Caract / Seg\n"
        f"• Ratio Caracteres / Audio ➤ {ratio_chars_audio:.2f}\n\n"
        f"🧠 BLOQUES Y TEXTO\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• Bloques TXT ➤ {total_bloques}\n"
        f"• Bloques Generados ➤ {len(archivos)}\n"
        f"• Tiempo Medio Bloque ➤ {tiempo_medio_bloque:.2f} Segs - ( {formatear_tiempo(tiempo_medio_bloque)} )\n"
        f"• Duración Media Bloque ➤ {media_audio:.3f} Segs - ( {formatear_tiempo(media_audio)} )\n"
        f"• Caracteres Medios Por Bloque ➤ {media_chars:.2f}\n"
        f"• Variabilidad De Caracteres ➤ {desviacion_chars:.2f}\n"
        f"• Bloque Más Largo Texto ➤ {max_chars_b}\n"
        f"• Bloque Más Corto Texto ➤ {min_chars_b}\n"
        f"• Variabilidad De Duración ➤ {desviacion:.2f} Segs - ( {formatear_tiempo(desviacion)} )\n"
        f"• Bloque Más Largo Audio ➤ {max_duracion:.2f} Segs - ( {formatear_tiempo(max_duracion)} )\n"
        f"• Bloque Más Corto Audio ➤ {min_duracion:.2f} Segs - ( {formatear_tiempo(min_duracion)} )\n"
        f"• Caracteres Originales ➤ {len(texto)}\n"
        f"• Caracteres Procesados ➤ {total_chars}\n"
        f"• Distancia Equivalente Del Texto ➤ {km_totales_texto:.3f} KM - ( Asumiendo 2 mm Por Carácter )\n\n"
        f"🧪 DETECCIÓN DE ERRORES\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• Bloques Fallidos ➤ {len(bloques_fallidos)}\n"
        f"• Porcentaje De Bloques Fallidos ➤ {porcentaje_fallidos:.2f}%\n"
        f"• Bloques Sospechosos ➤ {len(bloques_raros)}\n"
        f"• Porcentaje De Bloques Sospechosos ➤ {porcentaje_sospechosos:.2f}%\n\n"
        f"🎙️ VOCES\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• Voces Distintas ➤ {len(voces_usadas)}\n"
        f"• Tiempo Total Voces ➤ {sum(tiempo_por_voz.values()):.2f} Segs - ( {formatear_tiempo(sum(tiempo_por_voz.values()))} )\n"
        f"• Diferencia OPUS / Voces ➤ {abs(sum(tiempo_por_voz.values()) - duracion_opus):.2f} Segs\n\n"
        f"💾 TAMAÑOS Y COMPRESIÓN\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• Tamaño WAV ➤ {tamano:.2f} MB\n"
        f"• Tamaño OPUS ➤ {tamano_opus:.2f} MB\n"
        f"• Compresión ➤ {comp:.2f}%\n"
        f"• Ratio ➤ {ratio:.2f}x\n\n"
        f"🎬 PRODUCCIÓN DE VÍDEO\n"
        f"━━━━━━━━━━━━━━━━━━━━━━\n"
        f"• Vídeo ➤ {'ON' if usar_video else 'OFF'}\n"
        + (
            f"• Fondo ➤ {os.path.basename(video_fondo)}\n"
            f"• Logo ➤ {os.path.basename(logo_m8ax)}\n"
            f"• Efecto Visual ➤ {EFECTO_VIDEO}\n"
            f"• HUD ➤ ON\n"
            f"• Narrador ➤ {'ON' if mostrar_narrador else 'OFF'}\n"
            f"• Vúmetro ➤ {'ON' if mostrar_vumeter else 'OFF'}\n"
            f"• Visualizador ➤ {visualizador.capitalize() if mostrar_vumeter else 'OFF'}\n"
            f"• QRs Dinámicos ➤ {'ON' if usar_qr else 'OFF'}\n"
            if usar_video
            else ""
        )
        + (
            f"• Multipartes ➤ {len(partes_mp4)}\n"
            f"• Tamaño Multipartes ➤ "
            f"{f'{(sum(os.path.getsize(p) for p in partes_mp4)/(1024*1024*1024)):.2f} GB' if (sum(os.path.getsize(p) for p in partes_mp4)/(1024*1024)) >= 500 else f'{(sum(os.path.getsize(p) for p in partes_mp4)/(1024*1024)):.2f} MB'}\n"
            if usar_video and SEGMENTAR_MP4
            else ""
        )
        + (
            f"• Tamaño MP4 ➤ {tamano_m8ax(SALIDA_MP4)}\n"
            if usar_video and not SEGMENTAR_MP4
            else ""
        )
    )

    logging.getLogger("TTS").setLevel(logging.CRITICAL)

    luna_final_log = ephem.Moon()
    luna_final_log.compute()
    edad_luna = ephem.now() - ephem.previous_new_moon(ephem.now())

    mensaje_audio_final = (
        f"Audiolibro finalizado correctamente. "
        f"Tiempo total de producción: "
        f"{int(duracion_total_final // 86400)} días, "
        f"{int((duracion_total_final % 86400) // 3600)} horas, "
        f"{int((duracion_total_final % 3600) // 60)} minutos y "
        f"{int(duracion_total_final % 60)} segundos. "
        f"Erre te efe final: {str(round(rtf_total_final, 2)).replace('.', ' coma ')}. "
        f"Bloques por hora: {str(round(bloques_por_seg * 3600, 2)).replace('.', ' coma ')}. "
        f"Procesado usando: {device_nombre_ffmpeg}. "
        f"Generado el {fecha_luna_fin_total.replace(' ➤ ', ' a las ')}. Luna visible al {str(round(luna_final_log.phase, 2)).replace('.', ' coma ')}%. Edad lunar: {str(round(edad_luna, 1)).replace('.', ' coma ')} días. "
        f"Por eme ocho a equis. "
        f"En Honor A Emedededede. Mi Madre."
    )

    print(
        "- Generando Y Enviando Fichero De Audio OPUS De Estadísticas Cortas, A Tu Telegram... Por Favor Espera...\n"
    )

    with open(os.devnull, "w") as fnull:

        with contextlib.redirect_stdout(fnull):

            tts.tts_to_file(
                text=mensaje_audio_final,
                speaker_wav=voz_actual,
                language=idioma_bloque,
                file_path="M8AX_Final.wav",
                split_sentences=True,
            )

    cmd_audio_telegram = [
        "ffmpeg",
        "-y",
        "-v",
        "error",
        "-i",
        "M8AX_Final.wav",
        "-c:a",
        "libopus",
        "-b:a",
        "48k",
        "-ar",
        "24000",
        "M8AX_Final.opus",
    ]

    subprocess.run(
        cmd_audio_telegram, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL
    )

    telegram_ok = False

    try:

        with open("M8AX_Final.opus", "rb") as audio:

            requests.post(
                f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendAudio",
                data={
                    "chat_id": CHAT_ID_TELEGRAM,
                    "caption": "🔊 M8AX ➤ Resumen Final Del Engine",
                },
                files={
                    "audio": audio,
                },
                timeout=30,
            )

        telegram_ok = True

    except:
        pass

    if telegram_ok:
        print(
            "- Fichero De Audio OPUS De Estadísticas Cortas, Enviado Correctamente A Tu Telegram.\n"
        )

    try:

        LIMITE_TELEGRAM_OPUS = 45 * 1024 * 1024

        tamaño_opus_final = os.path.getsize(SALIDA_OPUS)

        if tamaño_opus_final <= LIMITE_TELEGRAM_OPUS:

            print(
                "- Enviando Audio OPUS ➤ ( AudioLibro Completo ) A Telegram.\n",
                flush=True,
            )

            with open(SALIDA_OPUS, "rb") as audio_opus_final:
                respuesta_telegram_opus = requests.post(
                    f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendDocument",
                    data={
                        "chat_id": CHAT_ID_TELEGRAM,
                        "caption": (
                            f"Audio OPUS Final ➤ {os.path.basename(SALIDA_OPUS)}\n"
                            f"Tamaño ➤ {tamaño_opus_final / 1024 / 1024:.2f} MB\n"
                        ),
                    },
                    files={"document": audio_opus_final},
                    timeout=600,
                )

            if respuesta_telegram_opus.status_code == 200:
                print(
                    "- Audio OPUS Final Enviado Correctamente A Telegram.\n",
                    flush=True,
                )
            else:
                print(
                    f"- Error Telegram Al Enviar OPUS Final ➤ HTTP {respuesta_telegram_opus.status_code} {respuesta_telegram_opus.text}\n",
                    flush=True,
                )

        else:
            print(
                f"- Audio OPUS Final No Enviado A Telegram ➤ Supera Los 45 MB Permitidos Por BOT - ({tamaño_opus_final / 1024 / 1024:.2f} MB)\n",
                flush=True,
            )

    except Exception as e:
        print(f"- Error Enviando Audio OPUS Final A Telegram ➤ {e}\n", flush=True)

    if usar_video and nombre_grafica and os.path.exists(nombre_grafica):

        try:

            with open(nombre_grafica, "rb") as grafica:

                respuesta_grafica = requests.post(
                    f"https://api.telegram.org/bot{TOKEN_TELEGRAM}/sendPhoto",
                    data={
                        "chat_id": CHAT_ID_TELEGRAM,
                        "caption": "📊 M8AX ➤ Gráficas PRO Del AudioLibro",
                    },
                    files={
                        "photo": grafica,
                    },
                    timeout=120,
                )

            if respuesta_grafica.status_code == 200:

                print("- Gráfica WEBP Enviada Correctamente A Telegram.\n")

            else:

                print(
                    f"- Error Telegram Al Enviar Gráfica ➤ HTTP {respuesta_grafica.status_code} {respuesta_grafica.text}\n"
                )

        except Exception as e:

            print(f"- Error Enviando Gráfica A Telegram ➤ {e}\n")

    if os.path.exists("M8AX_Final.wav"):
        os.remove("M8AX_Final.wav")

    if os.path.exists("M8AX_Final.opus"):
        os.remove("M8AX_Final.opus")

print(f"{'-'*175}\n")

if os.path.exists("M8AX-Bloques_Debug.TxT"):
    print(
        "----- ¿ Quieres Borrar El Fichero De Debug De Bloques M8AX-Bloques_Debug.TxT ? -----\n"
    )

    print("1. ➤ Sí\n")
    print("2. ➤ No\n")
    print("----- Selecciona Opción ----- ", end="", flush=True)

    opcion_debug = input().strip()
    sys.stdout.log.write("\n")
    sys.stdout.log.flush()

    if opcion_debug == "1":
        try:
            os.remove("M8AX-Bloques_Debug.TxT")
            print("\n- Fichero Eliminado ➤ M8AX-Bloques_Debug.TxT\n")
        except Exception as e:
            print(f"\n- Error Al Borrar ➤ M8AX-Bloques_Debug.TxT ➤ {e}\n")
    else:
        print("\n- Fichero De Debug Conservado. No Se Eliminará...\n")

print(f"{'-'*175}\n")

luna_final_log = ephem.Moon()
luna_final_log.compute()
edad_luna = ephem.now() - ephem.previous_new_moon(ephem.now())
distancia_km = luna_final_log.earth_distance * 149597870.7

print(
    f"- {fecha_espanol()} - "
    f"( Luna Visible ➤ {luna_final_log.phase:.2f}% | "
    f"Edad Lunar ➤ {edad_luna:.1f} Días | "
    f"Distancia A La Luna ➤ {distancia_km:,.0f} KM )"
)

print(f"\n- YouTube Channel ➤ https://youtube.com/m8ax ➤ ¡ Suscríbete !")
print(f"\n- ... By M8AX & {device_nombre} ...")
print(f"\n{'-'*175}")