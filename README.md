# 🌿 MindfulMate

**MindfulMate** is a clinical-grade, AI-powered mental wellness companion built with **Streamlit** and **Groq**. It acts as a safe space for users to track their mood, vent their anxieties, and receive empathetic, evidence-based triage and informational support.

With a beautiful, modern UI inspired by premium health applications, MindfulMate integrates advanced Retrieval-Augmented Generation (RAG) to remember user-uploaded medical journals, alongside seamless voice-to-text and text-to-speech capabilities.

---

## ✨ Key Features

- **Clinical-Grade Conversational AI:** Powered by Groq, Dr. MindfulMate adheres to a strict medical protocol—providing empathetic assessments, structured responses, and critical triage to emergency services when needed.
- **RAG Memory (Document Uploads):** Users can upload their clinical journals or medical records (PDF/TXT). The app uses **LangChain** and **FAISS** to embed and search these documents locally, allowing the AI to maintain context about the user's specific medical history.
- **Voice Interactions:** 
  - **Voice Input:** Speak directly to the AI using the integrated microphone UI (powered by `streamlit-mic-recorder` and Whisper).
  - **Text-to-Speech:** Listen to Dr. MindfulMate's responses aloud via the integrated `gTTS` audio generation engine.
- **Premium UI/UX:** Built with a beautiful glassmorphism aesthetic, custom CSS animations, circular chat inputs, pulsating buttons, and a responsive layout.
- **Crisis Safety Net:** Features an omnipresent red Floating Action Button (FAB) and strict prompt directives to redirect users to global crisis helplines (e.g., 988) if self-harm or emergencies are detected.

---

## 🛠️ Technology Stack

- **Frontend:** [Streamlit](https://streamlit.io/) with heavy custom CSS injections for a modern, non-standard aesthetic.
- **AI / LLM Engine:** [Groq API](https://groq.com/) for blazing-fast inference.
- **Vector Database:** [FAISS](https://faiss.ai/) (Facebook AI Similarity Search) for local, fast document retrieval.
- **Embeddings & Chunking:** [LangChain](https://www.langchain.com/) (`RecursiveCharacterTextSplitter`, `HuggingFaceEmbeddings`).
- **Audio Processing:** `gTTS` (Google Text-to-Speech) for audio output, and Groq's Whisper API for audio transcription.
- **Document Parsing:** `PyPDF2` for robust PDF text extraction.

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

**MindfulMate is an informational tool and is NOT a substitute for professional medical advice, diagnosis, treatment, or therapy.** 

The AI is designed for general mental wellness support and stress relief. If you are experiencing a mental health crisis, severe distress, or believe you may be in immediate danger, please contact your local emergency services (911 in the US, 999 in the UK) or reach out to a global crisis helpline immediately via [Find a Helpline](https://findahelpline.com/).
