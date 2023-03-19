from tkinter import *
from PIL import Image,ImageTk 
from tkinter import ttk, messagebox
import sqlite3
class CourseClass:
    def __init__(self,root):
        self.root=root
        self.root.title("Course Records")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="#CD6889")
        self.root.focus_force()



        self.logo_dash=ImageTk.PhotoImage(file="images/igdtuwlogo.png")

        title=Label(self.root, text="Indira Gandhi Delhi Technical University for Women\nStudent Result Management System", padx=50, compound= LEFT, image=self.logo_dash,font=("goudy old style",35,"bold"), bg="#8B475D", fg="black").place(x=0, y=0, relwidth=1)

        #===title===
        title=Label(self.root,text="Course Details",font=("Times New Roman",20,"bold"),bg="#8B475D", fg="white").place(x=10,y=215,width=1520,height=35)

        #===variables===
        self.var_number=StringVar()
        self.var_sno=StringVar()
        self.var_name=StringVar()
        self.var_duration=StringVar()
        self.var_sub1=StringVar()
        self.var_sub2=StringVar()
        self.var_sub3=StringVar()
        self.var_sub4=StringVar()
        self.var_sub5=StringVar()

        #===widgets===
        lbl_courseName=Label (self.root,text="Course Name", font=("Times New Roman",15,"bold"),bg='#CD6889').place(x=10,y=260)
        lbl_duration=Label (self.root,text="Duration", font=("Times New Roman",15,"bold"),bg='#CD6889').place(x=10,y=300)
        lbl_sub=Label (self.root,text="SUBJECTS:", font=("Times New Roman",15,"bold"),bg='#CD6889').place(x=200,y=340)
        lbl_sub1=Label (self.root,text="Subject 1", font=("Times New Roman",15,"bold"),bg='#CD6889').place(x=10,y=380)
        lbl_sub2=Label (self.root,text="Subject 2", font=("Times New Roman",15,"bold"),bg='#CD6889').place(x=10,y=420)
        lbl_sub3=Label (self.root,text="Subject 3", font=("Times New Roman",15,"bold"),bg='#CD6889').place(x=10,y=460)
        lbl_sub4=Label (self.root,text="Subject 4", font=("Times New Roman",15,"bold"),bg='#CD6889').place(x=10,y=500)
        lbl_sub5=Label (self.root,text="Subject 5", font=("Times New Roman",15,"bold"),bg='#CD6889').place(x=10,y=540)

        #==Entry Fields===
        self.txt_course=ttk.Combobox(self.root, textvariable=self.var_name,values=("Select","BTech Computer Science and Engineering","BTech Electrical and Electronics Engineering","BTech Information Technology","BTech Mechanical and Automation Engineering"),font=("Times New Roman",15,"bold"),state='readonly',justify=CENTER)
        self.txt_course.place(x=150,y=260,width=420)
        self.txt_course.current(0)
        
        txt_duration=Entry(self.root, textvariable=self.var_duration, font=("Times New Roman",15,"bold"),bg='lightyellow').place(x=150,y=300,width=200)
        
        self.txt_sub1=ttk.Combobox(self.root, textvariable=self.var_sub1,values=("Select","Applied Maths","Applied Physics","Applied Chemistry","Basic Electrical Engineering","Programming in C","Communication Skills","Engineering Mechanics"),font=("Times New Roman",15,"bold"),state='readonly',justify=CENTER)
        self.txt_sub1.place(x=150,y=380,width=320)
        self.txt_sub1.current(0)

        self.txt_sub2=ttk.Combobox(self.root, textvariable=self.var_sub2,values=("Select","Applied Maths","Applied Physics","Applied Chemistry","Basic Electrical Engineering","Programming in C","Communication Skills","Engineering Mechanics"),font=("Times New Roman",15,"bold"),state='readonly',justify=CENTER)
        self.txt_sub2.place(x=150,y=420,width=320)
        self.txt_sub2.current(0)
        
        self.txt_sub3=ttk.Combobox(self.root, textvariable=self.var_sub3,values=("Select","Applied Maths","Applied Physics","Applied Chemistry","Basic Electrical Engineering","Programming in C","Communication Skills","Engineering Mechanics"),font=("Times New Roman",15,"bold"),state='readonly',justify=CENTER)
        self.txt_sub3.place(x=150,y=460,width=320)
        self.txt_sub3.current(0)

        self.txt_sub4=ttk.Combobox(self.root, textvariable=self.var_sub4,values=("Select","Applied Maths","Applied Physics","Applied Chemistry","Basic Electrical Engineering","Programming in C","Communication Skills","Engineering Mechanics"),font=("Times New Roman",15,"bold"),state='readonly',justify=CENTER)
        self.txt_sub4.place(x=150,y=500,width=320)
        self.txt_sub4.current(0)

        self.txt_sub5=ttk.Combobox(self.root, textvariable=self.var_sub5,values=("Select","Applied Maths","Applied Physics","Applied Chemistry","Basic Electrical Engineering","Programming in C","Communication Skills","Engineering Mechanics"),font=("Times New Roman",15,"bold"),state='readonly',justify=CENTER)
        self.txt_sub5.place(x=150,y=540,width=320)
        self.txt_sub5.current(0)

        #===buttons===
        self.btn_add= Button(self.root,text='Save',font=("Times New Roman",15,"bold"),bg="#CD5B45",fg="white",cursor="hand2", command=self.add)
        self.btn_add.place(x=150,y=600,width=110,height=40)
        self.btn_update= Button(self.root,text='Update',font=("Times New Roman",15,"bold"),bg="#CD5B45",fg="white",cursor="hand2",command=self.update)
        self.btn_update.place(x=270,y=600,width=110,height=40)
        self.btn_delete= Button(self.root,text='Delete',font=("Times New Roman",15,"bold"),bg="#CD5B45",fg="white",cursor="hand2",command=self.delete)
        self.btn_delete.place(x=390,y=600,width=110,height=40)
        self.btn_clear= Button(self.root,text='Clear',font=("Times New Roman",15,"bold"),bg="#CD5B45",fg="white",cursor="hand2",command=self.clear)
        self.btn_clear.place(x=510,y=600,width=110,height=40)

        #====searchpanel===
        self.var_search=StringVar()
        lbl_search_courseName=Label (self.root,text="Course Name", font=("Times New Roman",15,"bold"),bg='#CD6889').place(x=720,y=260)
        txt_search_courseName=Entry(self.root, textvariable=self.var_search, font=("Times New Roman",15,"bold"),bg='lightyellow').place(x=870,y=260,width=180)
        btn_search= Button(self.root,text='Search',font=("Times New Roman",15,"bold"),bg="#CD5B45",fg="white",cursor="hand2",command=self.search).place(x=1070,y=260,width=120,height=28)
        
        #===content===
        self.C_Frame=Frame(self.root,bd=2,relief=RIDGE)
        self.C_Frame.place(x=720,y=300,width=750,height=440)

        scrolly=Scrollbar(self.C_Frame,orient=VERTICAL)
        scrollx=Scrollbar(self.C_Frame,orient=HORIZONTAL)
        self.CourseTable=ttk.Treeview(self.C_Frame,columns=("number","name","duration","sub1","sub2","sub3","sub4","sub5"),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        
        
        self.CourseTable.heading("number",text="S.No")
        self.CourseTable.heading("name",text=" Course Name")
        self.CourseTable.heading("duration",text="Duration")
        self.CourseTable.heading("sub1",text="Subject 1")
        self.CourseTable.heading("sub2",text="Subject 2")
        self.CourseTable.heading("sub3",text="Subject 3")
        self.CourseTable.heading("sub4",text="Subject 4")
        self.CourseTable.heading("sub5",text="Subject 5")
        self.CourseTable["show"]='headings'
        
        self.CourseTable.column("number",width=80)
        self.CourseTable.column("name",width=100)
        self.CourseTable.column("duration",width=100)
        self.CourseTable.column("sub1",width=100)
        self.CourseTable.column("sub2",width=100)
        self.CourseTable.column("sub3",width=100)
        self.CourseTable.column("sub4",width=100)
        self.CourseTable.column("sub5",width=100)
        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        
#===========================================================

    def clear(self):
        self.show()
    
        self.var_name.set("")
        self.var_duration.set("")
        self.var_sub1.set("")
        self.var_sub2.set("")
        self.var_sub3.set("")
        self.var_sub4.set("")
        self.var_sub5.set("")
        self.var_search.set("")
        self.txt_course.config(state=NORMAL)
 

    def delete(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                print(row)
                if row==None:
                    messagebox.showerror("Error","Please select course from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?", parent=self.root)
                    if op==True:
                        cur.execute("delete from course where name=?",(self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Course deleted successfully",parent=self.root)
                        self.clear()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def get_data(self,ev):
        self.txt_course.config(state='readonly')
        self.txt_course
        r=self.CourseTable.focus()
        content=self.CourseTable.item(r)
        row=content["values"]
        #print(row)
        self.var_sno.set(row[1])
        self.var_name.set(row[2])
        self.var_duration.set(row[3])
        self.var_sub1.set(row[4])
        self.var_sub2.set(row[5])
        self.var_sub3.set(row[6])
        self.var_sub4.set(row[7])
        self.var_sub5.set(row[8])
        #self.var_sub6.set(row[8])
        #self.var_course.set(row[4])

    def add(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where name=?",(self.var_name.get(),))
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","Course Name already present",parent=self.root)
                else:
                    cur.execute("insert into course (name,duration,sub1,sub2,sub3,sub4,sub5) values(?,?,?,?,?,?,?)" ,(
                        self.var_name.get(),
                        self.var_duration.get(),
                        self.var_sub1.get(),
                        self.var_sub2.get(),
                        self.var_sub3.get(),
                        self.var_sub4.get(),
                        self.var_sub5.get(),
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course Added Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def update(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Course Name should be required",parent=self.root)
            else:
                cur.execute("select * from course where course=?",(self.var_name.get(),))
                row=cur.fetchone()
                print(row)
                if row==None:
                    messagebox.showerror("Error","Select Course from list",parent=self.root)
                else:
                    cur.execute("Update course set duration=?,sub1=?,sub2=?,sub3=?,sub4=?,sub5=? where course=?" ,(
                        self.var_duration.get(),
                        self.var_sub1.get(),
                        self.var_sub2.get(),
                        self.var_sub3.get(),
                        self.var_sub4.get(),
                        self.var_sub5.get(),
                        self.var_name.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Course updated Successfully",parent=self.root)
                    self.show()

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
        
    def show(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")

    def search(self):
        con=sqlite3.connect(database="rms.db")
        cur=con.cursor()
        try:
            cur.execute(f"select * from course where name LIKE '%{self.var_search.get()}%'")
            rows=cur.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")        

if __name__=="__main__":
    root=Tk()
    obj=CourseClass(root)
    root.mainloop()


       