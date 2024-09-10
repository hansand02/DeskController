# pomodoro.py
from DeskController import DeskController
import time
import countdown


def up_and_down_alert(controller: DeskController):
    base_height = controller.get_current_height()
    for i in range(3):
        controller.move_to_position((base_height + 10) if i % 2 == 0 else (base_height))

def pomodoro_timer(controller: DeskController, sessions: int, firstType: str = 'stand'):
    if firstType not in ['stand', 'sit']:
        raise ValueError("firstType must be either 'stand' or 'sit'")
    
    working_time = "25m"
    pause_time = "5m"
    positions = ['stand', 'sit'] if firstType == 'stand' else ['sit', 'stand']
    for i in range(sessions):
        nextMove = positions[i%2]
        print("Moving to", nextMove)
        controller.move_to_position(nextMove)
        controller.terminal_countdown(working_time)

        controller.move_to_position('pause')
        controller.terminal_countdown(pause_time)
        time.sleep(pause_time)


if __name__ == "__main__":
    controller = DeskController()
    time.sleep(4)
    try:
        pomodoro_timer(controller, sessions=4)
    except KeyboardInterrupt:
        controller.kill_old_server()
