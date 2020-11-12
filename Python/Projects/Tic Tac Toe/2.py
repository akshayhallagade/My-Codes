import tkinter as tk
window = tk.Tk()
entry = tk.Entry(  # used to get input in the GUI.
    fg="yellow",
    bg="blue",
    width=50
)
entry.pack()
name = entry.get()
print(name)
btn = tk.Button()
window.mainloop()
