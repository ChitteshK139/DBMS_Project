from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
import mysql.connector

def med_details():

    def low_stock_med():
        conn = mysql.connector.connect(host='localhost', username='Pharmacist', password='MED@789', database='PDMS')
        cur = conn.cursor()

        query="SELECT m_id,drug_name,quantity from medicine WHERE drug_name IN (SELECT drug_name from medicine WHERE quantity<=5)"
        cur.execute(query)

        low_stock=cur.fetchall()

        if low_stock:
            win2 = Tk()
            win2.title("Low Stock Medicines")

            label = ttk.Label(win2, text="The prescription history of given pid is: ", font=('Calibri', 14, 'bold'))
            label.grid(row=0, column=0, pady=10)

            frame = ttk.Frame(win2)
            frame.grid(row=1, column=0)

            tree = ttk.Treeview(frame, columns=("m_id", "drug_name","quantity"))
            tree.heading("#1", text="Medicine ID")
            tree.heading("#2", text="Medicine Name")
            tree.heading("#3", text="Dosage")

            for hist in low_stock:
                tree.insert("", "end", values=hist)
            
            tree.grid(row=1, column=0)

            exit_button = Button(win2, text="Ok", command=win2.destroy)
            exit_button.grid(row=2, column=0, pady=10)

            win2.mainloop()


        else:
            messagebox.showinfo("Low Stock Medicines", "All medicines are available (In Stock)")
    
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

                label = ttk.Label(win2, text="The required medicine details are: ", font=('Calibri', 14, 'bold'))
                label.grid(row=0, column=0, pady=10)


                frame = ttk.Frame(win2)
                frame.grid(row=1, column=0)

                # Create the treeview widget
                tree = ttk.Treeview(frame, columns=("m_id", "drug_name", "company_name", "price", "expiry_date", "composition", "dd_id", "quantity"))

                # Columns and their headings
                tree.heading("#1", text="Medicine ID")
                tree.heading("#2", text="Medicine Name")
                tree.heading("#3", text="Company Name")
                tree.heading("#4", text="Price")
                tree.heading("#5", text="Expiry Date")
                tree.heading("#6", text="Composition")
                tree.heading("#7", text="dd_id")
                tree.heading("#8", text="Quantity")

                tree.column("#1",width=30)
                tree.column("#2",width=100)
                tree.column("#3",width=100)
                tree.column("#4",width=60)
                tree.column("#5",width=100)
                tree.column("#6",width=200)
                tree.column("#7",width=30)
                tree.column("#8",width=100)

                for hist in list1:
                    tree.insert("", "end", values=hist)

                tree.grid(row=0, column=0)

                win2.grid_rowconfigure(0, weight=1)
                win2.grid_columnconfigure(0, weight=1)

                # Vertical scrollbar
                vsb = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
                tree.configure(yscrollcommand=vsb.set)
                vsb.grid(row=0, column=1, sticky="ns")

                # Horizontal scrollbar
                hsb = ttk.Scrollbar(frame, orient="horizontal", command=tree.xview)
                tree.configure(xscrollcommand=hsb.set)
                hsb.grid(row=1, column=0, sticky="ew")

                exit_button = Button(win2, text="Ok", command=win2.destroy)
                exit_button.grid(row=2, column=0, pady=10)

                win2.mainloop()

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

    b1 = Button(w1, text="Check Low Stock Medicine(s)", bg='#fcfc03', font=('Calibri',12), pady=5, command=low_stock_med)
    w1.add(b1)

    b2 = Button(w1, text="Medicine Details", bg='#fcfc03', font=('Calibri',12), pady=5, command=search_med)
    w1.add(b2)

    b3 = Button(w1, text="Back", bg='#fcfc03', font=('Calibri',12), pady=5, command=medicine_window.destroy)
    w1.add(b3)

    medicine_window.mainloop()







