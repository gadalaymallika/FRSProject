from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import tkinter
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from faculty import Faculty
from calculations import Calculations

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x900+0+0")
        self.root.title("STUDENT MANAGEMENT SYSTEM")


        # background image
        #img_4= Image.open(r".\blackbg.jpg")
        img_4= Image.open(r".\b2.jpg")
        img_4= img_4.resize((1540,900),Image.ANTIALIAS)  # high level image to low level
        self.photo_4 = ImageTk.PhotoImage(img_4)

        bg_img = Label(self.root,image=self.photo_4,bd=2,relief=RIDGE)
        bg_img.place(x=0,y=0,width=1540,height=900)

        title_lable=Label(bg_img,text="VISUAL RECOGNITION LOG SYSTEM",font=("Courier",40,"bold"),bg="black",fg="white")
        title_lable.place(x=0,y=0,width=1540,height=70)

        # Student button
        img_5=Image.open(".\stud1.png")
        img_5= img_5.resize((220,220),Image.ANTIALIAS)
        self.photo_5= ImageTk.PhotoImage(img_5)

        b1 = Button(bg_img,image=self.photo_5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=150,width=220,height=220)

        b1_1 = Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=200,y=350,width=220,height=40)
        
        # Detect Face button
        img_6=Image.open(".\p5.jpg")
        img_6= img_6.resize((220,220),Image.ANTIALIAS)
        self.photo_6= ImageTk.PhotoImage(img_6)

        b1 = Button(bg_img,image=self.photo_6,cursor="hand2",command=self.face_data)
        b1.place(x=500,y=150,width=220,height=220)

        b1_1 = Button(bg_img,text="Face Detector",cursor="hand2",command=self.face_data,font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=500,y=350,width=220,height=40)

        # Attendance Face button
        img_7=Image.open(".\pic19.jpeg.jpg")
        img_7= img_7.resize((220,220),Image.ANTIALIAS)
        self.photo_7= ImageTk.PhotoImage(img_7)

        b1 = Button(bg_img,image=self.photo_7,cursor="hand2",command=self.attendance_data)
        b1.place(x=800,y=150,width=220,height=220)

        b1_1 = Button(bg_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=800,y=350,width=220,height=40)

        # Percentage button
        img_8=Image.open(".\per.png")
        img_8= img_8.resize((220,220),Image.ANTIALIAS)
        self.photo_8= ImageTk.PhotoImage(img_8)
        
        b1 = Button(bg_img,image=self.photo_8,cursor="hand2",command=self.cal_details)
        b1.place(x=1100,y=150,width=220,height=220)

        b1_1 = Button(bg_img,text="Percentage",cursor="hand2",command=self.cal_details,font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=1100,y=350,width=220,height=40)

        # Train face button
        img_9=Image.open(".\pic6.jpeg.jpg")
        img_9= img_9.resize((220,220),Image.ANTIALIAS)
        self.photo_9= ImageTk.PhotoImage(img_9)

        b1 = Button(bg_img,image=self.photo_9,cursor="hand2",command=self.train_data)
        b1.place(x=200,y=450,width=220,height=220)

        b1_1 = Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=200,y=650,width=220,height=40)

        # Photos button
        img_10=Image.open(".\pic13.jpeg.jpg")
        img_10= img_10.resize((220,220),Image.ANTIALIAS)
        self.photo_10= ImageTk.PhotoImage(img_10)

        b1 = Button(bg_img,image=self.photo_10,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=450,width=220,height=220)

        b1_1 = Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=500,y=650,width=220,height=40)                

        # Faculty button
        img_11=Image.open(".\p4.jpg")
        img_11=img_11.resize((220,220),Image.ANTIALIAS)
        self.photo_11= ImageTk.PhotoImage(img_11)

        b1 = Button(bg_img,image=self.photo_11,cursor="hand2",command=self.faculty_data)
        b1.place(x=800,y=450,width=220,height=220)

        b1_1 = Button(bg_img,text="Faculty Details",cursor="hand2",command=self.faculty_data,font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=800,y=650,width=220,height=40) 

        # Exit button
        img_12=Image.open(".\pic18.png")
        img_12=img_12.resize((220,220),Image.ANTIALIAS)
        self.photo_12= ImageTk.PhotoImage(img_12)

        b1 = Button(bg_img,image=self.photo_12,cursor="hand2",command=self.exit)
        b1.place(x=1100,y=450,width=220,height=220)

        b1_1 = Button(bg_img,text="Exit",cursor="hand2",command=self.exit,font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=1100,y=650,width=220,height=40) 

    # **** PHOTOS BUTTON ****

    def open_img(self):
        os.startfile(".\data")
       
    # **** EXIT BUTTON ****

    def exit(self):
        self.exit = tkinter.messagebox.askyesno("Exit","Exit Project?",parent=self.root)  
        if self.exit>0:
            self.root.destroy()
        else:
            return
       
        # **** Functions for buttons **** 

    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)
    
    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def faculty_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Faculty(self.new_window)

    def cal_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Calculations(self.new_window)
    


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()