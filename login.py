from atexit import register
import builtins
from cProfile import label
from email.mime import image
from fileinput import filename
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk  # pip install pillow
from PIL import ImageTk, Image
from easygui import egdemo
from tkinter import messagebox
import mysql.connector
import time
import datetime
from tkinter import messagebox
from tkinter import font
# from tkinter import _XYScrollCommand
import mysql.connector
import tkinter as tk
from tkinter import Tk, ttk
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()
    

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry("1550x800+0+0")
        
        self.root.configure(bg='#FEFCFF') 
  
        self.bg=ImageTk.PhotoImage(file=r"Images_GUI\loginBg1.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1) ; 

        frame = Frame(self.root, bg='black')
        frame.place(x=610, y=170, width=340, height=450)

        img1 = Image.open(r"registraion_related_images\LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimage1 = Label(image=self.photoimage1, bg='black', borderwidth=0)
        lblimage1.place(x=730, y=175, width=100, height=100)
        
        
        get_str=Label(frame,text='Get Started',font=('times of roman',20,'bold' ),fg='white',bg='black')
        get_str.place(x=95,y=105)
        
        #Label
        username=lbl1=Label(frame,text='Username',font=('times of roman',15,'bold'),fg='white',bg='black')
        username.place(x=70,y=155)
        
        self.textuser=ttk.Entry(frame,font=('times of roman',15,'bold'))
        self.textuser.place(x=40,y=180,width=270)
        
        def mark():
            if var.get()==1:
                self.textpass.configure(show = "")
            elif var.get()==0:
                self.textpass.configure(show='*')
        
        password=Label(frame,text='Password',font=('times of roman',15,'bold'),fg='white',bg='black')
        password.place(x=70,y=230)
        
        self.textpass=ttk.Entry(frame,font=('times of roman',15,'bold'),show='*')
        self.textpass.place(x=40,y=258,width=270)
    
        var = IntVar()
        bt = Checkbutton(frame,offvalue = 0,command=mark, onvalue = 1, variable = var)
        bt.place(x = 280, y = 259)
          
        
        
        #------------ Login icon image-----------------#
        
        
        img2=Image.open(r'registraion_related_images\LoginIconAppl.png')
        img2=img2.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg='black',borderwidth=0)
        lblimg1.place(x=650,y=323,width=25,height=25)
        
        img3=Image.open(r'registraion_related_images\lock-512.png')
        img3=img3.resize((25,25),Image.Resampling.LANCZOS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg='black',borderwidth=0)
        lblimg1.place(x=650,y=398,width=25,height=25)
        
        
        ###########------------Loginbtn-----------------################
        
        loginbtn=Button(frame,command=self.login,text='Login',font=('times of roman',15,'bold'),bd=8,relief=RIDGE,fg='white',bg='red',activeforeground='white',activebackground='red')
        loginbtn.place(x=110,y=300,width=120,height=40)
        
        
        # Register Button
        
        registerbtn=Button(frame,command=self.register_window,text='New User Register',font=('times of roman',10,'bold'),borderwidth=0,relief=RIDGE,fg='white',bg='black',activeforeground='white',activebackground='black')
        registerbtn.place(x=16,y=360,width=160)
        
        #password
        
        forgot_passwordbtn=Button(frame,command=self.forgot_password_window,text='Forgot Password',font=('times of roman',10,'bold'), borderwidth=0  ,relief=RIDGE,fg='white',bg='black',activeforeground='white',activebackground='black')
        forgot_passwordbtn.place(x=10,y=380,width=160)
        

    
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register( self.new_window)  
        
    def login(self):
        if self.textuser.get()=="" or self.textpass.get=="":
               messagebox.showerror("Error","all field required")
        elif self.textuser.get()=="rohit" or self.textpass.get=="12345":
            messagebox.showinfo("Success","Welcome to Python World")
        else:
            # messagebox.showerror("Invalid","Invalid username & Password")
            conn=mysql.connector.connect(host='localhost',user='root',password='R9140hit@',database='face_recognition')
            my_cursor=conn.cursor()
            my_cursor.execute("select *from register where Email=%s and password=%s",(
                
                                                                                     self.textuser.get(),
                                                                                     self.textpass.get()
                                                                                   
                                                                                   
                
            ))
            
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid User Name and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access Only Admin")
                if open_main > 0:
                    self.new_window=Toplevel(self.root)
                    self.app=Face_Recognition_System(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            # self.clear()
            conn.close()
            # messagebox.showinfo("success","Login Successful")
            
     ###############---------forgot Password function---------------------------#
     
    def reset_password(self):
        if self.combo_Security_Q.get()=='Select':
            messagebox.showinfo("Error","Select the Security Question",parent=self.root2)
        elif self.txt_Security.get()=="":
            messagebox.showerror("Error","Please Enter the Answer",parent=self.root2)
        elif self.txt_newpassword.get()=="":
            messagebox.showinfo("Error","Please Enter the Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='R9140hit@',database='mydata')
            my_cursor=conn.cursor()
            query=("Select *from register where Email=%s and securityQ=%s and securityA=%s")
            value=(self.textuser.get(),self.combo_Security_Q.get(),self.txt_Security.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Errror","Please Enter the correct Answer",parent=self.root2)
            else:
                # print("sdjsnjbasjbcdsjbjb")
                query=("update register set password=%s where Email=%s")
                value=(self.txt_newpassword.get(),self.textuser.get())
                my_cursor.execute(query,value)
                
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password  has been reset,please login new password",parent=self.root2)
                self.root2.destroy() 
                
               
            
                 
 
    def forgot_password_window(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","Please Enter the email address to reset password")
        else:
            conn=mysql.connector.connect(host='localhost',user='root',password='R9140hit@',database='mydata')
            my_cursor=conn.cursor()
            query=("select *from register where Email=%s")
            values=(self.textuser.get(),)
            my_cursor.execute(query,values)
            row=my_cursor.fetchone()
            # print(row)
            if row==None:
                messagebox.showerror('My Error',"Please Enter the valid User Name")
            else:
                conn.commit()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")
                
                l=Label(self.root2,text="Forgot Password",font=('times new roman',20,'bold'),fg='red',bg='white')
                l.place(x=0,y=10,relwidth=1)
                
                
                Security_Q=Label(self.root2,text='Select Security Question',font=("times ne w romn",15,'bold'),bg='white',fg='black')
                Security_Q.place(x=50,y=80)
        
                self.combo_Security_Q=ttk.Combobox(self.root2,font=("times ne w romn",15,'bold'),state="readonly")
                self.combo_Security_Q['values']=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
                self.combo_Security_Q.place(x=50,y=120,width=250)
                self.combo_Security_Q.current(0)
        
        
        
        
        
        
        
                Security_A=Label(self.root2,text='Security Answer',font=("times ne w romn",15,'bold'),bg='white',fg='black')
                Security_A.place(x=50,y=150)
                
                self.txt_Security=ttk.Entry(self.root2,font=("times new roman",15,))
                self.txt_Security.place(x=50,y=180,width=250)
                
        
                new_password=Label(self.root2,text='New Password',font=("times ne w romn",15,'bold'),bg='white',fg='black')
                new_password.place(x=50,y=220)
                
                self.txt_newpassword=ttk.Entry(self.root2,font=("times new roman",15,))
                self.txt_newpassword.place(x=50,y=250,width=250)
                
                btn=Button(self.root2,command=self.reset_password,text="Reset",font=('times new roman','15','bold'),fg='white',bg='green',border=7,activebackground='green')
                btn.place(x=50,y=290)
                
                
                
            
 
              
              
        
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")
        
        #---------------------------variable--------------------------------#
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_SecurityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        self.var_check=IntVar()
        
        
        #-------------background image---------------------#
        self.bg=ImageTk.PhotoImage(file=r"registraion_related_images\un.jpg")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1) ; 
        
        
        #-----------------left image---------------------------#
        self.bg1=ImageTk.PhotoImage(file=r"registraion_related_images\1.jpg")
        bg_lbl=Label(self.root,image=self.bg1)
        bg_lbl.place(x=180,y=100,width=470,height=550); 
        
        #-------------main-frame------------------------------#
        frame=Frame(self.root,bg='white')
        frame.place(x=650,y=100,width=650,height=550)
        
        register_lbl=Label(frame,text="REGISTER HERE",font=("times new roman",20,'bold'),fg='darkgreen',bg='white')
        register_lbl.place(x=20,y=20)  
        
        
        #--------------label and Entry Field------------------------#
        
        
        #------------- row1---------------------------------
        fname=Label(frame,text="First Name",font=("times new roman",15,'bold'),bg='white') 
        fname.place(x=50,y=100)    
        
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,'bold'))
        fname_entry.place(x=50,y=130,width=200) 
        
        lname=Label(frame,text="Last Name",font=("times new roman",15,'bold'),bg='white') 
        lname.place(x=370,y=100)    
        
         
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,))
        self.txt_lname.place(x=370,y=130,width=200)
        
        #--------------------------row2---------------------------------
        
        contact=Label(frame,text='Contact No',font=("times ne w romn",15,'bold'),bg='white',fg='black')
        contact.place(x=50,y=170)
        
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,))
        self.txt_contact.place(x=50,y=200,width=200)
        
        email=Label(frame,text='Email',font=("times ne w romn",15,'bold'),bg='white',fg='black')
        email.place(x=370,y=170)
        
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,))
        self.txt_email.place(x=370,y=200,width=200)
        
        #------------row3 ---------------------------------------------
        
        Security_Q=Label(frame,text='Select Security Question',font=("times ne w romn",15,'bold'),bg='white',fg='black')
        Security_Q.place(x=50,y=240)
        
        self.combo_Security_Q=ttk.Combobox(frame,textvariable=self.var_SecurityQ,font=("times ne w romn",15,'bold'),state="readonly")
        self.combo_Security_Q['values']=("Select","Your Birth Place","Your Girlfriend Name","Your Pet Name")
        self.combo_Security_Q.place(x=50,y=270,width=200)
        self.combo_Security_Q.current(0)
        
        
        
        
        
        
        
        Security_A=Label(frame,text='Security Answer',font=("times ne w romn",15,'bold'),bg='white',fg='black')
        Security_A.place(x=370,y=240)
        
        self.txt_Security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15,))
        self.txt_Security.place(x=370,y=270,width=200)
        
        
        
        
        
        
        
        
       
        
        pswd=Label(frame,text="Password",font=("times new roman",15,'bold'),bg='white') 
        pswd.place(x=50,y=310)    
        
        
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,))
        self.txt_pswd.place(x=50,y=340,width=200)
        
        confirm=Label(frame,text="Confirm Password",font=("times new roman",15,'bold'),bg='white') 
        confirm.place(x=370,y=310)    
        
        
        self.txt_confirm=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,))
        self.txt_confirm.place(x=370,y=340,width=200)
        
        
        #------------------Check----------------------
        
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms and Condition",font=("times new roman",15,),onvalue=1,offvalue=0,activebackground='green')
        checkbtn.place(x=50,y=380)
        
        
        #---------------------Button------------------------------
        
        img=Image.open(r"D:\all programming road map course\Python With Django Using Django Ineuron\INeuron Class Live\Core Python\Core Python Project\Registraion_form_Page\college_images\register-now-button1.jpg")
        img=img.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor='hand2')
        b1.place(x=30,y=440,width=200)
        
        img1=Image.open(r"Images_GUI\loginpng.png")
        img1=img1.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor='hand2')
        b2.place(x=330,y=440,width=200)
        


#-----------------------Function Declaration----------------------------------#

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_SecurityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            print("Hii")
            messagebox.showerror("Error","password and confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please agree our terms and condtion")
        else:
            # messagebox.showinfo("Success","Welcome friends")
            conn=mysql.connector.connect(host='localhost',user='root',password='R9140hit@',database='face_recognition')
            my_cursor=conn.cursor()
            query=("select*from register where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row !=None:
                messagebox.showerror("Error","User Already exist,please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                   
                   self.var_fname.get(),
                   self.var_lname.get(), 
                   self.var_contact.get(), 
                   self.var_email.get(), 
                   self.var_SecurityQ.get(),
                   self.var_SecurityA.get(),
                   self.var_pass.get(), 
                    
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("success","register Successful")
                
             

  
        
        
        
        
        
        #Icon images
        

    def return_login(self):
        self.root.destroy()

        
        

if __name__ == "__main__":
    main()
  

