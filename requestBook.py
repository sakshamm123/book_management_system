from tkinter import Tk,Label,Frame,Entry,FLAT,Canvas,Button
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import os
import subprocess
import math
import random
import smtplib

mypass="root"
mydatabase="mydb"
mail_id="bookmanagementsystem9@gmail.com"
app_password= "asqdfrhqbinbzzkp"

def send_mail():
    try:
        con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
        cur = con.cursor()
        cur.execute("select * from issued_books where bid = %s", bookid_entry.get())
        row = cur.fetchone()
        if row == None:
            messagebox.showerror("Error !", "Check your bid again or It is not Issued", parent=root)
        elif row != None:
            cur.execute("select email from issued_books where bid = %s",bookid_entry.get())
            email=cur.fetchone()
            s = smtplib.SMTP('smtp.gmail.com', 587)
            s.starttls()
            s.login(mail_id,app_password)
            s.sendmail('&&&&&&&&&&&',email,description_entry.get())
            messagebox.showinfo("success","Mail sent. Check your mail for more info",parent=root)
            root.destroy()
    except EXCEPTION as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}", parent=root)
                
                   
        
    

root=Tk()
root.title("Request Book")
root.maxsize(False,False)
root.geometry("700x600")



#background image
image=Image.open("lib.jpg")

# Resize the image using resize() method
resize_image = image.resize((700, 600))
 
img = ImageTk.PhotoImage(resize_image)
 
# create label and add resize image
label5 = Label(image=img)
label5.image = img
label5.pack()

lgn_frame = Frame(root, bg='#040405', width=450, height=500)
lgn_frame.place(x=120, y=60)

        # ========================================================================
        # ============ Request book  label =============================================
        # ========================================================================
sign_in_label = Label(lgn_frame, text="Request Book", bg="#040405", fg="white",
                                    font=("new york times", 40, "bold"))
sign_in_label.place(x=45, y=70)

        # ========================================================================
        # ============================Enter Book Id====================================
        # ========================================================================
bookid_label = Label(lgn_frame, text="Enter Book ID", bg="#040405", fg="white",
                                    font=("times new roman", 13, "bold"))
bookid_label.place(x=165, y=170)

bookid_entry = Entry(lgn_frame, highlightthickness=1, relief=FLAT, bg="#040405", fg="white",
                                    font=("times new roman", 12, "bold"))
bookid_entry.place(x=80, y=200, width=290)

#bookid_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
#bookid_line.place(x=80, y=230)

        # ========================================================================
        # ============================Description ====================================
        # ========================================================================
description_label = Label(lgn_frame, text="Enter Description", bg="#040405", fg="white",
                                    font=("times new roman", 13, "bold"))
description_label.place(x=165, y=260)

description_entry = Entry(lgn_frame, highlightthickness=1, relief=FLAT, bg="#040405", fg="white",
                                    font=("times new roman", 12, "bold"))
description_entry.place(x=80, y=290, width=290,height= 100)

#bookid_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
#bookid_line.place(x=55, y=320)

# -------Register  Button-----
bt_register = Button(lgn_frame, text="Send Mail", font=("times new roman", 20), bg="#0048ff", fg="white",bd=0, cursor="hand2",command= send_mail).place(x=105, y=415)

# -------Quit  Button-----
bt_quit = Button(lgn_frame, text="Quit", font=("times new roman", 20), bg="#0048ff", fg="white",bd=0, cursor="hand2",command= root.destroy).place(x=285, y=415)

root.mainloop()
