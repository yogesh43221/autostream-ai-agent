# AutoStream Agent - Quick Setup Guide

## 🚀 Quick Start (4 Steps)

### 1. Create Virtual Environment
```bash
python -m venv venv
```

### 2. Activate Virtual Environment
```bash
# Windows PowerShell
.\venv\Scripts\Activate.ps1

# Windows CMD
.\venv\Scripts\activate.bat

# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure API Key
```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your Gemini API key
# Get free key from: https://makersuite.google.com/app/apikey
```

### 5. Run the Agent
```bash
python app/main.py
```

---

## 📝 Test the Agent

Try this conversation flow:

```
You: Hi there!
Agent: [Greeting response]

You: What are your pricing plans?
Agent: [RAG response with Basic and Pro plans]

You: I want to try AutoStream
Agent: [Asks for your name]

You: John Doe
Agent: [Asks for email]

You: john@example.com
Agent: [Asks for platform]

You: Instagram
Agent: [Confirms and executes tool]
Console: "Lead captured successfully: John Doe, john@example.com, Instagram"
```

---

## 📂 Project Structure

```
app/
├── main.py              # Run this file
├── graph.py             # LangGraph workflow
├── state.py             # State schema
├── nodes/               # 5 agent nodes
├── rag/                 # Knowledge base + retriever
└── tools/               # Lead capture tool
```

---

## ✅ Features

- ✅ Intent classification (greeting/inquiry/high_intent)
- ✅ RAG-powered answers from local knowledge base
- ✅ Sequential lead collection (name → email → platform)
- ✅ Zero-cost (Gemini free tier + local embeddings)
- ✅ Stateful conversation (5-6+ turns)

---

## 📖 Full Documentation

See [README.md](file:///f:/MyProjects_YJ/Internshala/Social-to-Lead-Agentic-System-ServiceHive/README.md) for:
- Architecture details
- WhatsApp integration guide
- Complete API documentation
