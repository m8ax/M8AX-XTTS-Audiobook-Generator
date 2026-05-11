# 🔥 M8AX-XTTS-Audiobook-Generator 🔥

> Advanced XTTS v2 Audiobook Generator For Python
> Multi-Voice • OPUS • SRT • MP4 • CUDA • FFmpeg • Metrics PRO

---

# 📌 Description

**M8AX-XTTS-Audiobook-Generator** is an advanced Python script based on **Coqui XTTS v2** designed for:

* 🎙️ Voice cloning
* 📚 Audiobook generation
* 🎭 Multi-voice narration
* 🎞️ MP4 video rendering
* 📝 Automatic subtitle generation
* 📊 Advanced technical metrics
* ⚡ CPU and CUDA GPU support

The project was designed as a highly customizable **XTTS Engine / Framework**.

---

# ⚠️ IMPORTANT

This repository only includes:

```txt id="8z4dqp"
The main Python script
```

The repository DOES NOT include:

* WAV voice samples
* Background music
* Background videos
* Logos
* Fonts
* Custom assets

You must configure and add your own resources manually.

---

# 🧠 What You Need To Configure Yourself

The script was designed to be edited and customized.

You will need to:

## 🎙️ Add Your Own Voices

Create your own WAV voice collection.

Example:

```txt id="4prg9x"
m8ax-voces/
```

Then edit the `VOCES` list inside the script.

---

## 🎵 Add Background Music

Create your own music folder.

Example:

```txt id="a4v6cu"
M8AX-Música_Fondo/
```

The script expects files such as:

```txt id="6nv6yr"
MúsicaFondo1.mp3
MúsicaFondo2.mp3
MúsicaFondo3.mp3
...
```

---

## 🎞️ Add Background Videos

Create your own video folder.

Example:

```txt id="ajv8fh"
M8AX-Video_Subtítulos/
```

Example filenames:

```txt id="2cqfup"
VideoFondo1.mp4
VideoFondo2.mp4
VideoFondo3.mp4
...
```

---

## 🖼️ Add Logos

Create:

```txt id="3zdfq9"
M8AX-Logos/
```

Example:

```txt id="ppprba"
M8AX-1.png
M8AX-2.png
M8AX-3.png
...
```

---

# 🧪 Project Philosophy

This repository is intended as:

* A technical XTTS example
* A customizable audiobook engine
* A base framework for experimentation
* A professional TTS playground
* A long-form speech synthesis system

It is NOT intended to be a plug-and-play one-click application.

Some manual editing and configuration is expected.

---

# 🎙️ XTTS v2 Features

Uses:

```txt id="g6kw76"
tts_models/multilingual/multi-dataset/xtts_v2
```

Supports:

* Spanish synthesis
* Multi-WAV cloning
* Random narrator rotation
* Long audiobook generation
* Dynamic block assignment
* Multi-speaker narration

---

# ✂️ Intelligent Text Splitting

Custom text segmentation system with:

* Sentence-aware splitting
* Punctuation analysis
* Hard-limit protection
* UTF-8 compatibility
* Long-text optimization

Optimized specifically for XTTS stability.

---

# 🎵 Adaptive Background Music

Optional FFmpeg audio mixing system with:

* Ducking compression
* Infinite soundtrack looping
* Stereo voice conversion
* OPUS optimization
* Automatic soundtrack selection

Uses advanced FFmpeg filters such as:

```bash id="ytnu9v"
sidechaincompress
amix
pan
aformat
```

---

# 🎞️ MP4 Video Generation

Optional MP4 rendering with:

* Integrated subtitles
* Random background videos
* Narrator overlay system
* Automatic logo overlay
* Hardware encoder detection

Supported encoders:

```txt id="chvkp7"
hevc_nvenc
h264_qsv
hevc_amf
libx264
```

---

# 📝 Automatic SRT Subtitle Generation

The script automatically generates professional `.srt` subtitles compatible with:

* YouTube
* VLC
* FFmpeg
* Video editors
* External subtitle software

---

# 📊 Metrics PRO System

The engine includes advanced telemetry and statistics:

* Real-Time Factor
* XTTS pure RTF
* CPU monitoring
* RAM monitoring
* VRAM monitoring
* Character speed analysis
* Audio duration analysis
* Voice usage statistics
* ETA prediction
* Glitch detection
* Compression ratios
* Timeline synchronization

---

# 📈 Graph Generation

Automatically generates professional WEBP graphs using:

* Matplotlib
* NumPy

Includes:

* Generation speed
* Characters per block
* Audio duration curves
* Histograms
* Outlier detection

---

# 🎧 Audio Export

Final output:

```txt id="jhyfrv"
OPUS 48kbps / 24kHz
```

Optimized for:

* Audiobooks
* Speech clarity
* Small file sizes
* Long recordings

---

# ⚡ Hardware Support

## 🖥️ CPU

* Intel
* AMD

## 🚀 GPU

* NVIDIA CUDA

Automatic CUDA detection included.

---

# 📦 Requirements

## Python

Recommended:

```txt id="h53bcr"
Python 3.10.x
```

---

## FFmpeg

Required:

```txt id="gq22vk"
ffmpeg
ffprobe
```

Both must exist in PATH.

---

# 📚 Python Libraries

Install dependencies:

```bash id="s9ewrm"
pip install TTS torch psutil matplotlib numpy ephem
```

---

# ▶️ Usage

Place your text inside:

```txt id="42dyzv"
m8ax.txt
```

Run:

```bash id="q7qv6x"
python m8ax.py
```

The script will ask for:

* CPU or GPU
* Background music ON/OFF
* MP4 generation ON/OFF
* Narrator overlay ON/OFF

---

# 📂 Generated Files

## 🎵 Audio

```txt id="8hxj3e"
M8AX_DD-MM-YYYY_HH-MM-SS.opus
```

## 🎞️ Video

```txt id="dtvnn8"
M8AX_DD-MM-YYYY_HH-MM-SS.mp4
```

## 📝 Subtitles

```txt id="vw5g69"
M8AX_Subtitulos_DD-MM-YYYY_HH-MM-SS.srt
```

## 📈 Graphs

```txt id="p96k4u"
M8AX_Gráficas_DD-MM-YYYY_HH-MM-SS.webp
```

---

# 🛡️ Notes

The script contains many hardcoded paths and custom folder structures.

You are expected to:

* Modify paths
* Configure folders
* Add assets
* Customize voices
* Adapt the workflow to your own setup

This repository is aimed at advanced or technical users.

---

# 👨‍💻 Author

## M8AX

Created by:

```txt id="eq6ng5"
MarcoS OchoA DieZ
```

Development time:

```txt id="kgm2vc"
~85 Hours
```

---

# 🔗 YouTube

https://youtube.com/m8ax

---

# 🚀 M8AX XTTS ENGINE

> “The Future Is Not Set... There Is No Fate Except The One We Make.”
