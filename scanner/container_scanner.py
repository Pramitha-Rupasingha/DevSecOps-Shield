import subprocess
import json
from colorama import Fore, Style, init

init(autoreset=True)

def run_trivy_scan(image_name="python:3.11-slim"):
    """Run Trivy container image vulnerability scan"""
    print(f"\n{Fore.CYAN}🐳 Running Container Scan (Trivy)...{Style.RESET_ALL}")
    print(f"{Fore.CYAN}   Image: {image_name}{Style.RESET_ALL}")
    
    try:
        result = subprocess.run(
            [
                "trivy", "image",
                "--format", "json",
                "--severity", "CRITICAL,HIGH,MEDIUM",
                "--quiet",
                image_name
            ],
            capture_output=True,
            text=True
        )
        
        report = json.loads(result.stdout) if result.stdout else {}
        results = report.get("Results", [])
        
        total_critical = 0
        total_high = 0
        total_medium = 0
        all_vulns = []
        
        for r in results:
            vulns = r.get("Vulnerabilities", []) or []
            for v in vulns:
                severity = v.get("Severity", "")
                if severity == "CRITICAL":
                    total_critical += 1
                elif severity == "HIGH":
                    total_high += 1
                elif severity == "MEDIUM":
                    total_medium += 1
                all_vulns.append(v)
        
        total = total_critical + total_high + total_medium
        
        if total == 0:
            print(f"{Fore.GREEN}✅ No vulnerabilities found!{Style.RESET_ALL}")
            return {"status": "clean", "vulnerabilities": [], "count": 0,
                    "critical": 0, "high": 0, "medium": 0}
        
        print(f"{Fore.RED}❌ Found {total} vulnerability(s):{Style.RESET_ALL}")
        print(f"{Fore.RED}   🔴 Critical : {total_critical}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}   🟠 High     : {total_high}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}   🟡 Medium   : {total_medium}{Style.RESET_ALL}")
        
        # Show top 5 critical/high
        shown = 0
        for v in all_vulns:
            if shown >= 5:
                break
            severity = v.get("Severity", "")
            if severity in ["CRITICAL", "HIGH"]:
                vid = v.get("VulnerabilityID", "")
                pkg = v.get("PkgName", "")
                fixed = v.get("FixedVersion", "No fix available")
                color = Fore.RED if severity == "CRITICAL" else Fore.YELLOW
                print(f"{color}   → [{severity}] {vid} | {pkg} | Fix: {fixed}{Style.RESET_ALL}")
                shown += 1
        
        return {
            "status": "vulnerable",
            "vulnerabilities": all_vulns,
            "count": total,
            "critical": total_critical,
            "high": total_high,
            "medium": total_medium
        }
    
    except FileNotFoundError:
        print(f"{Fore.YELLOW}⚠️ Trivy not installed.{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}   GitHub Actions eke automatically run wanawa!{Style.RESET_ALL}")
        return {"status": "error", "vulnerabilities": [], "count": 0,
                "critical": 0, "high": 0, "medium": 0}
    
    except Exception as e:
        print(f"{Fore.RED}❌ Container scan failed: {e}{Style.RESET_ALL}")
        return {"status": "error", "vulnerabilities": [], "count": 0,
                "critical": 0, "high": 0, "medium": 0}


if __name__ == "__main__":
    print(f"{Fore.CYAN}{'='*50}")
    print(f"🛡️  DevSecOps Shield - Container Scanner")
    print(f"{'='*50}{Style.RESET_ALL}")
    
    result = run_trivy_scan("python:3.11-slim")
    
    print(f"\n{Fore.CYAN}📊 Scan Summary:{Style.RESET_ALL}")
    print(f"  Critical : {result['critical']}")
    print(f"  High     : {result['high']}")
    print(f"  Medium   : {result['medium']}")
    print(f"  Total    : {result['count']}")
    
    if result['count'] == 0:
        print(f"{Fore.GREEN}  Status  : ✅ CLEAN{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}  Status  : ❌ VULNERABLE{Style.RESET_ALL}")