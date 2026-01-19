import subprocess
import psutil


class ActiveWindows:
    def __init__(self,os):
        self.os = os
    
    def get_active_window_info_windows(self):
        """Windows: Returns (app_name, window_title)"""
        try:
            import ctypes
            from ctypes import wintypes
            
            user32 = ctypes.windll.user32
            h_wnd = user32.GetForegroundWindow()
            
            # Get Process ID (PID)
            pid = wintypes.DWORD()
            user32.GetWindowThreadProcessId(h_wnd, ctypes.byref(pid))
            
            # Get Process Name
            process = psutil.Process(pid.value)
            app_name = process.name()
            
            # Get Window Title
            length = user32.GetWindowTextLengthW(h_wnd)
            buf = ctypes.create_unicode_buffer(length + 1)
            user32.GetWindowTextW(h_wnd, buf, length + 1)
            window_title = buf.value
            url = None
            
            return app_name, window_title, url
        except Exception:
            return None, None


    
    def get_browser_url_macos(self, browser_name):
        """Specific AppleScript to extract URL from browsers on macOS"""
        if browser_name == "Google Chrome":
            script = 'tell application "Google Chrome" to return URL of active tab of front window'
        elif browser_name == "Safari":
            script = 'tell application "Safari" to return URL of front document'
        else:
            return None

        try:
            return subprocess.check_output(["osascript", "-e", script]).decode("utf-8").strip()
        except:
            return None

    def get_active_window_info_macos(self):
        """macOS: Returns (app_name, window_title, url)"""
        # 1. Get App Name and Window Title via AppleScript
        script = '''
        global frontApp, frontAppName, windowTitle
        set windowTitle to ""
        tell application "System Events"
            set frontApp to first application process whose frontmost is true
            set frontAppName to name of frontApp
            tell process frontAppName
                try
                    set windowTitle to value of attribute "AXTitle" of window 1
                end try
            end tell
        end tell
        return {frontAppName, windowTitle}
        '''
        
        try:
            result = subprocess.check_output(["osascript", "-e", script]).decode("utf-8").strip()
            app_name, window_title = result.split(", ")
        except:
            app_name, window_title = "Unknown", "Unknown"

        # 2. If Browser, try to get URL (macOS specific hack)
        url = None
        if app_name in ["Google Chrome", "Safari", "Brave Browser"]:
            url = self.get_browser_url_macos(app_name)
            
        return app_name, window_title, url


    
    def get_active_window_info_linux(self):
        """Linux: Returns (app_name, window_title). Requires xdotool."""
        try:
            # Get active window ID
            window_id = subprocess.check_output(["xdotool", "getactivewindow"]).decode("utf-8").strip()
            
            # Get Window Title
            window_title = subprocess.check_output(["xdotool", "getwindowname", window_id]).decode("utf-8").strip()
            
            # Get PID to find Process Name
            pid = subprocess.check_output(["xdotool", "getwindowpid", window_id]).decode("utf-8").strip()
            process = psutil.Process(int(pid))
            app_name = process.name()
            url = None
            
            return app_name, window_title, url
        except:
            return "Unknown", "Unknown"
    def get_active_windows(self):
        if self.os == "win32":
            return self.get_active_window_info_windows()
        elif self.os == "darwin":
            return self.get_active_window_info_macos()
        elif self.os.startswith("linux"):
            return self.get_active_window_info_linux()
        else:
            return None
