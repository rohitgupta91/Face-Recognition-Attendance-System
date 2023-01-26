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

from pyparsing import replaceWith
import mysql.connector








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
        
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree The Terms and Condition",font=("times new roman",15,),onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)
        
        
        #---------------------Button------------------------------
        
        img=Image.open(r"registraion_related_images\register-now-button1.jpg")
        img=img.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,command=self.register_data,image=self.photoimage,borderwidth=0,cursor='hand2')
        b1.place(x=30,y=440,width=200)
        
        img1=Image.open(r"registraion_related_images\loginpng.png")
        img1=img1.resize((200,50),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,borderwidth=0,cursor='hand2')
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
                
                

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()