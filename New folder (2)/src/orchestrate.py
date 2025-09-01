# Orchestration Script (Deploy/Scale)
import subprocess

def deploy_microservice():
    subprocess.run(['kubectl', 'apply', '-f', '../k8s/deployment.yaml'])
    subprocess.run(['kubectl', 'apply', '-f', '../k8s/service.yaml'])

def scale_microservice(replicas):
    subprocess.run(['kubectl', 'scale', 'deployment/microservice', f'--replicas={replicas}'])

if __name__ == '__main__':
    deploy_microservice()
    # scale_microservice(3)
