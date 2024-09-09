# pomodoro.py
from DeskController import DeskController
import time


def up_and_down_alert(controller: DeskController):
    base_height = controller.get_current_height()
    print(base_height)
    for i in range(3):
        controller.move_to_position((base_height + 10) if i % 2 == 0 else (base_height))

def pomodoro_timer(controller: DeskController):
    sitting_time = 25*60
    standing_time = 5*60

    while True:
        print("Moving to sitting position...")
        controller.move_to_position('sit')
        print("Sitting for 25 minutes...")
        time.sleep(sitting_time)

    
        print("Moving to standing position...")
        controller.move_to_position('stand')
        print("Standing for 5 minutes...")
        time.sleep(standing_time)

if __name__ == "__main__":
    controller = DeskController()
    time.sleep(4)
    try:
        pomodoro_timer(controller)
    except KeyboardInterrupt:
        controller.kill_old_server()
