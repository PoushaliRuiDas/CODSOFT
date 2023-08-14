import tkinter as tk

def on_click(event):
    current = entry.get()
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(current)
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Entry widget for displaying the calculations and results
entry = tk.Entry(root, font="Arial 20", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C" 
]

# Create and place the buttons
row, col = 1, 0
for text in button_texts:
    button = tk.Button(root, text=text, font="Arial 20", width=5, height=2)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the main event loop
root.mainloop()
