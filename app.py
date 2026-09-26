import streamlit as st
import os
import streamlit.components.v1 as components
from dotenv import load_dotenv
from groq import Groq
from streamlit_mic_recorder import mic_recorder

# --------------------------------------------------
# ENV
# --------------------------------------------------
load_dotenv()

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="MindfulMate — Your Wellness Companion",
    page_icon="🌿",
    layout="centered",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------
# GLOBAL CSS
# --------------------------------------------------
st.markdown(
    """
    <style>
    /* ---------- Fonts ---------- */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* ---------- Palette ---------- */
    :root {
        --mm-bg:        #f7faf7;
        --mm-surface:   #ffffff;
        --mm-primary:   #2f6b4f;
        --mm-primary-2: #3f8a66;
        --mm-accent:    #a7d7c5;
        --mm-text:      #1f2a24;
        --mm-muted:     #5c6b63;
        --mm-border:    #e2ece7;
        --mm-shadow:    0 4px 20px rgba(47,107,79,0.08);
        --mm-radius:    14px;
    }

    /* ---------- App background ---------- */
    .stApp {
        background:
            radial-gradient(1200px 600px at 10% -10%, #e8f3ed 0%, transparent 60%),
            radial-gradient(900px 500px at 100% 0%, #eef6f1 0%, transparent 55%),
            var(--mm-bg);
    }

    /* ---------- Hide Streamlit chrome ---------- */
    #MainMenu, footer, header { visibility: hidden; }
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 6rem;
        max-width: 860px;
    }

    /* ---------- Headings ---------- */
    h1, h2, h3 {
        color: var(--mm-text);
        letter-spacing: -0.02em;
    }
    h1 { font-weight: 700; }

    /* ---------- Hero ---------- */
    .mm-hero {
        background: linear-gradient(135deg, #ffffff 0%, #f0f8f3 100%);
        border: 1px solid var(--mm-border);
        border-radius: var(--mm-radius);
        padding: 1.5rem 1.75rem;
        box-shadow: var(--mm-shadow);
        margin-bottom: 1.25rem;
    }
    .mm-hero h1 {
        margin: 0 0 .35rem 0;
        font-size: 1.75rem;
        line-height: 1.2;
    }
    .mm-hero p {
        margin: 0;
        color: var(--mm-muted);
        font-size: 1rem;
    }
    .mm-badge {
        display: inline-block;
        background: #e8f3ed;
        color: var(--mm-primary);
        font-size: .75rem;
        font-weight: 600;
        letter-spacing: .04em;
        text-transform: uppercase;
        padding: .25rem .6rem;
        border-radius: 999px;
        margin-bottom: .75rem;
    }

    /* ---------- Sidebar ---------- */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #f3f9f5 100%);
        border-right: 1px solid var(--mm-border);
    }
    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.25rem;
    }
    .mm-brand {
        display: flex;
        align-items: center;
        gap: .6rem;
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--mm-primary);
        margin-bottom: .25rem;
    }
    .mm-brand-sub {
        color: var(--mm-muted);
        font-size: .9rem;
        margin-bottom: 1rem;
    }
    .mm-disclaimer {
        background: #fff8e6;
        border: 1px solid #f0e0a8;
        border-left: 4px solid #e0b84a;
        border-radius: 10px;
        padding: .85rem 1rem;
        font-size: .82rem;
        line-height: 1.45;
        color: #4a3f1a;
        margin: .5rem 0 1rem 0;
    }
    .mm-tip {
        display: flex;
        gap: .5rem;
        align-items: flex-start;
        font-size: .88rem;
        color: var(--mm-text);
        padding: .35rem 0;
    }
    .mm-tip span.dot {
        color: var(--mm-primary);
        font-weight: 700;
    }

    /* ---------- Cards ---------- */
    .mm-card {
        background: var(--mm-surface);
        border: 1px solid var(--mm-border);
        border-radius: var(--mm-radius);
        padding: 1.25rem 1.35rem;
        box-shadow: var(--mm-shadow);
        margin-bottom: 1rem;
    }

    /* ---------- Buttons ---------- */
    .stButton > button {
        border-radius: 999px;
        border: 1px solid var(--mm-border);
        background: #ffffff;
        color: var(--mm-text);
        font-weight: 600;
        padding: .55rem 1rem;
        transition: all .18s ease;
    }
    .stButton > button:hover {
        border-color: var(--mm-primary-2);
        color: var(--mm-primary);
        background: #f3faf6;
        transform: translateY(-1px);
        box-shadow: 0 6px 16px rgba(47,107,79,0.12);
    }
    .stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--mm-primary) 0%, var(--mm-primary-2) 100%);
        color: #ffffff;
        border: none;
        box-shadow: 0 6px 18px rgba(47,107,79,0.25);
        animation: pulseSoft 2.5s infinite;
    }
    .stButton > button[kind="primary"]:hover {
        color: #ffffff;
        filter: brightness(1.05);
    }

    /* ---------- Chat bubbles ---------- */
    div[data-testid="stChatMessage"] {
        background: var(--mm-surface);
        border: 1px solid var(--mm-border);
        border-radius: var(--mm-radius);
        padding: 1rem 1.1rem;
        box-shadow: 0 2px 10px rgba(31,42,36,0.04);
        margin-bottom: .75rem;
        animation: fadeInUp 0.4s ease-out forwards;
        word-break: break-word;
    }
    div[data-testid="stChatMessage"]:has(div[data-testid="stChatMessageAvatarUser"]) {
        background: #f3faf6;
        border-color: #d7e9df;
    }

    /* ---------- Chat input ---------- */
    div[data-testid="stChatInput"] {
        border-radius: 999px;
        border: 1px solid var(--mm-border);
        background: #ffffff;
        box-shadow: var(--mm-shadow);
    }
    div[data-testid="stChatInput"]:focus-within {
        border-color: var(--mm-primary-2);
        box-shadow: 0 0 0 3px rgba(63,138,102,0.15);
    }

    /* ---------- Alerts ---------- */
    div[data-testid="stAlert"] {
        border-radius: 10px;
    }

    /* ---------- Divider ---------- */
    hr {
        border: none;
        border-top: 1px solid var(--mm-border);
        margin: 1rem 0;
    }

    /* ---------- Section label ---------- */
    .mm-section-label {
        font-size: .8rem;
        font-weight: 700;
        letter-spacing: .08em;
        text-transform: uppercase;
        color: var(--mm-muted);
        margin: .25rem 0 .6rem 0;
    }
    /* ---------- Animations & Styling Enhancements ---------- */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulseSoft {
        0% { box-shadow: 0 0 0 0 rgba(63, 138, 102, 0.4); }
        70% { box-shadow: 0 0 0 10px rgba(63, 138, 102, 0); }
        100% { box-shadow: 0 0 0 0 rgba(63, 138, 102, 0); }
    }
    
    div[data-testid="stChatMessage"] h3 {
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        background: #e8f3ed;
        color: var(--mm-primary);
        padding: 0.3rem 0.6rem;
        border-radius: 6px;
        display: inline-block;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
        border-left: 3px solid var(--mm-primary-2);
    }
    
    .mm-fab {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        background-color: #d9381e;
        color: white !important;
        padding: 0.75rem 1.25rem;
        border-radius: 999px;
        font-weight: 600;
        text-decoration: none;
        box-shadow: 0 4px 12px rgba(217, 56, 30, 0.3);
        z-index: 9999;
        transition: all 0.2s ease;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .mm-fab:hover {
        background-color: #bd2a13;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(217, 56, 30, 0.4);
    }
    </style>
    
    <a href="https://findahelpline.com/" class="mm-fab" target="_blank" title="Find a Helpline Worldwide">🚨 Crisis Resources</a>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "mood_logged" not in st.session_state:
    st.session_state.mood_logged = False


if "groq_client" not in st.session_state:
    api_key = os.getenv("GROQ_API_KEY")
    st.session_state.groq_client = Groq(api_key=api_key) if api_key else None

# --------------------------------------------------
# SYSTEM PROMPT
# --------------------------------------------------
SYSTEM_PROMPT = """
You are an advanced, clinical-grade Medical AI named Dr. MindfulMate, operating with the professionalism, analytical rigor, and empathetic bedside manner of an elite, board-certified physician.

Your Directives:

1. CLINICAL ASSESSMENT: Listen carefully to the user's symptoms, concerns, or questions. Ask highly targeted, relevant follow-up questions to gather necessary medical context (duration, severity, onset, associated symptoms) just like a doctor would during an anamnesis.

2. EVIDENCE-BASED REASONING: Base all information on established medical science and peer-reviewed guidelines. Use precise medical terminology when appropriate, but always explain it in clear, accessible language for the patient.

3. EMPATHY & TONE: Maintain a calm, authoritative, yet deeply empathetic and reassuring tone. You are here to heal, comfort, and guide. Never shame, judge, or dismiss the user's feelings.

4. STRUCTURED RESPONSES: Organize your responses logically using clear headings such as:
   - Clinical Impression
   - Recommended Next Steps
   - Symptom Relief & Management
   - Follow-up Questions

5. CRITICAL DISCLAIMER & TRIAGE: You must clarify that you are providing informational triage and support, not a definitive diagnosis or a prescription. If symptoms suggest a medical or psychiatric emergency (e.g., chest pain, severe shortness of breath, sudden numbness, suicidal ideation, or self-harm), you MUST immediately and assertively instruct the patient to contact local emergency services (like 911), go to the nearest emergency room, or call a crisis hotline. Safety is paramount.
"""

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------
with st.sidebar:
    st.markdown(
        """
        <div class="mm-brand">🌿 MindfulMate</div>
        <div class="mm-brand-sub">Welcome to your safe space.</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="mm-disclaimer">
            <strong>Disclaimer</strong><br/>
            MindfulMate is an AI chatbot designed for general mental
            wellness support, stress relief, and informational guidance.
            It is <strong>NOT</strong> a substitute for professional
            medical advice, diagnosis, treatment, or therapy.<br/><br/>
            If you are experiencing a mental health crisis or believe
            you may be in immediate danger, contact local emergency
            services or a crisis helpline immediately.
        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown('<div class="mm-section-label">Tips for using MindfulMate</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="mm-tip"><span class="dot">•</span> Be honest about how you feel.</div>
        <div class="mm-tip"><span class="dot">•</span> Use the quick starters if you don't know what to say.</div>
        <div class="mm-tip"><span class="dot">•</span> Take slow, deep breaths.</div>
        <div class="mm-tip"><span class="dot">•</span> Seek professional help when needed.</div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.caption("v1.0 · Built with Streamlit + Groq")

# --------------------------------------------------
# HEADER
# --------------------------------------------------
st.markdown(
    """
    <div class="mm-hero">
        <span class="mm-badge">Wellness Companion</span>
        <h1>Hi there! I'm MindfulMate 🌿</h1>
        <p>I'm here to listen, support, and help you find a moment of calm.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# API KEY CHECK
# --------------------------------------------------
if not st.session_state.groq_client:
    st.error(
        "⚠️ **GROQ_API_KEY** is not set. "
        "Please add it to your `.env` file and restart the app."
    )
    st.stop()

# --------------------------------------------------
# MOOD CHECK-IN
# --------------------------------------------------
if not st.session_state.mood_logged:

    with st.container(border=True):
        st.markdown("### How are you feeling today?")
        st.caption("Your mood helps MindfulMate respond with more care.")

        mood = st.select_slider(
            "Rate your current mood:",
            options=["Struggling", "Anxious", "Okay", "Good", "Great"],
            value="Okay",
            label_visibility="collapsed",
        )

        st.markdown(
            f"<div style='text-align:center;color:#2f6b4f;font-weight:600;"
            f"margin:.25rem 0 .85rem 0;'>You selected: {mood}</div>",
            unsafe_allow_html=True,
        )

        if st.button("Start Chatting →", use_container_width=True, type="primary"):
            st.session_state.mood_logged = True

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": (
                        f"[Mood Context: The user indicated that they "
                        f"are feeling '{mood}' today. "
                        "Acknowledge this gently in your first response.]"
                    ),
                }
            )
            st.rerun()

# --------------------------------------------------
# CHAT APPLICATION
# --------------------------------------------------
else:

    # ---------- Quick starters ----------
    if len(st.session_state.messages) <= 1:
        st.markdown('<div class="mm-section-label">Not sure where to start?</div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        starter_prompts = {
            "😰 I feel anxious": "I'm feeling really anxious right now. Can you help me calm down?",
            "🌬️ Breathing exercise": "Can you guide me through a simple breathing exercise?",
            "💬 Just need to vent": "I just need someone to listen to me vent for a bit. Is that okay?",
        }

        for col, (label, prompt) in zip([col1, col2, col3], starter_prompts.items()):
            with col:
                if st.button(label, use_container_width=True):
                    st.session_state.messages.append({"role": "user", "content": prompt})
                    st.rerun()

    st.markdown("---")

    # ---------- Chat history ----------
    for i, message in enumerate(st.session_state.messages):
        if message["content"].startswith("[Mood Context:") or message["content"].startswith("[System:"):
            continue
        avatar = "🧑" if message["role"] == "user" else "🌿"
        with st.chat_message(message["role"], avatar=avatar):
            st.markdown(message["content"])
            if message["role"] == "assistant":
                if st.button("🔊 Read Aloud", key=f"tts_{i}"):
                    from gtts import gTTS
                    import io
                    with st.spinner("Generating audio..."):
                        tts = gTTS(message["content"], lang="en")
                        fp = io.BytesIO()
                        tts.write_to_fp(fp)
                        fp.seek(0)
                        import base64
                        b64 = base64.b64encode(fp.read()).decode()
                        audio_html = f'<audio autoplay="true" controls style="height: 40px; margin-top: 10px;"><source src="data:audio/mp3;base64,{b64}" type="audio/mp3"></audio>'
                        st.markdown(audio_html, unsafe_allow_html=True)

    # ---------- Chat input & Voice ----------
    audio = mic_recorder(start_prompt="🎙️", stop_prompt="🛑", key="recorder")
    
    prompt = st.chat_input("Type your message here...")
    
    if audio and not prompt:
        import io
        audio_file = io.BytesIO(audio['bytes'])
        audio_file.name = "audio.wav"
        try:
            with st.spinner("Transcribing audio..."):
                transcription = st.session_state.groq_client.audio.transcriptions.create(
                    file=(audio_file.name, audio_file.read()),
                    model="whisper-large-v3",
                )
                prompt = transcription.text
        except Exception as e:
            st.error(f"Audio Transcription Error: {e}")

    if prompt:
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user", avatar="🧑"):
            st.markdown(prompt)

    # ---------- Generate AI response ----------
    if (
        st.session_state.messages
        and st.session_state.messages[-1]["role"] == "user"
        and not st.session_state.messages[-1]["content"].startswith("[Mood Context:")
    ):
        with st.chat_message("assistant", avatar="🌿"):
            message_placeholder = st.empty()
            full_response = ""

            # Dynamically append a length constraint to prevent hitting the strict 1000 token limit
            api_messages = [{"role": "system", "content": SYSTEM_PROMPT + "\n\n[CRITICAL DIRECTIVE: You MUST keep your responses concise, ideally under 150 words. Do not give overly long answers, or your response will be cut off mid-sentence.]"}]
            api_messages += st.session_state.messages[:-1]
            
            user_query = st.session_state.messages[-1]["content"]
            
            api_messages.append({"role": "user", "content": user_query})

            try:
                with st.spinner("Dr. MindfulMate is typing..."):
                    stream = st.session_state.groq_client.chat.completions.create(
                        model="qwen/qwen3.8-27b",
                        messages=api_messages,
                        max_tokens=800,
                        stream=True,
                    )

                for chunk in stream:
                    if chunk.choices and chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
                        message_placeholder.markdown(full_response + "▌")

                message_placeholder.markdown(full_response)

                st.session_state.messages.append(
                    {"role": "assistant", "content": full_response}
                )

            except Exception as e:
                st.error(f"An error occurred while generating the response: {e}")

    # ---------- Inject JS to attach Mic to Chatbox ----------
    components.html(
        """
        <script>
            const parentDoc = window.parent.document;
            
            function moveMic() {
                const micFrames = parentDoc.querySelectorAll('iframe[title*="mic_recorder"]');
                const chatInput = parentDoc.querySelector('div[data-testid="stChatInput"]');
                
                if (micFrames.length > 0 && chatInput) {
                    const mic = micFrames[0];
                    const micContainer = mic.closest('div[data-testid="stElementContainer"]');
                    
                    if (micContainer && !micContainer.dataset.moved) {
                        // Position the mic container inside the chat input
                        micContainer.style.position = 'absolute';
                        micContainer.style.right = '3.5rem';
                        micContainer.style.bottom = '20px';
                        micContainer.style.zIndex = '99999';
                        micContainer.style.width = '45px';
                        micContainer.style.transform = 'scale(1.4)';
                        micContainer.style.transformOrigin = 'bottom right';
                        micContainer.dataset.moved = 'true';
                        
                        chatInput.appendChild(micContainer);
                        
                        // Add right padding to the chat textarea so text doesn't overlap mic
                        const textarea = chatInput.querySelector('textarea');
                        if (textarea) {
                            textarea.style.paddingRight = '6rem';
                        }
                    }
                }
            }
            
            moveMic();
            const observer = new MutationObserver(moveMic);
            observer.observe(parentDoc.body, { childList: true, subtree: true });
        </script>
        """,
        height=0,
        width=0,
    )
