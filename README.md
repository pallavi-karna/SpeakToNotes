<div align="center">

# 🎙️ SpeakToNotes
### Multilingual Meeting Intelligence & Speech Pipeline

[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![OpenAI Whisper](https://img.shields.io/badge/OpenAI-Whisper-412991?style=for-the-badge&logo=openai&logoColor=white)](https://github.com/openai/whisper)
[![Indic Languages](https://img.shields.io/badge/Support-Telugu%20|%20Hindi%20|%20English-FF6F00?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-brightgreen?style=for-the-badge)](#)

<p align="center">
  <b>Transcribe offline. Translate seamlessly. Generate meeting summaries with local AI.</b>
</p>

</div>

---

### 🌟 Highlights

> 🔒 **100% Local Speech Recognition**  
> Audio files stay on your machine—processed entirely offline with local Whisper models.

* 🗣️ **Multilingual & Indic Speech Support:** Accurate recognition for English, Hindi, and regional Dravidian languages like Telugu.
* ⚡ **Dual Task Engine:** Toggle instantly between native transcription (`transcribe`) and direct translation to English (`translate`).
* 🧠 **Executive Meeting Notes:** Condenses lengthy recordings into actionable minutes, key decisions, and follow-ups.
* 🎛️ **Scale On Demand:** Select from 5 model tiers (`tiny` to `large`) based on your GPU/RAM hardware.

---

### 📊 Model Hardware Guide

| Model | Parameters | Target Audio | Required VRAM |
| :---: | :---: | :--- | :---: |
| **`tiny`** | ~39 M | Quick English audio notes | ~1 GB |
| **`base`** | ~74 M | Standups & clean meeting audio | ~1 GB |
| **`small`** | ~244 M | Multilingual speech & Hindi dialogues | ~2 GB |
| **`medium`** | ~769 M | Indian accents & noisy background audio | ~5 GB |
| **`large`** | ~1550 M | Complex Telugu speech & heavy background music | ~10 GB |

---

### 🚀 Getting Started

Launch the desktop interface:

```bash
python w2sgui.py
