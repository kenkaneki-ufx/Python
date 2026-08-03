import tkinter as tk

window = tk.Tk()
window.title("GAME window")
window.geometry("300x200")
label = tk.Label(window, text="Hello User..\nThis is a GAME")
label.pack()
button = tk.Button(window, text="PLAY", width=25, command=window.destroy)
button.pack()
window.mainloop()

window1 = tk.Tk()
window1.title("Exit window")
window1.geometry("300x200")
label = tk.Label(window1, text="ThankYou for Playing the Game..\nGoodbyee...")
label.pack()
window1.mainloop()


import tkinter as tk

root = tk.Tk()
tk.Checkbutton(root, text="Male", variable=tk.IntVar()).grid(row=0, sticky=tk.W)
tk.Checkbutton(root, text="Female", variable=tk.IntVar()).grid(row=1, sticky=tk.W)
root.mainloop()

import tkinter as tk
from tkinter import ttk

def select(event):
    selected_item = combo_box.get()
    label.config(text="Selected Item: " + selected_item)
root = tk.Tk()
root.title("Combobox Example")
label = tk.Label(root, text="Selected Item:")
label.pack(pady=10)
# Create a Combobox widget
combo_box = ttk.Combobox(
    root,
    values=["Option 1", "Option 2", "Option 3"],
    state="readonly"
)
combo_box.pack(pady=5)
combo_box.set("Option 1")
combo_box.bind("<<ComboboxSelected>>", select)

root.mainloop()