from tkinter import *
from PIL import ImageTk,Image
import pymysql
from tkinter import messagebox

allBid = []


def Return():
    global submitBtn, quitBtn, LabelFrame, lb1, Canvas1, bookInfo1, root, status

    bid = bookInfo1.get()
    extractBid = "select bid from "+issueTable

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
                print(check)
            if check == 'issued':
                status = True
            else:
                status = False
        
        else:
            messagebox.showinfo("Error", "Book Id is not Present")

    except:
        messagebox.showinfo("Error", "Can't Fetch the book Id")

    #remove that book from issueTable
    issueSql = "delete from "+issueTable+" where bid = '"+bid+"'"
    show = "select * from "+issueTable
    
    print(bid in allBid)
    print(status)
    updateStatus = "update "+bookTable+" set status = 'available' where bid='"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSql)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success', "Book returned successfully")

        else:
            allBid.clear()
            messagebox.showerror('Message', "Please check the book id")
            root.destroy()
            return

    except:
        messagebox.showerror("Search Error", "the value you entered is wrong, try again!")

    allBid.clear()
    root.destroy()

def returnBook():
    global root, con, cur, labelFrame, submitBtn, quitBtn, Canvas1, bookInfo1, lb1

    root = Tk()
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
#    Canvas1.config(bg="pink")
#    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Return Book", bg="black", fg="white", font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg="black")
    labelFrame.place(relx=0.1, rely=0.3, relwidth=0.8, relheight=0.5)

    #book id
    lb1 = Label(labelFrame, text="Book Id", bg="black", fg="white")
    lb1.place(relx=0.05, rely=0.5)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.5, relwidth=0.62)

    #submit Button
    submitBtn = Button(root, text="Submit", bg="lightblue", fg="black", command=Return)
    submitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    #quit Button
    quitBtn = Button(root, text="Quit", bg="lightblue", fg="black", command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

bookTable = "books"
issueTable="books_issued"

mypass="root"
mydatabase="mydb"

con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()
returnBook()
#End
