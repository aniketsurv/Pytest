import subprocess
import os
class checkDocker:
    
    @staticmethod     
    def checkRunningContainer():
        try:
            result = subprocess.run(['sudo', 'docker', 'ps', '--format', '{{.ID}} {{.Names}}'], stdout=subprocess.PIPE)
            output = result.stdout.decode('utf-8')
            file_path = "/home/linaro/db/matterHub"
            if os.path.exists(file_path):
                docker_containers = ["edgeudpserver","edgerouter","edgemaintenance","devicecontroller","devicebridge","edgeprocessor","edgepercentage"]
            else:
                docker_containers = ["driver-1700461828192_980","udpserver","diagnostic","souldapi","soulhub","soulsystem","pyprocess","portal","startstandalone"]
            if output:
                running_containers = []
                for line in output.splitlines():
                    container_id, container_name = line.split()
                    #print(f"Container ID: {container_id}, Name: {container_name}")
                    if container_name in docker_containers:
                        running_containers.append(container_name)
                if sorted(running_containers) == sorted(docker_containers):
                    return True
                else:
                    return False  # Some containers are missing
            else:
                return False
        except Exception as e:
            return f"An error occurred: {str(e)}"