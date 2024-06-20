from tkinter import*
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Faculty:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("Face_Recogonition_System")

        # background image
        bg1 = Image.open("./b2.jpg")
        bg1 = bg1.resize((1530, 800), Image.ANTIALIAS)
        self.photobg1 = ImageTk.PhotoImage(bg1)

        # set image as label
        bg_img = tk.Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=0, width=1530, height=890)

        # Back button
        def back():
            self.root.destroy()
        b1_1 = Button(self.root,text="BACK",command=back,cursor="hand2",font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=1200,y=780,width=200,height=40)


        # title section
        title_lb1 = tk.Label(bg_img, text="Teachers Details", font=("Helvetica", 35 , "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1530, height=50)

        # background image
        img_4= Image.open(r".\blackbg.jpg")
        img_4= img_4.resize((1540,900),Image.ANTIALIAS)  # high level image to low level
        self.photo_4 = ImageTk.PhotoImage(img_4)

        bg_img = Label(self.root,image=self.photo_4,bd=2,relief=RIDGE)
        bg_img.place(x=0,y=0,width=1540,height=900)

        title_lable=Label(bg_img,text="VISUAL RECOGNITION LOG SYSTEM",font=("Courier",40,"bold"),bg="black",fg="green")
        title_lable.place(x=0,y=0,width=1540,height=50)

        # CC
        img_5=Image.open(".\supriyam.jpg")
        img_5= img_5.resize((220,220),Image.ANTIALIAS)
        self.photo_5= ImageTk.PhotoImage(img_5)

        b1 = Button(bg_img,image=self.photo_5,cursor="hand2")
        b1.place(x=400,y=150,width=220,height=220)

        b1_1 = Button(bg_img,text="Mrs.Supriya Samuel",cursor="hand2",font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=400,y=350,width=220,height=40)
        
        # NLP
        img_6=Image.open(".\jhumm.jpg")
        img_6= img_6.resize((220,220),Image.ANTIALIAS)
        self.photo_6= ImageTk.PhotoImage(img_6)

        b1 = Button(bg_img,image=self.photo_6,cursor="hand2")
        b1.place(x=700,y=150,width=220,height=220)

        b1_1 = Button(bg_img,text="Dr.Jhum Swain",cursor="hand2",font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=700,y=350,width=220,height=40)

        # PA
        img_7=Image.open(r".\thomass.jpg")
        img_7= img_7.resize((220,220),Image.ANTIALIAS)
        self.photo_7= ImageTk.PhotoImage(img_7)

        b1 = Button(bg_img,image=self.photo_7,cursor="hand2")
        b1.place(x=1000,y=150,width=220,height=220)

        b1_1 = Button(bg_img,text="Mr.G.Thomas Reddy",cursor="hand2",font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=1000,y=350,width=220,height=40)

        # POE
        img_8=Image.open(".\krishnas.jpg")
        img_8= img_8.resize((220,220),Image.ANTIALIAS)
        self.photo_8= ImageTk.PhotoImage(img_8)

        b1 = Button(bg_img,image=self.photo_8,cursor="hand2")
        b1.place(x=850,y=450,width=220,height=220)

        b1_1 = Button(bg_img,text="Mr.Gopal Krishna",cursor="hand2",font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=850,y=650,width=220,height=40)

        # WA
        img_9=Image.open(".\p13.jpg")
        img_9= img_9.resize((220,220),Image.ANTIALIAS)
        self.photo_9= ImageTk.PhotoImage(img_9)

        b1 = Button(bg_img,image=self.photo_9,cursor="hand2")
        b1.place(x=550,y=450,width=220,height=220)

        b1_1 = Button(bg_img,text="Mrs.Aruna",cursor="hand2",font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=550,y=650,width=220,height=40)

        # BACK BUTTON
       
        def back():
            self.root.destroy()
        b1_1 = Button(self.root,text="BACK",command=back,cursor="hand2",font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=1290,y=705,width=200,height=40)


if __name__ == "__main__":
    root = tk.Tk()
    obj = Faculty(root)
    root.mainloop()