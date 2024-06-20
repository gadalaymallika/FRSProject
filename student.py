from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("STUDENT DETAILS")

        # **** Variables ****
        self.var_Dep = StringVar()
        self.var_course = StringVar()
        self.var_course_year = StringVar()
        self.var_yearsem = StringVar()
        self.var_stu_id = StringVar()
        self.var_stu_name = StringVar()
        self.var_div = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_addr = StringVar()
        self.var_par_name = StringVar()
        self.var_caste = StringVar()
        self.var_imgid = StringVar()

        title_lable=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="blue")
        title_lable.place(x=0,y=0,width=1530,height=40)
        
        # Background image
        img_4= Image.open(r".\blackbg.jpg")
        img_4= img_4.resize((1530,8500),Image.ANTIALIAS)  # high level image to low level
        self.photo_4 = ImageTk.PhotoImage(img_4)

        bg_img = Label(self.root,image=self.photo_4,bd=2,relief=RIDGE)
        bg_img.place(x=0,y=40,width=1530,height=8500)
        
        main_frame = Frame(self.root,bd=2)
        main_frame.place(x=25,y=60,width=1480,height=660)

        # BACK BUTTON
       
        def back():
            self.root.destroy()
        b1_1 = Button(self.root,text="BACK",command=back,cursor="hand2",font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=1290,y=675,width=200,height=40)

        
        # Left side label frame
        Left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENTS DETAILS",font=("time new roman",14,"bold"))
        Left_frame.place(x=20,y=10,width=700,height=800)


        # Current course Information
        current_course_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",13,"bold"))
        current_course_frame.place(x=15,y=13,width=675,height=150)

        # Department
        dep_label = Label(current_course_frame,text="Department",font=("times new roman",13,"bold"))
        dep_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_Dep,font=("times new roman",13),width=17,state="readonly")
        dep_combo['values'] = ("Select Department","CSE","CSE-DS","CSE-AIML","CSE-CS","IT","IOT","MECHANICAL")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        # Course
        course_label = Label(current_course_frame,text="Course",font=("times new roman",13,"bold"))
        course_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13),width=17,state="readonly")
        course_combo['values'] = ("Select Course","B.Tech","MBA")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        year_label = Label(current_course_frame,text="Course Year",font=("times new roman",13,"bold"))
        year_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course_year,font=("times new roman",13),width=17,state="readonly")
        year_combo['values'] = ("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semester
        sem_level = Label(current_course_frame,text="Year & Semester",font=("times new roman",13,"bold"))
        sem_level.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo = ttk.Combobox(current_course_frame,textvariable=self.var_yearsem,font=("times new roman",13),width=17,state="readonly")
        sem_combo['values'] = ("Select Year & Semester","1-1","1-2","2-1","2-2","3-1","3-2","4-1","4-2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        # Class Student Information
        class_student_frame = LabelFrame(Left_frame,bd=2,relief=RIDGE,text="Student Information",font=("times new roman",13,"bold"))
        class_student_frame.place(x=15,y=190,width=675,height=400)

        # Student ID
        studentID_label = Label(class_student_frame,text="Student ID:",font=("times new roman",13,"bold"))
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        # Entry field
        student_ID_entry = ttk.Entry(class_student_frame,textvariable=self.var_stu_id,width=17,font=("times new roman",13))
        student_ID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student Name
        student_name_label = Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"))
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)
        student_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_stu_name,width=17,font=("times new roman",13))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)
        
        # Class Division
        class_division_label = Label(class_student_frame,text="Class Division:",font=("times new roman",13,"bold"))      
        class_division_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)
        div_combo = ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13),width=15,state="readonly")
        div_combo['values'] = ("Select","A","B")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=10,pady=10,sticky=W)


        # Parent Name
        parent_name_label = Label(class_student_frame,text="Parent Name:",font=("times new roman",13,"bold"))      
        parent_name_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)
        parent_name_entry = ttk.Entry(class_student_frame,textvariable=self.var_par_name,width=17,font=("time new roman",13))
        parent_name_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gender_label = Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"))      
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13),width=15,state="readonly")
        gender_combo['values'] = ("Select Gender","Female","Male","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=10,pady=10,sticky=W)

        # DOB
        DOB_label = Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"))      
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)
        DOB_entry = ttk.Entry(class_student_frame,textvariable=self.var_dob,width=17,font=("times new roman",13))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # Email
        email_label = Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"))      
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)
        email_entry = ttk.Entry(class_student_frame,textvariable=self.var_email,width=17,font=("times new roman",13))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        # Phone number
        phone_no_label = Label(class_student_frame,text="Phone Number:",font=("times new roman",13,"bold"))      
        phone_no_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)
        phone_no_entry = ttk.Entry(class_student_frame,textvariable=self.var_phone,width=17,font=("times new roman",13))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        # Address
        address_label = Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"))      
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)
        address_entry = ttk.Entry(class_student_frame,textvariable=self.var_addr,width=17,font=("times new roman",13))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        # Caste
        caste_label = Label(class_student_frame,text="Caste:",font=("times new roman",13,"bold"))      
        caste_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)
        caste_entry = ttk.Entry(class_student_frame,textvariable=self.var_caste,width=17,font=("times new roman",13))
        caste_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Image ID 
        image_ID_label = Label(class_student_frame,text="Image ID:",font=("times new roman",13,"bold"))
        image_ID_label.grid(row=25,column=0,pady=120)
        # Entry field
        image_ID_entry = ttk.Entry(class_student_frame,textvariable=self.var_imgid,width=17,font=("times new roman",13))
        image_ID_entry.grid(row=25,column=1,pady=120)


        # Radio Buttons
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)
        
        radiobtn2 = ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)
        
        # Buttons Frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=10,y=230,width=650,height=36)   

        save_button = Button(btn_frame,text="SAVE",command=self.add_data,width=15,height=1,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        save_button.grid(row=0,column=0)   
        
        update_button = Button(btn_frame,text="UPDATE",command=self.update_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        update_button.grid(row=0,column=1) 
        
        delete_button = Button(btn_frame,text="DELETE",command=self.delete_data,width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        delete_button.grid(row=0,column=2) 
        
        reset_button = Button(btn_frame,text="RESET",command=self.reset_data,width=16,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        reset_button.grid(row=0,column=3) 
        
        btn_frame1 = Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=9,y=266,width=650,height=38)  
        take_photo_button = Button(btn_frame1,command=self.generate_dataset,text="TAKE PHOTO SAMPLE",width=65,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        take_photo_button.grid(row=0,column=0) 


        # Right side label frame
        Right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("time new roman",14,"bold"))
        Right_frame.place(x=750,y=10,width=650,height=600)
        
        # **** SEARCHING SYSTEM ****
        search_frame = LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",13,"bold"))
        search_frame.place(x=15,y=13,width=627,height=77)
       
        self.var_search=StringVar()
        search_label = Label(search_frame,text="Search By Student ID/Name:",font=("times new roman",13,"bold"))
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

       

        # SEARCH BY ID
        #self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame,textvariable=self.var_search,width=15,font=("times new roman",13))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_button = Button(search_frame,command=self.search_data,text="SEARCH",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        search_button.grid(row=0,column=3,padx=3) 
        
        showall_button = Button(search_frame,command=self.fetch_data,text="SHOW ALL",width=10,font=("times new roman",13,"bold"),bg="blue",fg="white")  
        showall_button.grid(row=0,column=4,padx=3)


        # **** Table Frame****
        table_frame = Frame(Right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=15,y=120,width=627,height=420)

        scroll_x = ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.student_table = ttk.Treeview(table_frame,column=("Dep","course","course_year","yearsem","ID","Stu Name","Div","gender","dob","email","phone","addr","parent","caste","photo","imgid"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("course_year",text="Course Year")
        self.student_table.heading("yearsem",text="Year & Semester")
        self.student_table.heading("ID",text="Student ID")
        self.student_table.heading("Stu Name",text="Student Name")
        self.student_table.heading("Div",text="Class Division")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone Number")
        self.student_table.heading("addr",text="Address")
        self.student_table.heading("parent",text="Parent Name")
        self.student_table.heading("caste",text="Caste")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table.heading("imgid",text="ImageID")
        self.student_table["show"] = "headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("course_year",width=100)
        self.student_table.column("yearsem",width=100)
        self.student_table.column("ID",width=100)
        self.student_table.column("Stu Name",width=180)
        self.student_table.column("Div",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=180)
        self.student_table.column("phone",width=100)
        self.student_table.column("addr",width=200)
        self.student_table.column("parent",width=180)
        self.student_table.column("caste",width=100)
        self.student_table.column("photo",width=150)
        self.student_table.column("imgid",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

   # ****Function declaration*****

    def add_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="123456789",database="FRS")
                my_cursor = conn.cursor()  # We execute MYSQL query using cursor
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_Dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_course_year.get(),
                                                                                                                self.var_yearsem.get(),
                                                                                                                self.var_stu_id.get(),
                                                                                                                self.var_stu_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_addr.get(),
                                                                                                                self.var_par_name.get(),
                                                                                                                self.var_caste.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.var_imgid.get()
                                                                                                             ))
                conn.commit()
                self.fetch_data()
                conn.close
                messagebox.showinfo("Success","Student details has been added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

        # **** FETCHING DATA ****
    
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="123456789",database="FRS")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from Student")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()

 # **** GET CURSOR ****
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_Dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_course_year.set(data[2]),
        self.var_yearsem.set(data[3]),
        self.var_stu_id.set(data[4]),
        self.var_stu_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_gender.set(data[7]),
        self.var_dob.set(data[8]),
        self.var_email.set(data[9]),
        self.var_phone.set(data[10]),
        self.var_addr.set(data[11]),
        self.var_par_name.set(data[12]),
        self.var_caste.set(data[13]),
        self.var_radio1.set(data[14]),
        self.var_imgid.set(data[15])

 # **** UPDATE FUNCTION ****

    def update_data(self):
        if self.var_Dep.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
        else:
            try:
                Update = messagebox.askyesno("Update","Do you want to update the details?",parent=self.root)
                if Update>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="123456789",database="FRS")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update Student set Dep=%s,Course=%s,Course_Year=%s,Year_And_Semester=%s,StudentName=%s,Division=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Parent_Name=%s,Caste=%s,PhotoSample=%s,ImageID=%s where StudentID=%s",(

                                                                                                                                                                                                                                            self.var_Dep.get(),
                                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                                            self.var_course_year.get(),
                                                                                                                                                                                                                                            self.var_yearsem.get(),
                                                                                                                                                                                                                                            self.var_stu_name.get(),
                                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                                            self.var_addr.get(),
                                                                                                                                                                                                                                            self.var_par_name.get(),
                                                                                                                                                                                                                                            self.var_caste.get(),
                                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                                            self.var_imgid.get(),
                                                                                                                                                                                                                                            self.var_stu_id.get()
                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                       ))
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success","Student details updated successfully!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    # **** DELETE FUNCTION ****

    def delete_data(self):
        if self.var_stu_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student Delete Page","Do you want to delete this Student record?",parent=self.root)
                if delete>0:
                    conn = mysql.connector.connect(host="localhost",username="root",password="123456789",database="FRS")
                    my_cursor = conn.cursor()
                    sql="delete from student where StudentID=%s"
                    val = (self.var_stu_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)      

 # **** RESET FUNCTION ****
    def reset_data(self):
        self.var_Dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_course_year.set("Select Year")
        self.var_yearsem.set("Select Year & Semester")
        self.var_stu_id.set("")
        self.var_stu_name.set("")
        self.var_div.set("Select")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_addr.set("")
        self.var_par_name.set("")
        self.var_caste.set("")
        self.var_radio1.set("")
        self.var_imgid.set("")


# ****** SEARCH DATA ******
    def search_data(self):
        if self.var_search.get() == "":
            messagebox.showerror("Error", "Enter Student ID or Name", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="123456789", database="FRS")
                my_cursor = conn.cursor()

                search_query = self.var_search.get()
                conditions = []

            # Check if the search query is a number (assuming it's an ID)
                if '20P71A' in search_query:
                    conditions.append(f"StudentID = '{search_query}'")
                else:
                    conditions.append(f"StudentName LIKE '%{search_query}%'")

                conditions_str = " OR ".join(conditions)

                if conditions_str:
                    sql = f"SELECT Dep, Course, Course_Year, Year_And_Semester, StudentID, StudentName, Division, Gender, DOB, Email, Phone, Address, Parent_Name, Caste, PhotoSample, ImageID FROM student WHERE {conditions_str}"
                    print("Generated SQL Query:", sql)  # Print the generated SQL query for debugging
                    my_cursor.execute(sql)
                    rows = my_cursor.fetchall()

                    if rows:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in rows:
                            self.student_table.insert("", END, values=i)
                        conn.commit()
                    else:
                        messagebox.showerror("Error", "Data Not Found", parent=self.root)
                else:
                    messagebox.showerror("Error", "No search criteria selected", parent=self.root)

                conn.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To: {str(es)}", parent=self.root)




# **** GENERATE DATA SET / TAKE PHOTO SAMPLES ****

    def generate_dataset(self):
         if self.var_Dep.get()=="Select Department" or self.var_stu_name.get()=="" or self.var_stu_id.get()=="":
            messagebox.showerror("Error","All fields are required!",parent=self.root)
         else:
            try:
                conn = mysql.connector.connect(host="localhost",username="root",password="123456789",database="FRS")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from Student")
                myresult = my_cursor.fetchall()
                id = 0
                for x in myresult:
                    id+=1  
                my_cursor.execute("update Student set Dep=%s,Course=%s,Course_Year=%s,Year_And_Semester=%s,StudentName=%s,Division=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Parent_Name=%s,Caste=%s,PhotoSample=%s,ImageID=%s where StudentID=%s",(

                                                                                                                                                                                                                                            self.var_Dep.get(),
                                                                                                                                                                                                                                            self.var_course.get(),
                                                                                                                                                                                                                                            self.var_course_year.get(),
                                                                                                                                                                                                                                            self.var_yearsem.get(),
                                                                                                                                                                                                                                            self.var_stu_name.get(),
                                                                                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                                                                                            self.var_addr.get(),
                                                                                                                                                                                                                                            self.var_par_name.get(),
                                                                                                                                                                                                                                            self.var_caste.get(),
                                                                                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                                                                                            self.var_imgid.get(),
                                                                                                                                                                                                                                            self.var_stu_id.get() == id+1
                                                                                                                                                                                                                                       ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
            
            # **** LOAD PREDEFINED DATA ON FACE FRONTALS FROM OPENCV ****

                face_classifier=cv2.CascadeClassifier(".\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray,1.3,5)
                    # Scaling factor = 1.3
                    # Minimum Neighbor = 5
                    for(x,y,w,h) in faces:  # Rectangle
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                    
                cap = cv2.VideoCapture(0)  # Opening camera , 0--> web camera
                img_id=1    # For storing the captured images
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+= 1 
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        #file_name_path ="data/user."+str(id)+"."+str(img_id)+".jpg"
                        file_name_path = ".\data/user."+str(id)+"."+str(img_id)+".jpg"
                        #file_name_path = f"{photo_directory}user_{user_id}_{img_id}.jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)  # Font,Font scale,Font color,Text thickness
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==110:
                         break
            
                cap.release()
                cv2.destroyAllWindows()
                
                messagebox.showinfo("Result","Generating data sets completed!")   
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)



if __name__ == "__main__":
    root=Tk()
    obj = Student(root)
    root.mainloop()