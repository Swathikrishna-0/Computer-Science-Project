# Computer Science Project

A Python-based tool for scanning environments, discovering installed packages, checking for known vulnerabilities (CVEs), and providing risk classification. Future versions will include an alert/notification system.

## Project Structure

```
main.py                  # CLI entry point and orchestration
scanner.py               # Environment and package discovery
vulnerability_checker.py # CVE lookup and risk classification
tests/
    test_scanner.py
    test_vulnerability_checker.py
requirements.txt             # Python dependencies
README.md                    # Project overview and usage instructions
```

## Usage

1. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

2. **Run the main program:**
   ```
   python src/main.py
   ```

3. **Run tests:**
   ```
   python -m unittest discover tests
   ```

## Features

- Scans the environment for installed packages.
- Checks packages against known CVEs.
- Classifies risk levels.
- (Planned) Sends alerts/notifications for critical vulnerabilities.

## Requirements

- Python 3.7+
- See `requirements.txt` for dependencies.
