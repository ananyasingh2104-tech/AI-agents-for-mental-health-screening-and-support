# 🧠 MindCare

### WHO-Aligned AI System for Mental Well-Being Screening & Support

**MindCare** is an **offline, agent-based AI application** designed to support **mental well-being awareness**, **daily emotional check-ins**, and **early support**, while maintaining **privacy, safety, and ethical AI principles**.

The project is aligned with **SDG 8 – Decent Work & Economic Growth**, emphasizing how mental well-being directly impacts productivity, focus, and sustainable economic participation.

---

## 🌍 SDG Alignment

### **SDG 8 – Decent Work & Economic Growth**

Mental well-being is a foundational component of productive work and sustainable growth.
MindCare contributes to SDG-8 by:

* Reducing stress and burnout
* Supporting emotional balance and coping capacity
* Encouraging healthy routines that improve productivity
* Providing accessible, cost-free well-being support

---

## ✨ Key Features

* 🧠 **Agent-Based Architecture**
  Separate AI agents for screening, scoring, support, and safety escalation

* 📊 **Well-Being Score Dashboard**
  Dynamic score (0–100) reflecting emotional balance and coping capacity

* 🗓️ **Daily Check-In Mode**
  Structured self-reflection based on WHO mental well-being principles

* 🛡️ **Safety & Care Escalation**
  Detects high-risk language and responsibly guides users toward human support

* 📴 **100% Offline & Private**
  Powered by **Ollama** — no APIs, no data sharing, no internet required

* 🌱 **WHO-Aligned Language**
  Non-clinical, non-diagnostic, supportive, and stigma-free communication

---

## 🧩 AI Agent Workflow

```
User Input
   ↓
Critical Care Agent (Safety Check)
   ↓
Well-Being Scoring Agent
   ↓
Support Strategy Agent
   ↓
Reflective AI Agent (Ollama)
   ↓
Safe & Personalized Response
```

---

## 🛠️ Tech Stack

* **Python 3.9+**
* **Streamlit** – Interactive chat & dashboard UI
* **Ollama** – Local LLM runtime
* **LLaMA 3 (8B)** – Reasoning & response generation
* **JSON / Session State** – Context & interaction memory

---

## 🚀 Installation & Setup

### 1️⃣ Install Ollama

Download and install from:
👉 [https://ollama.com/download](https://ollama.com/download)

### 2️⃣ Pull the LLM Model

```bash
ollama pull llama3:8b
```

### 3️⃣ Install Python Dependencies

```bash
pip install streamlit
```

### 4️⃣ Run the Application

```bash
streamlit run mindcare.py
```

---

## 💬 Example Interaction

```
User: I’m not able to sleep properly
MindCare:
📊 Well-Being Score: 55/100 (Coping)

🌿 You seem to be coping, but something is clearly off.
Difficulty sleeping often signals mental or physical strain.
Would you like a sleep-support routine?
```

---

## ⚠️ Ethical Disclaimer

* MindCare **does NOT diagnose** mental health conditions
* It is **not a replacement** for professional care
* It promotes **self-awareness, coping, and early support**
* In high-risk situations, it encourages reaching out to **qualified professionals**

---

## 📁 Project Structure

```
├── mindcare.py                     # Main application
├── MindCare_Submission/             # Submission documents
│   ├── Lean_Canvas_MindCare.pdf
│   ├── Concept_Note_MindCare.pdf
│   └── MindCare_Project_Presentation.pptx
├── README.md
```

---

## 🎓 Use Cases

* Student mental well-being support
* Workplace burnout prevention
* Wellness awareness programs
* Academic capstone projects
* SDG-aligned AI demonstrations

---

## 🔮 Future Enhancements

* Weekly & monthly well-being trends
* WHO-5 Well-Being Index integration
* Multi-user profiles
* PDF well-being reports
* Mobile-friendly UI
* Institution-level dashboards

---

## 📜 License

This project is intended for **educational and non-clinical use**.
Open-source usage is encouraged with proper attribution.

---

## ⭐ Final Note

**MindCare** demonstrates how **responsible, privacy-first AI** can support mental well-being while contributing to **sustainable productivity and economic growth**.

---
