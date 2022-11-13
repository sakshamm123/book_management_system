from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox

bookTable = "books"
issueTable="books_issued"

mypass="root"
mydatabase="mydb"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()


def issue():
    global issuebtn, labelFrame, inf1, inf2, lb1, quitBtn, root, Canvas1, status
    bid = inf1.get()        #take the book id with get()
    issueto = inf2.get()    #take the name to whom it is issued

    issuebtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()
    
    extractBid = "select bid from "+ bookTable
    try:
        cur.execute(extractBid)
        con.commit()

        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "select status from "+bookTable+" where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]
            if check == 'available':
                status = True
            else:
                status = False
        else:
            messagebox.showinfo("Error", "Book Id not present")
    except:
        messagebox.showinfo("Error", "Can't fetch the Book Id")

    issueSql = "insert into "+issueTable+" values ('"+bid+"', '"+issueto+"')"
    show = "select * from "+issueTable
    updateStatus = "update "+ bookTable+" set status = 'issued' where bid = '"+bid+"'"

    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo("Success", "Book Issued successfully")
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo("Message", "Book Already Issued")
            root.destroy()
            return
    except:
        messagebox.showinfo("Search Error", "The value insert is wrong, Try again")
    print(bid)
    print(issueto)
    allBid.clear()

def issuebook():
    global issuebtn, labelFrame, inf1, inf2, lb1, quitBtn, root, Canvas1, status

    root=Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")
    #background image
    image=Image.open("lib.jpg")

    # Resize the image using resize() method
    resize_image = image.resize((700, 600))
 
    img = ImageTk.PhotoImage(resize_image)

     
# create label and add resize image
    label6 = Label(image=img)
    label6.image = img
    label6.pack()

#    Canvas1 = Canvas(root)
#    Canvas1.config(bg="yellow")
#    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel1 = Label(headingFrame1, text="Issue Book", bg="black", fg="white", font=('Courier',15))
    headingLabel1.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg="black")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    #Book Id
    lb1 = Label(labelFrame, text="Book Id", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.2)

    inf1 = Entry(labelFrame)
    inf1.place(relx=0.3, rely=0.2, relwidth=0.62)

    #to whom book is issued, student name
    lb2 = Label(labelFrame, text="Issue To", bg="black", fg="white")
    lb2.place(relx=0.05, rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3, rely=0.4, relwidth=0.62)

    #Issue Button
    issuebtn = Button(root, text="Issue", bg="#d1ccc0", fg="black", command=issue)
    issuebtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg="#aaa69d", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

allBid = []  #list to store all the book ids we have

issuebook()

