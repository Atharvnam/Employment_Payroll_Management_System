from tkinter import *
import tkinter as tk
from tkinter import messagebox,ttk
import pymysql 
import time
import os
import tempfile
class EmployeeSystem():
    def __init__(self,root) -> None:
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1400x700+0+0")
        self.root.config(bg="White")
        title=Label(self.root,text="Employee Payroll Management System" , font=("times new roman",30,"bold"),bg="#262626",fg="white",anchor=W).place(x=0,y=0,relwidth=1)
        btn_emp=Button(self.root,text="All Employee's",command=self.employee_frame,font=("times new roman",13),bg="lightgrey",fg="black",anchor=CENTER).place(x=1100,y=10,width=150)
        #--------------------Frame1-------------------------#
        #-----variables-----#
        self.var_emp=StringVar()
        self.var_desigantion=StringVar()
        self.var_name=StringVar()
        self.var_age=StringVar()
        self.var_gender=StringVar()
        self.var_experience=StringVar()
        self.var_email=StringVar()
        self.var_hr_location=StringVar()
        self.var_doj=StringVar()
        self.var_dob=StringVar()
        self.var_proof_id=StringVar()#Aadhar default
        self.var_contact=StringVar()
        self.var_status=StringVar()
        
        Frame1 = Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame1.place(x=10,y=70,width=740,height=565)
        title2=Label(Frame1,text="Employee Details" , font=("times new roman",20),bg="lightgrey",fg="black",anchor='w',padx=10).place(x=0,y=0,relwidth=1)

        lbl_code=Label(Frame1,text="Employee Code:" , font=("times new roman",20),bg="white",fg="black").place(x=10,y=70)
        self.txt_code=Entry(Frame1, font=("times new roman",15),textvariable=self.var_emp,bg="lightyellow",fg="black")
        self.txt_code.place(x=220,y=74,width=200)
        btn_search=Button(Frame1,text="Search" ,command=self.search, font=("times new roman",20),bg="grey",fg="black").place(x=440,y=72,height=30)
        
        #----------------Row1------------------#
        lbl_designation=Label(Frame1,text="Designation:" , font=("times new roman",20),bg="white",fg="black").place(x=10,y=120)
        txt_designation=Entry(Frame1, font=("times new roman",15),textvariable=self.var_desigantion,bg="lightyellow",fg="black").place(x=170,y=125,width=200)
        lbl_doj=Label(Frame1,text="D.O.J:" , font=("times new roman",20),bg="white",fg="black").place(x=390,y=120)
        txt_doj=Entry(Frame1, font=("times new roman",15),textvariable=self.var_doj,bg="lightyellow",fg="black").place(x=525,y=125)

        #----------------Row2------------------#
        lbl_name=Label(Frame1,text="Name:" , font=("times new roman",20),bg="white",fg="black").place(x=10,y=170)
        txt_name=Entry(Frame1, font=("times new roman",15),textvariable=self.var_name,bg="lightyellow",fg="black").place(x=170,y=175,width=200)
        lbl_dob=Label(Frame1,text="D.O.B:" , font=("times new roman",20),bg="white",fg="black").place(x=390,y=170)
        txt_dob=Entry(Frame1, font=("times new roman",15),textvariable=self.var_dob,bg="lightyellow",fg="black").place(x=525,y=175)

        #----------------Row3------------------#
        lbl_age=Label(Frame1,text="Age:" , font=("times new roman",20),bg="white",fg="black").place(x=10,y=220)
        txt_age=Entry(Frame1, font=("times new roman",15),textvariable=self.var_age,bg="lightyellow",fg="black").place(x=170,y=225,width=200)
        lbl_experience=Label(Frame1,text="Experience:" , font=("times new roman",20),bg="white",fg="black").place(x=390,y=220)
        txt_experience=Entry(Frame1, font=("times new roman",15),textvariable=self.var_experience,bg="lightyellow",fg="black").place(x=525,y=225)

        #----------------Row4------------------#
        lbl_gender=Label(Frame1,text="Gender:" , font=("times new roman",20),bg="white",fg="black").place(x=10,y=270)
        txt_gender=Entry(Frame1, font=("times new roman",15),textvariable=self.var_gender,bg="lightyellow",fg="black").place(x=170,y=275,width=200)
        lbl_proof=Label(Frame1,text="Proof ID:" , font=("times new roman",20),bg="white",fg="black").place(x=390,y=270)
        txt_proof=Entry(Frame1, font=("times new roman",15),textvariable=self.var_proof_id,bg="lightyellow",fg="black").place(x=525,y=275)

        #----------------Row5------------------#
        lbl_email=Label(Frame1,text="Email:" , font=("times new roman",20),bg="white",fg="black").place(x=10,y=320)
        txt_email=Entry(Frame1, font=("times new roman",15),textvariable=self.var_email,bg="lightyellow",fg="black").place(x=170,y=325,width=200)
        lbl_contact=Label(Frame1,text="Contact:" , font=("times new roman",20),bg="white",fg="black").place(x=390,y=320)
        txt_contact=Entry(Frame1, font=("times new roman",15),textvariable=self.var_contact,bg="lightyellow",fg="black").place(x=525,y=325)

        #----------------Row6------------------#
        lbl_hire=Label(Frame1,text="Hired Location:" , font=("times new roman",18),bg="white",fg="black").place(x=10,y=370)
        txt_hire=Entry(Frame1, font=("times new roman",15),textvariable=self.var_hr_location,bg="lightyellow",fg="black").place(x=170,y=375,width=200)
        lbl_status=Label(Frame1,text="Status:" , font=("times new roman",20),bg="white",fg="black").place(x=390,y=370)
        txt_status=Entry(Frame1, font=("times new roman",15),textvariable=self.var_status,bg="lightyellow",fg="black").place(x=525,y=375)

        lbl_address=Label(Frame1,text="Address:", font=("times new roman",20),bg="white",fg="black").place(x=10,y=420)
        self.txt_address=Text(Frame1, font=("times new roman",15),bg="lightyellow",fg="black")
        self.txt_address.place(x=170,y=425,width=557,height=120)


        #--------------------Frame2-------------------------#
        #-----variables-----#
        self.var_month=StringVar()
        self.var_year=StringVar()
        self.var_salary=StringVar()
        self.var_totaldays=StringVar()
        self.var_absents=StringVar()
        self.var_medical=StringVar()
        self.var_pf=StringVar()
        self.var_convence=StringVar()
        self.var_net_salary=StringVar()
       
        Frame2 = Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame2.place(x=755,y=70,width=515,height=300)
        title3=Label(Frame2,text="Employee Salary Details" , font=("times new roman",20),bg="lightgrey",fg="black",anchor='w',padx=10).place(x=0,y=0,relwidth=1)
  
        #--------------Row1-------------------#
        lbl_month=Label(Frame2,text="Month:" , font=("times new roman",17),bg="white",fg="black").place(x=6,y=60)
        txt_month=Entry(Frame2, font=("times new roman",15),textvariable=self.var_month,bg="lightyellow",fg="black").place(x=80,y=62,width=100)
        
        lbl_year=Label(Frame2,text="Year:" , font=("times new roman",17),bg="white",fg="black").place(x=184,y=60)
        txt_year=Entry(Frame2, font=("times new roman",15),textvariable=self.var_year,bg="lightyellow",fg="black").place(x=242,y=62,width=90)

        lbl_salary=Label(Frame2,text="Salary:" , font=("times new roman",17),bg="white",fg="black").place(x=335,y=60)
        txt_salary=Entry(Frame2, font=("times new roman",15),textvariable=self.var_salary,bg="lightyellow",fg="black").place(x=406,y=62,width=100)
        #----------------Row2------------------#
        lbl_ttl_days=Label(Frame2,text="Total Days:" , font=("times new roman",18),bg="white",fg="black").place(x=8,y=110)
        txt_ttl_days=Entry(Frame2, font=("times new roman",15),textvariable=self.var_totaldays,bg="lightyellow",fg="black").place(x=130,y=115,width=100)
        lbl_absents=Label(Frame2,text="Absents:" , font=("times new roman",18),bg="white",fg="black").place(x=250,y=110)
        txt_absents=Entry(Frame2, font=("times new roman",15),textvariable=self.var_absents,bg="lightyellow",fg="black").place(x=350,y=115,width=100)

        #----------------Row3------------------#
        lbl_medical=Label(Frame2,text="Medical:" , font=("times new roman",18),bg="white",fg="black").place(x=8,y=160)
        txt_medical=Entry(Frame2, font=("times new roman",15),textvariable=self.var_medical,bg="lightyellow",fg="black").place(x=115,y=165,width=200)
        lbl_pf=Label(Frame2,text="PF:" , font=("times new roman",18),bg="white",fg="black").place(x=330,y=160)
        txt_pf=Entry(Frame2, font=("times new roman",15),textvariable=self.var_pf,bg="lightyellow",fg="black").place(x=380,y=165,width=120)

        #----------------Row4------------------#
        lbl_convence=Label(Frame2,text="Convence:" , font=("times new roman",18),bg="white",fg="black").place(x=8,y=210)
        txt_convence=Entry(Frame2, font=("times new roman",15),textvariable=self.var_convence,bg="lightyellow",fg="black").place(x=120,y=215,width=150)
        lbl_netsalary=Label(Frame2,text="Net Salary:" , font=("times new roman",18),bg="white",fg="black").place(x=280,y=210)
        txt_netsalary=Entry(Frame2, font=("times new roman",15),textvariable=self.var_net_salary,bg="lightgrey",fg="black").place(x=400,y=215,width=100)

        btn_calculate=Button(Frame2,text="Calculate" ,command=self.calculate, font=("times new roman",18),bg="orange",fg="black").place(x=8,y=255,height=30,width=100)
        self.btn_save=Button(Frame2,text="Save" ,command=self.add,font=("times new roman",18),bg="green",fg="white")
        self.btn_save.place(x=125,y=255,height=30,width=80)
        btn_clear=Button(Frame2,text="Clear",command=self.clear_fields, font=("times new roman",18),bg="white",fg="black").place(x=220,y=255,height=30,width=80)
        self.btn_update=Button(Frame2,text="Update",state=DISABLED,command=self.update, font=("times new roman",18),bg="blue",fg="white")
        self.btn_update.place(x=318,y=255,height=30,width=80)
        self.ebtn_delete=Button(Frame2,text="Delete" ,state=DISABLED,command=self.delete,font=("times new roman",18),bg="red",fg="black")
        self.ebtn_delete.place(x=415,y=255,height=30,width=80)
        
        #--------------------Frame3-------------------------#
        Frame3 = Frame(self.root,bd=3,relief=RIDGE,bg="white")
        Frame3.place(x=755,y=380,width=515,height=255)

        #-------------Calculator Frame----------------------#
        #---calculator operating function----#
        self.var_txt=StringVar()
        self.var_operator=''
        def btn_click(num):
            self.var_operator=self.var_operator+str(num)
            self.var_txt.set(self.var_operator)
        def result():
            res=str(eval(self.var_operator))
            self.var_txt.set(res)
            self.var_operator=''
        def clear_cal():
            self.var_txt.set('')
            self.var_operator=''
        #-------------Calculator Frame----------------------#
        cal_frame=Frame(Frame3,bg='white',bd=2,relief='ridge')
        cal_frame.place(x=2,y=2,width=249,height=244)
        txt_result=Entry(cal_frame,bg='lightgrey',textvariable=self.var_txt,font=("times new roman",20,"bold"),justify='right').place(x=0,y=0,relwidth=1,height=40)
        
        #--------------------Row1-------------------------#
        btn_7=Button(cal_frame,text='7',command=lambda:btn_click(7),font=("times new roman",15,"bold")).place(x=1,y=43,width=60,height=48)
        btn_8=Button(cal_frame,text='8',command=lambda:btn_click(8),font=("times new roman",15,"bold")).place(x=61,y=43,width=60,height=48)
        btn_9=Button(cal_frame,text='9',command=lambda:btn_click(9),font=("times new roman",15,"bold")).place(x=122,y=43,width=60,height=48)
        btn_div=Button(cal_frame,text='/',command=lambda:btn_click('/'),font=("times new roman",15,"bold")).place(x=183,y=43,width=60,height=48)

        #--------------------Row2-------------------------#
        btn_4=Button(cal_frame,text='4',command=lambda:btn_click(4),font=("times new roman",15,"bold")).place(x=1,y=91,width=60,height=48)
        btn_5=Button(cal_frame,text='5',command=lambda:btn_click(5),font=("times new roman",15,"bold")).place(x=61,y=91,width=60,height=48)
        btn_6=Button(cal_frame,text='6',command=lambda:btn_click(6),font=("times new roman",15,"bold")).place(x=122,y=91,width=60,height=48)
        btn_mul=Button(cal_frame,text='*',command=lambda:btn_click('*'),font=("times new roman",15,"bold")).place(x=183,y=91,width=60,height=48)

        #--------------------Row3-------------------------#
        btn_1=Button(cal_frame,text='1',command=lambda:btn_click(1),font=("times new roman",15,"bold")).place(x=1,y=140,width=60,height=48)
        btn_2=Button(cal_frame,text='2',command=lambda:btn_click(2),font=("times new roman",15,"bold")).place(x=61,y=140,width=60,height=48)
        btn_3=Button(cal_frame,text='3',command=lambda:btn_click(3),font=("times new roman",15,"bold")).place(x=122,y=140,width=60,height=48)
        btn_minus=Button(cal_frame,text='-',command=lambda:btn_click('-'),font=("times new roman",15,"bold")).place(x=183,y=140,width=60,height=48)

        #--------------------Row4-------------------------#
        btn_0=Button(cal_frame,text='0',command=lambda:btn_click(0),font=("times new roman",15,"bold")).place(x=1,y=190,width=60,height=48)
        btn_clr=Button(cal_frame,text='C',command=clear_cal,font=("times new roman",15,"bold")).place(x=61,y=190,width=60,height=48)
        btn_add=Button(cal_frame,text='+',command=lambda:btn_click('+'),font=("times new roman",15,"bold")).place(x=122,y=190,width=60,height=48)
        btn_equal=Button(cal_frame,text='=',command=result,font=("times new roman",15,"bold")).place(x=183,y=190,width=60,height=48)

        #--------Salary Frame-------#
        sal_frame=Frame(Frame3,bg='white',bd=2,relief=RIDGE)
        sal_frame.place(x=250,y=2,width=256,height=244)
        title_salary=Label(sal_frame,text="Salary Slip" , font=("times new roman",20),bg="lightgrey",fg="black",anchor='w',padx=10).place(x=0,y=0,relwidth=1)

        sal_frame2=Frame(sal_frame,bg='white',bd=2,relief=RIDGE)
        sal_frame2.place(x=0,y=36,relwidth=1,height=170)
        self.sample=f'''Company Name,XYZ\nAddress: Xyz, Floor4
-----------------------------------
 Employee ID\t: 
 Salary of\t: mon-YYYY
 Generated on\t: DD-MM-YYYY
-----------------------------------
 Total Days\t: DD
 Total Present\t: DD
 Total Absent\t: DD
 Convence\t: Rs.---
 Medical\t: Rs.---
 PF\t: Rs.---
 Gross Payment\t: Rs.---
 Net Salary\t: Rs.---
-----------------------------------
This is computer generated slip, not
required any signature
'''

        scroll_y=Scrollbar(sal_frame2,orient=VERTICAL)
        scroll_y.pack(fill=Y,side=RIGHT)
        self.txt_salary_slip=Text(sal_frame2,font=('times new roman',12),bg='lightyellow',yscrollcommand=scroll_y.set,wrap=None)
        self.txt_salary_slip.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_salary_slip.yview)
        self.txt_salary_slip.insert(END,self.sample)
        self.btn_print=Button(sal_frame,text="Print",state=DISABLED,command=self.print, font=("times new roman",18),bg="orange",fg="black")
        self.btn_print.place(x=134,y=210,height=25,width=100)
        
        self.check_connection()

    def search(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary where e_id=%s",self.var_emp.get())
            row=cur.fetchone()
            #print(rows)
            if row==None:
                messagebox.showerror("Error","Invalid Employee ID Please try with another employee ID")
            else:
                self.var_emp.set(row[0])
                self.var_desigantion.set(row[1])
                self.var_name.set(row[2])
                self.var_age.set(row[3])
                self.var_gender.set(row[4])
                self.var_email.set(row[5])
                self.var_hr_location.set(row[6])
                self.var_doj.set(row[7])
                self.var_dob.set(row[8])
                self.var_experience.set(row[9])
                self.var_proof_id.set(row[10])
                self.var_contact.set(row[11])
                self.var_status.set(row[12])
                self.txt_address.delete('1.0',END)
                self.txt_address.insert(END,row[13])
                self.var_month.set(row[14])
                self.var_year.set(row[15])
                self.var_salary.set(row[16])
                self.var_totaldays.set(row[17])
                self.var_absents.set(row[18])
                self.var_medical.set(row[19])
                self.var_pf.set(row[20])
                self.var_convence.set(row[21])
                self.var_net_salary.set(row[22])
                file_=open('salary_reciept/'+str(row[23]),'r')
                self.txt_salary_slip.delete('1.0',END)
                for i in file_:
                    self.txt_salary_slip.insert(END,i)
                file_.close()
                self.btn_print.config(state=NORMAL)
                self.btn_save.config(state=DISABLED)
                self.btn_update.config(state=NORMAL)
                self.ebtn_delete.config(state=NORMAL)
                self.txt_code.config(state="readonly")
        except Exception as ex:
                messagebox.showerror("Error",f'Error due to:{str(ex)}')

    def delete(self):
        if self.var_emp.get()=='':
            messagebox.showerror("Error","Employee ID must be required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",self.var_emp.get())
                row=cur.fetchone()
                #print(rows)
                if row==None:
                    messagebox.showerror("Error","Invalid Employee ID Please try with another employee ID")
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?")
                    if op==True:
                        cur.execute('delete from emp_salary where e_id=%s',(self.var_emp.get()))
                        con.commit()
                        con.close()
                        messagebox.showinfo("Delete","Employee record deleted successfully")
                        self.clear_fields()
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to:{str(ex)}')

    def calculate(self):
        #---frame2 variables---#
        if self.var_month.get()=='' or self.var_year.get()=='' or self.var_salary.get()=='' or self.var_totaldays.get()=='' or self.var_absents.get()=='' or self.var_medical.get()==''or self.var_pf.get()==''or self.var_convence.get()=='' :
            messagebox.showerror('Error','All fields are required')
        else:
            per_day=int(self.var_salary.get())/int(self.var_totaldays.get())
            work_day=int(self.var_totaldays.get())-int(self.var_absents.get())
            sal_=per_day*work_day
            deduct=int(self.var_medical.get())+int(self.var_pf.get())
            addition=int(self.var_convence.get())
            net_sal=sal_-deduct+addition
            self.var_net_salary.set(str(round(net_sal, 2)))
            #--------------update the reciept------------#
            new_sample=f'''Company Name,XYZ\nAddress: Xyz, Floor4
-----------------------------------
 Employee ID\t: {self.var_emp.get()}
 Salary of\t: {self.var_month.get()}-{self.var_year.get()}
 Generated on\t: {str(time.strftime("%d-%m-%Y"))}
-----------------------------------
 Total Days\t: {self.var_totaldays.get()}
 Total Present\t: {str(int(self.var_totaldays.get())-int((self.var_absents.get())))}
 Total Absent\t: {self.var_absents.get()}
 Convence\t: Rs.{self.var_convence.get()}
 Medical\t: Rs.{self.var_medical.get()}
 PF\t: Rs.{self.var_pf.get()}
 Gross Payment\t: Rs.{self.var_salary.get()}
 Net Salary\t: Rs.{self.var_net_salary.get()}
-----------------------------------
This is computer generated slip, not
required any signature
'''
            self.txt_salary_slip.delete('1.0',END)
            self.txt_salary_slip.insert('1.0',new_sample)

        
    def add(self):
        if self.var_emp.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","Employee deatils are required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",self.var_emp.get())
                row=cur.fetchone()
                #print(rows)
                if row!=None:
                    messagebox.showerror("Error","This employee ID has already exist in our record, try again with new id")
                else:
                    cur.execute("insert into emp_salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (
                        self.var_emp.get(),
                        self.var_desigantion.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_hr_location.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof_id.get(),
                        self.var_contact.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0',END),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_totaldays.get(),
                        self.var_absents.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        self.var_emp.get()+".txt"
                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('salary_reciept/'+str(self.var_emp.get())+".txt",'w')
                    file_.write(self.txt_salary_slip.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("Success","Record Added Sucessfully")
                    self.btn_print.config(state=NORMAL)
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to:{str(ex)}')

    def update(self):
        if self.var_emp.get()=='' or self.var_net_salary.get()=='' or self.var_name.get()=='':
            messagebox.showerror("Error","Employee deatils are required")
        else:
            try:
                con=pymysql.connect(host='localhost',user='root',password='',db='ems')
                cur=con.cursor()
                cur.execute("select * from emp_salary where e_id=%s",self.var_emp.get())
                row=cur.fetchone()
                #print(rows)
                if row==None:
                    messagebox.showerror("Error","This employee ID is invalid, try again with valid employee id")
                else:
                    cur.execute("""
                    UPDATE emp_salary SET
                    designation=%s, name=%s, age=%s, gender=%s, email=%s, hr_location=%s, doj=%s, dob=%s, experience=%s,
                    proof_id=%s, contact=%s, status=%s, address=%s, month=%s, year=%s, basic_salary=%s, total_days=%s, 
                    absents=%s, medical=%s, pf=%s, convence=%s, net_salary=%s, salary_slip=%s 
                    WHERE e_id=%s""", 
                    (
                        
                        self.var_desigantion.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_hr_location.get(),
                        self.var_doj.get(),
                        self.var_dob.get(),
                        self.var_experience.get(),
                        self.var_proof_id.get(),
                        self.var_contact.get(),
                        self.var_status.get(),
                        self.txt_address.get('1.0',END),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_totaldays.get(),
                        self.var_absents.get(),
                        self.var_medical.get(),
                        self.var_pf.get(),
                        self.var_convence.get(),
                        self.var_net_salary.get(),
                        self.var_emp.get()+".txt",
                        self.var_emp.get(),
                    )
                    )
                    con.commit()
                    con.close()
                    file_=open('salary_reciept/'+str(self.var_emp.get())+".txt",'w')
                    file_.write(self.txt_salary_slip.get('1.0',END))
                    file_.close()
                    messagebox.showinfo("Success","Record Updated Sucessfully")
            except Exception as ex:
                messagebox.showerror("Error",f'Error due to:{str(ex)}')

    def clear_fields(self):
        self.btn_print.config(state=DISABLED)
        self.btn_save.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.ebtn_delete.config(state=DISABLED)
        self.txt_code.config(state=NORMAL)

        self.var_emp.set('')
        self.var_desigantion.set('')
        self.var_name.set('')
        self.var_age.set('')
        self.var_gender.set('')
        self.var_experience.set('')
        self.var_email.set('')
        self.var_hr_location.set('')
        self.var_doj.set('')
        self.var_dob.set('')
        self.var_proof_id.set('')
        self.var_contact.set('')
        self.var_status.set('')
        self.txt_address.delete('1.0', END)
        self.var_month.set(''),
        self.var_year.set(''),
        self.var_salary.set(''),
        self.var_totaldays.set(''),
        self.var_absents.set(''),
        self.var_medical.set(''),
        self.var_pf.set(''),
        self.var_convence.set(''),
        self.var_net_salary.set(''),
        self.txt_salary_slip.delete('1.0',END),
        self.txt_salary_slip.insert(END,self.sample)
    
    def check_connection(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            #print(rows)
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to:{str(ex)}')
    
    def show(self):
        try:
            con=pymysql.connect(host='localhost',user='root',password='',db='ems')
            cur=con.cursor()
            cur.execute("select * from emp_salary")
            rows=cur.fetchall()
            self.employee_tree.delete(*self.employee_tree.get_children())
            for row in rows:
                self.employee_tree.insert('',END,values=row)
            con.close()    
        except Exception as ex:
            messagebox.showerror("Error",f'Error due to:{str(ex)}')
    
    def employee_frame(self):
        self.root2 = Toplevel(self.root)
        self.root2.title("Employee Payroll Management System")
        self.root2.geometry("900x600+100+60")
        self.root2.config(bg="White")
        title=Label(self.root2,text="All Employee Details" , font=("times new roman",30,"bold"),bg="#262626",fg="white").pack(side=TOP,fill=X)
        self.root2.focus_force()

        scrolly=Scrollbar(self.root2,orient=VERTICAL)
        scrollx=Scrollbar(self.root2,orient=HORIZONTAL)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)

        self.employee_tree=ttk.Treeview(self.root2,columns=('e_id', 'designation', 'name', 'age', 'gender', 'email', 'hr_location', 'doj', 'dob', 'experience', 'proof_id', 'contact', 'status', 'address', 'month', 'year', 'basic_salary', 'total_days', 'absents', 'medical', 'pf', 'convence', 'net_salary', 'salary_slip'),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        self.employee_tree.heading('e_id',text='EID')
        self.employee_tree.heading('designation',text='Designation')
        self.employee_tree.heading('name',text='Name')
        self.employee_tree.heading('age',text='Age')
        self.employee_tree.heading('gender',text='Gender')
        self.employee_tree.heading('email',text='Email')
        self.employee_tree.heading('hr_location',text='HR Location')
        self.employee_tree.heading('doj',text='D.O.B')
        self.employee_tree.heading('dob',text='D.O.J')
        self.employee_tree.heading('experience',text='Experience')
        self.employee_tree.heading('proof_id',text='Proof')
        self.employee_tree.heading('contact',text='Contact')
        self.employee_tree.heading('status',text='Status')
        self.employee_tree.heading('address',text='Address')
        self.employee_tree.heading('month',text='Month')
        self.employee_tree.heading('year',text='Year')
        self.employee_tree.heading('basic_salary',text='Basic Salary')
        self.employee_tree.heading('total_days',text='Total Days')
        self.employee_tree.heading('absents',text='Absents')
        self.employee_tree.heading('medical',text='Medical')
        self.employee_tree.heading('pf',text='PF')
        self.employee_tree.heading('convence',text='Convence')
        self.employee_tree.heading('net_salary',text='Net Salary')
        self.employee_tree.heading('salary_slip',text='Salary Slip')
        
        self.employee_tree['show']='headings'

        self.employee_tree.column('e_id',width=50)
        self.employee_tree.column('designation',width=100)
        self.employee_tree.column('name',width=100)
        self.employee_tree.column('age',width=100)
        self.employee_tree.column('gender',width=100)
        self.employee_tree.column('email',width=100)
        self.employee_tree.column('hr_location',width=100)
        self.employee_tree.column('doj',width=100)
        self.employee_tree.column('dob',width=100)
        self.employee_tree.column('experience',width=100)
        self.employee_tree.column('proof_id',width=100)
        self.employee_tree.column('contact',width=100)
        self.employee_tree.column('status',width=100)
        self.employee_tree.column('address',width=500)
        self.employee_tree.column('month',width=100)
        self.employee_tree.column('year',width=100)
        self.employee_tree.column('basic_salary',width=100)
        self.employee_tree.column('total_days',width=100)
        self.employee_tree.column('absents',width=100)
        self.employee_tree.column('medical',width=100)
        self.employee_tree.column('pf',width=100)
        self.employee_tree.column('convence',width=100)
        self.employee_tree.column('net_salary',width=100)
        self.employee_tree.column('salary_slip',width=100)
        self.employee_tree.pack(fill=BOTH,expand=1)
        scrollx.config(command=self.employee_tree.xview)
        scrolly.config(command=self.employee_tree.yview)
        self.show()
        self.root2.mainloop()

    def print(self):
        file_=tempfile.mktemp(".txt")
        open(file_,'w').write(self.txt_salary_slip.get('1.0',END))
        os.startfile(file_,'print')

root=Tk()
obj=EmployeeSystem(root)
root.mainloop()