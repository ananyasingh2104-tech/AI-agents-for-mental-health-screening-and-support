import streamlit as st
import subprocess
import datetime

# =============================
# CONFIG
# =============================
OLLAMA_MODEL = "llama3:8b"

# =============================
# OLLAMA CALL (WINDOWS SAFE)
# =============================
def call_llm(prompt):
    try:
        result = subprocess.run(
            ["ollama", "run", OLLAMA_MODEL],
            input=prompt.encode("utf-8"),
            capture_output=True,
            timeout=60
        )
        output = result.stdout.decode("utf-8", errors="ignore").strip()
        return output if output else "I’m here with you. Please tell me more."
    except Exception:
        return "I’m here with you. Please tell me more."

# =============================
# CRITICAL CARE AGENT
# =============================
def critical_care_agent(text):
    phrases = [
        "suicide", "kill myself", "end my life",
        "i want to die", "no reason to live",
        "self harm", "hurt myself"
    ]
    return any(p in text.lower() for p in phrases)

def care_message():
    return (
        "🛑 **Thank you for sharing this.**\n\n"
        "What you’re experiencing matters, and support is available.\n\n"
        "Please reach out **now**:\n"
        "- Someone you trust\n"
        "- A mental health professional\n"
        "- Emergency services if you feel unsafe\n\n"
        "**India Helpline:** AASRA – 91-9820466726\n\n"
        "If you want, we can slow your breathing together."
    )

# =============================
# WELL-BEING SCORE AGENT (FIXED)
# =============================
def wellbeing_score_agent(text):
    score = 100
    t = text.lower()

    strong_negatives = [
        "hopeless", "worthless", "empty",
        "panic", "burnout", "exhausted"
    ]

    moderate_negatives = [
        "not able to sleep", "can't sleep", "insomnia",
        "poor sleep", "restless", "tired",
        "not feeling well", "something new",
        "uneasy", "uncomfortable"
    ]

    for w in strong_negatives:
        if w in t:
            score -= 25

    for w in moderate_negatives:
        if w in t:
            score -= 15

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

# =============================
# SUPPORT STRATEGY (WHO-ALIGNED)
# =============================
def support_strategy(score):
    if score >= 75:
        return (
            "🌱 **Your well-being appears generally stable,** "
            "though you may be experiencing a short-term disruption.\n\n"
            "• Small issues like sleep loss can affect balance\n"
            "• Gentle care and rest can help restore stability\n\n"
            "Would you like help with sleep or relaxation?"
        )

    if score >= 50:
        return (
            "🌿 **You seem to be coping, but something is clearly off.**\n\n"
            "• Difficulty sleeping often signals mental or physical strain\n"
            "• Let’s focus on restoring rest and calm\n\n"
            "Would you like a sleep-support routine?"
        )

    if score >= 25:
        return (
            "🔥 **Your well-being looks strained.**\n\n"
            "• Persistent discomfort deserves attention\n"
            "• Slowing down may help your nervous system\n\n"
            "Would you like a grounding exercise?"
        )

    return care_message()

# =============================
# DAILY CHECK-IN DASHBOARD
# =============================
def daily_checkin():
    st.subheader("🗓️ Daily Well-Being Check-In")

    mood = st.slider("Mood today", 0, 10, 5)
    energy = st.slider("Energy level", 0, 10, 5)
    sleep = st.slider("Sleep quality", 0, 10, 5)
    stress = st.slider("Stress level", 0, 10, 5)

    score = int((mood + energy + sleep + (10 - stress)) / 4 * 10)
    label = wellbeing_label(score)

    st.metric("Today’s Well-Being Score", f"{score}/100", label)

    st.info(
        "This check-in supports self-awareness and reflection. "
        "It does not diagnose mental health conditions."
    )

# =============================
# REFLECTIVE AI SUPPORT (OLLAMA)
# =============================
def reflective_support(user_input):
    prompt = f"""
You are MindCare, a WHO-aligned wellbeing support assistant.

Rules:
- Do not diagnose
- Do not use disorder labels
- Use supportive, non-judgmental language
- Focus on well-being and coping capacity
- Offer gentle, practical guidance

User message:
{user_input}
"""
    return call_llm(prompt)

# =============================
# STREAMLIT UI
# =============================
st.set_page_config(page_title="MindCare", page_icon="🧠")
st.title("🧠 MindCare")
st.caption("WHO-aligned mental well-being screening & daily support")

tab1, tab2 = st.tabs(["💬 Well-Being Chat", "📊 Daily Check-In"])

with tab1:
    if "chat" not in st.session_state:
        st.session_state.chat = []

    for msg in st.session_state.chat:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

with tab2:
    daily_checkin()

# ✅ CHAT INPUT ALWAYS AT BOTTOM
user_input = st.chat_input("How are you feeling right now?")

if user_input:
    st.session_state.chat.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    if critical_care_agent(user_input):
        reply = care_message()
    else:
        score = wellbeing_score_agent(user_input)
        label = wellbeing_label(score)

        st.session_state.chat.append({
            "role": "assistant",
            "content": f"📊 **Well-Being Score:** {score}/100 ({label})"
        })

        reply = support_strategy(score)

        if label != "Critical":
            reply += "\n\n" + reflective_support(user_input)

    st.session_state.chat.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)

st.markdown("---")
st.caption("⚠️ MindCare supports well-being awareness, not medical diagnosis")
st.caption(datetime.datetime.now().strftime("Session Time: %H:%M:%S"))
