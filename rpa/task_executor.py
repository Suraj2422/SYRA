import pyautogui
import time
import subprocess


class TaskExecutor:
    def __init__(self):
        pyautogui.FAILSAFE = True

        # Full path to Chrome executable (Windows)
        self.chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

        # Chrome profile directory for "Suraj Ghodke"
        self.chrome_profile_directory = "Profile 3"  # change if different

    def open_app(self, app_name):
        if app_name == "chrome":
            subprocess.Popen([
                self.chrome_path,
                f"--profile-directory={self.chrome_profile_directory}"
            ])
            time.sleep(3)
            return

        # Fallback for other apps
        pyautogui.press("win")
        time.sleep(1)
        pyautogui.write(app_name)
        time.sleep(1)
        pyautogui.press("enter")
        time.sleep(3)

    def type_text(self, text):
        time.sleep(1)

        # Switch focus back to Chrome
        pyautogui.hotkey("alt", "tab")
        time.sleep(0.4)

        # Focus address bar
        pyautogui.hotkey("ctrl", "l")
        time.sleep(0.3)

        pyautogui.write(text, interval=0.05)
