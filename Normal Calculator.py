import tkinter as tk

def press(key):
    entry.insert(tk.END, key)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        clear()
        entry.insert(0, result)
    except:
        clear()
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 20), borderwidth=5, relief="ridge", justify="right")
entry.pack(fill="x", padx=10, pady=10)

buttons = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+"
]

frame = tk.Frame(root)
frame.pack()

row = col = 0
for btn in buttons:
    action = lambda x=btn: calculate() if x == "=" else press(x)
    tk.Button(frame, text=btn, width=5, height=2,
              font=("Arial", 15),
              command=action).grid(row=row, column=col, padx=5, pady=5)
    col += 1
    if col > 3:
        col = 0
        row += 1

tk.Button(root, text="CLEAR", font=("Arial", 15),
          command=clear).pack(fill="x", padx=10, pady=10)

root.mainloop()