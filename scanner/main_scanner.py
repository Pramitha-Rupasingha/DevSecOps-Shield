import json
from colorama import Fore, Style, init
from code_scanner import run_bandit_scan, run_secret_scan
from dependency_scanner import run_safety_scan
from container_scanner import run_trivy_scan

init(autoreset=True)

def calculate_risk_score(bandit_result, secret_result, dependency_result, container_result):
    """Calculate overall AI risk score 0-100"""
    score = 100
    
    # Secret detection — highest weight
    score -= secret_result.get("count", 0) * 25
    
    # Bandit code issues
    score -= bandit_result.get("count", 0) * 10
    
    # Dependency vulnerabilities
    score -= dependency_result.get("count", 0) * 8
    
    # Container vulnerabilities
    score -= container_result.get("critical", 0) * 15
    score -= container_result.get("high", 0) * 8
    score -= container_result.get("medium", 0) * 3
    
    # Clamp between 0-100
    score = max(0, min(100, score))
    return score


def get_risk_level(score):
    """Get risk level based on score"""
    if score >= 80:
        return "LOW", Fore.GREEN, "✅ SAFE TO DEPLOY"
    elif score >= 50:
        return "MEDIUM", Fore.YELLOW, "⚠️ REVIEW BEFORE DEPLOY"
    else:
        return "CRITICAL", Fore.RED, "❌ DEPLOYMENT BLOCKED"


def run_full_pipeline(image_name="python:3.11-slim"):
    """Run full DevSecOps security pipeline"""
    
    print(f"{Fore.CYAN}{'='*60}")
    print(f"  🛡️  DevSecOps Shield - Full Security Pipeline")
    print(f"{'='*60}{Style.RESET_ALL}")
    
    # Run all scanners
    bandit_result = run_bandit_scan(".")
    secret_result = run_secret_scan(".")
    dependency_result = run_safety_scan()
    container_result = run_trivy_scan(image_name)
    
    # Calculate risk score
    score = calculate_risk_score(
        bandit_result, 
        secret_result, 
        dependency_result, 
        container_result
    )
    
    risk_level, color, verdict = get_risk_level(score)
    
    # Print final report
    print(f"\n{Fore.CYAN}{'='*60}")
    print(f"  📊 SECURITY PIPELINE REPORT")
    print(f"{'='*60}{Style.RESET_ALL}")
    
    print(f"\n  🔐 Secrets Detected   : {secret_result.get('count', 0)}")
    print(f"  🧪 Code Issues        : {bandit_result.get('count', 0)}")
    print(f"  📦 Dependency CVEs    : {dependency_result.get('count', 0)}")
    print(f"  🐳 Container Critical : {container_result.get('critical', 0)}")
    print(f"  🐳 Container High     : {container_result.get('high', 0)}")
    
    print(f"\n{color}  🤖 AI Risk Score  : {score}/100")
    print(f"  ⚡ Risk Level     : {risk_level}")
    print(f"  🚦 Verdict        : {verdict}{Style.RESET_ALL}")
    
    print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
    
    # Save report to JSON
    report = {
        "risk_score": score,
        "risk_level": risk_level,
        "verdict": verdict,
        "bandit": bandit_result,
        "secrets": secret_result,
        "dependencies": dependency_result,
        "container": container_result
    }
    
    with open("security_report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"{Fore.GREEN}  📄 Report saved: security_report.json{Style.RESET_ALL}")
    
    return report


if __name__ == "__main__":
    run_full_pipeline()