import tkinter as tk
from openpyxl import Workbook

def save_student_details():
    name = name_entry.get()
    age = age_entry.get()
    grade = grade_entry.get()
    # Create a new row in the Excel file and write the student details
    worksheet.append([name, age, grade])
    
    workbook.save('student_details.xlsx')

# Create a tkinter window
window = tk.Tk()
window.title("Student Details")

# Create labels and entry widgets for the student details
name_label = tk.Label(window, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=0, column=1)

age_label = tk.Label(window, text="Age:")
age_label.grid(row=1, column=0)
age_entry = tk.Entry(window)
age_entry.grid(row=1, column=1)

grade_label = tk.Label(window, text="Grade:")
grade_label.grid(row=2, column=0)
grade_entry = tk.Entry(window)
grade_entry.grid(row=2, column=1)

# Create a button to save the student details
save_button = tk.Button(window, text="Save", command=save_student_details)
save_button.grid(row=3, column=1)

# Create a new Excel workbook and worksheet
workbook = Workbook()
worksheet = workbook.active

# Add column headers to the worksheet
worksheet.append(["Name", "Age", "Grade"])

# Start the tkinter event loop
window.mainloop()
