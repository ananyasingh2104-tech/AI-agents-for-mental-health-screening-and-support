import streamlit as st
import subprocess
import datetime

# CONFIG

OLLAMA_MODEL = "llama3:8b"


# OLLAMA CALL (WINDOWS SAFE)

def call_llm(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL],
            input=prompt.encode("utf-8"),
            capture_output=True,
            timeout=60
        )
        output = result.stdout.decode("utf-8", errors="ignore").strip()
        return output if output else "I’m here with you."
    except Exception:
        return "I’m here with you."

# CRITICAL CARE AGENT

def critical_care_agent(text):
    phrases = [
        "suicide", "kill myself", "end my life",
        "i want to die", "no reason to live",
        "self harm", "hurt myself"
    ]
    return any(p in text.lower() for p in phrases)

def care_message():
    return (
        "🛑 **Thank you for telling me this.**\n\n"
        "What you’re experiencing matters, and you deserve real support.\n\n"
        "Please reach out **now**:\n"
        "- Someone you trust\n"
        "- A mental health professional\n"
        "- Emergency services if you feel unsafe\n\n"
        "**India Helpline:** AASRA – 91-9820466726\n\n"
        "If you want, we can pause and breathe together."
    )


# WELL-BEING SCORE AGENT

def wellbeing_score_agent(text):
    score = 100
    t = text.lower()

    strong_negatives = [
        "depressed", "hopeless", "worthless",
        "empty", "panic", "burnout", "exhausted"
    ]

    moderate_negatives = [
        "overthink", "overthinking",
        "sad", "low", "not feeling well",
        "can't sleep", "not able to sleep",
        "insomnia", "restless", "tired"
    ]

    for w in strong_negatives:
        if w in t:
            score -= 30

    for w in moderate_negatives:
        if w in t:
            score -= 20

    if critical_care_agent(text):
        score = 10

    return max(score, 0)

def wellbeing_label(score):
    if score >= 75:
        return "Thriving"
    if score >= 50:
        return "Coping"
    if score >= 25:
        return "Strained"
    return "Critical"


# SUPPORT STRATEGY (WHO-ALIGNED)

def support_strategy(score):
    if score >= 75:
        return (
            "🌱 **Your well-being seems mostly stable,** "
            "though something may be temporarily disturbing your balance.\n\n"
            "• Small issues like sleep loss or overthinking can have an impact\n"
            "• Gentle rest and care can help restore balance"
        )

    if score >= 50:
        return (
            "🌿 **You seem to be coping, but something is clearly weighing on you.**\n\n"
            "• Overthinking and low mood often mean your mind hasn’t had enough rest\n"
            "• Let’s focus on calming your thoughts and improving rest"
        )

    if score >= 25:
        return (
            "🔥 **Your well-being appears strained.**\n\n"
            "• Feeling sad, low, or mentally exhausted for a while is hard\n"
            "• You’re not weak for feeling this way\n"
            "• Slowing things down can help your nervous system recover"
        )

    return care_message()


# REFLECTIVE AI SUPPORT (REAL THINKING)

def reflective_support(context):
    prompt = f"""
You are MindCare, a WHO-aligned mental well-being support assistant.

The user is experiencing emotional distress.
Respond thoughtfully and specifically.

Rules:
- Do NOT diagnose
- Do NOT use clinical labels
- Do NOT say "tell me more" repeatedly
- Acknowledge feelings clearly
- Address sadness, overthinking, low mood, or sleep issues if present
- Offer 2–3 practical coping steps
- Use calm, human language

Recent user messages:
{context}

Respond with empathy and guidance.
"""
    return call_llm(prompt)


# STREAMLIT UI

st.set_page_config(page_title="MindCare", page_icon="🧠")
st.title("🧠 MindCare")
st.caption("WHO-aligned mental well-being support • Private • Offline")

# Chat memory
if "chat" not in st.session_state:
    st.session_state.chat = []

# Short-term context memory (IMPORTANT FIX)
if "context" not in st.session_state:
    st.session_state.context = []

# Tabs
tab1, tab2 = st.tabs(["💬 Well-Being Chat", "📊 Daily Check-In"])

with tab1:
    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

with tab2:
    st.subheader("🗓️ Daily Well-Being Check-In")

    mood = st.slider("Mood today", 0, 10, 5)
    energy = st.slider("Energy level", 0, 10, 5)
    sleep = st.slider("Sleep quality", 0, 10, 5)
    stress = st.slider("Stress level", 0, 10, 5)

    daily_score = int((mood + energy + sleep + (10 - stress)) / 4 * 10)
    st.metric("Today’s Well-Being Score", f"{daily_score}/100", wellbeing_label(daily_score))

    st.info(
        "This check-in supports self-awareness and reflection. "
        "It does not diagnose mental health conditions."
    )

# ✅ CHAT INPUT — ALWAYS AT BOTTOM
user_input = st.chat_input("How are you feeling right now?")

if user_input:
    # Store messages
    st.session_state.chat.append({"role": "user", "content": user_input})
    st.session_state.context.append(user_input)
    st.session_state.context = st.session_state.context[-6:]  # keep last 6 messages

    with st.chat_message("user"):
        st.markdown(user_input)

    # SAFETY FIRST
    if critical_care_agent(user_input):
        reply = care_message()
    else:
        combined_text = " ".join(st.session_state.context)
        score = wellbeing_score_agent(combined_text)
        label = wellbeing_label(score)

        st.session_state.chat.append({
            "role": "assistant",
            "content": f"📊 **Well-Being Score:** {score}/100 ({label})"
        })

        # Decide response intelligently
        if score <= 60:
            reply = reflective_support("\n".join(st.session_state.context))
        else:
            reply = support_strategy(score)

    st.session_state.chat.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)

st.markdown("---")
st.caption("⚠️ MindCare supports well-being awareness, not medical diagnosis")
st.caption(datetime.datetime.now().strftime("Session Time: %H:%M:%S"))
