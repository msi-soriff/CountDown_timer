import tkinter as tk
from datetime import timedelta

class ReverseTimeCounterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Reverse Time Counter App")

        self.duration = timedelta(minutes=1)  # Default duration is 1 minute
        self.time_left = self.duration
        self.running = False
        
        self.time_label = tk.Label(root, text=self.format_time(self.time_left), font=("Helvetica", 48))
        self.time_label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start", command=self.start)
        self.start_button.pack(side=tk.LEFT, padx=10)
        
        self.pause_button = tk.Button(root, text="Pause", command=self.pause)
        self.pause_button.pack(side=tk.LEFT, padx=10)
        
        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.pack(side=tk.LEFT, padx=10)
        
        self.set_button = tk.Button(root, text="Set Time", command=self.set_time)
        self.set_button.pack(side=tk.LEFT, padx=10)
        
        self.update_clock()
    
    def format_time(self, time):
        total_seconds = int(time.total_seconds())
        minutes, seconds = divmod(total_seconds, 60)
        return f"{minutes:02}:{seconds:02}"
    
    def update_clock(self):
        if self.running:
            if self.time_left > timedelta(0):
                self.time_left -= timedelta(seconds=1)
                self.time_label.config(text=self.format_time(self.time_left))
            else:
                self.running = False
                self.time_label.config(text="00:00")
        
        self.root.after(1000, self.update_clock)
    
    def start(self):
        if not self.running and self.time_left > timedelta(0):
            self.running = True
    
    def pause(self):
        if self.running:
            self.running = False
    
    def reset(self):
        self.running = False
        self.time_left = self.duration
        self.time_label.config(text=self.format_time(self.time_left))

    def set_time(self):
        self.running = False
        SetTimeWindow(self)

class SetTimeWindow:
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent.root)
        self.window.title("Set Time")

        self.minutes_label = tk.Label(self.window, text="Minutes:")
        self.minutes_label.grid(row=0, column=0)

        self.minutes_entry = tk.Entry(self.window)
        self.minutes_entry.grid(row=0, column=1)

        self.seconds_label = tk.Label(self.window, text="Seconds:")
        self.seconds_label.grid(row=1, column=0)

        self.seconds_entry = tk.Entry(self.window)
        self.seconds_entry.grid(row=1, column=1)

        self.set_button = tk.Button(self.window, text="Set", command=self.set_time)
        self.set_button.grid(row=2, column=0, columnspan=2)

    def set_time(self):
        try:
            minutes = int(self.minutes_entry.get())
            seconds = int(self.seconds_entry.get())
            self.parent.duration = timedelta(minutes=minutes, seconds=seconds)
            self.parent.reset()
            self.window.destroy()
        except ValueError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ReverseTimeCounterApp(root)
    root.mainloop()
