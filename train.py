from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import cv2
import os
import numpy as np

class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("TRAINING STUDENT DATA")

        img_top = Image.open(".\\p6.jpg")
        img_top = img_top.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)

        f_lb1 = Label(self.root, image=self.photoimg_top)
        f_lb1.place(x=0, y=0, width=1530, height=435)

        b1 = Button(self.root, text="TRAIN DATA", command=self.train_classifier, cursor="hand2", font=("Courier", 50, "bold"), bg="black", fg="red")
        b1.place(x=0, y=380, width=1530, height=80)

        img_bottom = Image.open(".\\p7.jpg")
        img_bottom = img_bottom.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lb2 = Label(self.root, image=self.photoimg_bottom)
        f_lb2.place(x=0, y=450, width=1530, height=320)

        def back():
            self.root.destroy()
        b1_1 = Button(self.root,text="BACK",command=back,cursor="hand2",font=("Helvetica",16,"bold"),bg="black",fg="red")
        b1_1.place(x=1200,y=780,width=200,height=40)

    def train_classifier(self):
        data_dir = ".\data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')  # Corrected typo: convert instead of conver
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training", imageNp)
            cv2.waitKey(1) == 13  # Corrected typo: waitKey

        ids = np.array(ids)

        # TRAINING THE CLASSIFIER
        clf = cv2.face.LBPHFaceRecognizer.create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()  # Corrected the function call
        messagebox.showinfo("Result", "Trained the datasets !!")
        

if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
