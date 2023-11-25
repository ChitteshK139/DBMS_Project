from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from medicine_details import *
from prescription_details_class import *
from patient_order import *
from add_medicines import *
from drug_dealer_details import *
from patient_purchase_analysis import *

uname_pwd_dict={'user1':'abc123','jahnavi':'jk1811'}


def login_option():
    global window1
    window1=Tk()
    window1.title('PDMS Login')
    window1.geometry('500x500')
    window1.configure(bg='#03cafc')

    icon1=PhotoImage(file='icon_1.png')
    window1.iconphoto(False,icon1)

    # TRIGGER 1 (Caution Message for showing Expired Medicines)

    conn = mysql.connector.connect(host='localhost', username='Pharmacist', password='MED@789', database='PDMS')
    cur = conn.cursor()

    # Create the trigger
    query = """
    CREATE TRIGGER Before_Delete_Expired_Medicine
    BEFORE DELETE ON medicine
    FOR EACH ROW
    BEGIN
        IF OLD.exp_date <= CURDATE() THEN 
            INSERT INTO deleted_expired_medicines (m_id, drug_name, exp_date) VALUES (OLD.m_id, OLD.drug_name, OLD.exp_date);
        END IF;
    END;
    """
    #cur.execute(query)

    cur.execute("DELETE FROM medicine where exp_date <= CURDATE();")

    cur.execute("SELECT * FROM deleted_expired_medicines where exp_date <= CURDATE()")
    expired_medicines = cur.fetchall()
    
    conn.close()

    if expired_medicines:
        win1 = Tk()
        win1.title("Expired Medicines")
        frame = ttk.Frame(win1)
        frame.grid(row=0, column=0)

        tree = ttk.Treeview(frame, columns=("Medicine ID", "Medicine Name", "Expiry Date"))
        tree.heading("#1", text="Medicine ID")
        tree.heading("#2", text="Medicine Name")
        tree.heading("#3", text="Expiry Date")

        for medicine in expired_medicines:
            tree.insert("", "end", values=medicine)

        tree.grid(row=0, column=0)
        messagebox.showwarning("Caution", "The following medicines are expired:")
        exit_button = Button(win1, text="Ok", command=win1.destroy)
        exit_button.grid(row=2, column=0, pady=10)

    else:
        messagebox.showinfo("No Expired Medicines", "No medicines have expired.")

    # Next login page

    w1=PanedWindow(orient=VERTICAL)
    w1.pack(fill = BOTH,pady=110)

    b1 = Button(w1, text = "Check Medicine In Stock",bg='#fcfc03',pady=5,command=med_details)   # Search for medicine in stock
    w1.add(b1)

    b2 = Button(w1, text = "Presciption Details",bg='#fcfc03',pady=5,command=pres_details_1)  
    w1.add(b2)

    b3 = Button(w1, text = "Add drug dealer details and Medicines",bg='#fcfc03',pady=5,command=add_dd_details)  
    w1.add(b3)

    b4 = Button(w1, text = "Add medication, after receiving delivery from the drug dealer",bg='#fcfc03',pady=5,command=add_med_details)  
    w1.add(b4)

    b5 = Button(w1, text = "Place an Order (Patient)",bg='#fcfc03',pady=5,command=patient_order_details_1)  
    w1.add(b5)

    b6=Button(w1, text='Analysis of Patient Medicine Purchase',bg='#fcfc03',pady=5,command=pat_analysis)
    w1.add(b6)

    b7 = Button(w1, text = "Logout",bg='#fcfc03',pady=5,command=pharmacist_logout)  
    w1.add(b7)

    window1.resizable(False,False)   
    window1.mainloop()

    
# Login Authentication
def login_authentication():
    global username
    username=p_uname_e.get()
    password=p_pwd_e.get()

    if username in uname_pwd_dict:
        if uname_pwd_dict[username]==password:
            messagebox.showinfo("Welcome to PDMS",  "Login Successfully")
            window.destroy()
            login_option()

        else:
            messagebox.showinfo("PDMS",  "Login Failed")


# Logout 
def pharmacist_logout():
    res=messagebox.askquestion('Exit Application', f'{username}, Are you sure that you want to logout?')
    if res == 'yes' :
        window1.destroy()

def pres_details_1():
    root = Toplevel()
    obj1 = pres_details(root)

def patient_order_details_1():
    root = Toplevel()
    obj2= patient_order_details(root)



window=Tk()
window.title('PDMS Login')
window.geometry('925x500+300+200')

icon1=PhotoImage(file='icon_1.png')
window.iconphoto(False,icon1)

window.configure(bg='white')

img1=PhotoImage(file='login_1 (2).png')
Label(window,image=img1,bg='white',height=450,width=416).place(x=40,y=20)

img2=ImageTk.PhotoImage(file='login_2_new.png')

frame1=Frame()

canvas1=Canvas(window,width=350,height=400)
canvas1.pack()

canvas1.place(x=530,y=50)

x = 0
y = 0 

canvas1.create_image(x, y, image=img2, anchor=NW)

text1=canvas1.create_text(175,130,text='Sign in',font=('Times New Roman',24))

x1, y1, x2, y2 = canvas1.bbox(text1)

# Create an underline (line) underneath the text
underline_y = y2 + 5  # Adjust the value to control the underline's position
canvas1.create_line(x1, underline_y, x2, underline_y, fill="black")

canvas1.create_text(120,185,text='Username: ',font=('Times New Roman',16))

p_uname_e=Entry(canvas1,bg='#fffdd0',width=15,font=('Verdana',11))
p_uname_e.place(x=170,y=175)

canvas1.create_text(120,230,text='Password: ',font=('Times New Roman',16))

p_pwd_e=Entry(canvas1,bg='#fffdd0',show='*')
p_pwd_e.place(x=170,y=220)


login_button = Button(canvas1, text="Login",padx=10,pady=3,bg='#90EE90',relief=RAISED,bd=2,command=login_authentication)
login_button.place(x=160, y=270)



window.resizable(False,False)   
window.mainloop()




