from tkinter import *
from tkinter import messagebox
import pymysql
#import sqlite3
import os

class Login:
   def __init__(self,root):
     self.root=root
     self.root.title("Login system")
     self.root.geometry("1350x700+0+0")
     #self.root.resizable(False, False) 

     self.bg=PhotoImage(file="images/IGDTUW-Delhi-Admission.png")
     self.bg_image=Label(self.root, image=self.bg).place(x=0, y=0, relwidth=1, relheight=1)

   
     Frame_login=Frame(self.root, bg="#8B475D")
     Frame_login.place(x=150, y=220, height=340, width=500)


     title=Label(Frame_login, text="LOGIN HERE", font=("Times new roman", 35, "bold"), bg="black", fg="white").place(x=90,y=30, width=300)
     desc=Label(Frame_login, text="Student Result Management System", font=("Times new roman", 12, "bold"), bg="black", fg="white").place(x=90,y=100, width=300)

     lbl_email=Label(Frame_login,text="Email Address", font=("Times new roman", 20, "bold"), bg="brown", fg="white").place(x=90,y=150)
     self.txt_email=Entry(Frame_login,font=("Times new roman", 15), bg="light gray")
     self.txt_email.place(x=90, y=180, width=350, height=35)

     lbl_pass=Label(Frame_login,text="Password", font=("Times new roman", 20, "bold"), bg="brown", fg="white").place(x=90,y=215)
     self.txt_pass=Entry(Frame_login,font=("Times new roman", 15), bg="light gray")
     self.txt_pass.place(x=90, y=245, width=350, height=35)

     # forget_btn=Button(Frame_login, text="Forget Password?", bg="white", bd=0, fg="black", font=("Times new Roman", 15)).place(x=90, y=280)
     reg_btn=Button(Frame_login, command= self.register_window, text="Register new account?",cursor="hand2", font=("Times new roman",14), bg="white", bd=0, fg="black").place(x=250, y=285, width=250, height=40)
     login_btn=Button(self.root,command=self.login_function, cursor="hand2",text="Login", bg="#CD5B45", fg="black", font=("Times new Roman", 25)).place(x=300, y=570, width=250, height=40)

     
   def register_window(self):
      self.root.destroy()
      import register
      

  
   def login_function(self):
       if self.txt_pass.get()=="" or self.txt_email.get()=="":
          messagebox.showerror("Error", "All field are required", parent=self.root)

       else:
          try:
             con=pymysql.connect(host="localhost", user="root", password="soni", database="employee")
             cur=con.cursor()
             cur.execute("Select * from login where email=%s and password=%s", (self.txt_email.get(), self.txt_pass.get()))
             row=cur.fetchone()
             if row==None:
                messagebox.showerror("Error", "Invalid username or password", parent=self.root)
                
             else:
                messagebox.showinfo("Success", "Welcome", parent=self.root)
                self.root.destroy()
                os.system("python dashboard.py")
                

             con.close()   
                

          except Exception as es:
             messagebox.showerror("Error", f"Error Due to: {str(es)}", parent=self.root)
             
   
                

      # elif self.txt_pass.get()!= "123456" or self.txt_email.get()!="Shecodes":
       #   messagebox.showerror("Error", "Invalid Username or Password", parent=self.root)
      # else: 
      #    messagebox.showinfo("Welcome", f"Welcome {self.txt_email.get()}\nYour Password:{self.txt_pass.get()}", parent=self.root)
    


     







root=Tk()
obj=Login(root)
root.mainloop()