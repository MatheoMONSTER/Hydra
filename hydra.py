import tkinter as tk

def on_closing():
    global window_count
    window_count += 2
    create_window()

def create_window():
    global window_count
    message = "Cut one head, the other will grow"
    window = tk.Tk()
    window.protocol("WM_DELETE_WINDOW", on_closing)
    window.geometry("500x500")
    label = tk.Label(window, text=message)
    label.pack()
    window.mainloop()

window_count = 1
create_window()
