from scanner import get_python_version, get_installed_packages, get_vscode_extensions
from vulnerability_checker import fetch_cve_data, classify_risk
import subprocess

def choose_scan_mode():
    """
    Provides the user with options for selecting the scan mode.
    """
    print("Choose scan mode:")
    print("1. Full Scan (Python, environments, IDE extensions, libraries)")
    print("2. Quick Scan (Python version and critical libraries only)")
    print("3. Custom Scan (Select specific areas to scan)")
    
    mode = input("Enter the number corresponding to your choice: ")
    return mode


def full_scan():
    """
    Full scan: Checks everything (Python, environments, IDE extensions, libraries)
    """
    print("Running Full Scan...\n")
    check_python_version()
    check_installed_environments()
    check_installed_libraries()
    check_installed_ide_extensions()


def quick_scan():
    """
    Quick scan: Only checks Python version and critical libraries
    """
    print("Running Quick Scan...\n")
    check_python_version()
    check_critical_libraries()


def custom_scan():
    """
    Custom scan: Allows the user to select which areas to scan
    """
    print("Running Custom Scan...\n")
    print("Select areas to scan:")
    scan_choice = input("1. Python version\n2. Libraries\n3. IDE extensions\nChoose options (e.g. 1, 2, 3): ")
    
    if "1" in scan_choice:
        check_python_version()
    if "2" in scan_choice:
        check_installed_libraries()
    if "3" in scan_choice:
        check_installed_ide_extensions()


def check_python_version():
    print("Checking Python version...")
    python_version = get_python_version()
    print(f"Python Version: {python_version}")


def check_installed_environments():
    """
    Check for installed environments like Anaconda or Miniconda.
    """
    print("Checking installed environments (Anaconda/Miniconda)...")
    try:
        result = subprocess.run(['conda', 'info'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print("Environments found:")
            print(result.stdout.decode())
        else:
            print("No Anaconda/Miniconda environments found.")
    except FileNotFoundError:
        print("Conda is not installed.")


def check_installed_libraries():
    print("Checking installed libraries (pip freeze)...")
    installed_libraries = get_installed_packages()
    print(f"Installed Libraries: {installed_libraries}")

    for package in installed_libraries:
        name, version = package.split("==")
        print(f"Checking vulnerabilities for {name} version {version}...")
        cve_data = fetch_cve_data(name, version)
        
        if cve_data:
            for cve in cve_data:
                risk = classify_risk(cve)
                print(f"CVE ID: {cve['cve']['CVE_data_meta']['ID']}")
                print(f"Description: {cve['cve']['description']['description_data'][0]['value']}")
                print(f"Published Date: {cve['publishedDate']}")
                print(f"Last Modified: {cve['lastModifiedDate']}")
                print(f"Risk Level: {risk}")
                print("-" * 50)
        else:
            print(f"No vulnerabilities found for {name} version {version}.")


def check_installed_ide_extensions():
    print("Checking installed IDE extensions (VS Code, PyCharm, Visual Studio)...")
    try:
        vscode_extensions = get_vscode_extensions()
        if vscode_extensions:
            print(f"Installed VS Code Extensions: {vscode_extensions}")
        else:
            print("No VS Code extensions found.")
    except FileNotFoundError:
        print("VS Code is not installed or not found in PATH.")
        print("Skipping VS Code extension check.")


def check_critical_libraries():
    print("Checking critical libraries...")
    critical_libraries = ['requests', 'flask', 'numpy']
    
    installed_packages = get_installed_packages()
    
    for package in critical_libraries:
        found_package = next((pkg for pkg in installed_packages if pkg.startswith(package)), None)
        
        if found_package:
            name, version = found_package.split("==")
            print(f"Checking vulnerabilities for {name} version {version}...")
            cve_data = fetch_cve_data(name, version)
            
            if cve_data:
                for cve in cve_data:
                    risk = classify_risk(cve)
                    print(f"CVE ID: {cve['cve']['CVE_data_meta']['ID']}")
                    print(f"Description: {cve['cve']['description']['description_data'][0]['value']}")
                    print(f"Risk Level: {risk}")
                    print("-" * 50)
        else:
            print(f"{package} is not installed or not found.")


def main():
    print("Starting the Python Security Vulnerability Scanner...")
    
    python_version = get_python_version()
    print(f"Python Version: {python_version}")
    
    installed_packages = get_installed_packages()
    print(f"Installed Packages: {installed_packages}")
    
    mode = choose_scan_mode()
    
    if mode == "1":
        full_scan()
    elif mode == "2":
        quick_scan()
    elif mode == "3":
        custom_scan()
    else:
        print("Invalid choice. Exiting.")
        
    input("Press Enter to exit...")


if __name__ == "__main__":
    main()
