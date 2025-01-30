from tkinter import *
from func import hash1, unhash
from tkinter import messagebox


master = Tk()
master.title('log in')

header = Label(master, text="default password is hello")
header.grid(row=0)
passw = Entry(master, width=50)
passw.grid(row=1)
passw.insert(0, 'password')


def opennewwindow():
    nw = Toplevel(master)
    nw.title('passwords')
    mylabel = Label(nw, text="password protector")
    mylabel.grid(row=0, column=0)
    # different messagebox.  showinfo showwarning showerror askquestion askokcancel askyesno
    # set message box = to a variable and use if else statement

    def info():
        messagebox.showinfo('info', 'all passwords entered are stored on your computer. '
                                    'The passwords are stored encrypted. '
                                    'The only place to find them decrypted is in your account')

    Button(nw, text='i', bg='blue', command=info).grid(row=0, column=3)
    user = Entry(nw, width=50)
    user.grid(row=1)
    user.insert(0, 'enter "username password"')

    def submit():
        usern = user.get()
        usernhash = hash1.hashr(usern)
        try:
            fh = open('user and pass.txt', 'a')
        except:
            label = Label(nw, text='please create a txt document called "user and pass.txt"'
                                    ' then put it in the same folder as this aplication')
            label.pack()
        fh.write(usernhash + '\n')
        fh.close()

    Button(nw, text='submit', command=submit).grid(row=2)


    def changepasswindow():
        nnw = Toplevel(nw)
        nnw.title('change password')
        Label(nnw, text='enter old password').grid(row=0)
        npass = Entry(nnw, width=50)
        npass.grid(row=1)
        npass.insert(0, 'enter password')

        def opennnewwindow():
            nnnw = Toplevel(nnw)
            nnnw.title = ('new password')
            new_password = Entry(nnnw, width=50)
            new_password.grid(row=1)
            new_password.insert(0, 'new password')

            def newpass():
                fo = open('password.txt', 'w+')
                fo.write(hash1.hashr(new_password.get()))
                fo.close()

            Button(nnnw, text='create password', command=newpass).grid(row=10)





        def submitpass():
                passwn1 = npass.get()
                f = open('password.txt', 'r')
                password1 = unhash.unhashr(f.read())
                if passwn1 == password1:
                    login = True
                else:
                    login = False
                    label7 = Label(nnw, text='error').grid(row=10)
                if login:
                    opennnewwindow()
                    f.close()

        Button(nnw, text="submit", command=submitpass).grid(row=3)


    def newpass():
        changepasswindow()



    Button(nw, text='change password', command=newpass).grid(row=3)

    file = open("user and pass.txt", "r")
    counter = 0

    Content = file.read()
    coList = Content.split("\n")

    for i in coList:
        if i:
            counter += 1

    number = 3
    f = open('user and pass.txt', 'r')

    for x in range(0, counter):
        txt = f.readline()
        txt = unhash.unhashr(txt)
        label1 = Label(nw, text=txt)
        label1.grid(row=number)
        number = number + 1

    f.close()



def loggin():
    passwn = passw.get()
    f = open('password.txt', 'r')
    password = unhash.unhashr(f.read())
    if passwn == password:
        login = True
    else:
        login = False
        label6 = Label(text='error').grid(row=10)
    if login:
        opennewwindow()
        f.close()


logginbutton = Button(master, text="log in", command=loggin).grid(row=3)


master.mainloop()