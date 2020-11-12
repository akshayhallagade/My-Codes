import tkinter as tk
window = tk.Tk()

# frame1 = tk.Frame(master=window, width=300, height=500, )
for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master=window, width=500, height=500,
            relief=tk.RAISED,
            borderwidth=1,
            bg="red"
        )
        frame.grid(row=i, column=j)
        label = tk.Label(master=frame, text=f"Row{i}\nColumn{j}")
        label.pack()
window.mainloop()
