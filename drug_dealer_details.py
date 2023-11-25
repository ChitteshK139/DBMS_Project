from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector

def add_dd_details():

    def add_med():
        win2=Tk()
        win2.geometry("1100x400")
        win2.configure(bg="#ffd7b5")

        win2.resizable(FALSE,FALSE)

        df=Frame(win2,bd=15,relief=RIDGE,padx=20)
        df.place(x=0,y=0,width=1095,height=395)

        df_f=LabelFrame(df,bd=10,relief=RIDGE,padx=20,text=' Drug Dealer Information ',fg='#fc8c03',font=('Arial',15,'bold'))
        df_f.place(x=2,y=2,width=1040,height=360)

        l_dd_id=Label(df_f,font=('Calibri',18,'bold'),text='Drug dealer ID',fg='#fc4a03')
        l_dd_id.grid(row=0,column=0,padx=10,pady=10)
        e_dd_id=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_dd_id.grid(row=0,column=1)

        l_med_name=Label(df_f,font=('Calibri',18,'bold'),text='Medicine Name',fg='#fc4a03')
        l_med_name.grid(row=1,column=0,padx=10,pady=10)
        e_med_name=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_med_name.grid(row=1,column=1)

        l_comp_name=Label(df_f,font=('Calibri',18,'bold'),text='DD Company Name',fg='#fc4a03')
        l_comp_name.grid(row=2,column=0,padx=10,pady=10)
        e_comp_name=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_comp_name.grid(row=2,column=1)

        l_qty=Label(df_f,font=('Calibri',18,'bold'),text='Quantity',fg='#fc4a03')
        l_qty.grid(row=0,column=2,padx=10,pady=10)
        e_qty=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_qty.grid(row=0,column=3)

        l_cost=Label(df_f,font=('Calibri',18,'bold'),text='Price of each medicine',fg='#fc4a03')
        l_cost.grid(row=1,column=2,padx=10,pady=10)
        e_cost=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_cost.grid(row=1,column=3)

        l_cont=Label(df_f,font=('Calibri',18,'bold'),text='Contact Number',fg='#fc4a03')
        l_cont.grid(row=2,column=2,padx=10,pady=10)
        e_cont=Entry(df_f,font=('Calibri',19,'bold'),width=20)
        e_cont.grid(row=2,column=3)

        
        
        def validate_and_add():
            if e_dd_id.get()=='' or e_med_name.get()=='' or e_qty.get()=='':
                messagebox.showinfo("No details Added", "No drug dealer details has added")
            else:
                dd_id = e_dd_id.get()
                med_name = e_med_name.get()
                comp_name = e_comp_name.get()
                qty = e_qty.get()
                cost = e_cost.get()
                contact_no=e_cont.get()

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
                
                query = "SELECT quantity FROM drug_dealer WHERE dd_id = %s AND drug_name = %s"
                cur.execute(query, (dd_id, med_name))
                existing_medicine = cur.fetchone()

                if existing_medicine:
                    existing_qty = existing_medicine[0]
                    existing_qty=existing_qty.split(' + ')
                    existing_qty=[int(i) for i in existing_qty]
                    existing_qty=str(sum(existing_qty))
                    updated_qty = existing_qty +' + '+ qty
                    update_query = "UPDATE drug_dealer SET quantity = %s WHERE dd_id = %s AND drug_name = %s"
                    cur.execute(update_query, (updated_qty, dd_id, med_name))
                    conn.commit()
                    messagebox.showinfo("Medicine Quantity Updated", f"Quantity of {med_name} with ID {dd_id} updated to {updated_qty}.")
                
                else:
                    query = "INSERT INTO drug_dealer (dd_id, drug_name, dd_company_name, quantity, price_of_each_med, contact_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    values = (dd_id, med_name, comp_name, qty, cost, contact_no)
                    cur.execute(query, values)
                    conn.commit()
                    messagebox.showinfo("Drug Dealer Added", f"{med_name} with ID {dd_id} added to the database with {qty} quantity.")
            
        add_btn = Button(win2, text="Add Drug Dealer Details", bg='#34cceb', padx=5, pady=5,command=validate_and_add)
        add_btn.place(x=480, y=290)

        back_btn = Button(win2, text="Back", bg='#34cceb', padx=1, pady=1, command=win2.destroy)
        back_btn.place(x=530, y=330)
        
    
    def search_med():
        win1=Tk()
        win1.geometry("400x300")
        win1.configure(bg="#ffd7b5")

        # Medicine ID
        ddid_l=Label(win1, text='What is Drug Dealer ID: ', font=('Calibri', 12, 'bold'))
        ddid_l.place(x=50,y=70)

        ddid_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        ddid_e.place(x=270,y=70,width=100)

        # Expiry Date

        ddn_l= Label(win1, text='Drug Dealer Name: ', font=('Calibri', 12, 'bold'))
        ddn_l.place(x=50,y=130)

        ddn_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        ddn_e.place(x=270,y=130,width=100)

        # Medicine name
        medn_l= Label(win1, text='What is Medicine Name: ', font=('Calibri', 12, 'bold'))
        medn_l.place(x=50,y=100)

        medn_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        medn_e.place(x=270,y=100,width=100)



        def validate_and_add():
            conn = mysql.connector.connect(host='localhost', username='Pharmacist', password='MED@789', database='PDMS')
            cur = conn.cursor()

            if ddid_e.get() != '':
                x = ddid_e.get()
                query = "SELECT * FROM drug_dealer WHERE dd_id=%s"
                cur.execute(query, (x,))
                list1 = cur.fetchall()

            elif ddn_e.get() != '':
                z = ddn_e.get()
                query = "SELECT * FROM drug_dealer WHERE dd_company_name LIKE %s"
                z = f"%{z}%"
                cur.execute(query, (z,))
                list1 = cur.fetchall()

            elif medn_e.get() != '':
                y = medn_e.get()
                query = "SELECT * FROM drug_dealer WHERE drug_name LIKE %s"
                y = f"%{y}%"
                cur.execute(query, (y,))
                list1 = cur.fetchall()

            else:
                query = "SELECT * FROM drug_dealer"
                cur.execute(query)
                list1 = cur.fetchall()

            # print(list1)
            x=list(list1[0])
            y=str(x[3]).split(' + ')
            z=[int(i) for i in y]
            x[3]=str(x[3])+'='+str(sum(z))
            list1[0]=tuple(x)

            if list1:
                win2 = Tk()
                win2.title("Drug Dealer Details")

                frame = ttk.Frame(win2)
                frame.grid(row=0, column=0)

                # Create the treeview widget
                tree = ttk.Treeview(frame, columns=("dd_id", "drug_name", "dd_company_name", "quantity","price_per_each_med","contact_no"))

                # Create and configure vertical scrollbar
                vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
                tree.configure(yscrollcommand=vsb.set)
                vsb.grid(row=0, column=1, sticky="ns")

                # Create and configure horizontal scrollbar
                hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
                tree.configure(xscrollcommand=hsb.set)
                hsb.grid(row=1, column=0, sticky="ew")

                # Columns and their headings
                tree.heading("#1", text="Drug Dealer ID")
                tree.heading("#2", text="Medicine Name")
                tree.heading("#3", text="Company Name")
                tree.heading("#4", text="Quantity")
                tree.heading("#5", text="Price per each med")
                tree.heading("#6", text="Contact No.")

                for hist in list1:
                    tree.insert("", "end", values=hist)

                tree.grid(row=0, column=0)

                exit_button = Button(win2, text="Ok", command=win2.destroy)
                exit_button.grid(row=2, column=0, pady=10)

                win2.grid_rowconfigure(0, weight=1)
                win2.grid_columnconfigure(0, weight=1)

            else:
                messagebox.showinfo("No Drug dealer found", "No Drug Dealer details found")

            conn.close()

        search_btn = Button(win1, text="Search", bg='#34cceb', command=validate_and_add)
        search_btn.place(x=190, y=180)

        back_btn = Button(win1, text="Back", bg='#34cceb', command=win1.destroy)
        back_btn.place(x=195, y=220)

    medicine_window = Toplevel()
    medicine_window.title("Drug Dealer Details")
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

