import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    if length <= 0:
        password_label.config(text="Invalid length!")
        return

    complexity = complexity_var.get()

    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    else:
        characters = string.ascii_letters + string.digits + string.punctuation

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    password_label.config(text="Generated Password: " + generated_password)

# Create the main application window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Password Length Input
length_label = tk.Label(root, text="Enter Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Password Complexity Options
complexity_var = tk.IntVar()
complexity_var.set(1)  # Default to low complexity
complexity_frame = tk.Frame(root)
complexity_frame.pack()

tk.Radiobutton(complexity_frame, text="Low Complexity (Letters)", variable=complexity_var, value=1).pack(anchor=tk.W)
tk.Radiobutton(complexity_frame, text="Medium Complexity (Letters and Digits)", variable=complexity_var, value=2).pack(anchor=tk.W)
tk.Radiobutton(complexity_frame, text="High Complexity (Letters, Digits, and Special Characters)", variable=complexity_var, value=3).pack(anchor=tk.W)

# Generate Password Button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Generated Password Display
password_label = tk.Label(root, text="Generated Password: ")
password_label.pack()

root.mainloop()
