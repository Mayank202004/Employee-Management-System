from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import mysql.connector



class employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1024x600+0+0")
        self.root.title("JP's Global PVT. LTD.")
        lbl_title=Label(self.root,text="CS Global PVT. LTD.",font=("Times New Roman",34,'bold'),fg='darkblue',bg='cornsilk2')
        lbl_title.place(x=0,y=0,width=1024,height=50)

        #variables for the code 

        self.var_dept=StringVar()
        self.var_name=StringVar()
        self.var_sal=StringVar()
        self.var_age=StringVar()
        self.var_mobo=StringVar()
        self.var_gen=StringVar()
        self.var_no=StringVar()
        self.var_csearch=StringVar()
        self.var_search=StringVar()
        
        #logo
        img_logo=Image.open(r"b.png")
        img_logo=img_logo.resize((50,50),Image.Resampling.LANCZOS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        self.logo=Label(self.root,image=self.photo_logo,bg='cornsilk2')
        self.logo.place(x=240,y=0,width=50,height=50)

        #frame1
        img_frame=Frame(self.root,bd=5,relief=RIDGE,bg='cornsilk2')
        img_frame.place(x=3,y=53,width=1014,height=118)

        #image1
        img1=Image.open(r"a.jpg")
        img1=img1.resize((500,100),Image.Resampling.LANCZOS)
        self.photo_img1=ImageTk.PhotoImage(img1)
        self.img1=Label(img_frame,image=self.photo_img1,bg='white')
        self.img1.place(x=270,y=5,width=500,height=100)

        #main frame border
        main_frame=Frame(self.root,bd=5,relief=RIDGE,bg='white')
        main_frame.place(x=2,y=170,width=1015,height=560)


                 #inner frame
        upper_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,bg='white',text='Add Employee',font=("times new roman",15,'bold'),fg='red')
        upper_frame.place(x=10,y=5,width=300,height=270)
        lblname=Label(upper_frame,text='Name',font=("arial",10,'bold'),bg='white')

           #labels and combobox+entry field
        lblemno=Label(upper_frame,font=('arial',10,'bold'),bg='white',text='Em_No')
        lblemno.grid(row=0,column=0,padx=2,sticky=W)
        txt_emno=ttk.Entry(upper_frame,textvariable=self.var_no,width=22,font=('arial',10,'bold'))
        txt_emno.grid(row=0,column=1,padx=2)
        lblname=Label(upper_frame,font=('arial',10,'bold'),bg='white',text='name')
        lblname.grid(row=1,column=0,padx=4,sticky=W)
        txt_name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',10,'bold'))
        txt_name.grid(row=1,column=1,padx=2,pady=4)
        lbldept=Label(upper_frame,font=('arial',10,'bold'),bg='white',text='department')
        lbldept.grid(row=2,column=0,padx=2,pady=4,sticky=W)
        text_dept=ttk.Combobox(upper_frame,textvariable=self.var_dept,width=22,font=('arial',10,'bold'),state='readonly')
        text_dept['values']=('select department','management','it','sales','customer care','freelancer')
        text_dept.current(0)
        text_dept.grid(row=2,column=1,padx=2,pady=4,sticky=W)
        lblsal=Label(upper_frame,text='Salary',font=("arial",10,'bold'),bg='white')
        lblsal.grid(row=3,column=0,padx=2,sticky=W)
        txt_sal=ttk.Entry(upper_frame,textvariable=self.var_sal,width=22,font=('arial',10,'bold'))
        txt_sal.grid(row=3,column=1,padx=2,pady=4)
        lblage=Label(upper_frame,text='Age',font=("arial",10,'bold'),bg='white')
        lblage.grid(row=4,column=0,padx=2,sticky=W)
        txt_age=ttk.Entry(upper_frame,textvariable=self.var_age,width=22,font=('arial',10,'bold'))
        txt_age.grid(row=4,column=1,padx=2,pady=12)
        lblno=Label(upper_frame,text='Mobile No.',font=("arial",10,'bold'),bg='white')
        lblno.grid(row=5,column=0,padx=2,sticky=W)
        txt_no=ttk.Entry(upper_frame,textvariable=self.var_mobo,width=22,font=('arial',10,'bold'))
        txt_no.grid(row=5,column=1,padx=2,pady=4)
        lblgen=Label(upper_frame,text='Gender',font=("arial",10,'bold'),bg='white')
        lblgen.grid(row=6,column=0,padx=2,sticky=W)
        text_dept=ttk.Combobox(upper_frame,textvariable=self.var_gen,width=22,font=('arial',10,'bold'),state='readonly')
        text_dept['values']=('select Gender','Male','Female','other','prefer not to say')
        text_dept.current(0)
        text_dept.grid(row=6,column=1,padx=2,pady=7,sticky=W)

                #lower frame for buttons
        lower_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,bg='white',text='',font=("times new roman",5,'bold'),fg='red')
        lower_frame.place(x=10,y=280,width=300,height=110)

                   #buttons code
        btn=Button(lower_frame,text='save',command=self.add_data,font=("arial",11,'bold'),width=14,bg='blue',fg='white')
        btn.grid(row=0,column=0,padx=1,pady=7)
        btn2=Button(lower_frame,text='update',command=self.update_data,font=("arial",11,'bold'),width=14,bg='blue',fg='white')
        btn2.grid(row=0,column=1,padx=1,pady=7)
        btn3=Button(lower_frame,command=self.delete_data,text='delete',font=("arial",11,'bold'),width=14,bg='blue',fg='white')
        btn3.grid(row=1,column=0,padx=3,pady=10)
        btn4=Button(lower_frame,command=self.reset_data,text='clear',font=("arial",11,'bold'),width=14,bg='blue',fg='white')
        btn4.grid(row=1,column=1,padx=3,pady=10)
        
        #inner frame 2 (search)
        inner_frame=LabelFrame(main_frame,bd=5,relief=RIDGE,bg='white',text='Search Employee',font=("times new roman",15,'bold'),fg='red')
        inner_frame.place(x=315,y=5,width=682,height=390)

              #search upper frame
        search_frame=LabelFrame(inner_frame,bd=5,relief=RIDGE,bg='white',text='',font=("times new roman",10,'bold'),fg='red')
        search_frame.place(x=10,y=10,width=653,height=50)

            #label and search field code

        lblsearch=Label(search_frame,text='Search By',font=("arial",10,'bold'),bg='red',fg='white')
        lblsearch.grid(row=0,column=0,padx=5,pady=5,sticky=W)
        search_by=ttk.Combobox(search_frame,textvariable=self.var_csearch,width=16,font=('arial',10,'bold'),state='readonly')
        search_by['values']=('search by','em_no','name','dept','salary','age','ascending','descending')
        search_by.current(0)
        search_by.grid(row=0,column=1,padx=12,pady=5,sticky=W)
        txt_search=ttk.Entry(search_frame ,textvariable=self.var_search,width=22,font=('arial',10,'bold'))
        txt_search.grid(row=0,column=2,padx=5,pady=5)

                   #search buttons
        btnsearch=Button(search_frame,command=self.search_data,text='search',font=("arial",10,'bold'),width=12,height=1,bg='blue',fg='white')
        btnsearch.grid(row=0,column=3,padx=5,pady=5)
        btnclear=Button(search_frame,command=self.fetch_data,text='Show All',font=("arial",10,'bold'),width=12,height=1,bg='blue',fg='white')
        btnclear.grid(row=0,column=4,padx=5,pady=5)

          #===========Search Table========
        table_frame=Frame(inner_frame,bd=5,relief=RIDGE,bg='white')
        table_frame.place(x=10,y=65,width=654,height=295)

              #scroll bar making

        s=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        s2=ttk.Scrollbar(table_frame,orient=VERTICAL)

                #table creation
        self.table=ttk.Treeview(table_frame,column=('no','nm','Desig','Sal','age','mno','gen'),xscrollcommand=s.set,yscrollcommand=s2.set)

               #scroll bar setup

        s.pack(side=BOTTOM,fill=X)
        s2.pack(side=RIGHT,fill=Y)
        s.config(command=self.table.xview)
        s2.config(command=self.table.yview)
        self.table.heading('no',text='em_no')
        self.table.heading('nm',text='em_name')
        self.table.heading('Desig',text='dept')
        self.table.heading('Sal',text='salary')
        self.table.heading('age',text='age')
        self.table.heading('mno',text='Mobo')
        self.table.heading('gen',text='gen')
        self.table['show']='headings'
        self.table.column('no',width=50)
        self.table.column('nm',width=150)
        self.table.column('Desig',width=150)
        self.table.column('Sal',width=120)
        self.table.column('age',width=35)
        self.table.column('mno',width=90)
        self.table.column('gen',width=60)
        self.table.pack(fill=BOTH,expand=1000)
        self.table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

             #function declaration======

    def add_data(self):
        if self.var_dept.get()==""or self.var_name.get()=="":
            messagebox.showerror('Error','name and department must be filled')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='mayank',database='gui')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee (em_no,name,dept,salary,age,mobo,gender)values(%s,%s,%s,%s,%s,%s,%s)',(
                self.var_no.get(),
                self.var_name.get(),
                self.var_dept.get(),
                self.var_sal.get(),
                self.var_age.get(),
                self.var_mobo.get(),
                self.var_gen.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('sucess','record inserted sucessfully')
            except Exception as es:
                messagebox.showerror('error',f'due to:{str(es)}',parent=self.root) 
 
               #fetch database table

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='mayank',database='gui')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.table.delete(*self.table.get_children())
            for i in data:
                self.table.insert("",END,values=i)
            conn.commit()
        conn.close()

                    #get cursor

    def get_cursor(self,event=""):
        cursor_row=self.table.focus()
        content=self.table.item(cursor_row)
        data=content["values"]
        self.var_no.set(data[0])
        self.var_name.set(data[1])
        self.var_dept.set(data[2])
        self.var_sal.set(data[3])
        self.var_age.set(data[4])
        self.var_mobo.set(data[5])
        self.var_gen.set(data[6])
        
                #update button

    def update_data(self):
            if self.var_dept.get()==""or self.var_name.get()=="":
                messagebox.showerror('Error','name and department must be filled')
            else:
                try:
                    update=messagebox.askyesno('Update','Are you sure to make changes')
                    if update>0:
                        conn=mysql.connector.connect(host='localhost',user='root',password='mayank',database='gui')
                        my_cursor=conn.cursor()
                        my_cursor.execute('update employee set name=%s,dept=%s,salary=%s,age=%s,mobo=%s,gender=%s where em_no=%s',(

                            self.var_name.get(),
                            self.var_dept.get(),
                            self.var_sal.get(),
                            self.var_age.get(),
                            self.var_mobo.get(),
                            self.var_gen.get(),
                            self.var_no.get()
                            ))
                    else:
                        if not update:
                            return
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo('Sucess','Employee sucessfully updated',parent=self.root)
                except Exception as es:
                    messagebox.showerror('error',f'due to:{str(es)}',parent=self.root)  
    def delete_data(self):
            if self.var_no.get()=="":
                messagebox.showerror('error','please ender em_no')
            else:
                try:
                    delete=messagebox.askyesno('delete','are you sure to delete record?')
                    if delete>0:
                        conn=mysql.connector.connect(host='localhost',user='root',password='mayank',database='gui')
                        my_cursor=conn.cursor()
                        sql='delete from employee where em_no=%s'
                        value=(self.var_no.get(),)
                        my_cursor.execute(sql,value)
                    else:
                        if not delete:
                            return
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo('Sucess','Employee sucessfully deleted',parent=self.root)
                except Exception as es:
                    messagebox.showerror('error',f'due to:{str(es)}',parent=self.root)
                    
                      #clear button 
                      #used to remove all filled information 
                      
    def reset_data(self):
                      self.var_no.set("")
                      self.var_name.set("")
                      self.var_dept.set('select department')
                      self.var_sal.set('')
                      self.var_age.set("")
                      self.var_mobo.set("")
                      self.var_gen.set('select Gender')
                      
                      #main search 
                      #you can search bye employee name , employee number , salary , department any of them
                      
    def search_data(self):
                      if self.var_csearch.get()=='':
                        messagebox.showerror('error','please select option')
                      else:
                        try:
                            conn=mysql.connector.connect(host='localhost',user='root',password='mayank',database='gui')
                            my_cursor=conn.cursor()
                            if self.var_csearch.get()=="ascending":
                                my_cursor.execute('select * from employee order by name ASC')
                            elif self.var_csearch.get()=="descending":
                                my_cursor.execute('select * from employee order by name DESC')
                                
                            else:
                                my_cursor.execute('select * from employee where ' +str(self.var_csearch.get())+" LIKE '%"+str(self.var_search.get()+"%'"))
                            rows=my_cursor.fetchall()
                            if len(rows)!=0:
                                self.table.delete(*self.table.get_children())
                                for i in rows:
                                    self.table.insert("",END,values=i)
                            conn.commit
                            conn.close()
                        except Exception as es:
                            messagebox.showerror('error',f'due to:{str(es)}',parent=self.root)
                        
if __name__=="__main__":
     root=Tk()
     obj=employee(root)
     root.mainloop()
    
    
    

    #====E.N.D. . . . O.F. . . . P.R.O.J.E.C.T.
    #T.H.A.N.K. . . Y.O.U.
