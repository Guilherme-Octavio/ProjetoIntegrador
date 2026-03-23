import Document, tkinter as tk
from tkinter import ttk, filedialog, messagebox
# from tkinter import

# global vars
Documents: list[Document.Document]

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('My Awesome App')
        self.geometry('1200x600')

        # label
        self.label = ttk.Label(self, text='Hello, Tkinter!')
        self.label.pack()

        # button
        self.button = ttk.Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()


    def button_clicked(self):
        file = filedialog.askopenfilename(
            initialdir="/",  # Start directory (e.g., "/" for root on many systems, "C:/" on Windows)
            title="Selecione um arquivo de texto", # Dialog window title
            filetypes=(
                ("Text files", "*.txt, *.pdf, *.docx"),  # Filter for text files
            )
        )
        if not ((file.endswith(".txt")) or (file.endswith(".docx")) or (file.endswith(".pdf"))):
            file = None
            messagebox.showerror("Essa extensão de arquivo não é permitida")

app = App()

app.mainloop()