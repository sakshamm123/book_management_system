from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import ttk,messagebox
import os
import subprocess

def run_program():
    subprocess.call(["python", "login_page.py"])
    root.destroy()

root=Tk()
root.title("Sign up")
root.maxsize(False,False)
root.geometry("1980x1080")

def register_data():

    if firstname_entry.get() == "" or lastname_entry.get() == "" or username_entry.get() == "" or contact_entry.get() == "" or email_entry.get() == "" or age_entry.get() == "" or cmb_gender.get() == "" or password_entry.get() == "" or cpassword_entry.get() == "":
        messagebox.showerror("Error !", "All Fields are Required !", parent=root)
    elif password_entry.get() != cpassword_entry.get():
        messagebox.showerror("Error !", "Password Didn't Match !", parent=root)
    elif var_chk.get() == 0:
        messagebox.showerror("Error !", "Please Agree our Terms & Conditions", parent=root)
    else:
        try:
            con = pymysql.connect(host="localhost", user="root", password="root", database="mydb")
            cur = con.cursor()

            cur.execute("select * from employee where email=%s", email_entry.get())
            row = cur.fetchone()
            if row != None:
                messagebox.showerror("Error !", "Already Exists Email ! Try with another one.", parent=root)

            else:
                cur.execute("insert into employee (firstname,lastname,username,contact,email,age,gender,password) values(%s,%s,%s,%s,%s,%s,%s,%s)", (firstname_entry.get(), lastname_entry.get(), username_entry.get(), contact_entry.get(), email_entry.get(), age_entry.get(), cmb_gender.get(),password_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo("Success !", "Registration Completed !", parent=root)
                clear_data()

        except EXCEPTION as es:
            messagebox.showerror("Error", f"Error due to : {str(es)}", parent=root)



#background image
image=Image.open("lib1.jpg")

# Resize the image using resize() method
resize_image = image.resize((1980, 1080))
 
img = ImageTk.PhotoImage(resize_image)


 
# create label and add resize image
label1 = Label(image=img)
label1.image = img
label1.pack()


# ====== Login Frame =========================
lgn_frame = Frame(root, bg='#040405', width=850, height=600)
lgn_frame.place(x=320, y=100)



# ========================================================================
# ============ Sign In Image =============================================
# ========================================================================

sign_in_image = Image.open('images\\hyy.png')
photo = ImageTk.PhotoImage(sign_in_image)
sign_in_image_label = Label(lgn_frame, image=photo, bg='#040405')
sign_in_image_label.image = photo
sign_in_image_label.place(x=255, y=20)


        # ========================================================================
        # ============ Sign In label =============================================
        # ========================================================================
sign_in_label = Label(lgn_frame, text="Sign Up", bg="#040405", fg="white",
                                    font=("times new roman", 40, "bold"))
sign_in_label.place(x=395, y=30)

        # ========================================================================
        # ============================first name====================================
        # ========================================================================
firstname_label = Label(lgn_frame, text="First Name", bg="#040405", fg="white",
                                    font=("times new roman", 13, "bold"))
firstname_label.place(x=55, y=170)

firstname_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#000000", fg="white",
                                    font=("times new roman", 12, "bold"))
firstname_entry.place(x=150, y=170, width=250)

firstname_line = Canvas(lgn_frame, width=250, height=2.0, bg="#bdb9b1", highlightthickness=0)
firstname_line.place(x=150, y=200)

        # ========================================================================
        # ============================second name====================================
        # ========================================================================
lastname_label = Label(lgn_frame, text="Last Name", bg="#040405", fg="white",
                                    font=("times new roman", 13, "bold"))
lastname_label.place(x=425, y=170)

lastname_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#000000", fg="white",
                                    font=("times new roman", 12, "bold"))
lastname_entry.place(x=520, y=170, width=250)

lastname_line = Canvas(lgn_frame, width=250, height=2.0, bg="#bdb9b1", highlightthickness=0)
lastname_line.place(x=520, y=200)


        # ========================================================================
        # ============================contact====================================
        # ========================================================================
contact_label = Label(lgn_frame, text="Contact", bg="#040405", fg="white",
                                    font=("times new roman", 13, "bold"))
contact_label.place(x=55, y=240)

contact_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",
                                    font=("times new roman", 12, "bold"))
contact_entry.place(x=150, y=240, width=250)

contact_line = Canvas(lgn_frame, width=250, height=2.0, bg="#bdb9b1", highlightthickness=0)
contact_line.place(x=150, y=270)


# ========================================================================
# ============================email====================================
# ========================================================================
email_label = Label(lgn_frame, text="E-Mail", bg="#040405", fg="white",
                                    font=("times new roman", 13, "bold"))
email_label.place(x=425, y=240)

email_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",
                                    font=("times new roman", 12, "bold"))
email_entry.place(x=520, y=240, width=250)

email_line = Canvas(lgn_frame, width=250, height=2.0, bg="#bdb9b1", highlightthickness=0)
email_line.place(x=520, y=270)


        # ========================================================================
        # ============================age====================================
        # ========================================================================
age_label = Label(lgn_frame, text="Age", bg="#040405", fg="white",
                                    font=("times new roman", 13, "bold"))
age_label.place(x=55, y=310)

age_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",
                                    font=("times new roman", 12, "bold"))
age_entry.place(x=150, y=310, width=250)

age_line = Canvas(lgn_frame, width=250, height=2.0, bg="#bdb9b1", highlightthickness=0)
age_line.place(x=150, y=340)


# -------Gender


gender = Label(lgn_frame, text="Gender", font=("times new roman", 13, "bold"), bg="#040405", fg="white").place(x=425, y=310)
cmb_gender = ttk.Combobox(lgn_frame, font=("times new roman", 12), state='readonly', justify=CENTER)
cmb_gender['values']=("Select", "Male", "Female", "Other")
cmb_gender.place(x=520, y=310, width=250)
cmb_gender.current(0)

        # ========================================================================
        # ============================username====================================
        # ========================================================================
username_label = Label(lgn_frame, text="Username", bg="#040405", fg="white",
                                    font=("times new roman", 13, "bold"))
username_label.place(x=55, y=380)

username_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",
                                    font=("times new roman", 12, "bold"))
username_entry.place(x=150, y=380, width=250)

username_line = Canvas(lgn_frame, width=250, height=2.0, bg="#bdb9b1", highlightthickness=0)
username_line.place(x=150, y=410)


# ========================================================================
# ============================password====================================
# ========================================================================
password_label = Label(lgn_frame, text="Password", bg="#040405", fg="white",
                                    font=("times new roman", 13, "bold"))
password_label.place(x=425, y=380)

password_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",
                                    font=("times new roman", 12, "bold"))
password_entry.place(x=520, y=380, width=250)

password_line = Canvas(lgn_frame, width=250, height=2.0, bg="#bdb9b1", highlightthickness=0)
password_line.place(x=520, y=410)

# ========================================================================
# ============================ confirm password====================================
# ========================================================================
cpassword_label = Label(lgn_frame, text="Re-enter", bg="#040405", fg="white",
                                    font=("times new roman", 13, "bold"))
cpassword_label.place(x=55, y=450)

cpassword_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="white",
                                    font=("times new roman", 12, "bold"))
cpassword_entry.place(x=150, y=450, width=250)

cpassword_line = Canvas(lgn_frame, width=250, height=2.0, bg="#bdb9b1", highlightthickness=0)
cpassword_line.place(x=150, y=480)

        # --------Terms
var_chk = IntVar()
chk = Checkbutton(lgn_frame, text="I Agree the Terms & Conditions ", variable=var_chk, onvalue=1, offvalue=0, bg="white", font=("times new roman", 12)).place(x=425, y=460)




# -------Register  Button-----
bt_register = Button(lgn_frame, text="Register", font=("times new roman", 20), bg="#0048ff", fg="white",bd=0,command=register_data, cursor="hand2").place(x=325, y=500)

# -------Sign in Button-----
login = Button(lgn_frame, text="Sign In", font=("times new roman", 20), bd=0, bg="#0048ff", fg="white",cursor="hand2",command=run_program).place(x=450, y=500)

root.mainloop()
