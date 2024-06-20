from tkinter import *
from tkinter import ttk, messagebox, simpledialog
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
from datetime import datetime

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x900+0+0")
        self.root.title("FACE RECOGNITION")
        self.subject = None
        self.filename = None

        title_label = Label(self.root, text="FACE RECOGNITION", font=("Courier", 43, "bold"), bg="black", fg="red")
        title_label.place(x=0, y=0, width=1530, height=53)

        img_bottom = Image.open("fr.jpeg")
        img_bottom = img_bottom.resize((1400,800), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lb2 = Label(self.root, image=self.photoimg_bottom)
        f_lb2.place(x=0, y=55, width=1530, height=900)

        b1 = Button(f_lb2, text="RECOGNITION THE FACE", cursor="hand2", font=("times new roman", 18, "bold"), bg="black", fg="red", command=self.face_recog)
        b1.place(x=500, y=400, width=500, height=50)

        def back():
            self.root.destroy()
        b1_1 = Button(self.root, text="BACK", command=back, cursor="hand2", font=("Helvetica", 16, "bold"), bg="black", fg="red")
        b1_1.place(x=1200, y=780, width=200, height=40)

    def mark_attendance(self, n, r, d, subject, filename):
        now = datetime.now()
        d1 = now.strftime("%d/%m/%Y")
        dtString = now.strftime("%H:%M:%S")
            # Check if student details are already present in the CSV file
        with open(filename, "r", newline="\n") as f:
            lines = f.readlines()
            for line in lines[1:]:  # Skip the header line
                if f"{n}, {r}, {d}" in line:
                    print(f"Student {n} with ID {r} and Department {d} already marked present.")
                    return
                
         # If not present, add the details to the CSV file
        with open(filename, "a", newline="\n") as f:
            f.writelines(f"{n}, {r}, {d}, {dtString}, {d1}, Present\n")
    

    def draw_boundray(self, img, classifier, scaleFactor, minNeighbors, color, text, clf, subject, filename):
        try:    
            if img is None:
                return img, []  # Skip processing if the image is None
            
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

            # self.mark_attendance(n, r, d, subject, filename)
            coord = []
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y + h, x:x + w])

                # Check if predict is a valid ID
                #if 1 <= id <= 1000:
                image_id = id
                id = f"'{image_id}'"
                print(id)

                confidence=int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost", username="root", password="123456789", database="FRS", consume_results=True)
                cursor = conn.cursor()

                cursor.execute(f"select StudentName from student where ImageID= {id}")
                n = cursor.fetchone()
                if n:
                    n = "+".join(n)
                else:
                    n = "Unknown"

                cursor.execute(f"select StudentID from student where ImageID= {id}")
                r = cursor.fetchone()
                if r:
                    r = "+".join(r)
                else:
                    r = "Unknown"

                cursor.execute(f"select Dep from student where ImageID= {id}")
                d = cursor.fetchone()
                if d:
                    d = "+".join(d)
                else:
                    d = "Unknown"

                print("Processed n:", n)
                print("Processed r:", r)
                print("Processed d:", d)

                if confidence > 77:
                    print(f"Confidence: {confidence}")
                    cv2.putText(img, f"StudentName:{n}", (x, y - 80), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"StudentID:{r}", (x, y - 55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Department:{d}", (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(n, r, d, subject, filename)
                else:
                    print(f"Confidence: {confidence}")
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coord = [x, y, w, h]

            return img, coord
        except Exception as e:
            messagebox.showerror("Error", f"Error in drawing boundary: {str(e)}", parent=self.root)
            return img, []

    def recognize(self, video_cap, clf, faceCascade, subject, filename):
        try:
            ret, img = video_cap.read()

            if not ret:
                messagebox.showerror("Error", "Failed to capture frame", parent=self.root)
                return None  # Return None to indicate a failure

            img, _ = self.draw_boundray(img,faceCascade, 1.1, 10, (0, 255, 0), "Face", clf, subject, filename)

            if img.shape[0] == 0 or img.shape[1] == 0:
                print("Empty image")
                return img

            return img
        except Exception as e:
            messagebox.showerror("Error", f"Error in recognizing face: {str(e)}", parent=self.root)
            return img

# Modify the face_recog method where recognize is called
    def face_recog(self):
        try:
            subject = simpledialog.askstring("Input", "Enter the subject name:")

            if not subject:
                messagebox.showwarning("Warning", "Subject name cannot be empty.", parent=self.root)
                return

            subject_folder = f"./attendances/{subject}"
            os.makedirs(subject_folder, exist_ok=True)

            now = datetime.now()
            date_str = now.strftime("%Y-%m-%d")
            filename = f"{subject_folder}/{subject}_{date_str}_attendance.csv"

            if not os.path.isfile(filename):
                with open(filename, "w", newline="\n") as f:
                    f.write("StudentName,StudentID,Department,Time,Date,Attendance Status\n")

            faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("classifier.xml")

            video_cap = cv2.VideoCapture(0)

            while True:
                ret, img = video_cap.read()

                if not ret:
                    messagebox.showerror("Error", "Failed to capture frame", parent=self.root)
                    break

                img = self.recognize(video_cap, clf, faceCascade, subject, filename)
                if img is None:
                    continue  # Skip the current iteration if the image is not readable

                cv2.imshow("Welcome To Face Recognition", img)

                key = cv2.waitKey(1)
                if key == 13:
                    break  # Break the loop when Enter key is pressed

            video_cap.release()
            cv2.destroyAllWindows()

        except Exception as es:
            messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
