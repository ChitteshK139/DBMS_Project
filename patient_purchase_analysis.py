from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk,Image
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import mysql.connector

def pat_analysis():

    def monthly_analysis():
        win1=Tk()
        win1.geometry("400x300")
        win1.configure(bg="#ffd7b5")

        # Patient Name
        pid_l=Label(win1, text='Patient ID: ', font=('Calibri', 12, 'bold'))
        pid_l.place(x=50,y=70)

        pid_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        pid_e.place(x=270,y=70,width=100)

        # Month Number
        mon_l= Label(win1, text='Enter Month: ', font=('Calibri', 12, 'bold'))
        mon_l.place(x=50,y=100)

        mon_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        mon_e.place(x=270,y=100,width=100)

        # Year
        year_l= Label(win1, text='Enter Year: ', font=('Calibri', 12, 'bold'))
        year_l.place(x=50,y=130)

        year_e=Entry(win1,relief=RIDGE,font=('Calibri',12,'bold'),bg='#ffffe0')
        year_e.place(x=270,y=130,width=100)

        def validate_and_evaluate():
            pid=pid_e.get()
            mon=mon_e.get()
            yr=year_e.get()
    
            if pid=='' or mon=='' or yr=='':
                if pid=='':
                    messagebox.showerror("No Patient Name entered", "Please enter Patient Name")
                    return
                elif mon=='' and yr=='':
                    mon,yr=11,2023
                elif mon=='':
                    mon=11
                elif yr=='':
                    yr=2023
            
            conn = mysql.connector.connect(host='localhost', username='Pharmacist', password='MED@789', database='PDMS')
            cur = conn.cursor()

            # Function
            # query='''
            # CREATE FUNCTION Calculate_Monthly_Expense(patient_id VARCHAR(20), month INT, year INT)
            # RETURNS DECIMAL(8, 2) DETERMINISTIC
            # BEGIN
            #     DECLARE total_cost DECIMAL(8, 2);

            #     SELECT SUM(cost) INTO total_cost
            #     FROM med_order_p
            #     WHERE Patient_ID = patient_id AND MONTH(order_timestamp) = month AND YEAR(order_timestamp) = year
            #     GROUP BY patient_id;

            #     RETURN total_cost;
            # END
            # '''

            query='''SELECT patient_id,SUM(cost) AS total_cost
                  FROM med_order_p
                  WHERE Patient_ID = %s AND MONTH(order_timestamp) = %s AND YEAR(order_timestamp) = %s
                  GROUP BY %s'''
            

            try:
                mon,yr=int(mon),int(yr)
                print(pid,mon,yr)
                # print("Before function")
                # cur.callproc('Calculate_Monthly_Expense', (pid,mon,yr))
                # print("After function!")
                # list1 = None
                # for list1 in cur.stored_results():
                #     list1 = list1.fetchall()
                # print("After result!")
                cur.execute(query,(pid,mon,yr,pid))
                list1=cur.fetchall()
                if list1:
                    win2 = Tk()
                    win2.title("Prescription History")
                    frame = ttk.Frame(win2)
                    frame.grid(row=0, column=0)

                    tree = ttk.Treeview(win2, columns=("Patient_Name","total_Cost"))
                    tree.heading("#1", text="Patient Name")
                    tree.heading("#2", text="Total Cost (Monthly Expense)")

                    for item in list1:
                        tree.insert("", "end", values=item)

                    tree.grid(row=0, column=0)

                    exit_button = Button(win2, text="Ok", command=win2.destroy)
                    exit_button.grid(row=2, column=0, pady=10)
                
                else:
                    messagebox.showinfo("No medicine purchased",f"{pid} has not purchased any medicine this month.")

            except mysql.connector.Error as err:
                print(err)

                #messagebox.showerror("Error Found", "Please enter valid input")
        
        def search_pid():
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

            win1.mainloop()
            

        search_btn = Button(win1, text="Search", bg='#34cceb', command=validate_and_evaluate)
        search_btn.place(x=190, y=180)
        search_btn = Button(win1, text="Search Patient ID", bg='#34cceb', command=search_pid)
        search_btn.place(x=160, y=220)
        exit_button = Button(win1, text="Ok", bg='#34cceb', command=win1.destroy)
        exit_button.place(x=190, y=260)
        

    def com_med_analysis():
        conn = mysql.connector.connect(host='localhost', username='Pharmacist', password='MED@789', database='PDMS')
        cur = conn.cursor()
        # Nested Query
        query='''
        SELECT DISTINCT doc.d_id, doc.d_name
        FROM doctor AS doc
        WHERE EXISTS (
            SELECT *
            FROM doctor AS d2
            JOIN prescription AS p2 ON d2.d_id = p2.d_id
            WHERE doc.d_id <> d2.d_id
            AND p2.drug_name IN (
                SELECT DISTINCT p1.drug_name
                FROM prescription AS p1
                WHERE p1.d_id = doc.d_id
            )
        );
        '''

        cur.execute(query)
        list2=cur.fetchall()

        query1='SELECT med_name,SUM(Dosage) AS total_dosage FROM med_order_p GROUP BY med_name ORDER BY total_dosage DESC'
        try:
            cur.execute(query1)
            list3=cur.fetchall()

            if list2:
                win2 = Tk()
                win2.title("Doctors prescribed same medication")

                frame = ttk.Frame(win2)
                frame.grid(row=0, column=0)

                # Create the treeview widget
                tree = ttk.Treeview(frame, columns=("d_id", "d_name"))

                # Columns and their headings
                tree.heading("#1", text="Doctor ID")
                tree.heading("#2", text="Doctor Name")

                for hist in list2:
                    tree.insert("", "end", values=hist)

                tree.grid(row=0, column=0)

                win2.grid_rowconfigure(0, weight=1)
                win2.grid_columnconfigure(0, weight=1)
                print("list2")

            if list3:
                print("list3")
                win3=Tk()
                win3.geometry("700x500")
                win3.configure(bg="#ffd7b5")

                fig=plt.figure(figsize=(5,5),dpi=100)
                fig.set_size_inches(5,3.5)
                labels=[i[0] for i in list3] 
                val=[i[1] for i in list3]

                explode1 = [0.2 if i == 0 else 0 for i in range(len(labels))]

                plt.pie(val,explode=explode1,labels=labels,autopct='%1.1f%%',shadow=True,startangle=140)
                plt.axis('equal')

                canvasbar=FigureCanvasTkAgg(fig,master=win3)
                canvasbar.draw()

                canvasbar.get_tk_widget().place(x=300,y=250,anchor=CENTER)
                #plt.show()
            
            else:
                messagebox.showinfo("Not Found", "Not Found")

                
        except mysql.connector.Error as err:
            print(err)
            # messagebox.showerror("Error Found", "Please enter valid input")

        conn.close()

    
    def age_grp_analysis():  # Medication usage patterns and doctor performance analysis (Research and Studies) -> Correlated Query
        conn = mysql.connector.connect(host='localhost', username='Pharmacist', password='MED@789', database='PDMS')
        cur = conn.cursor()
        # Correlated Query
        query='''
        SELECT CASE
        WHEN p.age < 18 THEN 'Under 18'
        WHEN p.age BETWEEN 18 AND 45 THEN '18-45'
        WHEN p.age BETWEEN 46 AND 65 THEN '45-65'
        ELSE '65+'
        END AS age_grp, drug_name AS Medication, 
        (SELECT COUNT(*) FROM prescription pr_inner WHERE pr_inner.p_id = p.p_id AND pr_inner.drug_name = pr.drug_name) AS pres_count
        FROM prescription pr JOIN patient p ON pr.p_id = p.p_id
        GROUP BY age_grp, Medication ORDER BY age_grp, pres_count DESC;
        '''

        cur.execute(query)
        list1=cur.fetchall()
        conn.close()

        if list1:
            win2 = Tk()
            win2.title("Doctors prescribed same medication")

            frame = ttk.Frame(win2)
            frame.grid(row=0, column=0)

            # Create the treeview widget
            tree = ttk.Treeview(frame, columns=("age_grp", "Medication","pres_count"))

            # Columns and their headings
            tree.heading("#1", text="Age Group")
            tree.heading("#2", text="Medication")
            tree.heading("#3", text="Prescription Dosage Count")

            for hist in list1:
                tree.insert("", "end", values=hist)

            tree.grid(row=0, column=0)

            win2.grid_rowconfigure(0, weight=1)
            win2.grid_columnconfigure(0, weight=1)

            # Bar Chart
            fig, ax = plt.subplots(figsize=(8, 6))

            age_groups = [data[0] for data in list1]
            medications = [data[1] for data in list1]
            prescription_counts = [data[2] for data in list1]

            for age_group in set(age_groups):
                age_group_indices = [i for i, value in enumerate(age_groups) if value == age_group]
                ax.bar([medications[i] for i in age_group_indices], [prescription_counts[i] for i in age_group_indices], label=age_group)

            ax.set_xlabel('Medication')
            ax.set_ylabel('Prescription Dosage Count')
            ax.set_title('Medication Prescription Count by Age Group')
            ax.legend()

            canvas = FigureCanvasTkAgg(fig, master=win2)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.grid(row=1, column=0)

            # Pie Chart
            fig2, ax2 = plt.subplots()

            age_group_counts = {}
            for age_group in age_groups:
                age_group_counts[age_group] = age_group_counts.get(age_group, 0) + 1

            ax2.pie(age_group_counts.values(), labels=age_group_counts.keys(), autopct='%1.1f%%', startangle=90)
            ax2.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
            ax2.set_title('Age Group Distribution')

            canvas2 = FigureCanvasTkAgg(fig2, master=win2)
            canvas_widget2 = canvas2.get_tk_widget()
            canvas_widget2.grid(row=1, column=1)

            # plt.show()
            # win2.mainloop()

        else:
            messagebox.showinfo("Not Found", "Not Found")

        

    medicine_window = Toplevel()
    medicine_window.title("Medicine Details")
    medicine_window.geometry("500x400")
    medicine_window.configure(bg='#03cafc')

    w1 = PanedWindow(medicine_window, orient=VERTICAL)
    w1.pack(fill=BOTH, pady=100)

    b1 = Button(w1, text="Monthly medication expense", bg='#fcfc03', font=('Calibri',12), pady=5, command=monthly_analysis)
    w1.add(b1)

    b2 = Button(w1, text="Common Medication prescribed by many doctors ", bg='#fcfc03', font=('Calibri',12), pady=5, command=com_med_analysis)
    w1.add(b2)

    b3 = Button(w1, text="Analyze medication usage within different age groups ", bg='#fcfc03', font=('Calibri',12), pady=5, command=age_grp_analysis)
    w1.add(b3)

    b4 = Button(w1, text="Back", bg='#fcfc03', font=('Calibri',12), pady=5, command=medicine_window.destroy)
    w1.add(b4)

    medicine_window.mainloop()