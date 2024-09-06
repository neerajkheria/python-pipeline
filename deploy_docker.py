import paramiko
import sys

def deploy_docker_image(host, port, username, password):
	try:

		ssh = paramiko.SSHClient()
		ssh.set_missing_host_jey_policy(paramiko.AutoAddPolicy())
		ssh.connect(hostname=host, post=port, username=username, password=password)

		commands = [
		'sudo docker pull nkheria/python-ci-cd:latest',
		'sudo docker run -d -p 80:5000 nkheria/python-ci-cd:latest'
		]

		for cmd in commands:
			stdin, stout, stderr = ssh.exec_command(cmd)
			print(stdout.read().decode())
			print(stderr.read().decode())

		ssh.close()
		print("Deployment successful!")
	except Exception as e:
		print(f"Deployment failed!: {e}")
		sys.exit(1)


if __name__ == "__main__":
	host = '3.92.134.168'
	port = 22
	username = 'ubuntu'
	key_file = '/home/ubuntu/python-app/ansible-key.pem'

	deploy_docker_image(host, username, key_file)
