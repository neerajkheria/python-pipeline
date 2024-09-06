import subprocess
import sys

def build_docker_image():
	try:
		subprocess.run(['docker','build','-t','my-app:latest','.'], check=True)
		print("Docker image built successfully!")
	except subprocess.CalledProcessError as e:
		print(f"Docker build failed: {e}")
		sys.exit(1)

if __name__ =="__main__":
	build_docker_image()
