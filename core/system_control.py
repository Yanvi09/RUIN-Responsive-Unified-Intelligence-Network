import os
import subprocess
import psutil
import pyautogui
import keyboard
import ctypes
import webbrowser
import pyttsx3

# --------------------------------------------
# 🌐 Basic App Launchers
# --------------------------------------------

def open_gmail():
    os.system("start chrome https://mail.google.com")

def open_folder(path):
    os.startfile(path)

def open_vscode():
    subprocess.Popen(["C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"])
 

def open_app_by_path(path):
    subprocess.Popen(path)

def open_file_explorer():
    os.system("explorer")

def open_website(url):
    webbrowser.open(url)

# --------------------------------------------
# 🧾 Code Automation
# --------------------------------------------

def write_python_file(file_name, code):
    with open(file_name, "w") as f:
        f.write(code)
    subprocess.Popen([
        "C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe", file_name
    ])


def run_python_file(file_name):
    os.system(f"python {file_name}")

# --------------------------------------------
# 🧹 Process Manager
# --------------------------------------------

def kill_process(app_name):
    for proc in psutil.process_iter():
        try:
            if app_name.lower() in proc.name().lower():
                proc.kill()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

# --------------------------------------------
# 🧠 Advanced System Control
# --------------------------------------------



def lock_screen():
    ctypes.windll.user32.LockWorkStation()

def open_task_manager():
    os.system("taskmgr")

def restart_computer():
    os.system("shutdown /r /t 1")

def shutdown_computer():
    os.system("shutdown /s /t 1")

def mute_volume():
    keyboard.press_and_release("volume_mute")

def unmute_volume():
    keyboard.press_and_release("volume_mute")

# --------------------------------------------
# 🗣️ Voice Feedback (Offline)
# --------------------------------------------

def speak_status(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
