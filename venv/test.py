# pomodoro.py
from DeskController import DeskController
import time
import countdown
import threading

def up_and_down_alert(controller: DeskController):
    base_height = controller.get_current_height()
    for i in range(3):
        controller.move_to_position((base_height + 10) if i % 2 == 0 else (base_height))

def pomodoro_timer(controller: DeskController, sessions: int):

    
    pause_time = "5m"
    for i in range(sessions):
        total_time = "25m"  # Convert standing and sitting time to seconds
        countdown_thread = threading.Thread(target=controller.terminal_countdown, args=(total_time,))
        countdown_thread.start()
        controller.move_to_position('stand')
        time.sleep(12 * 60)  # Wait for standing time
        controller.move_to_position('sit')
        time.sleep(13 * 60)  # Wait for sitting time
        controller.move_to_position('pause')
        controller.terminal_countdown(pause_time)


if __name__ == "__main__":
    controller = DeskController()
    time.sleep(4)
    try:
        pomodoro_timer(controller, sessions=4)
    except KeyboardInterrupt:
        controller.kill_old_server()
