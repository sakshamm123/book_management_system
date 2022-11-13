from tkinter import Tk,Label,Frame,Entry,FLAT,Canvas,Button
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox
import os
import subprocess


def run_program():
    subprocess.call(["python", "homepage.py"])
    root.destroy()

def run_program1():
    subprocess.call(["python","signuppage.py"])
    root.destroy()

def forgot_Password():
    subprocess.call(["python","forgot_password.py"])
    root.destroy


root=Tk()
root.title("Login Page")
root.maxsize(False,False)
root.geometry("700x600")

def check_data():
    if username_entry.get()=='' or password_entry.get()=='':
        messagebox.showerror('Error','All fields are required',parent=root)

    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='root',database='mydb')
            cur = con.cursor()
            cur.execute('select * from employee where username=%s and password=%s',(username_entry.get(),password_entry.get()))
            row=cur.fetchone()
            if row == None:
                messagebox.showerror('Error','Invalid USERNAME & PASSWORD',parent=root)
                                   
            else:
                messagebox.showinfo('Success','Welcome',parent=root)
                run_program()
            con.close()
        except Exception as es:
            messagebox.showerror('Error',f'Error due to {str(es)}',parent=root)
            #messagebox.showinfo('Success','Successfully Login',parent=self.root)





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
        # ============ Sign In label =============================================
        # ========================================================================
sign_in_label = Label(lgn_frame, text="Sign In", bg="#040405", fg="white",
                                    font=("yu gothic ui", 17, "bold"))
sign_in_label.place(x=195, y=130)
        # ========================================================================
        # ============================username====================================
        # ========================================================================
username_label = Label(lgn_frame, text="Username", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
username_label.place(x=55, y=170)

username_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui ", 12, "bold"))
username_entry.place(x=80, y=200, width=270)

username_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
username_line.place(x=55, y=230)

       # ===== Username icon =========
username_icon = Image.open('images\\username_icon.png')
photo = ImageTk.PhotoImage(username_icon)
username_icon_label = Label(lgn_frame, image=photo, bg='#040405')
username_icon_label.image = photo
username_icon_label.place(x=55, y=197)

        # ========================================================================
        # ============================password====================================
        # ========================================================================
password_label = Label(lgn_frame, text="Password", bg="#040405", fg="#4f4e4d",
                                    font=("yu gothic ui", 13, "bold"))
password_label.place(x=55, y=250)

password_entry = Entry(lgn_frame, highlightthickness=0, relief=FLAT, bg="#040405", fg="#6b6a69",
                                    font=("yu gothic ui", 12, "bold"), show="*")
password_entry.place(x=80, y=280, width=244)

password_line = Canvas(lgn_frame, width=300, height=2.0, bg="#bdb9b1", highlightthickness=0)
password_line.place(x=55, y=310)

# ======== Password icon ================
password_icon = Image.open('images\\password_icon.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(lgn_frame, image=photo, bg='#040405')
password_icon_label.image = photo
password_icon_label.place(x=55, y=277)


#=========== show / hide password  ============================================================
def show():
    hide_button = Button(lgn_frame, image=hide_image, command=hide, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
    hide_button.place(x=330, y=277)
    password_entry.config(show='')

def hide():
    show_button = Button(lgn_frame, image=show_image, command=show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
    show_button.place(x=330, y=277)
    password_entry.config(show='*')

#
show_image = ImageTk.PhotoImage \
            (file='images\\show.png')

hide_image = ImageTk.PhotoImage \
            (file='images\\hide.png')

show_button = Button(lgn_frame, image=show_image, command=show, relief=FLAT,
                                  activebackground="white"
                                  , borderwidth=0, background="white", cursor="hand2")
show_button.place(x=330, y=277)

        # ========================================================================
        # ============================login button================================
        # ========================================================================
lgn_button = Image.open('images\\btn1.png')
photo = ImageTk.PhotoImage(lgn_button)
lgn_button_label = Label(lgn_frame, image=photo, bg='#040405')
lgn_button_label.image = photo
lgn_button_label.place(x=55, y=350)
login = Button(lgn_button_label, text='LOGIN', font=("yu gothic ui", 13, "bold"), width=25, bd=0,
                           bg='#3047ff', cursor='hand2', activebackground='#3047ff', fg='white',command=check_data)
login.place(x=20, y=10)

        # ========================================================================
        # ============================Forgot password=============================
        # ========================================================================
forgot_button = Button(lgn_frame, text="Forgot Password ?",
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405"
                                    , borderwidth=0, background="#040405", cursor="hand2",command=forgot_Password)
forgot_button.place(x=140, y=410)
        # ========================================================================
        # ============================Sign up=============================
        # ========================================================================
user_button = Button(lgn_frame, text="New User?  Click Here to Sign Up" ,
                                    font=("yu gothic ui", 13, "bold underline"), fg="white", relief=FLAT,
                                    activebackground="#040405"
                                    , borderwidth=0, background="#040405", cursor="hand2",command=run_program1)
user_button.place(x=100, y=450)

root.mainloop()
