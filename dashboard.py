from tkinter import *
from PIL import Image, ImageTk  #pip install
from tkinter import messagebox
import os
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
class RMS:
    def __init__(self,root):
        self.root= root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#CD6889")

        self.logo_dash=ImageTk.PhotoImage(file="images/igdtuwlogo.png")

        title=Label(self.root, text="Indira Gandhi Delhi Technical University for Women\nStudent Result Management System", padx=50, compound= LEFT, image=self.logo_dash,font=("goudy old style",35,"bold"), bg="#8B475D", fg="black").place(x=0, y=0, relwidth=1)
        #frame1 = Frame(self.root, highlightbackground="black", highlightthickness=2)
        #frame1.pack(padx=20, pady=20)  

        self.photo=PhotoImage(file="images/frr.png")  #inserting images
        self.photo_image=Label(self.root, image=self.photo).place(x=700, y=200, height=300,width=300)

        self.pic=PhotoImage(file="images/flag.png")  #inserting images
        self.pic_image=Label(self.root, image=self.pic).place(x=1390, y=190, height=100,width=150)

        self.picc=PhotoImage(file="images/gg.png")  #inserting images
        self.picc_image=Label(self.root, image=self.picc).place(x=1390, y=300, height=100,width=150)

        self.pics=PhotoImage(file="images/azadii.png")  #inserting images
        self.pics_image=Label(self.root, image=self.pics).place(x=1390, y=410, height=100,width=150)


        
         

        #self.bg=PhotoImage(file="images/IGDTUW-Delhi-Admission.png")
        #self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

   
        
        

        
        M_Frame=LabelFrame(self.root, text="Menu", font=("Times new roman",30), bg="#8B2323")
        M_Frame.place(x=20,y=200, width=300, height=350)

        btn_course=Button(self.root,text="Course",font=("Times new roman",25,"bold"), bg="#CD8162", fg="black", cursor="hand2", command=self.add_course)
        btn_course.place(x=20, y=250, width=300, height=70)
        btn_student=Button(self.root,text="Student Details",font=("Times new roman",25,"bold"), bg="#CD8162", fg="black", cursor="hand2", command=self.add_student).place(x=20, y=320, width=300, height=70)
        btn_result=Button(self.root,text="Student Marks",font=("Times new roman",25,"bold"), bg="#CD8162", fg="black", cursor="hand2", command=self.add_result).place(x=20, y=390, width=300, height=70)
        btn_view=Button(self.root,text="View Result",font=("Times new roman",25,"bold"), command=self.add_report ,bg="#CD8162", fg="black", cursor="hand2").place(x=20, y=460, width=300, height=70)
        btn_logout=Button(self.root,text="Logout",font=("Times new roman",25,"bold"), bg="#CD8162", fg="black", cursor="hand2", command=self.logout).place(x=20, y=530, width=300, height=70)
        btn_exit=Button(self.root,text="Exit",font=("Times new roman",25,"bold"), bg="#CD8162", fg="black", cursor="hand2", command=self.exit).place(x=20, y=600, width=300, height=70)

        #self.bg_img=Image.open("images/bggg.png")
        #self.bg_img=self.bg_img.resize((350,350), Image.ANTIALIAS)
        #self.bg_img=ImageTk.PhotoImage(self.bg_img)

     #self.bg=PhotoImage(file="images/IGDTUW-Delhi-Admission.png")
     #self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

        #self.lbl_bg=Label(self.root, image=self.bg_img).place(x=300,y=300, width=920, height=350)

        self.lbl_course=Label(self.root, text="AWARDS AND ACHEIVEMENTS OF IGDTUW", font=("goudy old style", 15), bd=1, bg="#7D7D7D", fg="black", justify=CENTER)
        self.lbl_course.place(x=400, y=515, width=920, height=50)


        self.lbl_course=Label(self.root, text="Award for Best\nPlacement Opportunities", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#8B008B", fg="black")
        self.lbl_course.place(x=400, y=570, width=300, height=100)

        self.lbl_course=Label(self.root, text="E-Learning\nExcellence Award", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#CD0000", fg="black")
        self.lbl_course.place(x=710, y=570, width=300, height=100)

        self.lbl_course=Label(self.root, text="Stree Shakti\n Samaan Award", font=("goudy old style", 20), bd=10, relief=RIDGE, bg="#CD3700", fg="black")
        self.lbl_course.place(x=1020, y=570, width=300, height=100)




        footer=Label(self.root, text="SRMS Student Result Management System. Contact:9875463210\nCopyright@2020 Indira Gandhi Delhi Technical University for Women. All Rights Reserved.\n Madrasa Road, Opposite St. James Church, Kashmere Gate, Delhi-110006", font=("goudy old style", 12), bg="#262626", fg="white").pack(side=BOTTOM, fill=X)
    
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)    


    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)

    def logout(self):
        op=messagebox.askyesno("Confirm", "Do you really want to logout", parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")

    def exit(self):
        op=messagebox.askyesno("Confirm", "Do you really want to exit", parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")        


        


      
if __name__=="__main__":
    root=Tk()
    obj=RMS(root)











































































































    root.mainloop()

 

















        

