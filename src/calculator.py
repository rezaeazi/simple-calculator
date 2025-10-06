import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("simple calculator")
        self.geometry("300x400")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):

        self.result_var = tk.StringVar()


        entry = tk.Entry(
            self,
            textvariable=self.result_var,
            font=("Arial", 20),
            bd=10,
            relief=tk.RIDGE,
            justify='right'
        )
        entry.pack(fill='both', ipadx=8, ipady=8, padx=10, pady=10)


        buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+']
        ]


        for row in buttons:
            frame = tk.Frame(self)
            frame.pack(expand=True, fill='both')
            for btn_text in row:
                btn = tk.Button(
                    frame,
                    text=btn_text,
                    font=("Arial", 18),
                    command=lambda txt=btn_text: self.on_button_click(txt)
                )
                btn.pack(side='left', expand=True, fill='both')

    def on_button_click(self, char):
        if char == '=':
            try:

                result = str(eval(self.result_var.get()))
                self.result_var.set(result)
            except Exception:
                self.result_var.set("خطا")
        else:

            current = self.result_var.get()
            self.result_var.set(current + char)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
