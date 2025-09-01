# Monitoring Script (Resource Usage)
import subprocess

def get_pod_metrics():
    result = subprocess.run(['kubectl', 'top', 'pods', '--no-headers'], capture_output=True, text=True)
    print(result.stdout)

if __name__ == '__main__':
    get_pod_metrics()
