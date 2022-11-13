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


#Add the background Image
#same = True
#n = 0.28

#background_image = Image.open("lib.jpg")
#[imageSizeWidth, imageSizeHeight] = background_image.size
#set the new image width and height
#newImageSizeWidth = int(imageSizeWidth * n)

#if same:
#    newImageSizeHeight = int(imageSizeHeight * n)
#else:
#    newImageSizeHeight = int(imageSizeHeight / n)

#background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight))

#add an image to canva
#img = ImageTk.PhotoImage(background_image)
#canvas1 = Canvas(root)
#canvas1.create_image(300, 340, image=img)
#canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
#canvas1.pack(expand=True, fill=BOTH)

#adding a heading Frame to library
headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)
headingLabel = Label(headingFrame1, text="BOOK MANAGEMENT SYSTEM", bg="black", 
                fg="white", font=('Courier',15))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

#Add the buttons
btn1 = Button(root, text="Add Book Details", bg="black", fg="white", command=addbook)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Delete Book", bg="black", fg="white", command=deletebook)
btn2.place(relx=0.28, rely=0.5, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Book list", bg="black", fg="white", command=viewbook)
btn3.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

btn4 = Button(root, text="Issue Book", bg="black", fg="white", command=issuebook)
btn4.place(relx=0.28, rely=0.7, relwidth=0.45, relheight=0.1)

btn5 = Button(root, text="Return Book", bg="black", fg="white", command=returnbook)
btn5.place(relx=0.28, rely=0.8, relwidth=0.45, relheight=0.1)

root.mainloop() #call the mainloop to run the application
