import unittest
from src.scanner import get_python_version, get_installed_packages

class TestScanner(unittest.TestCase):
    
    def test_get_python_version(self):
        version = get_python_version()
        self.assertTrue(version.startswith("Python"))
    
    def test_get_installed_packages(self):
        packages = get_installed_packages()
        self.assertIsInstance(packages, list)
        self.assertTrue(len(packages) > 0)

if __name__ == "__main__":
    unittest.main()
