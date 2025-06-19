import subprocess

def get_python_version():
    try:
        version = subprocess.check_output(["python", "--version"], stderr=subprocess.STDOUT)
        return version.decode("utf-8").strip()
    except subprocess.CalledProcessError:
        return "Error fetching Python version"

def get_installed_packages():
    try:
        installed_packages = subprocess.check_output([ "pip", "freeze"])
        return installed_packages.decode("utf-8").strip().split("\n")
    except subprocess.CalledProcessError:
        return "Error fetching installed packages"

def get_vscode_extensions():
    try:
        extensions = subprocess.check_output(["code", "--list-extensions"])
        return extensions.decode("utf-8").strip().split("\n")
    except subprocess.CalledProcessError:
        return "Error fetching VS Code extensions"

# Example Usage
if __name__ == "__main__":
    print(get_python_version())
    print(get_installed_packages())
    print(get_vscode_extensions())
