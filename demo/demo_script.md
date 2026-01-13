# AutoStream Agent - Demo Script

This script demonstrates all key features of the AutoStream conversational agent.

## Prerequisites

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your Gemini API key:
```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

3. Run the agent:
```bash
python app/main.py
```

---

## Demo Flow

### Turn 1: Greeting
**You:** Hi there!

**Expected Response:** Friendly greeting introducing AutoStream

---

### Turn 2: Pricing Inquiry (RAG)
**You:** What are your pricing plans?

**Expected Response:** 
- Basic Plan: $29/month, 10 videos/month, 720p
- Pro Plan: $79/month, unlimited videos, 4K, AI captions

---

### Turn 3: Policy Question (RAG)
**You:** What's your refund policy?

**Expected Response:** No refunds after 7 days

---

### Turn 4: High Intent Detection
**You:** I want to try AutoStream

**Expected Response:** Agent asks for your name

---

### Turn 5: Provide Name
**You:** John Doe

**Expected Response:** Agent asks for email

---

### Turn 6: Provide Email
**You:** john@example.com

**Expected Response:** Agent asks for platform

---

### Turn 7: Provide Platform
**You:** Instagram

**Expected Response:** 
- Confirmation message
- **Tool execution:** Console prints "Lead captured successfully: John Doe, john@example.com, Instagram"

---

## Verification Checklist

- [ ] Agent responds to greetings appropriately
- [ ] RAG answers are accurate and based on knowledge base
- [ ] High intent triggers lead collection flow
- [ ] Lead info is collected sequentially (name → email → platform)
- [ ] Tool executes ONLY when all fields are present
- [ ] Tool executes ONLY once (tool_called flag prevents duplicates)
- [ ] Conversation state persists across 5-6+ turns
- [ ] No paid APIs used (only Gemini free tier + local embeddings)

---

## Alternative Test Scenarios

### Scenario 2: Direct High Intent
**You:** I'm interested in signing up

**Expected:** Lead collection starts immediately

### Scenario 3: Multiple Inquiries
**You:** Tell me about the Pro plan features

**Expected:** RAG response about Pro plan (4K, unlimited, AI captions)

**You:** Do you have 24/7 support?

**Expected:** RAG response (24/7 support only on Pro plan)
