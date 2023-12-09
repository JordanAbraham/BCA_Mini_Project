from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
import mysql.connector
import qrcode
import cv2
import numpy as np
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt; plt.rcdefaults()
import matplotlib.pyplot as plt



root = Tk()
root.title("WARE HOUSE MANGEMENT")
root.geometry("1000x650")
root.maxsize(1000,650)

mydb = mysql.connector.connect(
  host="localhost",
  user="Jordan",
  password="Jordan@25",
  port = "3306",
  database = "WMP"
)
mycursor = mydb.cursor()



def singUp():
    frame2.destroy()

    # create frame3 for sing up entry
    frame3 = Frame(root, width=500, height=650, bg="#c3c4c3")
    frame3.pack(side=LEFT)

    FirstName = Label(frame3, text="First Name : ", font=("Times New Roman", 12, 'bold'), bg="#c3c4c3", fg="#4c4e4d")
    FirstName.place(x=146, y=100 )
    LastName = Label(frame3, text="Last Name : ", font=("Times New Roman", 12, 'bold'), bg="#c3c4c3", fg="#4c4e4d")
    LastName.place(x=145, y=140)
    PhoneNumber = Label(frame3, text="Phone Number : ", font=("Times New Roman", 12, 'bold'), bg="#c3c4c3", fg="#4c4e4d")
    PhoneNumber.place(x=120, y=180)
    EmailId = Label(frame3, text="Email Id : ", font=("Times New Roman", 12, 'bold'), bg="#c3c4c3", fg="#4c4e4d")
    EmailId.place(x=162, y=220)
    Password = Label(frame3, text="Password : ", font=("Times New Roman", 12, 'bold'), bg="#c3c4c3", fg="#4c4e4d")
    Password.place(x=155, y=260)
    ConfirmPassword = Label(frame3, text="Confirm Password : ", font=("Times New Roman", 12, 'bold'), bg="#c3c4c3", fg="#4c4e4d")
    ConfirmPassword.place(x=98, y=300)

    FirstNameBox = Entry(frame3, font=("Times New Roman", 12, 'bold'))
    FirstNameBox.place(x=240, y=100)
    LastNameBox = Entry(frame3, font=("Times New Roman", 12, 'bold'))
    LastNameBox.place(x=240, y=140)
    PhoneNumberBox = Entry(frame3, font=("Times New Roman", 12, 'bold'))
    PhoneNumberBox.place(x=240, y=180)
    EmailIdBox = Entry(frame3, font=("Times New Roman", 12, 'bold'))
    EmailIdBox.place(x=240, y=220)
    PasswordBox = Entry(frame3, font=("Times New Roman", 12, 'bold'),show="*")
    PasswordBox.place(x=240, y=260)
    ConfirmPasswordBox = Entry(frame3, font=("Times New Roman", 12, 'bold'),show="*")
    ConfirmPasswordBox.place(x=240, y=300)

    def SingUpClick():
        data = "Please Enter All Fileld"
        if FirstNameBox.get()!= "" or LastNameBox.get()!= "" or PhoneNumberBox.get()!= "" or EmailIdBox.get()!= "" or PasswordBox.get()!= "" or ConfirmPasswordBox.get()!= "" :
            if PasswordBox.get() == ConfirmPasswordBox.get():
                sql = "INSERT INTO employee (first_name, last_name, phone_no, email, password) VALUES (%s, %s, %s, %s, %s)"
                val = (FirstNameBox.get(), LastNameBox.get(), PhoneNumberBox.get(), EmailIdBox.get(), PasswordBox.get())
                mycursor.execute(sql, val)
                mydb.commit()
                data="Data entered sucessfully"

            else:
                data = "Password Not Match"
        else:
            data = "Please Enter All Fileld"

        Label3 = Label(frame3, text=data, font=("Times New Roman", 12, 'bold'), bg="#c3c4c3", fg="#4c4e4d")
        Label3.place(x=162, y=450)



    SubmitButton = Button(frame3, text="Submit", font=("Times New Roman", 12, 'bold'), bg="#4c4e4d", fg="#c3c4c3", padx=125, command=SingUpClick )
    SubmitButton.place(x=100, y=350)

# Login function
def login():
    global pwd
    try:
        mycursor.execute(f"select *from employee where email ='{NameBox.get()}'")
        usernames = mycursor.fetchall()
        for username in usernames:
            pwd = username[5]
            print(pwd)

        if pwd==PassBox.get():
            frame1.destroy()
            frame2.destroy()
            home()

    except:
        errorup = Label(frame2, text="Enter Correct username and password", font=("Times New Roman", 12, 'bold'), bg="#c3c4c3", fg="#4c4e4d")
        errorup.place(x=130, y=320)

#Title Frame

frame1 = Frame(root,width=500, height=650, bg='#4c4e4d')
frame1.pack(side=LEFT)

#Login frame
frame2 = Frame(root, width=500, height=650, bg="#c3c4c3")
frame2.pack(side=LEFT)

#title Image
img = ImageTk.PhotoImage(Image.open("Untitled.png"))
label = Label(frame1, image = img)
label.place(x=0, y=0)


label1 = Label(frame2, text="   Email Id : ", font=("Times New Roman", 12, 'bold'),bg="#c3c4c3", fg="#4c4e4d" )
label1.place(x = 130, y = 200)
NameBox = Entry(frame2, font=("Times New Roman", 12, 'bold'))
NameBox.insert(0, "username")
NameBox.place(x=220, y=200)

label2 = Label(frame2, text="Password : ",font=("Times New Roman", 12, 'bold'),bg="#c3c4c3", fg="#4c4e4d" )
label2.place(x = 135, y = 230)
PassBox = Entry(frame2, font=("Times New Roman", 12, 'bold'),show="*")
# PassBox.insert(0, "")
PassBox.place(x=220, y=230)

LoginButton = Button(frame2, text ="LogIn",font=("Times New Roman", 12, 'bold'),bg="#4c4e4d", fg="#c3c4c3", padx=30, command=login )
LoginButton.place(x=140, y=270)

SingUPButton = Button(frame2, text ="SignUP",font=("Times New Roman", 12, 'bold'),bg="#4c4e4d", fg="#c3c4c3", padx=30, command=singUp )
SingUPButton.place(x=260, y=270)


def home():
    frameTop = Frame(root,width=1000, height=650, bg="#707371")
    frameTop.pack(side=TOP)

    ProductScanner = Button(frameTop, text="Product Scanner", font=("Times New Roman", 12, 'bold'), bg="#4c4e4d", fg="White", padx=188, pady=150, relief='ridge', command=productScannerFun, activebackground='#2c2d2c')
    ProductScanner.grid(row=0, column=0)

    GenQrCode = Button(frameTop, text="Genrate Qr Code", font=("Times New Roman", 12, 'bold'), bg="#4c4e4d", fg="White", padx=188, pady=150,relief='ridge', command=genQrCodeFun, activebackground='#2c2d2c')
    GenQrCode.grid(row=0, column=1)

    ProductDetails = Button(frameTop, text="Product Details", font=("Times New Roman", 12, 'bold'), bg="#4c4e4d", fg="White", padx=191, pady=150,relief='ridge', command=productDetailsFun, activebackground='#2c2d2c')
    ProductDetails.grid(row=1, column=0)

    EmployeeDetils = Button(frameTop, text="Employee Detils", font=("Times New Roman", 12, 'bold'), bg="#4c4e4d", fg="White", padx=191, pady=150,relief='ridge', activebackground='#2c2d2c', command=employeeDetailsFun)
    EmployeeDetils.grid(row=1, column=1)



def employeeDetailsFun():

    window = tk.Tk()
    window.configure(bg="#d3d4d3")
    window.title("Employee Details")
    window.maxsize(950, 650)

    employeeFrame = Frame(window, width=1000, height=610, bg="#c3c4c3")
    employeeFrame.pack(side=BOTTOM)

    e = Label(employeeFrame, width=20, text='Employee Deatils', bg='#c3c4c3',font=("Times New Roman", 22, 'bold'), fg='#444645')
    e.place(x=330, y=30)

    my_w = Frame(employeeFrame)
    my_w.place(x=0, y=100)

    mycursor.execute("SELECT * FROM employee")
    usernames = mycursor.fetchall()

    e = Label(my_w, width=20, text='First Name', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=0)
    e = Label(my_w, width=20, text='Last Name', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=1)
    e = Label(my_w, width=20, text='Phone Number', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=2)
    e = Label(my_w, width=20, text='Email', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=3)
    e = Label(my_w, width=20, text='Employee Id', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=4)
    e = Label(my_w, width=20, text='Password', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=5)

    i = 1
    for student in usernames:
        for j in range(len(student)):
            # e = Entry(my_w, width=10, fg='blue')
            e = Label(my_w, width=20, text=student[j], borderwidth=1, relief='ridge', anchor="center", bg='#d3d4d3',
                      font=("Times New Roman", 12, 'bold'), fg='#444645', pady=4, padx=4)
            e.grid(row=i, column=j)
            # e.insert(END, student[j])
        i = i + 1


    window.mainloop()


def genQrCodeFun():
    window = tk.Tk()
    window.configure(bg="#d3d4d3")
    window.title("Genrate Qr Code")
    window.maxsize(1000, 650)
    window.minsize(1000, 650)

    title = Label(window, width=20, text='Genraete Qr Code', bg='#d3d4d3', font=("Times New Roman", 22, 'bold'),fg='#444645')
    title.place(x=330, y=30)

    frame = Frame(window, bg='#d3d4d3')
    frame.place(x=300, y=150)


    ProductName = Label(frame, text="Product Name : ", bg='#d3d4d3',font=("Times New Roman", 12, 'bold'),fg='#444645')
    ProductName.grid(row=0, column=0, sticky=E, padx=10)
    ProductNameBox = Entry(frame,font=("Times New Roman", 12, 'bold'),fg='#444645')
    ProductNameBox.grid(row=0, column=1, pady=5)


    CompanyName = Label(frame, text="Company Name : ", bg='#d3d4d3',font=("Times New Roman", 12, 'bold'),fg='#444645')
    CompanyName.grid(row=1, column=0, sticky=E, padx=10)
    CompanyNameBox = Entry(frame,font=("Times New Roman", 12, 'bold'),fg='#444645')
    CompanyNameBox.grid(row=1, column=1, pady=5)

    Country = Label(frame, text="Country : ", bg='#d3d4d3',font=("Times New Roman", 12, 'bold'),fg='#444645')
    Country.grid(row=2, column=0, sticky=E, padx=10)
    CountryBox = Entry(frame,font=("Times New Roman", 12, 'bold'),fg='#444645')
    CountryBox.grid(row=2, column=1, pady=5)

    Import_date = Label(frame, text="Import Date : ", bg='#d3d4d3',font=("Times New Roman", 12, 'bold'),fg='#444645')
    Import_date.grid(row=3, column=0, sticky=E, padx=10)
    Import_dateBox = Entry(frame, font=("Times New Roman", 12, 'bold'),fg='#444645')
    Import_dateBox.grid(row=3, column=1, pady=5)
    label = Label(frame, text="* Format YYYY-MM-DD", bg='#d3d4d3',font=("Times New Roman", 10),fg='Black')
    label.grid(row=3, column=2, pady=5, padx=10)

    Export_date = Label(frame, text="Export Date : ", bg='#d3d4d3',font=("Times New Roman", 12, 'bold'),fg='#444645')
    Export_date.grid(row=4, column=0, sticky=E, padx=10)
    Export_dateBox = Entry(frame,font=("Times New Roman", 12, 'bold'),fg='#444645')
    Export_dateBox.grid(row=4, column=1, pady=5)
    label = Label(frame, text="* Format YYYY-MM-DD", bg='#d3d4d3', font=("Times New Roman", 10), fg='Black')
    label.grid(row=4, column=2, pady=5, padx=10)

    Manufacturing_date = Label(frame, text="Manufacturing Date : ", bg='#d3d4d3', font=("Times New Roman", 12, 'bold'), fg='#444645')
    Manufacturing_date.grid(row=5, column=0, sticky=E, padx=10)
    Manufacturing_dateBox = Entry(frame,font=("Times New Roman", 12, 'bold'),fg='#444645')
    Manufacturing_dateBox.grid(row=5, column=1, pady=5)
    label = Label(frame, text="* Format YYYY-MM-DD", bg='#d3d4d3', font=("Times New Roman", 10), fg='Black')
    label.grid(row=5, column=2, pady=5, padx=10)

    Expiry_date = Label(frame, text="Expiry Date : ", bg='#d3d4d3',font=("Times New Roman", 12, 'bold'),fg='#444645')
    Expiry_date.grid(row=6, column=0, sticky=E, padx=10)
    Expiry_dateBox = Entry(frame,font=("Times New Roman", 12, 'bold'),fg='#444645')
    Expiry_dateBox.grid(row=6, column=1, pady=5)
    label = Label(frame, text="* Format YYYY-MM-DD", bg='#d3d4d3', font=("Times New Roman", 10), fg='Black')
    label.grid(row=6, column=2, pady=5, padx=10)

    Location = Label(frame, text="Location In Wear House : ", bg='#d3d4d3',font=("Times New Roman", 12, 'bold'),fg='#444645')
    Location.grid(row=7, column=0, sticky=E, padx=10)
    LocationBox = Entry(frame,font=("Times New Roman", 12, 'bold'),fg='#444645')
    LocationBox.grid(row=7, column=1, pady=5)

    Price = Label(frame, text="Price : ", bg='#d3d4d3', font=("Times New Roman", 12, 'bold'),fg='#444645')
    Price.grid(row=8, column=0, sticky=E, padx=10)
    PriceBox = Entry(frame, font=("Times New Roman", 12, 'bold'), fg='#444645')
    PriceBox.grid(row=8, column=1, pady=5)

    def addDaatabase():

        if ProductNameBox.get() != "" or CompanyNameBox.get() != "" or CountryBox.get() != "" or Import_dateBox.get() != "" or Export_dateBox.get() != "" or Manufacturing_dateBox.get() != "" or Expiry_dateBox.get()!= "" or LocationBox.get()!= "" or PriceBox.get()!= "":

            mycursor.execute("select max(Product_id) from products")
            Id = mycursor.fetchone()
            Product_Id = Id[0] + 1
            # Product_Id = 1
            pp = str(Product_Id)

            roll =pp+" "+ProductNameBox.get()+" "+CompanyNameBox.get()+" "+CountryBox.get()+" "+Import_dateBox.get()+" "+Export_dateBox.get()+" "+Manufacturing_dateBox.get()+" "+Expiry_dateBox.get()+" "+LocationBox.get()+" "+PriceBox.get()
            qr_img = qrcode.make(roll)
            dataString = roll
            stre = f"Barcode/{dataString}.jpg"
            qr_img.save(stre)

            sql = "INSERT INTO Products(Product_name ,Cop_name , Country , Import_date ,Export_date ,Manufacturing_date, Expiry_date ,location, Total_price) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (ProductNameBox.get(), CompanyNameBox.get(), CountryBox.get(), Import_dateBox.get(), Export_dateBox.get(), Manufacturing_dateBox.get(), Expiry_dateBox.get(), LocationBox.get(), int(PriceBox.get()))
            mycursor.execute(sql, val)
            mydb.commit()
            data = f"Image Stored in Path =  {stre}"

        else:
            data = "Please Enter All Fileld"

        Label3 = Label(frame, text=data, font=("Times New Roman", 12, 'bold'), bg="#c3c4c3", fg="#4c4e4d")
        Label3.grid(row=10, columnspan=3, pady=10)

    Submit = Button(frame, text="Store Data In DataBase",  bg='#444645',font=("Times New Roman", 12, 'bold'),fg='#d3d4d3', padx=90, command=addDaatabase)
    Submit.grid(row=9, columnspan=2, pady=20)

    window.mainloop()


def productDetailsFun():
    window = tk.Tk()
    window.configure(bg="#c3c4c3")
    window.title("Product Details")
    window.maxsize(1500, 750)
    window.minsize(1500, 750)

    e = Label(window, width=20, text='Product Deatils', bg='#c3c4c3', font=("Times New Roman", 22, 'bold'),
              fg='#444645')
    e.place(x=600, y=30)

    ProductFrame = Frame(window, width=1500, height=700, bg="#c3c4c3")
    ProductFrame.place(x=3, y=150)

    mycursor.execute("SELECT * FROM products")
    usernames = mycursor.fetchall()

    e = Label(ProductFrame, width=14, text='Product Name', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=0)
    e = Label(ProductFrame, width=14, text='Company Name', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=1)
    e = Label(ProductFrame, width=14, text='Country', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=2)
    e = Label(ProductFrame, width=14, text='Import Date', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=3)
    e = Label(ProductFrame, width=14, text='Export Date', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=4)
    e = Label(ProductFrame, width=14, text='Manufacturing Date', borderwidth=1, relief='ridge', anchor='center',
              bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=5)
    e = Label(ProductFrame, width=14, text='Expiry Date', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=6)
    e = Label(ProductFrame, width=14, text='Total Price', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=7)
    e = Label(ProductFrame, width=14, text='Other Information', borderwidth=1, relief='ridge', anchor='center',
              bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=8)
    e = Label(ProductFrame, width=14, text='Product Id', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=9)
    e = Label(ProductFrame, width=14, text='Location', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
              font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
    e.grid(row=0, column=10)

    i = 1
    for student in usernames:
        for j in range(len(student)):
            e = Label(ProductFrame, width=14, text=student[j], borderwidth=1, relief='ridge', anchor="center",
                      bg='#d3d4d3',
                      font=("Times New Roman", 12, 'bold'), fg='#444645', pady=4, padx=4)
            e.grid(row=i, column=j)
        i = i + 1

    search = Entry(window, width=50, font=("Times New Roman", 12, 'bold'))
    search.place(x=400, y=100)


    def searchfun():

        ProductFrame.destroy()

        searchframme = Frame(window, width=1500, height=700, bg="#c3c4c3")
        searchframme.place(x=3, y=150)

        var1 = search.get()

        sql = "SELECT * FROM products where Product_name = %s"
        val = (var1,)
        mycursor.execute(sql, val)
        result = mycursor.fetchall()

        if not result:
            sql = "Select *from products where Cop_name = %s"
            mycursor.execute(sql, val)
            result = mycursor.fetchall()
            if not result:
                sql = "Select *from products where Country = %s"
                mycursor.execute(sql, val)
                result = mycursor.fetchall()
                if not result:
                    sql = "Select *from products where Product_id = %s"
                    mycursor.execute(sql, val)
                    result = mycursor.fetchall()
                    if not result:
                        sql = "Select *from products where Location = %s"
                        mycursor.execute(sql, val)
                        result = mycursor.fetchall()
                        if not result:
                            sql = "Select *from products where Other = %s"
                            mycursor.execute(sql, val)
                            result = mycursor.fetchall()


        print(result)
        print(type(result))

        e = Label(searchframme, width=14, text='Product Name', borderwidth=1, relief='ridge', anchor='center',
                  bg='#444645',
                  font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
        e.grid(row=0, column=0)
        e = Label(searchframme, width=14, text='Company Name', borderwidth=1, relief='ridge', anchor='center',
                  bg='#444645',
                  font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
        e.grid(row=0, column=1)
        e = Label(searchframme, width=14, text='Country', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
                  font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
        e.grid(row=0, column=2)
        e = Label(searchframme, width=14, text='Import Date', borderwidth=1, relief='ridge', anchor='center',
                  bg='#444645',
                  font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
        e.grid(row=0, column=3)
        e = Label(searchframme, width=14, text='Export Date', borderwidth=1, relief='ridge', anchor='center',
                  bg='#444645',
                  font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
        e.grid(row=0, column=4)
        e = Label(searchframme, width=14, text='Manufacturing Date', borderwidth=1, relief='ridge', anchor='center',
                  bg='#444645',
                  font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
        e.grid(row=0, column=5)
        e = Label(searchframme, width=14, text='Expiry Date', borderwidth=1, relief='ridge', anchor='center',
                  bg='#444645',
                  font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
        e.grid(row=0, column=6)
        e = Label(searchframme, width=14, text='Total Price', borderwidth=1, relief='ridge', anchor='center',
                  bg='#444645',
                  font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
        e.grid(row=0, column=7)
        e = Label(searchframme, width=14, text='Other Information', borderwidth=1, relief='ridge', anchor='center',
                  bg='#444645',
                  font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
        e.grid(row=0, column=8)
        e = Label(searchframme, width=14, text='Product Id', borderwidth=1, relief='ridge', anchor='center',
                  bg='#444645',
                  font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
        e.grid(row=0, column=9)
        e = Label(searchframme, width=14, text='Location', borderwidth=1, relief='ridge', anchor='center', bg='#444645',
                  font=("Times New Roman", 12, 'bold'), fg='#d3d4d3', pady=4, padx=4)
        e.grid(row=0, column=10)

        i = 1
        for student in result:
            for j in range(len(student)):
                e = Label(searchframme, width=14, text=student[j], borderwidth=1, relief='ridge', anchor="center",
                          bg='#d3d4d3', font=("Times New Roman", 12, 'bold'), fg='#444645', pady=4, padx=4)
                e.grid(row=i, column=j)
            i = i + 1

    LoginButton = Button(window, text="Search", font=("Times New Roman", 12, 'bold'), bg="#4c4e4d", fg="#c3c4c3",padx=30, command=searchfun)
    LoginButton.place(x=850, y=95)

    def ProductVsPriceFun():

        mycursor.execute("select Product_name from products")
        usernames = mycursor.fetchall()
        ObjectList = []
        for name in usernames:
            aList = list(name)
            ObjectList = ObjectList + aList
        # print(ObjectList)

        mycursor.execute("select Total_price from products")
        usernames = mycursor.fetchall()
        PriceList = []
        for name in usernames:
            aList = list(name)
            PriceList = PriceList + aList
        # print(PriceList)

        y_pos = np.arange(len(ObjectList))

        plt.bar(y_pos, PriceList, align='center', alpha=0.5)
        plt.xticks(y_pos, ObjectList)
        plt.ylabel('Price')
        plt.title('Product Vs Price')
        plt.show()

    def CompneyVsPriceFun():

        mycursor.execute("select Cop_name from products")
        usernames = mycursor.fetchall()
        ObjectList = []
        for name in usernames:
            aList = list(name)
            ObjectList = ObjectList + aList
        # print(ObjectList)

        mycursor.execute("select Total_price from products")
        usernames = mycursor.fetchall()
        PriceList = []
        for name in usernames:
            aList = list(name)
            PriceList = PriceList + aList
        # print(PriceList)

        y_pos = np.arange(len(ObjectList))

        plt.bar(y_pos, PriceList, align='center', alpha=0.5)
        plt.xticks(y_pos, ObjectList)
        plt.ylabel('Price')
        plt.title('Compney Vs Price')
        plt.show()

    def CountryVsPriceFun():

        mycursor.execute("select Country from products")
        usernames = mycursor.fetchall()
        ObjectList = []
        for name in usernames:
            aList = list(name)
            ObjectList = ObjectList + aList
        # print(ObjectList)

        mycursor.execute("select Total_price from products")
        usernames = mycursor.fetchall()
        PriceList = []
        for name in usernames:
            aList = list(name)
            PriceList = PriceList + aList
        # print(PriceList)

        y_pos = np.arange(len(ObjectList))

        plt.bar(y_pos, PriceList, align='center', alpha=0.5)
        plt.xticks(y_pos, ObjectList)
        plt.ylabel('Price')
        plt.title('Country Vs Price')
        plt.show()



    ProductVsPrice = Button(window, text="Product Vs Price", font=("Times New Roman", 12, 'bold'), bg="#4c4e4d", fg="#c3c4c3",padx=20, command=ProductVsPriceFun)
    ProductVsPrice.place(x=1010, y=95)

    CompneyVsPrice = Button(window, text="Company Vs Price", font=("Times New Roman", 12, 'bold'), bg="#4c4e4d", fg="#c3c4c3",padx=20, command=CompneyVsPriceFun)
    CompneyVsPrice.place(x=1170, y=95)

    CountryVsPrice = Button(window, text="Country Vs Price", font=("Times New Roman", 12, 'bold'), bg="#4c4e4d", fg="#c3c4c3",padx=20, command=CountryVsPriceFun)
    CountryVsPrice.place(x=1330, y=95)

    window.mainloop()

def productScannerFun():
    window = tk.Tk()
    window.configure(bg="#d3d4d3")
    window.title("Product Scanner")
    window.maxsize(1000, 650)
    window.minsize(1000, 650)

    global data

    title = Label(window, width=20, text='Product Scanner', bg='#d3d4d3', font=("Times New Roman", 22, 'bold'),fg='#444645')
    title.place(x=330, y=30)

    def Scanner():
        cap = cv2.VideoCapture(0)
        cap.set(3, 640)
        cap.set(4, 480)

        while True:

            data = "none"
            success, img = cap.read()
            for barcode in decode(img):
                myData = barcode.data.decode('utf-8')
                # print(myData)
                data = myData
                pts = np.array([barcode.polygon], np.int32)
                pts = pts.reshape((-1, 1, 2))
                cv2.polylines(img, [pts], True, (255, 0, 255), 5)

            cv2.imshow('result', img)
            cv2.waitKey(1)

            if data == "none":
                continue
            else:
                cap.release()
                my_str = data
                words = my_str.split()
                # print(words)

                frame = Frame(window, bg='#d3d4d3')
                frame.place(x=330, y=100)

                ProductId = Label(frame, text=f"Product Id :      {words[0]}", bg='#d3d4d3', font=("Times New Roman", 12, 'bold'),fg='#444645')
                ProductId.grid(row=0, column=0, sticky=E, padx=10)

                ProductName = Label(frame, text="Product Name : ", bg='#d3d4d3', font=("Times New Roman", 12, 'bold'),fg='#444645')
                ProductName.grid(row=1, column=0, sticky=E, padx=10)
                Product_NameBox = Entry(frame, font=("Times New Roman", 12, 'bold'), fg='#444645')
                Product_NameBox.insert(0, words[1])
                Product_NameBox.grid(row=1, column=1, pady=5)

                CompanyName = Label(frame, text="Company Name : ", bg='#d3d4d3', font=("Times New Roman", 12, 'bold'),fg='#444645')
                CompanyName.grid(row=2, column=0, sticky=E, padx=10)
                Cop_NameBox = Entry(frame, font=("Times New Roman", 12, 'bold'), fg='#444645')
                Cop_NameBox.insert(0, words[2])
                Cop_NameBox.grid(row=2, column=1, pady=5)

                Country = Label(frame, text="Country : ", bg='#d3d4d3', font=("Times New Roman", 12, 'bold'),fg='#444645')
                Country.grid(row=3, column=0, sticky=E, padx=10)
                CountryBox = Entry(frame, font=("Times New Roman", 12, 'bold'), fg='#444645')
                CountryBox.insert(0, words[3])
                CountryBox.grid(row=3, column=1, pady=5)

                Import_date = Label(frame, text="Import Date : ", bg='#d3d4d3', font=("Times New Roman", 12, 'bold'),fg='#444645')
                Import_date.grid(row=4, column=0, sticky=E, padx=10)
                Import_DateBox= Entry(frame, font=("Times New Roman", 12, 'bold'), fg='#444645')
                Import_DateBox.insert(0, words[4])
                Import_DateBox.grid(row=4, column=1, pady=5)

                Export_date = Label(frame, text="Export Date : ", bg='#d3d4d3', font=("Times New Roman", 12, 'bold'),fg='#444645')
                Export_date.grid(row=5, column=0, sticky=E, padx=10)
                Export_DateBox = Entry(frame, font=("Times New Roman", 12, 'bold'), fg='#444645')
                Export_DateBox.insert(0, words[5])
                Export_DateBox.grid(row=5, column=1, pady=5)

                Manufacturing_date = Label(frame, text="Manufacturing Date : ", bg='#d3d4d3',font=("Times New Roman", 12, 'bold'), fg='#444645')
                Manufacturing_date.grid(row=6, column=0, sticky=E, padx=10)
                Manufacturing_dateBox = Entry(frame, font=("Times New Roman", 12, 'bold'), fg='#444645')
                Manufacturing_dateBox.insert(0, words[6])
                Manufacturing_dateBox.grid(row=6, column=1, pady=5)

                Expiry_date = Label(frame, text="Expiry Date : ", bg='#d3d4d3', font=("Times New Roman", 12, 'bold'), fg='#444645')
                Expiry_date.grid(row=7, column=0, sticky=E, padx=10)
                Expiry_dateBox = Entry(frame, font=("Times New Roman", 12, 'bold'), fg='#444645')
                Expiry_dateBox.insert(0, words[7])
                Expiry_dateBox.grid(row=7, column=1, pady=5)

                Price = Label(frame, text="Price : ", bg='#d3d4d3', font=("Times New Roman", 12, 'bold'), fg='#444645')
                Price.grid(row=8, column=0, sticky=E, padx=10)
                Total_priceBox = Entry(frame, font=("Times New Roman", 12, 'bold'), fg='#444645')
                Total_priceBox.insert(0, words[9])
                Total_priceBox.grid(row=8, column=1, pady=5)

                Location = Label(frame, text="Location In Wear House : ", bg='#d3d4d3', font=("Times New Roman", 12, 'bold'), fg='#444645')
                Location.grid(row=9, column=0, sticky=E, padx=10)
                LocationBox = Entry(frame, font=("Times New Roman", 12, 'bold'), fg='#444645')
                LocationBox.insert(0, words[8])
                LocationBox.grid(row=9, column=1, pady=5)

                Other_statement = Label(frame, text="Other Statement : ", bg='#d3d4d3',font=("Times New Roman", 12, 'bold'), fg='#444645')
                Other_statement.grid(row=10, column=0, sticky=E, padx=10)
                Other_statementBox = Entry(frame, font=("Times New Roman", 12, 'bold'), fg='#444645')
                Other_statementBox.grid(row=10, column=1, pady=5)

                Prod = Product_NameBox.get()
                Cop = Cop_NameBox.get()
                Con = CountryBox.get()
                Impo = Import_DateBox.get()
                Expo = Export_DateBox.get()
                Man = Manufacturing_dateBox.get()
                Loc = LocationBox.get()
                Exp = Expiry_dateBox.get()
                Oth = Other_statementBox.get()
                Tp = int(Total_priceBox.get())
                Id = int(words[0])

                # print(type(Man))


                def Updatefun():
                    sql = "UPDATE Products set Product_name = %s,Cop_name = %s, Country = %s, Import_date = %s, Export_date = %s,Manufacturing_date = %s,location = %s, Expiry_date = %s, Other = %s, Total_price = %s where Product_id = %s"
                    var = (Prod, Cop, Con, Impo, Expo, Man, Loc, Exp, Oth, Tp, Id)
                    mycursor.execute(sql, var)

                    Other_statement = Label(frame, text="Query Updated", bg='#d3d4d3', font=("Times New Roman", 12, 'bold'),
                                            fg='#444645')
                    Other_statement.grid(row=12, columnspan=2, padx=15)

                Update = Button(frame, text="Update", bg='#444645', font=("Times New Roman", 12, 'bold'), fg='#d3d4d3',
                                padx=40, command=Updatefun)
                Update.grid(row=11, columnspan=2, pady=15)

                break


    Submit = Button(window, text="Scan", bg='#444645', font=("Times New Roman", 12, 'bold'),fg='#d3d4d3', padx=10, command=Scanner)
    Submit.place(x=100, y=30)




    window.mainloop()





root.mainloop()