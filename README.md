# SpeakToNotes: Multilingual Meeting Transcription & Intelligence

An offline speech-to-text and meeting intelligence pipeline built with OpenAI Whisper and LLMs. It converts speech recordings into transcripts, summaries, and action items.

---

## Key Features

- **Offline / Local Speech Recognition:** Runs OpenAI Whisper locally without sending raw audio streams to third-party endpoints.
- **Multilingual Support:** Transcribes English, Hindi, and regional Indic languages like Telugu.
- **Dynamic Task Routing:** Supports native transcription (`transcribe`) and cross-lingual translation to English (`translate`).
- **Flexible Model Selection:** Switch between `tiny`, `base`, `small`, `medium`, and `large` models depending on accuracy and hardware constraints.

---

## Whisper Model Overview

| Model | Parameters | Target Workload | VRAM |
| :--- | :--- | :--- | :--- |
| **`tiny`** | ~39 M | Resource-constrained edge devices (English only) | ~1 GB |
| **`base`** | ~74 M | Standard English transcription | ~1 GB |
| **`small`** | ~244 M | High-resource multilingual audio | ~2 GB |
| **`medium`** | ~769 M | Mixed audio and regional accents | ~5 GB |
| **`large`** | ~1550 M | Complex Dravidian speech (Telugu) and high background music | ~10 GB |
