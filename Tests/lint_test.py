import subprocess
import os


def test_flake8():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    file_to_test = os.path.join(base_dir, "hailstone.py")

    result = subprocess.run(['flake8', file_to_test], capture_output=True, text=True)
    assert result.returncode == 0, f"Linting failed:\n{result.stdout}"