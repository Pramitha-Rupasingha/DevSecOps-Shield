from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import os
import sys
from datetime import datetime

# Add scanner folder to path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'scanner'))

from code_scanner import run_bandit_scan, run_secret_scan
from dependency_scanner import run_safety_scan
from container_scanner import run_trivy_scan
from main_scanner import run_full_pipeline, calculate_risk_score, get_risk_level

app = FastAPI(
    title="🛡️ DevSecOps Shield API",
    description="AI-Powered DevSecOps Security Pipeline API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "name": "DevSecOps Shield",
        "version": "1.0.0",
        "status": "running",
        "timestamp": datetime.now().isoformat()
    }


@app.get("/health")
def health():
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


@app.post("/scan/full")
def full_scan():
    """Run full security pipeline scan"""
    try:
        report = run_full_pipeline()
        return {
            "status": "success",
            "timestamp": datetime.now().isoformat(),
            "report": report
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.post("/scan/code")
def code_scan():
    """Run code scan only"""
    try:
        bandit = run_bandit_scan(".")
        secrets = run_secret_scan(".")
        return {
            "status": "success",
            "timestamp": datetime.now().isoformat(),
            "bandit": bandit,
            "secrets": secrets
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.post("/scan/dependencies")
def dependency_scan():
    """Run dependency scan only"""
    try:
        result = run_safety_scan()
        return {
            "status": "success",
            "timestamp": datetime.now().isoformat(),
            "result": result
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}


@app.get("/report/latest")
def latest_report():
    """Get latest security report"""
    try:
        report_path = os.path.join(
            os.path.dirname(__file__), '..', 'scanner', 'security_report.json'
        )
        if os.path.exists(report_path):
            with open(report_path, "r") as f:
                report = json.load(f)
            return {"status": "success", "report": report}
        return {"status": "no_report", "message": "No report found. Run a scan first."}
    except Exception as e:
        return {"status": "error", "message": str(e)}