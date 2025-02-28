import os
import subprocess
from connections.MqttConnection import FrontMqttConnection
from connections.Container import checkDocker
from utils import logConfig
logConfig.setup_logging()

class TestRunner:
    
    def ensure_pytest_installed(self):
        """Ensure pytest is installed using pip if not present."""
        try:
            import pytest
        except ImportError:
            subprocess.check_call(["sudo", "pip", "install", "pytest", "pytest-html"])
    
    def run_tests(self):
        self.ensure_pytest_installed()
        import pytest
        runningContainer = checkDocker.checkRunningContainer()
        if runningContainer:
            FrontMqttConnection.client_connection()
            container = {
                "MaintenanceFramework": ["test_token.py","test_validate.py"],
            }
            for test_folder, test_files in container.items():
                report_path = f"{test_folder}_report.html"  # e.g., hubInstallationFramework_report.html
                test_paths = [os.path.join(test_folder, test_file) for test_file in test_files]
                print(f"Running tests for {test_folder}...")
                result = pytest.main(["-v", "-s", "--html", report_path, "--self-contained-html"] + test_paths)
                if result != 0:
                    print(f"Some tests failed in {test_folder}. Test result code: {result}")
                    break
                else:
                    print(f"All tests passed in {test_folder}.")
            FrontMqttConnection.client_disconnect()
        else:
            print("Expected container not running-->",runningContainer)
            
if __name__ == "__main__":
    test_runner = TestRunner()
    test_runner.run_tests()
