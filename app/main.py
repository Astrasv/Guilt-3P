from random import random
import sys
import threading
import time
from flask import Flask, request
import logging

from data.browsers import BROWSER_PROCESS_NAMES
from data.roasts import ROASTS
from app.get_active_windows import ActiveWindows
from roast_modules.roaster_speaker import speak_alert, speak
from roast_modules.log_shame import log_shame
from roast_modules.send_nag import send_nag, send_alert
from roast_modules.bring_vscode import bring_vscode_to_front

from utils.break_input import handle_user_input


from data.forbidden import FORBIDDEN
from flask import Flask, request
from flask_cors import CORS

from app.state import current_state

app = Flask(__name__)

CORS(app) 

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

ActiveWindowsFetcher = ActiveWindows(sys.platform)

CURRENT_BROWSER_URL = ""
CONSECUTIVE_SECONDS = 0
BREAK_UNTIL_TIMESTAMP = 0  # Timestamp when break ends
BREAK_WARNING_SENT = False # To ensure we only warn once

@app.route('/update', methods=['POST'])
def receive_url():
    global CURRENT_BROWSER_URL
    data = request.json
    url = data.get('url', '')
    
    # Update the global variable
    CURRENT_BROWSER_URL = url
    return "OK", 200


@app.route('/health', methods=['GET'])
def health_check():
    return "Activity Spy is running.", 200

def run_server():
    """Starts the Flask server in a separate thread"""
    app.run(port=5000, use_reloader=False)

def main():
    global CONSECUTIVE_SECONDS


    print("--- 💀 THE DISAPPOINTED SENIOR DEV IS WATCHING 💀 ---")
    threading.Thread(target=run_server, daemon=True).start()
    threading.Thread(target=handle_user_input, daemon=True).start()
    try:
        while True:
            current_time = time.time()
            
            if current_time < current_state.BREAK_UNTIL_TIMESTAMP:
                remaining = int(current_state.BREAK_UNTIL_TIMESTAMP - current_time)
                
                if remaining <= 10 and not current_state.BREAK_WARNING_SENT:
                    print("\n BREAK ENDING SOON")
                    speak("Ten seconds left. Prepare to work.")
                    send_nag("Break Ending", "10 seconds remaining.")
                    current_state.BREAK_WARNING_SENT = True
                
                time.sleep(1)
                continue
                
            # If break JUST finished
            if current_state.BREAK_UNTIL_TIMESTAMP > 0 and current_time >= current_state.BREAK_UNTIL_TIMESTAMP:
                print("\nBREAK OVER. BACK TO WORK.")
                speak("Break is over. Get back to code.")
                current_state.BREAK_UNTIL_TIMESTAMP = 0 # Reset so we dont trigger this again
            
            app_name, window_title = ActiveWindowsFetcher.get_active_windows()
            is_distracted = False
            
            if any(b in app_name for b in ["chrome", "edge", "firefox", "brave"]):
                if any(d in CURRENT_BROWSER_URL for d in FORBIDDEN):
                    is_distracted = True
            
            if is_distracted:
                CONSECUTIVE_SECONDS += 1
                print(f"Distracted for: {CONSECUTIVE_SECONDS}s")

                if CONSECUTIVE_SECONDS == 2:
                    print("\n!!! DISTRACTION DETECTED !!!")
                    speak_alert("roast") # Speak a roast

                if CONSECUTIVE_SECONDS == 10:
                    send_nag()
                
                if CONSECUTIVE_SECONDS == 20:
                    log_shame(CURRENT_BROWSER_URL)
                    send_alert("CHECK YOUR DESKTOP - HALL OF SHAME", "Your distraction has been logged in hall of shame.")
                    speak_alert("roast") # Speak again

                if CONSECUTIVE_SECONDS > 30 and CONSECUTIVE_SECONDS % 10 == 0:
                    print("!!! FORCING WINDOW SWAP !!!")
                    bring_vscode_to_front()

            else:
                if CONSECUTIVE_SECONDS > 0:
                    print("-> User returned to work. Timer reset.")
                    speak_alert("praise")
                CONSECUTIVE_SECONDS = 0

            time.sleep(1)

    except KeyboardInterrupt:
        print("\nExiting.")


if __name__ == "__main__":
    main()