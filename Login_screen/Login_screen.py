from tkinter import*
from tkinter import messagebox
from PIL import ImageTk
class login_system:
    def __init__(self,root):
        self.root=root
        self.root.title("Login System")
        self.root.geometry("1350x700+0+0")

        #========All_images==========
        self.bg_icon=ImageTk.PhotoImage(file="Image/bgc.jpg")
        self.user_icon=ImageTk.PhotoImage(file="Image/user.jpg")
        self.pas_icon=ImageTk.PhotoImage(file="Image/pas.png")
        self.logo_icon=ImageTk.PhotoImage(file="Image/logo.png")
        #VARIABLES
        self.uname=StringVar()
        self.upas=StringVar()


        bg_lbl=Label(self.root,image=self.bg_icon).pack()

        title=Label(self.root,text="Login System",font=("times new roman",40,"bold"),bg="yellow",fg="red",bd="10",relief=GROOVE)
        title.place(x=0,y=0,relwidth=1)

        Login_Frame=Frame(self.root,bg="white")
        Login_Frame.place(x=400,y=150)
        logolbl=Label(Login_Frame,image=self.logo_icon).grid(row=0,columnspan=2,pady=3)
        lbluser=Label(Login_Frame,text="Username",image=self.user_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=1,column=0,padx=20,pady=10)
        txtuser=Entry(Login_Frame,bd=5,textvariable=self.uname,relief=GROOVE,font=("",15)).grid(row=2,columnspan=2,padx=20)
        lblpas=Label(Login_Frame,text="Password",image=self.pas_icon,compound=LEFT,font=("times new roman",20,"bold"),bg="white").grid(row=3,column=0,padx=20,pady=10)
        txtpas=Entry(Login_Frame,bd=5,textvariable=self.upas,relief=GROOVE,font=("",15)).grid(row=4,columnspan=2,padx=20)
        btn_log=Button(Login_Frame,text="Login",width=15,font=("times new roman",14,"bold"),bg="yellow",fg="Red").grid(row=5,column=1,pady=10)
def login(self):
    if self.uname.get()==" " or self.upas.get()==" ":
        messagebox.showerror("Error","all feild are required")
    elif self.uname.get()=="SABA" and self.upas.get()=="1234":
        messagebox.showerror("successful",f"WELCOME{self.uname.get()}")
    else:
        messagebox.showerror("Error","INVALID username or password")
root=Tk()
obj=login_system(root)
root.mainloop()



