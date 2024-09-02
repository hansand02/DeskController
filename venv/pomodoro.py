# pomodoro.py

import subprocess
import time

result = subprocess.run(["linak-controller"],  capture_output=True, text=True)
print(result.stdout)

def move_to_position(position):
    subprocess.run(["linak-controller", f"--move-to", str(position), "--forward"])

def start_server():
    subprocess.Popen(["linak-controller", "--server"])

def pomodoro_timer():
    sitting_time = 25  # 25 minutes in seconds
    standing_time = 5  # 5 minutes in seconds

    while True:
        print("Moving to sitting position...")
        move_to_position(250)
        print("Sitting for 25 minutes...")
        time.sleep(sitting_time)

        print("Moving to standing position...")
        move_to_position(650)
        print("Standing for 5 minutes...")
        time.sleep(standing_time)

if __name__ == "__main__":
    subprocess.Popen('linak-controller --server', shell=True)
    start_server()
    pomodoro_timer()