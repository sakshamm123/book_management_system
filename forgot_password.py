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
app_password="asqdfrhqbinbzzkp"

    
def check_Pass():
    global issuebtn, lgn_frame, password_entry, rpassword_entry, password_label,rpassword_label, root, Canvas1, pass_btn,email_entry
    password = password_entry.get()
        
    try:
        if password_entry.get() != rpassword_entry.get():
            messagebox.showerror("Error ! ","Password didn't match",parent=root)
        else:
            con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
            cur = con.cursor()
            update="UPDATE employee SET password = '"+password+"' WHERE email = '"+e_mail+"'"
            cur.execute(update)
            con.commit()
            con.close()
            print("done")
            messagebox.showinfo("success","Password Updated",parent=root)
            root.destroy()
                
    except EXCEPTION as es:
        messagebox.showerror("Error", f"Error due to : {str(es)}", parent=root)
   
def pass_change():

    global issuebtn, lgn_frame, password_entry, rpassword_entry, password_label,rpassword_label, root, Canvas1, pass_btn,email_entry

    root=Tk()
    root.title("Change Password")
    root.maxsize(False,False)
    root.geometry("700x600")




#-------background image
    image=Image.open("lib.jpg")

#--- ----Resize the image using resize() method
    resize_image = image.resize((700, 600))
 
    img = ImageTk.PhotoImage(resize_image)
 
#--- ---create label and add resize image
    label5 = Label(image=img)
    label5.image = img
    label5.pack()


#== ======== Login Frame =========================
    lgn_frame = Frame(root, bg='#040405', width=450, height=500)
    lgn_frame.place(x=120, y=60)



#-=-=-=-=-========================================================================
# ========-=-=-=-===== Sign In Image =============================================
# -=-=-=-=========================================================================
    sign_in_image = Image.open('images\\hyy.png')
    photo = ImageTk.PhotoImage(sign_in_image)
    sign_in_image_label = Label(lgn_frame, image=photo, bg='#040405')
    sign_in_image_label.image = photo
    sign_in_image_label.place(x=155, y=20)




       # ========================================================================
        # ============ Change password label =============================================
        # ========================================================================
    sign_in_label = Label(lgn_frame, text="Change Password", bg="#040405", fg="white",
                                    font=("times new roman", 17, "bold"))
    sign_in_label.place(x=145, y=130)

        # ========================================================================
        # ============================password label====================================
        # ========================================================================
    password_label = Label(lgn_frame, text="Password", bg="#040405", fg="white",
                                    font=("times new roman", 13, "bold"))
    password_label.place(x=55, y=240)

    password_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",
                                    font=("times new roman", 12, "bold"))

    print(password_entry.get())
    password_entry.place(x=150, y=240, width=250)

    password_line = Canvas(lgn_frame, width=250, height=2.0, bg="#bdb9b1", highlightthickness=0)
    password_line.place(x=150, y=270)
    

        # ========================================================================
        # ============================Re-enter Password ====================================
        # ========================================================================
    rpassword_label = Label(lgn_frame, text="Re-enter", bg="#040405", fg="white",
                                    font=("times new roman", 13, "bold"))
    rpassword_label.place(x=55, y=310)

    rpassword_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",
                                    font=("times new roman", 12, "bold"))
    rpassword_entry.place(x=150, y=310, width=250)


    rpassword_line = Canvas(lgn_frame, width=250, height=2.0, bg="#bdb9b1", highlightthickness=0)
    rpassword_line.place(x=150, y=340)
#------------------change password button -----
    pass_btn = Button(lgn_frame, text="Change Password", font=("times new roman", 20), bg="#0048ff", fg="white",bd=0, cursor="hand2",command=check_Pass).place(x=125, y=400)




    root.mainloop()

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)] # generate otp

def otp_check():
    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    cur.execute("select * from employee where email=%s", email_entry.get()) #check whether email exist or not
    row = cur.fetchone()
    if row == None:
        messagebox.showerror("Error !", "Check your email again", parent=root)
    else:
        otp = OTP + " is your OTP"    # compose message
        msg= otp
        s = smtplib.SMTP('smtp.gmail.com', 587)  # start session to send mail
        s.starttls()
        s.login(mail_id, app_password)  # senders mail and app password
        s.sendmail('&&&&&&&&&&&',email_entry.get(),msg)   # send the mail to the mention email and add message to mail
def valid_otp():
    if otp_entry.get() == OTP:   # validate otp
        messagebox.showinfo("Success !","OTP verified", parent=root)  
        root.destroy()   # closes the window
        pass_change()
    else:
        messagebox.showerror("Error !","OTP is not correct check again",parent=root) 
    
root=Tk()
root.title("Forgot Password")
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


# ====== Login Frame =========================
lgn_frame = Frame(root, bg='#040405', width=450, height=500)
lgn_frame.place(x=120, y=60)



        # ========================================================================
        # ============ Sign In Image =============================================
        # ========================================================================
sign_in_image = Image.open('images\\hyy.png')
photo = ImageTk.PhotoImage(sign_in_image)
sign_in_image_label = Label(lgn_frame, image=photo, bg='#040405')
sign_in_image_label.image = photo
sign_in_image_label.place(x=155, y=20)




       # ========================================================================
        # ============ Forgot password label =============================================
        # ========================================================================
sign_in_label = Label(lgn_frame, text="Forgot Password", bg="#040405", fg="white",
                                    font=("times new roman", 17, "bold"))
sign_in_label.place(x=145, y=130)

        # ========================================================================
        # ============================EMail====================================
        # ========================================================================
email_label = Label(lgn_frame, text="Email", bg="#040405", fg="white",
                                    font=("times new roman", 13, "bold"))
email_label.place(x=55, y=240)

email_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",
                                    font=("times new roman", 12, "bold"))
email_entry.place(x=150, y=240, width=250)

email_line = Canvas(lgn_frame, width=250, height=2.0, bg="#bdb9b1", highlightthickness=0)
email_line.place(x=150, y=270)


        # ========================================================================
        # ============================OTP====================================
        # ========================================================================
otp_label = Label(lgn_frame, text="OTP", bg="#040405", fg="white",
                                    font=("times new roman", 13, "bold"))
otp_label.place(x=55, y=310)

otp_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",
                                    font=("times new roman", 12, "bold"))
otp_entry.place(x=150, y=310, width=250)

otp_line = Canvas(lgn_frame, width=250, height=2.0, bg="#bdb9b1", highlightthickness=0)
otp_line.place(x=150, y=340)


# -------Send Otp button -----
otp_btn = Button(lgn_frame, text="Send OTP", font=("times new roman", 20), bg="#0048ff", fg="white",bd=0, cursor="hand2",command=otp_check).place(x=55, y=400)


#--------Validate OTP button -------
otpcheck_btn = Button(lgn_frame, text="Check OTP", font=("times new roman", 20), bg="#0048ff", fg="white",bd=0, cursor="hand2",command=valid_otp).place(x=250, y=400)


e_mail=email_entry.get() # add email entered to the variable

root.mainloop()


