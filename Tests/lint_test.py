import subprocess
import os


def lint_function():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    file_to_test = os.path.join(base_dir, "hailstone.py")  # Pointing to the correct file for linting

    # Run linting on the file using the .flake8 file in the test folder
    result = subprocess.run(['flake8', '--config=Tests/.flake8', file_to_test], capture_output=True, text=True) # CI Pipeline
    # result = subprocess.run(['flake8', '--config=.flake8', file_to_test], capture_output=True, text=True) # Local Run

    # Fail the function if the linting is not correct
    assert result.returncode == 0, f"Linting failed:\n{result.stdout}"


if __name__ == '__main__':
    lint_function()
    print("Lint Test Passed")
