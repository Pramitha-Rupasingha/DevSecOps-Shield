import subprocess
import json
import os
from colorama import Fore, Style, init

init(autoreset=True)

def run_bandit_scan(target_path="."):
    """Run Bandit static code analysis"""
    print(f"\n{Fore.CYAN}🧪 Running Static Code Analysis (Bandit)...{Style.RESET_ALL}")
    
    try:
        result = subprocess.run(
            ["python", "-m", "bandit", "-r", target_path, "-f", "json",
             "-x", ".git,frontend,node_modules"],
            capture_output=True,
            text=True
        )
        
        report = json.loads(result.stdout) if result.stdout else {}
        issues = report.get("results", [])
        
        if not issues:
            print(f"{Fore.GREEN}✅ No issues found!{Style.RESET_ALL}")
            return {"status": "clean", "issues": [], "count": 0}
        
        print(f"{Fore.RED}❌ Found {len(issues)} issue(s):{Style.RESET_ALL}")
        for issue in issues:
            severity = issue.get("issue_severity", "UNKNOWN")
            text = issue.get("issue_text", "")
            filename = issue.get("filename", "")
            line = issue.get("line_number", 0)
            
            color = Fore.RED if severity == "HIGH" else Fore.YELLOW
            print(f"{color}  [{severity}] {text}")
            print(f"  → File: {filename} Line: {line}{Style.RESET_ALL}")
        
        return {"status": "issues_found", "issues": issues, "count": len(issues)}
    
    except Exception as e:
        print(f"{Fore.RED}❌ Bandit scan failed: {e}{Style.RESET_ALL}")
        return {"status": "error", "issues": [], "count": 0}


def run_secret_scan(target_path="."):
    """Run detect-secrets scan"""
    print(f"\n{Fore.CYAN}🔐 Running Secret Detection...{Style.RESET_ALL}")
    
    try:
        result = subprocess.run(
            ["python", "-m", "detect_secrets", "scan", target_path],
            capture_output=True,
            text=True
        )
        
        report = json.loads(result.stdout) if result.stdout else {}
        secrets = report.get("results", {})
        
        if not secrets:
            print(f"{Fore.GREEN}✅ No secrets detected!{Style.RESET_ALL}")
            return {"status": "clean", "secrets": {}, "count": 0}
        
        total = sum(len(v) for v in secrets.values())
        print(f"{Fore.RED}❌ Found {total} secret(s)!{Style.RESET_ALL}")
        for file, items in secrets.items():
            for item in items:
                print(f"{Fore.RED}  → {file} Line: {item.get('line_number')}: {item.get('type')}{Style.RESET_ALL}")
        
        return {"status": "secrets_found", "secrets": secrets, "count": total}
    
    except Exception as e:
        print(f"{Fore.RED}❌ Secret scan failed: {e}{Style.RESET_ALL}")
        return {"status": "error", "secrets": {}, "count": 0}


if __name__ == "__main__":
    print(f"{Fore.CYAN}{'='*50}")
    print(f"🛡️  DevSecOps Shield - Code Scanner")
    print(f"{'='*50}{Style.RESET_ALL}")
    
    bandit_result = run_bandit_scan(".")
    secret_result = run_secret_scan(".")
    
    print(f"\n{Fore.CYAN}📊 Scan Summary:{Style.RESET_ALL}")
    print(f"  Code Issues : {bandit_result['count']}")
    print(f"  Secrets     : {secret_result['count']}")