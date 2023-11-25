from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector

def doctor_details():

    def add_doctor():
        win2=Tk()
        win2.geometry("1000x400")
        win2.configure(bg="#ffd7b5")

        win2.resizable(FALSE,FALSE)

        df=Frame(win2,bd=15,relief=RIDGE,padx=20)
        df.place(x=0,y=0,width=995,height=395)

        df_f=LabelFrame(df,bd=10,relief=RIDGE,padx=20,text=' Medicine Information ',fg='#fc8c03',font=('Arial',15,'bold'))
        df_f.place(x=2,y=2,width=940,height=360)

        l_d_id=Label(df_f,font=('Calibri',18,'bold'),text='Doctor ID',fg='#fc4a03')
        l_d_id.grid(row=0,column=0,padx=10,pady=10)
        e_d_id=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_d_id.grid(row=0,column=1)

        l_d_name=Label(df_f,font=('Calibri',18,'bold'),text='Doctor Name',fg='#fc4a03')
        l_d_name.grid(row=1,column=0,padx=10,pady=10)
        e_d_name=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_d_name.grid(row=1,column=1)

        l_sp=Label(df_f,font=('Calibri',18,'bold'),text='Specification',fg='#fc4a03')
        l_sp.grid(row=2,column=0,padx=10,pady=10)
        e_sp=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_sp.grid(row=2,column=1)

        l_hn=Label(df_f,font=('Calibri',18,'bold'),text='Hospital Name',fg='#fc4a03')
        l_hn.grid(row=0,column=2,padx=10,pady=10)
        e_hn=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_hn.grid(row=0,column=3)

        l_hid=Label(df_f,font=('Calibri',18,'bold'),text='Hospital ID',fg='#fc4a03')
        l_hid.grid(row=1,column=2,padx=10,pady=10)
        e_hid=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_hid.grid(row=1,column=3)

        l_cont=Label(df_f,font=('Calibri',18,'bold'),text='Contact Number',fg='#fc4a03')
        l_cont.grid(row=2,column=2,padx=10,pady=10)
        e_cont=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_cont.grid(row=2,column=3)

        
        def validate_and_add():
            d_id = e_d_id.get()
            d_name = e_d_name.get()
            sp = e_sp.get()
            hn = e_hn.get()
            hid = e_hid.get()
            cont = e_cont.get()

            if d_id=='':
                res=messagebox.askquestion('Adding Doctor details', 'Adding New Doctor?')
                if res == 'yes' :
                    x=5
                    y=str(x)
                    d_id='dd_'+y
                    x+=1  
                else:
                    messagebox.showinfo("Check", "Please enter the existed Doctor ID")

            if d_name=='' or sp=='' or hn=='' or hid=='':
                messagebox.showinfo("No Doctor Added", "Please enter the doctor details")

            else:    
                conn = mysql.connector.connect(host='localhost', username='Pharmacist', password='MED@789', database='PDMS')
                cur = conn.cursor()
                
                query = "INSERT INTO doctor (d_id, d_name, specification, h_name, h_id, contact_no) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (d_id, d_name, sp, hn, hid, cont)
                cur.execute(query, values)
                conn.commit()
                messagebox.showinfo("Doctor Details Added", f"{d_name} with ID {d_id} added to the database")
            
        add_btn = Button(win2, text="Add Doctor Details", bg='#34cceb', padx=5, pady=5,command=validate_and_add)
        add_btn.place(x=500, y=290)

        back_btn = Button(win2, text="Back", bg='#34cceb', padx=1, pady=1, command=win2.destroy)
        back_btn.place(x=530, y=330)

        
    
    def search_doc():
        win1=Tk()
        win1.geometry("400x300")
        win1.configure(bg="#ffd7b5")

        # Doctor ID
        did_l=Label(win1, text='Enter Doctor ID: ', font=('Calibri', 12, 'bold'))
        did_l.place(x=50,y=70)

        did_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        did_e.place(x=270,y=70,width=100)

        # Doctor name
        ddn_l= Label(win1, text='Enter Doctor Name: ', font=('Calibri', 12, 'bold'))
        ddn_l.place(x=50,y=100)

        ddn_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        ddn_e.place(x=270,y=100,width=100)

        # Specialization
        dsp_l= Label(win1, text='Enter Doctor\'s Specialization: ', font=('Calibri', 12, 'bold'))
        dsp_l.place(x=50,y=130)

        dsp_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        dsp_e.place(x=270,y=130,width=100)

        # Hospital Name
        hn_l= Label(win1, text='Enter Hospital Name: ', font=('Calibri', 12, 'bold'))
        hn_l.place(x=50,y=160)

        hn_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        hn_e.place(x=270,y=160,width=100)

        def validate_and_search():
            conn = mysql.connector.connect(host='localhost', username='Pharmacist', password='MED@789', database='PDMS')
            cur = conn.cursor()

            if did_e.get() != '':
                x = did_e.get()
                query = "SELECT * FROM doctor WHERE d_id=%s"
                cur.execute(query, (x,))
                list1 = cur.fetchall()

            elif ddn_e.get() != '':
                y = ddn_e.get()
                query = "SELECT * FROM doctor WHERE d_name LIKE %s"
                y = f"%{y}%"
                cur.execute(query, (y,))
                list1 = cur.fetchall()

            elif dsp_e.get() != '':
                z = dsp_e.get()
                query = "SELECT * FROM doctor WHERE specification LIKE %s"
                z = f"%{z}%"
                cur.execute(query, (z,))
                list1 = cur.fetchall()

            elif hn_e.get() != '':
                z = hn_e.get()
                query = "SELECT * FROM doctor WHERE h_name LIKE %s"
                z = f"%{z}%"
                cur.execute(query, (z,))
                list1 = cur.fetchall()

            else:
                query = "SELECT * FROM doctor"
                cur.execute(query)
                list1 = cur.fetchall()

            if list1:
                win2 = Tk()
                win2.title("Prescribed Doctor Details")

                frame = ttk.Frame(win2)
                frame.grid(row=0, column=0)

                # Create the treeview widget
                tree = ttk.Treeview(frame, columns=("d_id", "d_name", "specification", "h_name", "n_id", "contact_no"))


                # Columns and their headings
                tree.heading("#1", text="Doctor ID")
                tree.heading("#2", text="Doctor Name")
                tree.heading("#3", text="Specification")
                tree.heading("#4", text="Hospital Name")
                tree.heading("#5", text="Hospital ID")
                tree.heading("#6", text="Contact No.")

                for hist in list1:
                    tree.insert("", "end", values=hist)

                tree.grid(row=0, column=0)

                win2.grid_rowconfigure(0, weight=1)
                win2.grid_columnconfigure(0, weight=1)

                # Create and configure vertical scrollbar
                vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
                tree.configure(yscrollcommand=vsb.set)
                vsb.grid(row=0, column=1, sticky="ns")

                # Create and configure horizontal scrollbar
                hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
                tree.configure(xscrollcommand=hsb.set)
                hsb.grid(row=1, column=0, sticky="ew")

                exit_button = Button(win2, text="Ok", command=win2.destroy)
                exit_button.grid(row=2, column=0, pady=10)

            else:
                messagebox.showinfo("No Doctor Found", "No prescribed doctor found in the Medical Store")

            conn.close()

        search_btn = Button(win1, text="Search", bg='#34cceb', command=validate_and_search)
        search_btn.place(x=190, y=200)

        back_btn = Button(win1, text="Back", bg='#34cceb', command=win1.destroy)
        back_btn.place(x=195, y=240)

    medicine_window = Toplevel()
    medicine_window.title("Prescribed Doctor Details")
    medicine_window.geometry("500x400")
    medicine_window.configure(bg='#03cafc')

    w1 = PanedWindow(medicine_window, orient=VERTICAL)
    w1.pack(fill=BOTH, pady=120)

    b1 = Button(w1, text="Add Doctor Details", bg='#fcfc03', font=('Calibri',12), pady=5, command=add_doctor)
    w1.add(b1)

    b2 = Button(w1, text="Search Doctor", bg='#fcfc03', font=('Calibri',12), pady=5, command=search_doc)
    w1.add(b2)

    b3 = Button(w1, text="Back", bg='#fcfc03', font=('Calibri',12), pady=5, command=medicine_window.destroy)
    w1.add(b3)

    medicine_window.mainloop()

