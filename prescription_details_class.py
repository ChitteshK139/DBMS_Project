from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
from tkcalendar import DateEntry
import mysql.connector
from tkcalendar import *
from pres_doctor_details import *

class pres_details:

    def __init__(self,root):
        self.win=root
        self.win.title("Pharmacy Database Management System")
        self.win.geometry("1550x800+0+0")

        self.patient_id=StringVar()
        self.Med_Name=StringVar()
        self.Dosage=StringVar()
        self.add_comm=StringVar()

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

        df_left=LabelFrame(df,bd=10,relief=RIDGE,padx=20,text=' Prescription Details ',fg='#fc8c03',font=('Arial',15,'bold'))
        df_left.place(x=0,y=5,width=580,height=250)

        df_right=LabelFrame(df,bd=10,relief=RIDGE,padx=20,text=' Prescription ',fg='#fc8c03',font=('Arial',15,'bold'))
        df_right.place(x=590,y=5,width=660,height=250)

        self.txtPrescription=Text(df_right,font=('Calibri',14,'bold'),width=60,height=9)
        self.txtPrescription.grid(row=0,column=0)

        df_img=LabelFrame(df,bd=10,relief=RIDGE)
        df_img.place(x=1270,y=5,width=210,height=260)

        img1=ImageTk.PhotoImage(Image.open("prescription_img.png"))
        label = Label(df_img, image = img1)
        label.image = img1
        label.pack()
        

        # Button Frame
        but_frame=Frame(self.win,bd=15,relief=RIDGE,padx=20)
        but_frame.place(x=75,y=430,width=1350,height=65)

        # Main Button 
        but_add=Button(but_frame,text='Add',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=self.Prescription_Data)
        but_add.grid(row=0,column=0,padx=5)

        but_upd=Button(but_frame,text='Update',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=self.update_order)
        but_upd.grid(row=0,column=1,padx=5)

        but_del=Button(but_frame,text='Delete',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=self.delete_record)
        but_del.grid(row=0,column=2,padx=5)

        but_presc=Button(but_frame,text='Prescription Overview',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=self.iPrescription_overview)
        but_presc.grid(row=0,column=3,padx=5)

        but_reset=Button(but_frame,text='Search Record',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=self.search_records)
        but_reset.grid(row=0,column=4,padx=5)

        but_spid=Button(but_frame,text='Search Patient ID',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=self.search_pid)
        but_spid.grid(row=0,column=5,padx=5)

        but_doc= Button(but_frame,text='Doctor Details',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=doctor_details)
        but_doc.grid(row=0,column=6,padx=5)

        but_back=Button(but_frame,text='Back',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=self.win.destroy)
        but_back.grid(row=0,column=7,padx=5)

        # Label and Entry
        
        l_p_id=Label(df_left,font=('Calibri',18,'bold'),text='Patient_ID',fg='#fc4a03')
        l_p_id.grid(row=0,column=0,padx=10,pady=10)
        e_p_id=Entry(df_left,textvariable=self.patient_id,font=('Calibri',19,'bold'),width=20)
        e_p_id.grid(row=0,column=1)

        l_drug_name=Label(df_left,font=('Calibri',18,'bold'),text='Drug Name',fg='#fc4a03')
        l_drug_name.grid(row=1,column=0,padx=10,pady=10)
        e_drug_name=Entry(df_left,textvariable=self.Med_Name,font=('Calibri',19,'bold'),width=20)
        e_drug_name.grid(row=1,column=1)

        l_dosage=Label(df_left,font=('Calibri',18,'bold'),text='Dosage',fg='#fc4a03')
        l_dosage.grid(row=2,column=0,padx=10,pady=10)
        e_dosage=Entry(df_left,textvariable=self.Dosage,font=('Calibri',19,'bold'),width=20)
        e_dosage.grid(row=2,column=1)

        l_comment=Label(df_left,font=('Calibri',18,'bold'),text='Additional Comments',fg='#fc4a03')
        l_comment.grid(row=3,column=0,padx=10,pady=10)
        e_comment=Entry(df_left,textvariable=self.add_comm,font=('Calibri',19,'bold'),width=20)
        e_comment.grid(row=3,column=1)



        # Detail frame
        det_frame=Frame(self.win,bd=20,relief=RIDGE)
        det_frame.place(x=110,y=500,width=1300,height=265)

        # Tree View (Table)

        self.order_table=ttk.Treeview(det_frame,column=("pid","drug_name","dosage","add_comm"))

        self.order_table.heading("pid",text="Patient ID")
        self.order_table.heading("drug_name",text="Drug Name")
        self.order_table.heading("dosage",text="Quantity/Dosage")
        self.order_table.heading("add_comm",text="Additional Comment")

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

    def Prescription_Data(self):
        if self.patient_id.get()=='' or self.Med_Name.get()=='' or self.Dosage.get()=='' or self.add_comm.get()=='':
            messagebox.showerror("Error","All fields are mandatory")
        else:
            conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
            cur=conn.cursor()
            
            #try:
            cur.execute("INSERT INTO Prescription(p_id,drug_name,dosage,add_comment) VALUES(%s, %s, %s, %s)", (self.patient_id.get(), self.Med_Name.get(), self.Dosage.get(), self.add_comm.get()))
            conn.commit()   # Used trigger for cur_date and cur_time
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")

            #except mysql.connector.Error:
            #    messagebox.showerror("Error", "Error: Already Existed")

    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
        cur=conn.cursor()
        cur.execute("SELECT p_id,drug_name,dosage,add_comment FROM prescription")
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
            self.patient_id.set(row[0])
            self.Med_Name.set(row[1])
            self.Dosage.set(row[2])
            self.add_comm.set(row[3])


    def update_order(self): 
        conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
        cur=conn.cursor()
        cur.execute("UPDATE prescription SET drug_name=%s,dosage=%s,add_comment=%s",
                    (self.Med_Name.get(),self.Dosage.get(), self.add_comm.get()))
    

    def iPrescription_overview(self):
        conn=conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
        cur=conn.cursor()
        p1=self.patient_id.get()
        d1=self.Med_Name.get()
        cur.execute("SELECT p_name FROM patient WHERE p_id LIKE %s", (f"%{p1}%",))
        x=cur.fetchone()
        cur.execute("SELECT pres_date,pres_time FROM prescription WHERE p_id LIKE %s AND drug_name LIKE %s", (f"%{p1}%",f"%{d1}%"))
        y=cur.fetchone()


        # Clear the context, if it is present
        self.txtPrescription.delete('1.0', END)

        self.txtPrescription.insert(END,"Patient ID :\t\t"+self.patient_id.get()+"\n")
        self.txtPrescription.insert(END,"Patient Name :\t\t"+x[0]+"\n")
        self.txtPrescription.insert(END,"Medicine name:\t\t"+self.Med_Name.get()+"\n")
        self.txtPrescription.insert(END,"Dosage:\t\t"+self.Dosage.get()+"\n")
        self.txtPrescription.insert(END,"Reason/Comment:\t\t"+self.add_comm.get()+"\n")
        self.txtPrescription.insert(END,"Prescription Timestamp:\t\t"+str(y[0])+" "+str(y[1])+"\n")

        conn.close()
    
    def search_records(self):
        from tkinter.simpledialog import askstring
        from tkinter.messagebox import showinfo

        win1=Tk()
        win1.geometry("500x300")

        # Functions to pick date from Calender

        def pick_start_date(e):
            global cal, date_window
            date_window = Toplevel()
            date_window.grab_set()
            date_window.title('Choose start date')
            date_window.geometry('250x220+590+370')
            cal = Calendar(date_window, selectmode='day', date_pattern="yyyy-mm-dd")
            cal.place(x=0, y=0)

            submit_btn = Button(date_window, text='submit', command=grab_start_date)
            submit_btn.place(x=100, y=190)

        def pick_end_date(e):
            global cal, date_window
            date_window = Toplevel()
            date_window.grab_set()
            date_window.title('Choose end date')
            date_window.geometry('250x220+590+370')
            cal = Calendar(date_window, selectmode='day', date_pattern="yyyy-mm-dd")
            cal.place(x=0, y=0)

            submit_btn = Button(date_window, text='submit', command=grab_end_date)
            submit_btn.place(x=100, y=190)

        def grab_start_date():
            selected_date = cal.get_date()
            print('Start date')
            print(selected_date)
            sd_e.delete(0, END)
            sd_e.insert(0, selected_date)
            date_window.destroy()

        def grab_end_date():
            selected_date = cal.get_date()
            print('End date')
            print(selected_date)
            ed_e.delete(0, END)
            ed_e.insert(0, selected_date)
            date_window.destroy()


        #pid = askstring('Patient ID', 'What is patient ID?')

        # Patient ID
        pid_l=Label(win1, text='What is Patient ID: ', font=('Calibri', 12, 'bold'))
        pid_l.place(x=50,y=70)

        pid_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        pid_e.place(x=200,y=70,width=100)

        # Start date
        sd = Label(win1, text='What is start date: ', font=('Calibri', 12, 'bold'))
        sd.place(x=50,y=100)

        sd_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        sd_e.place(x=200,y=100,width=100)

        sd_e.insert(0,"yyyy-mm-dd")
        sd_e.bind("<Button-1>",pick_start_date)

        # End Date
        ed_l = Label(win1, text='What is end date: ', font=('Calibri', 12, 'bold'))
        ed_l.place(x=50,y=130)

        ed_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        ed_e.place(x=200,y=130,width=100)

        ed_e.insert(0,"yyyy-mm-dd")
        ed_e.bind("<Button-1>",pick_end_date)

        conn = mysql.connector.connect(host='localhost', username='Pharmacist', password='MED@789', database='PDMS')
        cur = conn.cursor()

        # Create the procedural query
        query = """
        CREATE PROCEDURE GetPrescriptionHistory(IN pid VARCHAR(7),IN start_date DATE, IN end_date DATE)
        BEGIN
            SELECT p_id, drug_name, dosage, add_comment, pres_date, pres_time
            FROM prescription
            WHERE p_id = pid AND pres_date BETWEEN start_date AND end_date;
        END;
        """
        # Execute the stored procedure
        # cur.execute(query)
        conn.close()

        def validate_and_search():
            conn = mysql.connector.connect(host='localhost', username='Pharmacist', password='MED@789', database='PDMS')
            cur = conn.cursor()

            if pid_e.get() and sd_e.get()!='yyyy-mm-dd' and ed_e.get()!='yyyy-mm-dd':
                print(pid_e.get(), sd_e.get(), ed_e.get())
                try:
                    cur.execute("CALL GetPrescriptionHistory(%s, %s, %s)",(pid_e.get(), sd_e.get(), ed_e.get()))
                    # cur.callproc('GetPrescriptionHistory', (pid_e.get(), sd_e.get(), ed_e.get()))

                    # Fetching the results
                    pres_history = cur.fetchall()
                    print(pres_history)


                    if pres_history:
                        win2 = Tk()
                        win2.title("Prescription History")

                        label = ttk.Label(win2, text="The prescription history of given pid is: ", font=('Calibri', 14, 'bold'))
                        label.grid(row=0, column=0, pady=10)

                        frame = ttk.Frame(win2)
                        frame.grid(row=1, column=0)

                        tree = ttk.Treeview(frame, columns=("Patient ID", "Medicine Name","Dosage","Add comment","pres_date","pres_time"))
                        tree.heading("#1", text="Patient ID")
                        tree.heading("#2", text="Medicine Name")
                        tree.heading("#3", text="Dosage")
                        tree.heading("#4", text="Add comment")
                        tree.heading("#5", text="pres_date")
                        tree.heading("#6", text="pres_time")

                        for hist in pres_history:
                            tree.insert("", "end", values=hist)

                        tree.grid(row=0, column=0)

                        exit_button = Button(win2, text="Ok", command=win2.destroy)
                        exit_button.grid(row=2, column=0, pady=10)

                        win2.mainloop()

                    else:
                        messagebox.showinfo("No Prescription History", "No Prescription History as per specified range")
                
                except mysql.connector.Error as err:
                    if err.errno == 1305:
                        print("Stored procedure doesn't exist")
                    else:
                        print(err)
                finally:
                    conn.close()
                    win1.destroy()
                
        
        search_btn = Button(win1, text="Search", command=validate_and_search)
        search_btn.place(x=200, y=160)

        search_btn = Button(win1, text="Back", command=win1.destroy)
        search_btn.place(x=200, y=190)



    def delete_record(self):
        messagebox.showinfo("No delete record", "No implementation as we should not delete patient's prescription.")
        '''conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
        cur=conn.cursor()
        query="DELETE FROM Med_Order_p WHERE Item_No = %s"
        value=(self.Item_No.get(),)
        cur.execute(query,value)

        conn.commit()
        conn.close()
        self.fetch_data()
        messagebox.showinfo("The patient has been deleted successfully.")'''
    
    
    def search_pid(self):
        from tkinter.simpledialog import askstring
        from tkinter.messagebox import showinfo

        win1=Tk()
        win1.geometry("700x300")

        pname = askstring('Patient ID', 'What is patient name?')
        
        conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
        cur=conn.cursor()
        query="SELECT p_id,p_name from patient where p_name= %s"
        cur.execute(query,(pname,))
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
        

# if __name__ == "__main__":
#    root = Toplevel()
#    obj1 = pres_details(root)
#    root.mainloop()
