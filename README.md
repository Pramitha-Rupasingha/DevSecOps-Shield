# 🛡️ DevSecOps Shield
### AI-Powered DevSecOps Security Pipeline

<img width="1112" height="792" alt="Screenshot 2026-06-03 035200" src="https://github.com/user-attachments/assets/bb3aa9b4-bad2-400d-b7a7-bdff2db31fb1" />
<img width="1290" height="837" alt="image" src="https://github.com/user-attachments/assets/395063bb-972d-4e4e-8c2a-fcce172fb518" />

---

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-black?style=flat-square&logo=githubactions)
![AWS](https://img.shields.io/badge/AWS-EC2-orange?style=flat-square&logo=amazonaws)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue?style=flat-square&logo=docker)
![Security](https://img.shields.io/badge/Security-DevSecOps-red?style=flat-square&logo=shield)

---

## 💡 Overview

**DevSecOps Shield** is an AI-powered security pipeline that automatically scans source code, dependencies, and container images for vulnerabilities at every stage of the CI/CD process — blocking unsafe builds before they reach AWS deployment.

> "Shift-Left Security — catching vulnerabilities at the source, not in production."

---

## 🚀 Features

| Feature | Description |
|---------|-------------|
| 🔍 Secret Detection | Detects hardcoded credentials, API keys & tokens |
| 🧪 Static Code Analysis | Scans Python code for security flaws (SAST) |
| 📦 Dependency Scanning | Checks libraries for known CVEs |
| 🐳 Container Scanning | Analyzes Docker images before deployment |
| 🤖 AI Risk Scoring | Scores overall pipeline risk 0-100 |
| 🚦 Deployment Gating | Blocks unsafe builds from reaching AWS |
| 📊 Security Dashboard | Visual report of all scan results |

---

## 🔄 Pipeline Flow
Code Push
↓
🔐 Secret Detection (detect-secrets)
↓
🧪 Static Code Scan (Bandit)
↓
📦 Dependency Scan (Safety)
↓
🐳 Container Scan (Trivy)
↓
🤖 AI Risk Score
↓
✅ Deploy to AWS  /  ❌ Block & Alert

---

## 🧠 Architecture
DevSecOps-Shield/
├── .github/
│   └── workflows/         ← GitHub Actions CI/CD pipelines
├── frontend/              ← React security dashboard
│   └── Dockerfile
├── backend/               ← FastAPI backend
│   └── Dockerfile
├── scanner/               ← Security scanning modules
├── docker-compose.yml     ← Container orchestration
└── README.md

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|-----------|
| CI/CD | GitHub Actions |
| Secret Detection | detect-secrets |
| Code Scan | Bandit |
| Dependency Scan | Safety |
| Container Scan | Trivy |
| Backend | Python / FastAPI |
| Frontend | React |
| Containerization | Docker + Docker Compose |
| Cloud | AWS EC2 |
| AI Risk Scoring | Claude AI |

---

## 🐳 Docker Setup

```bash
# Clone repository
git clone https://github.com/Pramitha-Rupasingha/DevSecOps-Shield.git
cd DevSecOps-Shield

# Run with Docker Compose
docker compose up --build -d

# Access
# Frontend: http://localhost
# Backend API: http://localhost:8000
# Swagger UI: http://localhost:8000/docs
```

---

## ⚙️ Manual Setup

```bash
# Clone repository
git clone https://github.com/Pramitha-Rupasingha/DevSecOps-Shield.git
cd DevSecOps-Shield

# Install dependencies
pip install -r requirements.txt

# Run backend
cd backend
python -m uvicorn main:app --reload

# Run frontend
cd frontend
npm install
npm start
```

---

## 🔑 Configuration

Create `.env` file in root:
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=ap-south-1

---

## 📊 Sample Output
🔐 Secret Scan
→ No secrets detected ✅
🧪 Code Scan (Bandit)
→ eval() usage detected ❌ [HIGH]
→ Hardcoded password found ❌ [HIGH]
📦 Dependency Scan (Safety)
→ Flask 2.0 — CVE-2023-XXXX found ❌
🐳 Container Scan (Trivy)
→ Critical: 2  High: 5  Medium: 8
🤖 AI Risk Score: 35/100
❌ CRITICAL — Deployment Blocked

---

## 🌐 Live Demo

| Service | URL |
|---------|-----|
| 🖥️ Frontend Dashboard | http://13.235.246.11 |
| 🔌 Backend API | http://13.235.246.11:8000 |
| 📖 Swagger UI | http://13.235.246.11:8000/docs |

---

## 🔗 Related Projects

| Project | Description |
|---------|-------------|
| [AutoShield AI](https://github.com/Pramitha-Rupasingha/AutoShield-AI) | AI-Powered Cloud Security Automation |
| DevSecOps Shield | AI-Powered DevSecOps Pipeline ← You are here |

---

## 👨‍💻 Developer

**Pramitha Rupasingha**  
🎓 SLIIT — Cyber Security  
🔗 [GitHub](https://github.com/Pramitha-Rupasingha)

---

## 📜 License

MIT License — Free to use and modify.
