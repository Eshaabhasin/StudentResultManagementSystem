import sqlite3
def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()

    cur.execute("CREATE TABLE course(cid INTEGER text PRIMARY KEY,name text,duration text, sub1 text,sub2 text,sub3 text,sub4 text,sub5 text)")
    con.commit()
    
    cur.execute("CREATE TABLE student(roll INTEGER PRIMARY KEY,name text,email text,gender text,dob text,contact text,year text,course text)" )
    con.commit()

    cur.execute("CREATE TABLE result(rid INTEGER PRIMARY KEY,roll text, name text, course text, subja text, subjb text, subj3c text, subjd text, subje text, fullmarks text, totalmarks text, per text)" )
    con.commit()

    cur.execute("CREATE TABLE employee(eid INTEGER PRIMARY KEY,f_name text, l_name text, contact text, email text, question text, answer text, password text)" )
    con.commit()


    

    con.close()



create_db()