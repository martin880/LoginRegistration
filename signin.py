from tkinter import *
from PIL import ImageTk

# Functionality Part


def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)


def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)


def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)


def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)


# GUI Part
login_window = Tk()
login_window.geometry('990x660+50+50')
login_window.title('Login')

bgImage = ImageTk.PhotoImage(file='bg2.jpg')

bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)

heading = Label(login_window, text='USER LOGIN', font=(
    'Microsoft Yahei UI Light', 23, 'bold'), bg='white', fg='red')
heading.place(x=870, y=120)

# usename
usernameEntry = Entry(login_window, width=24, font=(
    'Microsoft Yahei UI Light', 18, 'bold'), bd=0, fg='red')
usernameEntry.place(x=800, y=200)
usernameEntry.insert(0, 'Username')

usernameEntry.bind('<FocusIn>', user_enter)

frame1 = Frame(login_window, width=320, height=2, bg='red')
frame1.place(x=800, y=240)

# password
passwordEntry = Entry(login_window, width=24, font=(
    'Microsoft Yahei UI Light', 18, 'bold'), bd=0, fg='red')
passwordEntry.place(x=800, y=270)
passwordEntry.insert(0, 'Password')

passwordEntry.bind('<FocusIn>', password_enter)

# hidden password
frame2 = Frame(login_window, width=320, height=2, bg='red')
frame2.place(x=800, y=300)

openeye = PhotoImage(file='openeye.png')
eyeButton = Button(login_window, image=openeye, bd=0,
                   bg='white', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=1095, y=274)

forgetButton = Button(login_window, text='Forgot Password?', bd=0,
                      bg='white', activebackground='white', cursor='hand2', font=(
                          'Microsoft Yahei UI Light', 11, 'bold'), fg='red', activeforeground='red')
forgetButton.place(x=985, y=320)

loginButton = Button(login_window, text='Login', font=(
    'Open Sans', 16, 'bold'), fg='white', bg='red', activeforeground='white', activebackground='red', cursor='hand2', bd=0, width=24)
loginButton.place(x=800, y=380)

orLabel = Label(login_window, text='OR', font=(
    'Open Sans', 16), fg='red', bg='white')
orLabel.place(x=940, y=430)

facebook_logo = PhotoImage(file='facebook.png')
fbLabel = Label(login_window, image=facebook_logo, bg='white')
fbLabel.place(x=880, y=470)

google_logo = PhotoImage(file='google.png')
googleLabel = Label(login_window, image=google_logo, bg='white')
googleLabel.place(x=940, y=470)

twitter_logo = PhotoImage(file='twitter.png')
twitterLabel = Label(login_window, image=twitter_logo, bg='white')
twitterLabel.place(x=1000, y=470)

signupLabel = Label(login_window, text='Dont have an account ', font=(
    'Open Sans', 9, 'bold'), fg='red', bg='white')
signupLabel.place(x=850, y=530)

newaccountButton = Button(login_window, text='Create new one', font=(
    'Open Sans', 9, 'bold underline'), fg='blue', bg='white', activeforeground='blue', cursor='hand2', bd=0, width=14)
newaccountButton.place(x=980, y=530)

login_window.mainloop()
