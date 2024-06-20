import os
import pandas as pd
from tkinter import Tk, Label, StringVar

class Calculations:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculations")

        # Create a StringVar to dynamically update the label text
        self.result_var = StringVar()
        self.result_var.set("Total students and percentage attendance in each subject:\n\n")

        # Increase the font size (change the value of 25 to your desired size)
        self.result_label = Label(root, textvariable=self.result_var, font=("Helvetica", 25))
        self.result_label.pack()

        # Replace 'your_attendances_folder_path' with the actual path to the 'attendances' folder
        self.count_students_in_attendances(r'.\attendances')

    def count_students_in_attendances(self, attendances_folder):
        # Get a list of all subject folders in the 'attendances' folder
        subject_folders = [folder for folder in os.listdir(attendances_folder) if os.path.isdir(os.path.join(attendances_folder, folder))]

        # Iterate through each subject folder and count the number of students in each CSV file
        for subject in subject_folders:
            subject_folder = os.path.join(attendances_folder, subject)
            csv_files = [file for file in os.listdir(subject_folder) if file.endswith('.csv')]

            # Initialize the total_students count for the current subject
            total_students = 0

            # Iterate through each CSV file for the current subject
            for csv_file in csv_files:
                file_path = os.path.join(subject_folder, csv_file)

                # Read the CSV file into a DataFrame
                df = pd.read_csv(file_path)

                # Add the number of students in the current file to the total count
                total_students += len(df)

            # Calculate percentage attendance for each class
            if total_students > 0:
                percentage_attendance = (total_students / 55) * 100
            else:
                percentage_attendance = 0

            # Update the label text with the total students and percentage attendance for the current subject
            current_text = self.result_var.get()
            new_text = f"{current_text}{subject}: {total_students} students, {percentage_attendance:.2f}% attendance\n"
            self.result_var.set(new_text)

if __name__ == "__main__":
    root = Tk()
    obj = Calculations(root)
    root.mainloop()
