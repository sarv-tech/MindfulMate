# 🌿 MindfulMate

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mindfulmate-xrz9svvq9bvq9ee7cd5fzv.streamlit.app/)

**MindfulMate** is a supportive, conversational AI wellness companion built with **Streamlit** and **Groq**. It acts as a safe space for users to track their mood, reflect on their anxieties, and receive empathetic, practical, and everyday emotional support.

With a beautiful, modern UI inspired by premium health applications, MindfulMate integrates a warm conversational AI core alongside seamless voice-to-text and text-to-speech capabilities.

---

## ✨ Key Features

- **Empathetic Conversational AI:** Powered by Groq, MindfulMate acts as a supportive friend and wellness coach. It avoids clinical jargon, prioritizing warm, practical, and non-judgmental interactions for everyday stress management.
- **Voice Interactions:** 
  - **Voice Input:** Speak directly to the AI using the integrated microphone UI (powered by `streamlit-mic-recorder` and Whisper).
  - **Text-to-Speech:** Listen to MindfulMate's responses aloud via the integrated `gTTS` audio generation engine.
- **Premium UI/UX:** Built with a beautiful aesthetic, completely transparent floating navigation, pulsating buttons, and a responsive chat layout.
- **Flawless Layout & Stability:** Includes automated context-window management to handle infinitely long conversations, seamless component positioning, and auto-recovery loops to prevent UI crashes.
- **Native Light/Dark Mode:** Features a custom, seamlessly integrated Light & Dark mode toggle in the sidebar that dynamically rewrites the core Streamlit configuration to ensure a flawless, glitch-free UI experience across all components.
- **Crisis Safety Net:** Features an omnipresent red Floating Action Button (FAB) and strict prompt directives to redirect users to global crisis helplines (e.g., 988) if self-harm or emergencies are detected.

---

## 🛠️ Technology Stack

- **Frontend:** [Streamlit](https://streamlit.io/) with heavy custom CSS injections for a modern, floating, non-standard aesthetic.
- **AI / LLM Engine:** [Groq API](https://groq.com/) for blazing-fast inference.
- **Audio Processing:** `gTTS` (Google Text-to-Speech) for audio output, and Groq's Whisper API for flawless audio transcription.

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have **Python 3.9+** installed on your machine.

### 2. Clone and Setup Environment
Clone the repository and navigate to the project directory:
```bash
cd MindfulMate
```

Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Install all required packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Rename `.env.example` to `.env` (or create a new `.env` file) and add your Groq API key:
```ini
GROQ_API_KEY="your_groq_api_key_here"
```

### 5. Run the Application
Start the Streamlit server:
```bash
streamlit run app.py
```
The app will automatically open in your default web browser (usually at `http://localhost:8501`).

---

## ⚠️ Disclaimer

**MindfulMate is a supportive informational tool and is NOT a doctor, therapist, psychiatrist, psychologist, emergency responder, or clinical-grade medical system.** 

The AI is designed for general mental wellness support and stress relief. If you are experiencing a mental health crisis, severe distress, or believe you may be in immediate danger, please contact your local emergency services (911 in the US, 999 in the UK) or reach out to a global crisis helpline immediately via [Find a Helpline](https://findahelpline.com/).
