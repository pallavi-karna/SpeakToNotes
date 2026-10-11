# SpeakToNotes: Multilingual Meeting Transcription & Intelligence

An offline-capable speech-to-text pipeline and meeting intelligence tool built with OpenAI Whisper and LLMs. It converts enterprise meetings, standups, and multilingual speech recordings (English, Telugu, Hindi) into structured transcripts, executive summaries, and action items.

---

## Key Features

- **Offline / Local Speech Recognition:** Runs OpenAI Whisper locally without sending raw audio streams to third-party endpoints.
- **Multilingual & Indic Language Support:** Supports native transcription and direct translation across English, Hindi, and low-resource Dravidian languages like Telugu.
- **Dynamic Task Routing:** Choose between native script generation (`transcribe`) or cross-lingual conversion to English (`translate`).
- **Configurable Model Tiers:** Switch between `tiny`, `base`, `small`, `medium`, and `large` based on hardware availability and accuracy requirements.
- **Meeting Intelligence:** Summarizes lengthy audio transcripts into structured agendas, decisions, and deadlines using GPT.

---

## Whisper Model Sizing & Trade-offs

| Model | Parameters | Target Workload | VRAM |
| :--- | :--- | :--- | :--- |
| **`tiny`** | ~39 M | Resource-constrained edge devices (English only) | ~1 GB |
| **`base`** | ~74 M | Standard corporate English syncs and standups | ~1 GB |
| **`small`** | ~244 M | High-resource multilingual audio (Hindi, Spanish) | ~2 GB |
| **`medium`** | ~769 M | Noisy meeting audio and regional accents | ~5 GB |
| **`large`** | ~1550 M | Complex Dravidian speech (Telugu), songs, and high background interference | ~10 GB |

---

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/pallavi-karna/SpeakToNotes.git](https://github.com/pallavi-karna/SpeakToNotes.git)
   cd SpeakToNotes
