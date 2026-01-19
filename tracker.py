import time
import sys
from utils.get_active_windows import ActiveWindows


def main():
    print(f"--- Monitoring Activity on {sys.platform} ---")
    print("Press Ctrl+C to stop.\n")
    
    last_app = None
    last_title = None
    ActiveWindowsFetcher = ActiveWindows(sys.platform)
    
    try:
        while True:
            url = None

            app_name, window_title, url = ActiveWindowsFetcher.get_active_windows()

            if app_name != last_app or window_title != last_title:
                
                output = f"[App]: {app_name} | [Title]: {window_title}"
                
                if url:
                    output += f" | [URL]: {url}"
                
                print(output)
                
                last_app = app_name
                last_title = window_title

            time.sleep(1) 
            
    except KeyboardInterrupt:
        print("\nStopping monitor.")

if __name__ == "__main__":
    main()