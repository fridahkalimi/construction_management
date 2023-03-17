from tkinter import *
from tkinter import messagebox, ttk
import sqlite3
con = sqlite3.connect('LMS.db')
cur = con.cursor()

class Issuejob(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("800x800")
        self.title("Issue Work")
        self.resizable(False,False)

        self.top_frame = Frame(self, height=150, bg='grey')
        self.top_frame.pack(fill=X)
        heading = Label(self.top_frame, text='Issue work position',font='arial 18 bold' ,bg='grey')
        heading.place(x=300, y=60)

        self.bodyframe = Frame(self,height=650,bg='white')
        self.bodyframe.pack(fill=X)

        jobs = cur.execute("SELECT * FROM jobs WHERE job_status=0").fetchall()
        job_list = []
        for job in jobs:
            job_list.append(str(job[0])+'-'+job[1])

        

        self.lbl_name = Label(self.bodyframe, text='Position Name:', font='arial 12 bold', bg='white')
        self.lbl_name.place(x=40, y=40)
        self.job_name = StringVar()
        self.txt_job_combo = ttk.Combobox(self.bodyframe, textvariable=self.job_name)
        self.txt_job_combo.place(x= 200,y=45)
        self.txt_job_combo['values'] = job_list

        members = cur.execute("SELECT * FROM member").fetchall()
        member_list = []
        for member in members:
            member_list.append(str(member[0])+'-'+member[1])

        self.lbl_company = Label(self.bodyframe, text='Select member:', font='arial 12 bold', bg='white')
        self.lbl_company.place(x=40, y=80)
        self.member_name = StringVar()
        self.txt_member_combo = ttk.Combobox(self.bodyframe,textvariable=self.member_name)
        self.txt_member_combo.place(x= 200,y=80)

        self.txt_member_combo['values'] = member_list

        # Save Button
        savebutton = Button(self.bodyframe, text='Issue now',command=self.issue_job)
        savebutton.place(x=270, y=200)

    def issue_job(self):


        selected_job = self.txt_job_combo.get().split('-')[0]
        selected_member = self.txt_member_combo.get().split('-')[0]
        try:
            query = "INSERT INTO issuedjobs(job_id,member_id)VALUES(?,?)"
            cur.execute(query, (selected_job, selected_member))
            con.commit()
            cur.execute("UPDATE books SET job_status=1 WHERE job_id=?",(selected_job,))
            con.commit()
            messagebox.showinfo("Success","work has been issued successfully!",icon='info')
        except:
            messagebox.showerror('Error','Transaction not commit',icon='warning')
