from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import csv
from tkinter import filedialog

mydata = []   # csv file data will be stored
class Attendance:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("ATTENDANCE SYSTEM")

        # **** Variables **** 

        self.var_atten_id = StringVar()
        self.var_dep = StringVar()
        self.var_name = StringVar()
        self.var_time = StringVar()
        self.var_date = StringVar()
        self.var_atten_status = StringVar()

        title_lable=Label(self.root,text="ATTENDANCE MANAGEMENT SYSTEM",font=("Courier",40,"bold"),bg="white",fg="green")
        title_lable.place(x=0,y=0,width=1530,height=40)
        
        # Background image
        img_4= Image.open(".\p6.jpg")
        img_4= img_4.resize((1530,850),Image.ANTIALIAS)  # high level image to low level
        self.photo_4 = ImageTk.PhotoImage(img_4)

        bg_img = Label(self.root,image=self.photo_4,bd=2,relief=RIDGE)
        bg_img.place(x=0,y=40,width=1530,height=850)
        
        main_frame = Frame(self.root,bd=2)
        main_frame.place(x=25,y=65,width=1480,height=800)

        # Left side Frame
        full_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,background="yellow")
        full_frame.place(x=20,y=20,width=1430,height=750)

       
        search_label = Label(full_frame,text="Search By Student ID / Student Name:",font=("times new roman",15,"bold"),background="yellow")
        search_label.grid(row=4,column=2,padx=10)#,padx=25,pady=15)
        self.var_searchTX=StringVar()


        self.var_search=StringVar()
        search_entry = ttk.Entry(full_frame,width=19,textvariable=self.var_search,font=("times new roman",13))
        search_entry.grid(row=4,column=3)#padx=10,pady=20)

        search_button = Button(full_frame,command=self.search_data,text="SEARCH",width=19,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        search_button.grid(row=4,column=7,padx=40,pady=20) 
        
        showall_button = Button(full_frame,command=self.fetchData,text="SHOW ALL",width=19,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        showall_button.grid(row=4,column=8,padx=40,pady=20)

        delete_button = Button(full_frame,command=self.delete_record,text="DELETE",width=19,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        delete_button.grid(row=4,column=9,padx=30,pady=20)


        # Buttons Frame
        btn_frame = Frame(full_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=500,y=670,width=400,height=36)

        import_button = Button(btn_frame,text="IMPORT csv",command=self.importcsv,width=19,height=1,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        import_button.grid(row=500,column=0)   
        
        export_button = Button(btn_frame,text="EXPORT csv",command=self.exportcsv,width=19,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        export_button.grid(row=500,column=1) 
        

        def back():
            self.root.destroy()
        b1_1 = Button(self.root,text="BACK",command=back,cursor="hand2",font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=1200,y=780,width=200,height=40)

        table_frame = Frame(full_frame,bd=2,relief=RIDGE)
        table_frame.place(x=60,y=80,width=1300,height=550)

        # **** SCROLL BAR TABLE ****
        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame,column=("name","id","dep","time","date","status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("name",text="Student Name")
        self.AttendanceReportTable.heading("id",text="Student ID")
        self.AttendanceReportTable.heading("dep",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("status",text="Attendance Status")

        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("name",width=130)
        self.AttendanceReportTable.column("id",width=130)
        self.AttendanceReportTable.column("dep",width=130)
        self.AttendanceReportTable.column("time",width=130)
        self.AttendanceReportTable.column("date",width=130)
        self.AttendanceReportTable.column("status",width=130)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
   

    def fetchData(self, rows=None):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        if rows is None:
        # Fetch all records from your data source (in this case, mydata)
            rows = mydata  # You may need to adjust this based on your data source
        
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)
        

    # ***** DELETE DATA *****

    # Add a new method for deleting a record
    def delete_record(self):
        try:
            # Get the selected record
            cursor_focus = self.AttendanceReportTable.focus()
            selected_record = self.AttendanceReportTable.item(cursor_focus)
            selected_values = selected_record["values"]

        # Confirm deletion with the user
            confirmation = messagebox.askyesno("Confirmation", f"Do you want to delete the record for {selected_values[0]} with ID {selected_values[1]}?")

            if confirmation:
            # Remove the record from the data source (mydata)
                mydata.remove(selected_values)

            # Update the table to reflect the changes
                self.fetchData()

        except Exception as es:
            messagebox.showerror("Error", f"Deletion Error: {str(es)}")


    # **** IMPORTING CSV FILE ****
    def importcsv(self):
        global mydata
        mydata.clear()
        file_name = filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)
        with open(file_name) as myfile:
            csvread = csv.reader(myfile,delimiter=",")
            header = next(csvread)  # Skip the header row
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # **** EXPORTING CSV FILE ****
    def exportcsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error","No Data Found To Export!",parent=self.root)
                return False
            file_name = filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("All File","*.*")),parent=self.root)    
            with open(file_name,mode="w",newline="") as myfile:
                exp_write = csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Your Data is Exported to "+os.path.basename(file_name)+"successfully!!")
            self.fetchData(mydata)
        except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)        

    def get_cursor(self,event=""):
        cursor_focus = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_focus)
        rows = content["values"]

        self.var_name.set(rows[0])
        self.var_atten_id.set(rows[1])
        self.var_dep.set(rows[2])
        self.var_time.set(rows[3])
        self.var_date.set(rows[4])
        self.var_atten_status.set(rows[5])

  
    
    # ***** SEARCH BY ID *****   

    def search_data(self):
        try:
            search_value = self.var_search.get().strip()  # Get the search value from the entry widget

            if not search_value:
                messagebox.showwarning("Warning", "Please enter a Student ID or Name to search.")
                return

            print(f"Searching for: {search_value}")

            with open('attendance.csv', 'r') as file:
                csv_reader = csv.reader(file)
                header = next(csv_reader)  # Read and discard the header row
                results = []

                for row in csv_reader:
                # Assuming student ID is in the 2nd column (index 1) and student name is in the 1st column (index 0)
                    if row[1].strip() == search_value or row[0].strip().lower() == search_value.lower():
                        results.append(row)

                if results:
                    self.fetchData(results)  # Display the result in the table
                else:
                    messagebox.showinfo("Info", f"No record found for: {search_value}")

        except Exception as es:
            messagebox.showerror("Error", f"Search Error: {str(es)}")  

    

if __name__ == "__main__":
    root=Tk()
    obj = Attendance(root)
    root.mainloop()