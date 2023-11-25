from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
from tkcalendar import DateEntry
import mysql.connector
from tkcalendar import *
from pres_doctor_details import *
import sys 

def pres_details():
    sys.path.append('F:/PES/B_Tech (Sem_5)/Database Management System/Mini Project') 
    print(sys.path)
    print("Done!")
    win = Toplevel()
    win.title("Pharmacy Database Management System")
    win.geometry("1550x800+0+0")

    patient_id=StringVar()
    Med_Name=StringVar()
    Dosage=StringVar()
    add_comm=StringVar()

    l_title=Label(win,text="Pharmacy Database Mangement System",bd=15,relief=RIDGE,bg='white',fg='#04AF70',font=('Georgia',45,'bold'),padx=2,pady=4)
    l_title.pack(side=TOP,fill=X) # fill in X axis

    icon_img = ImageTk.PhotoImage(file="F:/PES/B_Tech (Sem_5)/Database Management System/Mini Project/pharmacy_logo (1).png")
    # icon_img = icon_img.subsample(2,1)  # Adjust the subsample factor if needed
    b1 = Button(win, image=icon_img, borderwidth=0)

    #img1=Image.open("pharmacy_logo (1).png")
    # img1.resize((70,70), Image.BILINEAR)
    # icon_img=ImageTk.PhotoImage(img1)
    # b1=Button(win,image=icon_img,borderwidth=0)
    b1.place(x=50,y=30)

    # DataFrame
    df=Frame(win,bd=15,relief=RIDGE,padx=20)
    df.place(x=0,y=120,width=1530,height=300)

    df_left=LabelFrame(df,bd=10,relief=RIDGE,padx=20,text=' Prescription Details ',fg='#fc8c03',font=('Arial',15,'bold'))
    df_left.place(x=0,y=5,width=580,height=250)

    df_right=LabelFrame(df,bd=10,relief=RIDGE,padx=20,text=' Prescription ',fg='#fc8c03',font=('Arial',15,'bold'))
    df_right.place(x=590,y=5,width=660,height=250)

    txtPrescription=Text(df_right,font=('Calibri',14,'bold'),width=60,height=9)
    txtPrescription.grid(row=0,column=0)

    df_img=LabelFrame(df,bd=10,relief=RIDGE)
    df_img.place(x=1270,y=5,width=210,height=260)

    img1=ImageTk.PhotoImage(Image.open("prescription_img.png"))
    label = Label(df_img, image = img1)
    label.image = img1
    label.pack()
    

    # Button Frame
    but_frame=Frame(win,bd=15,relief=RIDGE,padx=20)
    but_frame.place(x=75,y=430,width=1350,height=65)

    # Main Button 
    but_add=Button(but_frame,text='Add',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=Prescription_Data)
    but_add.grid(row=0,column=0,padx=5)

    but_upd=Button(but_frame,text='Update',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=update_order)
    but_upd.grid(row=0,column=1,padx=5)

    but_del=Button(but_frame,text='Delete',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=delete_record)
    but_del.grid(row=0,column=2,padx=5)

    but_presc=Button(but_frame,text='Prescription Overview',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=iPrescription_overview)
    but_presc.grid(row=0,column=3,padx=5)

    but_reset=Button(but_frame,text='Search Record',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=search_records)
    but_reset.grid(row=0,column=4,padx=5)

    but_spid=Button(but_frame,text='Search Patient ID',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=search_pid)
    but_spid.grid(row=0,column=5,padx=5)

    but_doc= Button(but_frame,text='Doctor Details',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=doctor_details)
    but_doc.grid(row=0,column=6,padx=5)

    but_back=Button(but_frame,text='Back',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command=win.destroy)
    but_back.grid(row=0,column=7,padx=5)

    # Label and Entry
    
    l_p_id=Label(df_left,font=('Calibri',18,'bold'),text='Patient_ID',fg='#fc4a03')
    l_p_id.grid(row=0,column=0,padx=10,pady=10)
    e_p_id=Entry(df_left,textvariable=patient_id,font=('Calibri',19,'bold'),width=20)
    e_p_id.grid(row=0,column=1)

    l_drug_name=Label(df_left,font=('Calibri',18,'bold'),text='Drug Name',fg='#fc4a03')
    l_drug_name.grid(row=1,column=0,padx=10,pady=10)
    e_drug_name=Entry(df_left,textvariable=Med_Name,font=('Calibri',19,'bold'),width=20)
    e_drug_name.grid(row=1,column=1)

    l_dosage=Label(df_left,font=('Calibri',18,'bold'),text='Dosage',fg='#fc4a03')
    l_dosage.grid(row=2,column=0,padx=10,pady=10)
    e_dosage=Entry(df_left,textvariable=Dosage,font=('Calibri',19,'bold'),width=20)
    e_dosage.grid(row=2,column=1)

    l_comment=Label(df_left,font=('Calibri',18,'bold'),text='Additional Comments',fg='#fc4a03')
    l_comment.grid(row=3,column=0,padx=10,pady=10)
    e_comment=Entry(df_left,textvariable=add_comm,font=('Calibri',19,'bold'),width=20)
    e_comment.grid(row=3,column=1)



    # Detail frame
    det_frame=Frame(win,bd=20,relief=RIDGE)
    det_frame.place(x=110,y=500,width=1300,height=265)

    # Tree View (Table)

    order_table=ttk.Treeview(det_frame,column=("pid","drug_name","dosage","add_comm"))

    order_table.heading("pid",text="Patient ID")
    order_table.heading("drug_name",text="Drug Name")
    order_table.heading("dosage",text="Quantity/Dosage")
    order_table.heading("add_comm",text="Additional Comment")

    order_table['show']='headings'

    # Scroll bar

    scroll_x_treeview = Scrollbar(det_frame, orient=HORIZONTAL, command=order_table.xview)
    scroll_y_treeview = Scrollbar(det_frame, orient=VERTICAL, command=order_table.yview)

    order_table.configure(xscrollcommand=scroll_x_treeview.set, yscrollcommand=scroll_y_treeview.set)

    scroll_x_treeview.pack(side=BOTTOM, fill=X)
    scroll_y_treeview.pack(side=RIGHT, fill=Y)

    order_table.pack(fill=BOTH,expand=1)

    order_table.bind("<ButtonRelease-1>",get_cursor)

    fetch_data()

    # Functionality Declaration

    def Prescription_Data():
        if patient_id.get()=='' or Med_Name.get()=='' or Dosage.get()=='' or add_comm.get()=='':
            messagebox.showerror("Error","All fields are mandatory")
        else:
            conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
            cur=conn.cursor()
            
            #try:
            cur.execute("INSERT INTO Prescription(p_id,drug_name,dosage,add_comment) VALUES(%s, %s, %s, %s)", (patient_id.get(), Med_Name.get(), Dosage.get(), add_comm.get()))
            conn.commit()   # Used trigger for cur_date and cur_time
            fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")

            #except mysql.connector.Error:
            #    messagebox.showerror("Error", "Error: Already Existed")

    def fetch_data():
        conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
        cur=conn.cursor()
        cur.execute("SELECT p_id,drug_name,dosage,add_comment FROM prescription")
        rows=cur.fetchall()
        print(rows)
        if len(rows)!=0:
            order_table.delete(*order_table.get_children())
            for r in rows:
                order_table.insert("",END,values=r)
            conn.commit()
        conn.close()

    def get_cursor(event=''):
        cur_row=order_table.focus()
        content=order_table.item(cur_row)
        row=content['values']

        if row:
            patient_id.set(row[0])
            Med_Name.set(row[1])
            Dosage.set(row[2])
            add_comm.set(row[3])


    def update_order(): 
        conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
        cur=conn.cursor()
        cur.execute("UPDATE prescription SET drug_name=%s,dosage=%s,add_comment=%s",
                    (Med_Name.get(),Dosage.get(), add_comm.get()))


    def iPrescription_overview():
        txtPrescription.insert(END,"Item No. :\t\t"+patient_id.get()+"\n")
        txtPrescription.insert(END,"Medicine name:\t\t"+Med_Name.get()+"\n")
        txtPrescription.insert(END,"Dosage:\t\t"+Dosage.get()+"\n")
        txtPrescription.insert(END,"Patient_Name:\t\t"+add_comm.get()+"\n")

    def search_records():
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
        #cur.execute(query)

        def validate_and_search():
            if pid_e.get() and sd_e.get()!='yyyy-mm-dd' and ed_e.get()!='yyyy-mm-dd':
                cur.callproc('GetPrescriptionHistory', (pid_e.get(), sd_e.get(), ed_e.get()))

                # Fetch the results
                cur.nextset()
                pres_history = cur.fetchall()

                conn.close()

                if pres_history:
                    win2 = Tk()
                    win2.title("Prescription History")
                    frame = ttk.Frame(win2)
                    frame.grid(row=0, column=0)

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
                    messagebox.showwarning("Prescription History", "The prescription history of given pid is: ")

                else:
                    messagebox.showinfo("No Prescription History", "No Prescription History as per specified range")
                
                win1.destroy()
                
        
        search_btn = Button(win1, text="Search", command=validate_and_search)
        search_btn.place(x=200, y=160)

        search_btn = Button(win1, text="Back", command=win1.destroy)
        search_btn.place(x=200, y=190)



    def delete_record():
        pass
        '''conn=mysql.connector.connect(host='localhost',username='Pharmacist',password='MED@789',database='PDMS')
        cur=conn.cursor()
        query="DELETE FROM Med_Order_p WHERE Item_No = %s"
        value=(Item_No.get(),)
        cur.execute(query,value)

        conn.commit()
        conn.close()
        fetch_data()
        messagebox.showinfo("The patient has been deleted successfully.")'''


    def search_pid():
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

        #but_add=Button(win1,text='OK',font=('Calibri',12,'bold'),bg='#03c2fc',padx=30,command = win1.destroy)
        #but_add.grid(row=0,column=0,padx=5) 
        

if __name__ == "__main__":
   root = Tk()
   obj1 = pres_details(root)
   root.mainloop()
