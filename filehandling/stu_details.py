import tkinter as tk
from openpyxl import Workbook

class StudentDetails(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Name:").grid(row=0, column=0)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.master, text="Age:").grid(row=1, column=0)
        self.age_entry = tk.Entry(self.master)
        self.age_entry.grid(row=1, column=1)

        tk.Button(self.master, text="Save", command=self.save_details).grid(row=2, column=0)

    def save_details(self):
        name = self.name_entry.get()
        age = self.age_entry.get()

        # create a new workbook and worksheet
        wb = Workbook()
        ws = wb.active

        # write the student details to the worksheet
        ws.append([name, age])

        # save the workbook to a file
        wb.save('student_detail.xlsx')

        # clear the entry fields
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentDetails(master=root)
    app.mainloop()
