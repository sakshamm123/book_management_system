from tkinter import *
from PIL import ImageTk,Image #PIL -> Pillow
import pymysql
from tkinter import messagebox


import os
import subprocess

def issuebook():
    subprocess.call(["python", "issueBook.py"])
    root.destroy

def returnbook():
    subprocess.call(["python","returnBook.py"])
    root.destroy

def addbook():
    subprocess.call(["python","addBook.py"])

def deletebook():
    subprocess.call(["python","deleteBook.py"])
    

def viewbook():
    subprocess.call(["python","viewBook.py"])

def requestbook():
    subprocess.call(["python","requestBook.py"])
    
    


mypass="root"
mydatabase="mydb"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()





#enter table names here
bookTable = "books"

#desinging a window

root = Tk()
root.title("Library")
root.minsize(width=700, height=600)
root.geometry("1920x1080")
image=Image.open("lib1.jpg")

# Resize the image using resize() method
resize_image = image.resize((1920, 1080))
 
img = ImageTk.PhotoImage(resize_image)

     
# create label and add resize image
label6 = Label(image=img)
label6.image = img
label6.pack()




#adding a heading Frame to library
headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="BOOK MANAGEMENT SYSTEM", bg="black", 
                fg="white", font=('Courier',15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

#Add the buttons
btn1 = Button(root, text="Add Book Details", bg="black", fg="white", command=addbook)
btn1.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

btn6 = Button(root, text="Request Book", bg="black", fg="white", command=requestbook)
btn6.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg="black", fg="white", command=deletebook)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book list", bg="black", fg="white", command=viewbook)
btn3.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book/Rent Book", bg="black", fg="white", command=issuebook)
btn4.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg="black", fg="white", command=returnbook)
btn5.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

root.mainloop() #call the mainloop to run the application
