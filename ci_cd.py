import subprocess
import sys

def run_tests():
	try:
		result = subprocess.run(['pytest'],check=True)
		print("Test passed!")
	except subprocess.CalledProcessError as e:
		print(f"Tests failed: {e}")
		sys.exit(1)

if __name__ == "__main__":
	run_tests()
