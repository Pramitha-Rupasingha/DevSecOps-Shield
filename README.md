# 🛡️ DevSecOps Shield
### AI-Powered DevSecOps Security Pipeline

![Python](https://img.shields.io/badge/Python-3.14-blue?style=flat-square&logo=python)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-CI%2FCD-black?style=flat-square&logo=githubactions)
![AWS](https://img.shields.io/badge/AWS-Cloud-orange?style=flat-square&logo=amazonaws)
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
├── backend/               ← FastAPI backend
├── scanner/               ← Security scanning modules
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
| Cloud | AWS EC2, S3, IAM |
| AI Risk Scoring | Claude AI |

---

## ⚙️ Installation

```bash
# Clone repository
git clone https://github.com/Pramitha-Rupasingha/DevSecOps-Shield.git
cd DevSecOps-Shield

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install fastapi uvicorn bandit safety detect-secrets boto3 python-dotenv
```

---

## 🔑 Configuration

Create `.env` file in root:
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_REGION=us-east-1

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