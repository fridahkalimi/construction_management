from tkinter import *
from tkinter import messagebox
import sqlite3
con = sqlite3.connect('LMS.db')
cur = con.cursor()

class Storejob(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("800x800")
        self.title("Add job")
        self.resizable(False,False)

        self.top_frame = Frame(self, height=150, bg='grey')
        self.top_frame.pack(fill=X)
        heading = Label(self.top_frame, text='Add new Job',font='arial 18 bold' ,bg='grey')
        heading.place(x=300, y=60)

        self.bodyframe = Frame(self,height=650,bg='white')
        self.bodyframe.pack(fill=X)

        self.lbl_name = Label(self.bodyframe, text='position Available:', font='arial 12 bold', bg='white')
        self.lbl_name.place(x=40, y=40)
        self.txt_job_name = Entry(self.bodyframe, width=30, bd=2)
        self.txt_job_name.place(x= 200,y=45)

        self.lbl_company = Label(self.bodyframe, text='Company Name:', font='arial 12 bold', bg='white')
        self.lbl_company.place(x=40, y=80)
        self.txt_company = Entry(self.bodyframe, width=30, bd=2)
        self.txt_company.place(x= 200,y=80)

        self.lbl_slots = Label(self.bodyframe, text='slots available:', font='arial 12 bold', bg='white')
        self.lbl_slots.place(x=40, y=120)
        self.txt_slots = Entry(self.bodyframe, width=30, bd=2)
        self.txt_slots.place(x= 200,y=120)

        # Save Button
        savebutton = Button(self.bodyframe, text='Save now', command=self.savejob)
        savebutton.place(x=270, y=200)

    def savejob(self):
        """
            Saves the job and updates the DB
        """

        jobname = self.txt_job_name.get()
        company = self.txt_company.get()
        slots = self.txt_slots.get()

        if(jobname != '' and company != '' and slots != ''):
            try:
                query = "INSERT INTO jobs(job_name, company, slots)VALUES(?,?,?)"
                cur.execute(query,(jobname,company,slots))
                con.commit()
                messagebox.showinfo('Success','vacancy has been saved successfully',icon='info')
            except:
                messagebox.showerror('Error','Transaction failed!',icon='warning')
        
        else:
            messagebox.showerror('Error','All fields are required!',icon='warning')
