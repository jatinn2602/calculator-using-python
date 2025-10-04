import tkinter as tk
from tkinter import messagebox

# Custom colors for aesthetic and professional look
BG_COLOR = '#282c34'
FG_COLOR = '#abb2bf'
BUTTON_BG = '#3e4451'
BUTTON_FG = '#61afef'
BUTTON_HOVER_BG = '#528bff'
ENTRY_BG = '#21252b'
ENTRY_FG = '#ffffff'

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Professional Calculator")
        self.geometry("320x450")
        self.configure(bg=BG_COLOR)
        self.resizable(False, False)

        self.expression = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        entry_frame = tk.Frame(self, bg=BG_COLOR, pady=10)
        entry_frame.pack(fill='x')

        self.entry = tk.Entry(entry_frame, textvariable=self.expression, font=("Segoe UI", 28), bg=ENTRY_BG, fg=ENTRY_FG, borderwidth=0, justify='right')
        self.entry.pack(fill='both', padx=20, pady=10, ipady=15)

        buttons_frame = tk.Frame(self, bg=BG_COLOR)
        buttons_frame.pack(expand=True, fill='both')

        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        rows = 4
        cols = 4

        # Create buttons with hover effect
        for i in range(rows):
            buttons_frame.rowconfigure(i, weight=1)
            for j in range(cols):
                buttons_frame.columnconfigure(j, weight=1)
                text = button_texts[i * cols + j]
                button = tk.Button(
                    buttons_frame, text=text, font=("Segoe UI", 20), bg=BUTTON_BG, fg=BUTTON_FG,
                    activebackground=BUTTON_HOVER_BG, activeforeground='white', borderwidth=0,
                    command=lambda x=text: self.on_click(x)
                )
                button.grid(row=i, column=j, sticky='nsew', padx=4, pady=4)

    def on_click(self, char):
        if char == 'C':
            self.expression.set('')
        elif char == '=':
            self.calculate()
        else:
            current = self.expression.get()
            self.expression.set(current + char)

    def calculate(self):
        expr = self.expression.get()
        try:
            result = eval(expr)
            self.expression.set(result)
        except Exception:
            messagebox.showerror("Error", "Invalid Expression")
            self.expression.set('')

if __name__ == '__main__':
    app = Calculator()
    app.mainloop()