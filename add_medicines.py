from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector

def add_med_details():

    def add_med():
        win2=Tk()
        win2.geometry("1000x400")
        win2.configure(bg="#ffd7b5")

        win2.resizable(FALSE,FALSE)

        df=Frame(win2,bd=15,relief=RIDGE,padx=20)
        df.place(x=0,y=0,width=995,height=395)

        df_f=LabelFrame(df,bd=10,relief=RIDGE,padx=20,text=' Medicine Information ',fg='#fc8c03',font=('Arial',15,'bold'))
        df_f.place(x=2,y=2,width=940,height=360)

        l_med_id=Label(df_f,font=('Calibri',18,'bold'),text='Medicine ID',fg='#fc4a03')
        l_med_id.grid(row=0,column=0,padx=10,pady=10)
        e_med_id=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_med_id.grid(row=0,column=1)

        l_med_name=Label(df_f,font=('Calibri',18,'bold'),text='Medicine Name',fg='#fc4a03')
        l_med_name.grid(row=1,column=0,padx=10,pady=10)
        e_med_name=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_med_name.grid(row=1,column=1)

        l_comp_name=Label(df_f,font=('Calibri',18,'bold'),text='Company Name',fg='#fc4a03')
        l_comp_name.grid(row=2,column=0,padx=10,pady=10)
        e_comp_name=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_comp_name.grid(row=2,column=1)

        l_exp_d=Label(df_f,font=('Calibri',18,'bold'),text='Expiry Date',fg='#fc4a03')
        l_exp_d.grid(row=3,column=0,padx=10,pady=10)
        e_exp_d=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_exp_d.grid(row=3,column=1)

        l_cost=Label(df_f,font=('Calibri',18,'bold'),text='Price',fg='#fc4a03')
        l_cost.grid(row=0,column=2,padx=10,pady=10)
        e_cost=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_cost.grid(row=0,column=3)

        l_comp=Label(df_f,font=('Calibri',18,'bold'),text='Composition',fg='#fc4a03')
        l_comp.grid(row=1,column=2,padx=10,pady=10)
        e_comp=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_comp.grid(row=1,column=3)

        l_ddid=Label(df_f,font=('Calibri',18,'bold'),text='dd_id',fg='#fc4a03')
        l_ddid.grid(row=2,column=2,padx=10,pady=10)
        e_ddid=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_ddid.grid(row=2,column=3)

        l_qty=Label(df_f,font=('Calibri',18,'bold'),text='Quantity',fg='#fc4a03')
        l_qty.grid(row=3,column=2,padx=10,pady=10)
        e_qty=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_qty.grid(row=3,column=3)

        
        def validate_and_add():
            if e_med_id.get()=='' or e_med_name.get()=='' or e_comp_name.get()=='' or e_exp_d.get()=='' or e_cost.get()=='' or e_comp.get()=='' or e_ddid.get()=='' or e_qty.get()=='':
                messagebox.showinfo("No Medicine Added", "No medicine has added")
            else:
                med_id = e_med_id.get()
                med_name = e_med_name.get()
                comp_name = e_comp_name.get()
                exp_date = e_exp_d.get()
                cost = e_cost.get()
                comp = e_comp.get()
                dd_id = e_ddid.get()
                qty = e_qty.get()

                if dd_id == '':
                    x=7
                    y=str(x)
                    dd_id='dd_'+y
                    x+=1  

                if med_name == '':
                    messagebox.showinfo("Missing Information", "Please enter Medicine Name.")
                    return 
                
                conn = mysql.connector.connect(host='localhost', username='Pharmacist', password='MED@789', database='PDMS')
                cur = conn.cursor()
                
                query = "SELECT quantity FROM medicine WHERE m_id = %s AND drug_name = %s"
                cur.execute(query, (med_id, med_name))
                existing_medicine = cur.fetchone()

                if existing_medicine:
                    existing_qty = existing_medicine[0]
                    updated_qty = existing_qty + int(qty)
                    update_query = "UPDATE medicine SET quantity = %s WHERE m_id = %s AND drug_name = %s"
                    cur.execute(update_query, (updated_qty, med_id, med_name))
                    conn.commit()
                    messagebox.showinfo("Medicine Updated", f"Quantity of {med_name} with ID {med_id} updated to {updated_qty}.")
                
                else:
                    query = "INSERT INTO medicine (m_id, drug_name, company_name, price, exp_date, composition, dd_id, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    values = (med_id, med_name, comp_name, cost, exp_date, comp, dd_id, qty)
                    cur.execute(query, values)
                    conn.commit()
                    messagebox.showinfo("Medicine Added", f"{med_name} with ID {med_id} added to the database with {qty} quantity.")
            
        add_btn = Button(win2, text="Add medicine", bg='#34cceb', padx=5, pady=5,command=validate_and_add)
        add_btn.place(x=500, y=290)

        back_btn = Button(win2, text="Back", bg='#34cceb', padx=1, pady=1, command=win2.destroy)
        back_btn.place(x=530, y=330)

        
    
    def search_med():
        win1=Tk()
        win1.geometry("400x300")
        win1.configure(bg="#ffd7b5")

        # Medicine ID
        mid_l=Label(win1, text='Medicine ID: ', font=('Calibri', 12, 'bold'))
        mid_l.place(x=50,y=70)

        mid_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        mid_e.place(x=270,y=70,width=100)

        # Medicine name
        medn_l= Label(win1, text='What is Medicine Name: ', font=('Calibri', 12, 'bold'))
        medn_l.place(x=50,y=100)

        medn_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        medn_e.place(x=270,y=100,width=100)

        # Expiry Date

        comp_l= Label(win1, text='Enter composition: ', font=('Calibri', 12, 'bold'))
        comp_l.place(x=50,y=130)

        comp_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        comp_e.place(x=270,y=130,width=100)


        def validate_and_search():
            conn = mysql.connector.connect(host='localhost', username='Pharmacist', password='MED@789', database='PDMS')
            cur = conn.cursor()

            if mid_e.get() != '':
                x = mid_e.get()
                query = "SELECT * FROM medicine WHERE m_id=%s"
                cur.execute(query, (x,))
                list1 = cur.fetchall()

            elif medn_e.get() != '':
                y = medn_e.get()
                query = "SELECT * FROM medicine WHERE drug_name LIKE %s"
                y = f"%{y}%"
                cur.execute(query, (y,))
                list1 = cur.fetchall()

            elif comp_e.get() != '':
                z = comp_e.get()
                query = "SELECT * FROM medicine WHERE composition LIKE %s"
                z = f"%{z}%"
                cur.execute(query, (z,))
                list1 = cur.fetchall()

            else:
                query = "SELECT * FROM medicine"
                cur.execute(query)
                list1 = cur.fetchall()

            if list1:
                win2 = Tk()
                win2.title("Medicine Details")

                frame = ttk.Frame(win2)
                frame.grid(row=0, column=0)

                # Create the treeview widget
                tree = ttk.Treeview(frame, columns=("m_id", "drug_name", "company_name", "price", "expiry_date", "composition", "dd_id", "quantity"))

                # Create and configure vertical scrollbar
                vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
                tree.configure(yscrollcommand=vsb.set)
                vsb.grid(row=0, column=1, sticky="ns")

                # Create and configure horizontal scrollbar
                hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
                tree.configure(xscrollcommand=hsb.set)
                hsb.grid(row=1, column=0, sticky="ew")

                # Columns and their headings
                tree.heading("#1", text="Medicine ID")
                tree.heading("#2", text="Medicine Name")
                tree.heading("#3", text="Company Name")
                tree.heading("#4", text="Price")
                tree.heading("#5", text="Expiry Date")
                tree.heading("#6", text="Composition")
                tree.heading("#7", text="dd_id")
                tree.heading("#8", text="Quantity")

                for hist in list1:
                    tree.insert("", "end", values=hist)

                tree.grid(row=0, column=0)

                win2.grid_rowconfigure(0, weight=1)
                win2.grid_columnconfigure(0, weight=1)

            else:
                messagebox.showinfo("No Medicines", "No medicines found in the Medical Store")

            conn.close()

        search_btn = Button(win1, text="Search", bg='#34cceb', command=validate_and_search)
        search_btn.place(x=190, y=180)

        back_btn = Button(win1, text="Back", bg='#34cceb', command=win1.destroy)
        back_btn.place(x=195, y=220)

    medicine_window = Toplevel()
    medicine_window.title("Medicine Details")
    medicine_window.geometry("500x400")
    medicine_window.configure(bg='#03cafc')

    w1 = PanedWindow(medicine_window, orient=VERTICAL)
    w1.pack(fill=BOTH, pady=120)

    b1 = Button(w1, text="Add Medicine", bg='#fcfc03', font=('Calibri',12), pady=5, command=add_med)
    w1.add(b1)

    b2 = Button(w1, text="Search Medicine", bg='#fcfc03', font=('Calibri',12), pady=5, command=search_med)
    w1.add(b2)

    b3 = Button(w1, text="Back", bg='#fcfc03', font=('Calibri',12), pady=5, command=medicine_window.destroy)
    w1.add(b3)

    medicine_window.mainloop()

