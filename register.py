from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
#import sqlite3
import pymysql
import os

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registeration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#CD6889")



        self.logo_dash=ImageTk.PhotoImage(file="images/igdtuwlogo.png")

        title=Label(self.root, text="Indira Gandhi Delhi Technical University for Women\nStudent Result Management System", padx=50, compound= LEFT, image=self.logo_dash,font=("goudy old style",35,"bold"), bg="#8B475D", fg="black").place(x=0, y=0, relwidth=1)
        

       #bg image
        #self.bg=ImageTk.PhotoImage(file="images/reg.png")  
        #bg=Label(self.root, image=self.bg).place(x=0, y=0,width=1500, height=800)

        #left image
        self.left=ImageTk.PhotoImage(file="images/student.png")  
        bg=Label(self.root, image=self.left).place(x=200, y=250, width=400, height=500)

             

        #register frame
        frame1=Frame(self.root, bg="white")
        frame1.place(x=600, y=250, width=700, height=500)


        
        title=Label(frame1,text="REGISTRATION", font=("Times new roman",35), bg="#8B5742", justify=CENTER).place(x=50,y=50)

        #row1
        
        f_name=Label(frame1,text="First Name", font=("Times new roman",20), bg="#CD8162").place(x=50,y=110)
        self.txt_fname=Entry(frame1, font=("Times new roman",20), bg="gray")
        self.txt_fname.place(x=50,y=140,width=250)

        l_name=Label(frame1,text="Last Name", font=("Times new roman",20), bg="#CD8162").place(x=370,y=110)
        self.txt_lname=Entry(frame1, font=("Times new roman",20), bg="gray")
        self.txt_lname.place(x=370,y=140,width=250)

        f_contact=Label(frame1,text="Contact No.", font=("Times new roman",20), bg="#CD8162").place(x=50,y=180)
        self.txt_contact=Entry(frame1, font=("Times new roman",20), bg="gray")
        self.txt_contact.place(x=50,y=210,width=250)


        email=Label(frame1,text="Email", font=("Times new roman",20), bg="#CD8162").place(x=370,y=180)
        self.txt_email=Entry(frame1, font=("Times new roman",20), bg="gray")
        self.txt_email.place(x=370,y=210,width=250)

        question=Label(frame1,text="Security Question", font=("Times new roman",20), bg="#CD8162").place(x=50,y=250)
        self.cmb_quest=ttk.Combobox(frame1, font=("Times new roman",15), state='readonly', justify=CENTER)
        self.cmb_quest['values']=("Select", "Your First Pet Name", "Your Birth Place", "Your Best Friend Name")
        self.cmb_quest.place(x=50,y=280,width=250)
        self.cmb_quest.current(0)

     
        
        answer=Label(frame1,text="Answer", font=("Times new roman",20), bg="#CD8162").place(x=370,y=250)
        self.txt_answer=Entry(frame1, font=("Times new roman",20), bg="gray")
        self.txt_answer.place(x=370,y=285,width=250)

        
        password=Label(frame1,text="Password", font=("Times new roman",20), bg="#CD8162").place(x=50,y=310)
        self.txt_password=Entry(frame1, font=("Times new roman",20), bg="gray")
        self.txt_password.place(x=50,y=350,width=250)

        cpassowrd=Label(frame1,text="Confirm Password", font=("Times new roman",20), bg="#CD8162").place(x=370,y=320)
        self.txt_cpassword=Entry(frame1, font=("Times new roman",20), bg="gray")
        self.txt_cpassword.place(x=370,y=355,width=250)


        self.var_chk=IntVar()
        chk=Checkbutton(frame1, text="I Agree to the terms and conditions",variable=self.var_chk, onvalue=1, offvalue=0, bg="white", fg="black").place(x=50, y=390)

        self.btn_img=ImageTk.PhotoImage(file="images/registrraa.png")
        btn_register=Button(frame1, image=self.btn_img, bd=0, cursor="hand2", command=self.register_data).place(x=50, y=430, width=100, height=50)

        btn_login=Button(self.root,text="Sign In",command= self.login_window, font=("Times New Roman",20) ,cursor="hand2", bg="#CD5B45").place(x=300, y=650, width=150, height=50)

    def login_window(self):
      self.root.destroy()
      os.system("python login.py")

    def clear(self):
        self.txt_fname.delete(0, END)
        self.txt_lname.delete(0, END)
        self.txt_contact.delete(0, END)
        self.txt_email.delete(0, END)
        self.txt_password.delete(0, END)
        self.txt_cpassword.delete(0, END)
        self.txt_answer.delete(0, END)
        self.cmb_quest.current(0)



    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.txt_contact.get()=="":
            messagebox.showerror("Error", "All Field are Required", parent=self.root)
        elif self.txt_password.get()!= self.txt_cpassword.get():
            messagebox.showerror("Error", "Password and Confirm password should be same", parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error", "Please Agree to our Terms & Conditions", parent=self.root)
        else:  
            try:
                con=pymysql.connect(host="localhost", user="root", password="soni", database="employee2")
                cur=con.cursor()
                cur.execute("select* from employee where email=%s", self.txt_email.get())
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error", "User already exists. Please try with another email", parent=self.root)
                else: cur.execute("insert into employee (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)"
                            (self.txt_fname.get(),
                             self.txt_lname.get(),
                             self.txt_contact.get(),
                             self.txt_email.get(),
                             self.txt_answer.get(),
                             self.txt_cpassword.get())
                            
                            )
                con.commit()
                con.close()
                messagebox.showinfo( "Success", "Your Registration is successful", parent=self.root)
                self.clear()
                self.login_window()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to: {str(es)}", parent=self.root)
            
            

         

            #  self.txt_answer.get(),
             #  self.txt_contact.get(),
              #  self.txt_email.get(),
               #  self.txt_password.get(),
                #  self.txt_lname.get(),
                #   self.cmb_quest.get(),
                #    self.txt_cpassword.get() 










        




        











root=Tk()
obj=Register(root)
root.mainloop()    
