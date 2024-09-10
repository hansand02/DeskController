import subprocess
SERVER_ADDRESS = 'localhost'
SERVER_PORT = '9123'


class DeskController:
    def __init__(self):
        self.start_server()

    def terminal_countdown(self, time:str):
        """ runs countdown package
            use time string of format xxmxxs
            both minutes and seconds can be omitted
            max value of 60 on both
           """
        subprocess.run(["countdown", time ])

    def move_to_position(self, position):
        try:
            subprocess.run(["linak-controller", f"--move-to", str(position), "--forward"])
        except subprocess.CalledProcessError as error:
            print(f'Error happened while moving desk to height {position}mm, with error code: {error}')

    def start_server(self):
        try:
            subprocess.Popen(["linak-controller", "--server", "--server-address", SERVER_ADDRESS, "--server_port", SERVER_PORT, "--config", '../temp_config.yaml' ])
        except OSError as error:
            print(f'Error happened while starting the local server, with error code: {error}')

    def kill_old_server(self):
        """ Kill process on specified address and port """
        try:
            lines = subprocess.check_output(["lsof", "-i", f'@{SERVER_ADDRESS}:{SERVER_PORT}']).decode().splitlines()
            indexOfPid = lines[0].split().index("PID")
            pid = lines[1].split()[indexOfPid]
            subprocess.run(["kill", "-9", pid])
        except subprocess.CalledProcessError as error:
            print(f"Error occurred while trying to kill the old server, most likely there is no server running: {error}")

    def get_current_height(self) -> int:
        try:
            lines = subprocess.check_output(["linak-controller", "--forward"]).decode().splitlines()
            height_line = next(line for line in lines if line.startswith("Height:"))
            height_value = height_line.split(":")[1].strip()
            return int(height_value.removesuffix('mm'))
        except subprocess.CalledProcessError as error:
            print(f'An error occured during retrieval of the desk height, check your connection. Error: {error}')
    
    def __del__(self):
        self.kill_old_server()
