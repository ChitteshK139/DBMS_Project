from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
from tkcalendar import DateEntry
import mysql.connector

class patient_order_details:

    def __init__(self,root):
        self.win=root
        self.win.title("Pharmacy Database Management System")
        self.win.geometry("1550x800+0+0")

        self.order_No=StringVar()
        self.Item_No=StringVar()
        self.Med_Name=StringVar()
        self.Dosage=StringVar()
        self.Patient_ID=StringVar()
        self.Doctor_Name=StringVar()
        self.Pharmacist_Name=StringVar()

        l_title=Label(self.win,text="Pharmacy Database Mangement System",bd=15,relief=RIDGE,bg='white',fg='#04AF70',font=('Georgia',45,'bold'),padx=2,pady=4)
        l_title.pack(side=TOP,fill=X) # fill in X axis

        img1=Image.open("pharmacy_logo (1).png")

        img1.resize((70,70), Image.BILINEAR)
        self.icon_img=ImageTk.PhotoImage(img1)
        b1=Button(self.win,image=self.icon_img,borderwidth=0)
        b1.place(x=50,y=30)

        # DataFrame
        df=Frame(self.win,bd=15,relief=RIDGE,padx=20)
        df.place(x=0,y=120,width=1530,height=300)

        df_left=LabelFrame(df,bd=10,relief=RIDGE,padx=20,text=' Medicine Information ',fg='#fc8c03',font=('Arial',15,'bold'))
        df_left.place(x=0,y=5,width=980,height=250)

        df_right=LabelFrame(df,bd=10,relief=RIDGE,padx=20,text=' Prescription ',fg='#fc8c03',font=('Arial',15,'bold'))
        df_right.place(x=990,y=5,width=460,height=250)

        self.txtPrescription=Text(df_right,font=('Calibri',14,'bold'),width=40,height=9)
        self.txtPrescription.grid(row=0,column=0)

        # Button Frame
        but_frame=Frame(self.win,bd=15,relief=RIDGE,padx=20)
        but_frame.place(x=175,y=430,width=1200,height=65)

        # Main Button 
        but_add=Button(but_frame,text='Add',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=self.add_Prescription_Data)
        but_add.grid(row=0,column=0,padx=5)

        but_upd=Button(but_frame,text='Update',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=self.update_order)
        but_upd.grid(row=0,column=1,padx=5)

        but_del=Button(but_frame,text='Delete',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=self.delete_record)
        but_del.grid(row=0,column=2,padx=5)

        but_med=Button(but_frame,text='Medicine Overview',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=self.search_med)
        but_med.grid(row=0,column=3,padx=5)

        but_spid=Button(but_frame,text='Search Patient ID',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=self.search_pid)
        but_spid.grid(row=0,column=4,padx=5)

        but_presc=Button(but_frame,text='Prescription Overview',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=self.iPrescription_overview)
        but_presc.grid(row=0,column=5,padx=5)

        but_back=Button(but_frame,text='Back',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=self.win.destroy)
        but_back.grid(row=0,column=6,padx=5)

        # Label and Entry
        
        l_order_no=Label(df_left,font=('Calibri',18,'bold'),text='Order_No',fg='#fc4a03')
        l_order_no.grid(row=0,column=0,padx=10,pady=10)
        e_order_no=Entry(df_left,textvariable=self.order_No,font=('Calibri',19,'bold'),width=20)
        e_order_no.grid(row=0,column=1)

        l_item_no=Label(df_left,font=('Calibri',18,'bold'),text='Item_No',fg='#fc4a03')
        l_item_no.grid(row=1,column=0,padx=10,pady=10)
        e_item_no=Entry(df_left,textvariable=self.Item_No,font=('Calibri',19,'bold'),width=20)
        e_item_no.grid(row=1,column=1)

        l_med_name=Label(df_left,font=('Calibri',18,'bold'),text='Med_Name',fg='#fc4a03')
        l_med_name.grid(row=2,column=0,padx=10,pady=10)
        e_med_id=Entry(df_left,textvariable=self.Med_Name,font=('Calibri',19,'bold'),width=20)
        e_med_id.grid(row=2,column=1)

        l_med_dosage=Label(df_left,font=('Calibri',18,'bold'),text='Dosage',fg='#fc4a03')
        l_med_dosage.grid(row=3,column=0,padx=10,pady=10)
        e_med_id=Entry(df_left,textvariable=self.Dosage,font=('Calibri',19,'bold'),width=20)
        e_med_id.grid(row=3,column=1)

        l_patient_id=Label(df_left,font=('Calibri',18,'bold'),text='Patient ID',fg='#fc4a03')
        l_patient_id.grid(row=0,column=2,padx=30,pady=10)
        e_patient_id=Entry(df_left,textvariable=self.Patient_ID,font=('Calibri',19,'bold'),width=20)
        e_patient_id.grid(row=0,column=3)

        l_doctor_name=Label(df_left,font=('Calibri',18,'bold'),text='Doctor Name',fg='#fc4a03')
        l_doctor_name.grid(row=1,column=2,padx=30,pady=10)
        e_doctor_name=Entry(df_left,textvariable=self.Doctor_Name,font=('Calibri',19,'bold'),width=20)
        e_doctor_name.grid(row=1,column=3)

        l_ph_name=Label(df_left,font=('Calibri',18,'bold'),text='Pharmacist Name',fg='#fc4a03')
        l_ph_name.grid(row=2,column=2,padx=30,pady=10)
        e_ph_name=Entry(df_left,textvariable=self.Pharmacist_Name,font=('Calibri',19,'bold'),width=20)
        e_ph_name.grid(row=2,column=3)


        # Detail frame
        det_frame=Frame(self.win,bd=20,relief=RIDGE)
        det_frame.place(x=110,y=500,width=1300,height=265)

        # Tree View (Table)

        self.order_table=ttk.Treeview(det_frame,column=("order_No","item_no","med_name","dosage","cost","patient_id","doctor_name","pharmacist_name"))

        self.order_table.heading("order_No",text="Order no.")
        self.order_table.heading("item_no",text="Item no.")
        self.order_table.heading("med_name",text="Medicine name")
        self.order_table.heading("dosage",text="Quantity/Dosage")
        self.order_table.heading("cost",text="Total Cost")
        self.order_table.heading("patient_id",text="Patient ID")
        self.order_table.heading("doctor_name",text="Doctor Name")
        self.order_table.heading("pharmacist_name",text="Pharmacist Name")

        self.order_table['show']='headings'

        # Scroll bar

        scroll_x_treeview = Scrollbar(det_frame, orient=HORIZONTAL, command=self.order_table.xview)
        scroll_y_treeview = Scrollbar(det_frame, orient=VERTICAL, command=self.order_table.yview)

        self.order_table.configure(xscrollcommand=scroll_x_treeview.set, yscrollcommand=scroll_y_treeview.set)

        scroll_x_treeview.pack(side=BOTTOM, fill=X)
        scroll_y_treeview.pack(side=RIGHT, fill=Y)

        self.order_table.pack(fill=BOTH,expand=1)

        self.order_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.fetch_data()

    # Functionality Declaration

    def add_Prescription_Data(self):
        if self.order_No.get()=='' or self.Item_No.get()=='' or self.Med_Name.get()=='' or self.Dosage.get()=='' or self.Patient_ID.get()=='' or self.Doctor_Name.get()==''or self.Pharmacist_Name.get()=='':
            messagebox.showerror("Error","All fields are mandatory")
        else:
            conn = mysql.connector.connect(host='localhost', username='Pharmacist', password='MED@789', database='PDMS')
            cur = conn.cursor()
            d = self.Dosage.get()
            m = self.Med_Name.get()

            # Check if the medicine exists in the database
            cur.execute("SELECT quantity FROM medicine WHERE drug_name = %s", (m,))
            result = cur.fetchone()

            if result is not None:
                current_quantity = result[0]
                d=int(d)
                # Sufficient stock, proceed with the order
                if current_quantity >= d:
                    cur.execute("INSERT INTO Med_Order_p (order_no, item_no, med_name, dosage, patient_id, doctor_name, pharmacist_name) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                (self.order_No.get(), self.Item_No.get(), m, d, self.Patient_ID.get(), self.Doctor_Name.get(), self.Pharmacist_Name.get()))
                    
                    cur.execute("UPDATE med_order_p JOIN medicine ON med_order_p.med_name=medicine.drug_name SET med_order_p.cost = med_order_p.dosage * medicine.price WHERE med_order_p.med_name = %s", (m,))


                    # Update the quantity in the medicine table
                    new_quantity = current_quantity - d
                    cur.execute("UPDATE medicine SET quantity = %s WHERE drug_name = %s", (new_quantity, m))

                    # If the quantity is zero, delete the medicine
                    if new_quantity == 0:
                        cur.execute("DELETE FROM medicine WHERE drug_name = %s", (m,))
                    conn.commit()
                    
                else:
                    messagebox.showinfo("Dosage Checking", "Medicines out of stock")
            else:
                messagebox.showinfo("Medicine Not Found", "The medicine is not found in the database")


            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success","Record has been inserted")
            
            #except mysql.connector.Errorexcept as err:
            #    messagebox.showerror("Error", f"Error: {err}")

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
        cur=conn.cursor()
        cur.execute("SELECT * from Med_Order_p")
        rows=cur.fetchall()
        print(rows)
        if len(rows)!=0:
            self.order_table.delete(*self.order_table.get_children())
            for r in rows:
                self.order_table.insert("",END,values=r)
            conn.commit()
        conn.close()

    def get_cursor(self,event=''):
        cur_row=self.order_table.focus()
        content=self.order_table.item(cur_row)
        row=content['values']

        if row:
            self.order_No.set(row[0])
            self.Item_No.set(row[1])
            self.Med_Name.set(row[2])
            self.Dosage.set(row[3])
            self.Patient_ID.set(row[5])
            self.Doctor_Name.set(row[6])
            self.Pharmacist_Name.set(row[7])
            global o,i,dos
            o = row[0] 
            i = row[1] 
            dos=row[3]


    def update_order(self): 
        conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
        cur=conn.cursor()
        m = self.Med_Name.get()

        cur.execute("UPDATE Med_Order_p SET Item_No=%s,Med_Name=%s,Dosage=%s,Patient_ID=%s,Doctor_Name=%s,Pharmacist_Name=%s WHERE order_no=%s AND Item_No=%s",
                            (self.Item_No.get(),self.Med_Name.get(),self.Dosage.get(),
                            self.Patient_ID.get(),self.Doctor_Name.get(),self.Pharmacist_Name.get(),o,i))
        
        cur.execute("SELECT quantity FROM medicine WHERE drug_name = %s", (m,))
        result = cur.fetchone()

        if result is not None:
            med_dos = result[0]
            # Sufficient stock, proceed with the update
            if dos > int(self.Dosage.get()):
                cur.execute("UPDATE med_order_p JOIN medicine ON med_order_p.med_name=medicine.drug_name SET med_order_p.cost = %s * medicine.price WHERE med_order_p.med_name = %s", (self.Dosage.get(),m))
                new_quantity = med_dos+(dos-int(self.Dosage.get()))
                cur.execute("UPDATE medicine SET quantity = %s WHERE drug_name = %s", (new_quantity, m))

            elif dos < int(self.Dosage.get()):
                cur.execute("UPDATE med_order_p JOIN medicine ON med_order_p.med_name=medicine.drug_name SET med_order_p.cost = %s * medicine.price WHERE med_order_p.med_name = %s", (self.Dosage.get(),m))
                new_quantity = med_dos-(int(self.Dosage.get())-dos)
                cur.execute("UPDATE medicine SET quantity = %s WHERE drug_name = %s", (new_quantity, m))
            
        conn.commit()
        conn.close()

        self.fetch_data()
    

    def iPrescription_overview(self):
        conn=conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
        cur=conn.cursor()
        m=self.Med_Name.get()
        cur.execute("SELECT cost FROM med_order_p WHERE med_name LIKE %s", (f"%{m}%",))
        x=cur.fetchone()

        # Clear the context, if it is present
        self.txtPrescription.delete('1.0', END)

        self.txtPrescription.insert(END,"Item No. :\t\t"+self.Item_No.get()+"\n")
        self.txtPrescription.insert(END,"Medicine name:\t\t"+self.Med_Name.get()+"\n")
        self.txtPrescription.insert(END,"Dosage:\t\t"+self.Dosage.get()+"\n")
        self.txtPrescription.insert(END,"Total Cost:\t\t"+str(x[0])+"\n")
        self.txtPrescription.insert(END,"Patient_ID:\t\t"+self.Patient_ID.get()+"\n")
        self.txtPrescription.insert(END,"Doctor Name:\t\t"+self.Doctor_Name.get()+"\n")
        self.txtPrescription.insert(END,"Pharmacist_Name:\t\t"+self.Pharmacist_Name.get()+"\n")

        conn.close()

    def delete_record(self):
        conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
        cur=conn.cursor()

        m=self.Med_Name.get()
        cur.execute("SELECT quantity FROM medicine where drug_name=%s",(m,))
        med_dos=cur.fetchone()[0]
        new_quantity = med_dos + int(self.Dosage.get())
        cur.execute("UPDATE medicine SET quantity = %s WHERE drug_name = %s", (new_quantity,m))

        query="DELETE FROM Med_Order_p WHERE order_no=%s and Item_No = %s"
        value=(self.order_No.get(),self.Item_No.get())
        cur.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("Deleted Recorded","The patient's order item has been deleted successfully.")
    
    
    def search_pid(self):
        from tkinter.simpledialog import askstring
        from tkinter.messagebox import showinfo

        win1=Tk()
        win1.geometry("700x300")

        pname = askstring('Patient ID', 'What is patient name?')
        
        conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
        cur=conn.cursor()
        query="SELECT p_id,p_name from patient where p_name LIKE %s"
        cur.execute(query,(f"%{pname}%",))
        data1=cur.fetchall()
        conn.close()

        tree = ttk.Treeview(win1, columns=("Patient ID","Patient Name"))
        tree.heading("#1", text="Patient ID")
        tree.heading("#2", text="Patient Name")
        tree.pack()

        for item in data1:
            tree.insert("", "end", values=item)

        exit_button = Button(win1, text="Ok", command=win1.destroy)
        exit_button.pack()

        win1.mainloop()

    def search_med(self):
        from tkinter.simpledialog import askstring
        from tkinter.messagebox import showinfo

        win1=Tk()
        win1.geometry("700x300")

        mname = askstring('Quick Medicine Overiew', 'What is Medicine Name?')
        
        conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
        cur=conn.cursor()
        query="SELECT m_id,drug_name,composition,company_name,quantity FROM medicine where drug_name LIKE %s"
        cur.execute(query,(f"%{mname}%",))
        data1=cur.fetchall()
        conn.close()

        tree = ttk.Treeview(win1, columns=("Medicine ID","Medicine Name","Composition","Company Name","Quantity"))
        tree.heading("#1", text="Medicine ID")
        tree.heading("#2", text="Medicine Name")
        tree.heading("#3", text="Composition")
        tree.heading("#4", text="Company Name")
        tree.heading("#5", text="Quantity")
        tree.pack()

        for item in data1:
            tree.insert("", "end", values=item)
        
        exit_button = Button(win1, text="Ok", command=win1.destroy)
        exit_button.pack()

        win1.mainloop()
 

# if __name__ == "__main__":
#    root = Tk()
#    obj1 = patient_order_details(root)
#    root.mainloop()
