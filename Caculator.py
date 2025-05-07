import tkinter as tk
import time
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("My Calculator")
        self.root.geometry("360x550")
        self.root.resizable(False, False)
        self.root.configure(bg="Black")  #Too keep background Black

        self.equation = ""

        # Entry / Display
        self.entry_text = tk.StringVar()
        self.entry = tk.Entry(root, textvariable=self.entry_text, font=('Arial', 28, 'bold'),
                              bd=0, bg="white", fg="black", justify='right',
                              relief='flat', insertbackground="black")
        self.entry.pack(pady=(30, 20), padx=20, fill="x", ipady=20)

        # Start Button (centered)
        self.start_button = tk.Button(root, text="Start", font=('Arial', 18, 'bold'),
                                      bg="#4caf50", fg="white", width=15, height=2,
                                      command=self.start_calculator, relief='flat')
        self.start_button.pack(pady=150)

        # Integrate keyboard inputs
        self.root.bind('<Key>', self.keypress)

    def start_calculator(self):
        self.start_button.destroy()
        self.entry.config(state='normal')
        self.entry_text.set("Welcome User")
        self.entry.config(justify='center')
        self.root.update()
        time.sleep(1.5)

        self.entry_text.set("")
        self.entry.config(justify='right')
        self.entry.config(state='readonly')

        self.create_buttons()

    def press(self, val):
        self.equation += str(val)
        self.update_entry(self.equation)

    def clear(self):
        self.equation = ""
        self.update_entry("")

    def backspace(self):
        self.equation = self.equation[:-1]
        self.update_entry(self.equation)

    def equalpress(self):
        try:
            result = str(self.evaluate_equation(self.equation))
            self.equation = result
            self.update_entry(result)
        except:
            self.equation = ""
            self.update_entry("Error")

    def percentage(self):
        try:
            result = str(self.evaluate_equation(self.equation) / 100)
            self.equation = result
            self.update_entry(result)
        except:
            self.update_entry("Error")

    def squareroot(self):
        try:
            result = str(math.sqrt(self.evaluate_equation(self.equation)))
            self.equation = result
            self.update_entry(result)
        except:
            self.update_entry("Error")

    def delete_specific(self):
        if self.equation:
            self.equation = self.equation[:-1]  # Deletes last character
            self.update_entry(self.equation)

    def evaluate_equation(self, eq):
        # Handle equation evaluation and return result
        return eval(eq)

    def update_entry(self, value):
        self.entry.config(state='normal')
        self.entry_text.set(value)
        self.entry.config(state='readonly')

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="white")
        button_frame.pack(padx=10, pady=10, fill="both", expand=True)

        buttons = [
            ['C', 'Del', '/', '%'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '√']
        ]

        color_map = {
            'C': "#f44336",
            'Del': "#9c27b0",
            '=': "#4caf50",
            '/': "#2196f3",
            '*': "#2196f3",
            '-': "#2196f3",
            '+': "#2196f3",
            '%': "#3f51b5",
            '√': "#00bcd4"
        }

        for r, row in enumerate(buttons):
            for c, char in enumerate(row):
                if char == '':
                    continue
                action = (
                    self.clear if char == 'C' else
                    self.delete_specific if char == 'Del' else
                    self.equalpress if char == '=' else
                    self.percentage if char == '%' else
                    self.squareroot if char == '√' else
                    lambda ch=char: self.press(ch)
                )
                button = tk.Button(button_frame, text=char,
                                   font=('Arial', 18, 'bold'), fg="white",
                                   bg=color_map.get(char, "#424242"),
                                   relief='flat', bd=0,
                                   command=action)
                button.grid(row=r, column=c, sticky="nsew", padx=5, pady=5, ipadx=5, ipady=15)

        for i in range(len(buttons)):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)

    def keypress(self, event):
        key = event.char
        if key in '0123456789+-*/.':
            self.press(key)
        elif key == 'C':
            self.clear()
        elif key == '\r':  # Enter key
            self.equalpress()
        elif key == '\x08':  # Backspace key
            self.backspace()
        elif key == '%':
            self.percentage()
        elif key == 'r':  # Use 'r' for square root
            self.squareroot()

# --- Run App ---
if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()





