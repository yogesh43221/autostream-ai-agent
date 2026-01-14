# 🎥 Enhanced Demo Video Script

## 📋 Overview
This script will help you record a professional demo video that showcases not just the features, but also your technical thinking and communication skills.

**Length:** 2-3 minutes
**Style:** Professional with optional voice-over

---

## 🎬 SCRIPT (With Voice-Over)

### **Opening (15 seconds)**

**[Show terminal ready to run]**

**Voice-over:**
> "Hi, I'm [Your Name]. I built this conversational AI agent for AutoStream as part of the ServiceHive assignment. What makes it different? Three things: it's truly conversational with smart interruption handling, it's zero-cost using Gemini's free tier and local embeddings, and it's production-ready with proper state management. Let me show you."

---

### **Scene 1: Start Agent (5 seconds)**

**[Type and run]**
```powershell
.\run_agent.ps1
```

**[Wait for startup message]**

---

### **Scene 2: Greeting (10 seconds)**

**[Type]**
```
Hi there!
```

**Voice-over (optional):**
> "First, natural greetings."

---

### **Scene 3: RAG Demo - Pricing (20 seconds)**

**[Type]**
```
What are your pricing plans?
```

**[Wait for response showing Basic & Pro plans]**

**Voice-over:**
> "The agent uses RAG with local embeddings to retrieve accurate information from the knowledge base. Notice it loads the embedding model and performs semantic search."

---

### **Scene 4: High-Intent Detection (15 seconds)**

**[Type]**
```
I want to try AutoStream
```

**[Wait for "May I have your name?"]**

**Voice-over:**
> "When it detects high intent, it automatically starts lead qualification."

---

### **Scene 5: Smart Interruption Handling (25 seconds)** ⭐ KEY DIFFERENTIATOR

**[Type]**
```
Wait, what's your refund policy?
```

**[Wait for refund policy response]**

**Voice-over:**
> "Here's the key feature: users can ask questions mid-flow. The agent detects the question pattern, answers it, then resumes lead collection. This was the trickiest part to implement—maintaining context while allowing interruptions."

---

### **Scene 6: Resume Lead Collection (10 seconds)**

**[Agent should ask for name again]**

**[Type]**
```
Okay, John Doe
```

**[Wait for email request]**

---

### **Scene 7: Email Collection (10 seconds)**

**[Type]**
```
john@example.com
```

**[Wait for platform request]**

---

### **Scene 8: Tool Execution (20 seconds)**

**[Type]**
```
Instagram
```

**[Wait for tool execution]**

**[IMPORTANT: Make sure this is visible]**
```
Lead captured successfully: John Doe, john@example.com, Instagram
```

**Voice-over:**
> "Once all information is collected, the tool executes automatically. The agent uses a dual-flag system to ensure the tool is called exactly once."

---

### **Closing (15 seconds)**

**[Type]**
```
quit
```

**Voice-over:**
> "If I had more time, I'd add conversation analytics to track conversion rates and A/B test different approaches. The code is production-ready with comprehensive documentation including lessons learned and a clear path to WhatsApp integration. Thanks for watching!"

---

## 🎯 ALTERNATIVE: Silent Demo (No Voice-Over)

If you prefer not to do voice-over, add text overlays at key moments:

- **After greeting:** "Natural conversation handling"
- **After RAG:** "Semantic search with local embeddings"
- **After interruption:** "Smart question detection during lead collection"
- **After tool execution:** "Automated lead capture with state management"

---

## 📝 KEY POINTS TO HIGHLIGHT

1. ✅ **RAG working** - Show "Loading embedding model" message
2. ✅ **High-intent detection** - Automatic transition to lead collection
3. ✅ **Smart interruptions** - THE DIFFERENTIATOR!
4. ✅ **Tool execution** - Console output clearly visible
5. ✅ **Professional presentation** - Clean, confident delivery

---

## 🎥 RECORDING TIPS

### **Before Recording:**
- [ ] Close unnecessary applications
- [ ] Clear terminal history
- [ ] Test the full flow once
- [ ] Ensure good lighting (if showing face)
- [ ] Test microphone (if doing voice-over)
- [ ] Disable notifications

### **During Recording:**
- [ ] Speak clearly and confidently
- [ ] Type at normal speed (not too fast)
- [ ] Pause briefly after each response
- [ ] Make sure console output is readable
- [ ] Don't rush - 2-3 minutes is perfect

### **After Recording:**
- [ ] Review the video
- [ ] Check audio quality
- [ ] Verify all 4 requirements are shown
- [ ] Trim any dead space

---

## ✅ REQUIREMENTS CHECKLIST

Your demo MUST show:
- [x] Agent answering pricing question (RAG)
- [x] Agent detecting high-intent
- [x] Agent collecting user details (name, email, platform)
- [x] Successful tool execution with console output

**BONUS (Makes you stand out):**
- [x] Smart interruption handling
- [x] Professional voice-over explaining technical decisions
- [x] Clear, confident presentation

---

## 🚀 YOU'RE READY!

This enhanced script will make your demo stand out by showing:
1. **Technical depth** - You understand the hard parts (state management, interruptions)
2. **Communication skills** - You can explain complex concepts clearly
3. **Product thinking** - You focus on user experience, not just features

**Good luck!** 🎬
