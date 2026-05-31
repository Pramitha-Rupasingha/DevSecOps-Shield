import subprocess
import json
from colorama import Fore, Style, init

init(autoreset=True)

def run_safety_scan():
    """Run Safety dependency vulnerability scan"""
    print(f"\n{Fore.CYAN}📦 Running Dependency Vulnerability Scan (Safety)...{Style.RESET_ALL}")
    
    try:
        result = subprocess.run(
            ["safety", "check", "--json"],
            capture_output=True,
            text=True
        )
        
        output = result.stdout if result.stdout else result.stderr
        
        try:
            report = json.loads(output)
        except json.JSONDecodeError:
            print(f"{Fore.GREEN}✅ No vulnerabilities found!{Style.RESET_ALL}")
            return {"status": "clean", "vulnerabilities": [], "count": 0}
        
        if not report:
            print(f"{Fore.GREEN}✅ No vulnerabilities found!{Style.RESET_ALL}")
            return {"status": "clean", "vulnerabilities": [], "count": 0}
        
        print(f"{Fore.RED}❌ Found {len(report)} vulnerability(s):{Style.RESET_ALL}")
        for vuln in report:
            pkg_name = vuln[0] if len(vuln) > 0 else "Unknown"
            affected = vuln[1] if len(vuln) > 1 else "Unknown"
            description = vuln[3] if len(vuln) > 3 else "No description"
            cve = vuln[4] if len(vuln) > 4 else "No CVE"
            
            print(f"{Fore.RED}  ❌ Package  : {pkg_name}")
            print(f"     Affected : {affected}")
            print(f"     CVE      : {cve}")
            print(f"     Info     : {description[:100]}...{Style.RESET_ALL}")
        
        return {"status": "vulnerable", "vulnerabilities": report, "count": len(report)}
    
    except FileNotFoundError:
        print(f"{Fore.YELLOW}⚠️ Safety not installed. Run: pip install safety{Style.RESET_ALL}")
        return {"status": "error", "vulnerabilities": [], "count": 0}
    
    except Exception as e:
        print(f"{Fore.RED}❌ Dependency scan failed: {e}{Style.RESET_ALL}")
        return {"status": "error", "vulnerabilities": [], "count": 0}


if __name__ == "__main__":
    print(f"{Fore.CYAN}{'='*50}")
    print(f"🛡️  DevSecOps Shield - Dependency Scanner")
    print(f"{'='*50}{Style.RESET_ALL}")
    
    result = run_dependency_scan()
    
    print(f"\n{Fore.CYAN}📊 Scan Summary:{Style.RESET_ALL}")
    print(f"  Vulnerabilities Found : {result['count']}")
    
    if result['count'] == 0:
        print(f"{Fore.GREEN}  Status : ✅ CLEAN{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}  Status : ❌ VULNERABLE{Style.RESET_ALL}")