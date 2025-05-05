import tkinter as tk

def click(event):
    current = str(entry.get())
    entry.delete(0, tk.END)
    entry.insert(0, current + str(event.widget["text"]))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="groove", justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="we")

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
]

# Create button grid
for r, row in enumerate(buttons, start=1):
    for c, char in enumerate(row):
        if char == '=':
            btn = tk.Button(root, text=char, font=("Arial", 20), command=calculate)
        else:
            btn = tk.Button(root, text=char, font=("Arial", 20))
            btn.bind("<Button-1>", click)
        btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

# Clear button
clear_btn = tk.Button(root, text='C', font=("Arial", 20), command=clear)
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

# Expand layout for responsiveness
for i in range(6):  # rows 0-5
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # columns 0-3
    root.grid_columnconfigure(j, weight=1)

root.mainloop()

