# AutoStream AI Agent - GitHub Push Guide

## 📛 Repository Name
**Recommended**: `autostream-ai-agent`

## 🚀 Step-by-Step Instructions

### Step 1: Create GitHub Repository

1. Go to: https://github.com/new
2. Repository name: `autostream-ai-agent`
3. Description: `Conversational AI agent built with LangGraph for AutoStream - Features RAG, intent detection, and automated lead capture`
4. **Public** repository
5. ❌ **DO NOT** initialize with README (we already have one)
6. Click "Create repository"

### Step 2: Initialize Git Locally

Open PowerShell in project directory and run:

```powershell
# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Complete AutoStream AI Agent with LangGraph, RAG, and lead capture"
```

### Step 3: Connect to GitHub

Replace `YOUR_USERNAME` with your actual GitHub username:

```powershell
# Add remote
git remote add origin https://github.com/YOUR_USERNAME/autostream-ai-agent.git

# Rename branch to main
git branch -M main

# Push to GitHub
git push -u origin main
```

### Step 4: Verify

1. Go to: `https://github.com/YOUR_USERNAME/autostream-ai-agent`
2. Check that all files are there
3. Verify README.md displays correctly

## ✅ What Gets Pushed

- ✅ All Python code (`app/`)
- ✅ requirements.txt
- ✅ README.md
- ✅ .env.example
- ✅ demo/demo_script.md
- ✅ .gitignore

## ❌ What Gets Ignored

- ❌ .env (your API key - SAFE!)
- ❌ venv/ (virtual environment)
- ❌ __pycache__/
- ❌ *.pyc files

## 🔐 Security Check

**IMPORTANT**: Make sure `.env` is in `.gitignore` so your API key is NOT pushed!

Already done: ✅ `.gitignore` includes `.env`

## 📝 After Pushing

Update your README.md to add:
- GitHub repository link
- Demo video link (when ready)
- Live demo link (when deployed)
